import logging
from typing import Any, Dict

from src.config import Config
from src.core.definitions import ActionDirection
from src.exchange.hyperliquid_private import (
    HyperliquidOrderRequest,
    HyperliquidPrivateClient,
    symbol_to_hyperliquid_coin,
)

logger = logging.getLogger(__name__)


class HyperliquidLiveExecutor:
    """
    Thin execution adapter that sends signed orders and returns normalized results.
    """

    def __init__(self, client: HyperliquidPrivateClient):
        self.client = client

    @staticmethod
    def _entry_side(direction: ActionDirection) -> str:
        if direction == ActionDirection.LONG:
            return "BUY"
        if direction == ActionDirection.SHORT:
            return "SELL"
        raise ValueError(f"Unsupported entry direction: {direction}")

    @staticmethod
    def _exit_side(position_direction: str) -> str:
        d = (position_direction or "").upper()
        if d == "LONG":
            return "SELL"
        if d == "SHORT":
            return "BUY"
        raise ValueError(f"Unsupported position direction: {position_direction}")

    @staticmethod
    def _safe_qty(size_usd: float, ref_price: float) -> float:
        if ref_price <= 0:
            return 0.0
        qty = size_usd / ref_price
        return max(qty, 0.0)

    def place_entry(
        self,
        symbol: str,
        direction: ActionDirection,
        size_usd: float,
        reference_price: float,
        decision_id: str,
    ) -> Dict[str, Any]:
        qty = self._safe_qty(size_usd=size_usd, ref_price=reference_price)
        if qty <= 0:
            return {"ok": False, "error": "invalid_qty", "requested_size_usd": size_usd}

        request = HyperliquidOrderRequest(
            symbol=symbol,
            side=self._entry_side(direction),
            size=qty,
            limit_price=None,
            reduce_only=False,
            client_order_id=decision_id,
        )
        response = self.client.place_order(request)
        response["requested_qty"] = qty
        response["reference_price"] = reference_price
        return response

    def place_exit(self, position: Dict[str, Any], current_price: float, reason: str = "EXIT") -> Dict[str, Any]:
        qty = float(position.get("size_qty") or 0.0)
        if qty <= 0:
            qty = self._safe_qty(float(position.get("size_usd", 0.0)), max(float(current_price), 1e-9))
        if qty <= 0:
            return {"ok": False, "error": "invalid_exit_qty", "reason": reason}

        symbol = str(position.get("symbol", ""))
        side = self._exit_side(str(position.get("direction", "")))
        # Use reduce-only IOC limit to avoid flipping positions.
        slippage = float(Config.HYPERLIQUID_ORDER_SLIPPAGE)
        if current_price <= 0:
            return {"ok": False, "error": "invalid_exit_price", "reason": reason}
        if side == "BUY":
            limit_price = current_price * (1.0 + slippage)
        else:
            limit_price = current_price * (1.0 - slippage)
        request = HyperliquidOrderRequest(
            symbol=symbol,
            side=side,
            size=qty,
            limit_price=float(limit_price),
            tif="Ioc",
            reduce_only=True,
            client_order_id=f"{position.get('decision_id', '')}:{reason}",
        )
        response = self.client.place_order(request)
        response["requested_qty"] = qty
        response["reason"] = reason
        return response

    def fetch_exchange_position_sizes(self) -> Dict[str, float]:
        return self.client.fetch_position_sizes()

    @staticmethod
    def coin_for_symbol(symbol: str, market_type: str = "") -> str:
        return symbol_to_hyperliquid_coin(symbol, market_type=market_type)
