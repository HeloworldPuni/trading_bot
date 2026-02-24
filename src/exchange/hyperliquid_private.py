import hashlib
import logging
import threading
import time
import uuid
from dataclasses import dataclass
from typing import Any, Dict, Optional

from src.config import Config

logger = logging.getLogger(__name__)


def symbol_to_hyperliquid_coin(symbol: str, market_type: str = "") -> str:
    """
    Map generic symbols to Hyperliquid coin naming.
    Perp markets use base coin (e.g. BTC/USDC -> BTC).
    Spot keeps pair naming when explicitly configured as spot.
    """
    if not symbol:
        return symbol

    normalized = symbol.strip().upper()
    if ":" in normalized:
        normalized = normalized.split(":")[0]

    if "/" not in normalized:
        return normalized

    base, quote = normalized.split("/", 1)
    if (market_type or "").lower() in {"spot", "cash"}:
        return f"{base}/{quote}"
    return base


class NonceThrottle:
    """
    Ensures API calls are serialized at >=1ms spacing, reducing duplicate-nonce risk.
    """

    def __init__(self):
        self._lock = threading.Lock()
        self._last_nonce = 0

    def reserve_slot(self) -> int:
        with self._lock:
            now_ms = int(time.time() * 1000)
            next_ms = now_ms if now_ms > self._last_nonce else self._last_nonce + 1
            wait_ms = next_ms - now_ms
            if wait_ms > 0:
                time.sleep(wait_ms / 1000.0)
            self._last_nonce = next_ms
            return next_ms


@dataclass
class HyperliquidOrderRequest:
    symbol: str
    side: str  # BUY/SELL/LONG/SHORT
    size: float
    limit_price: Optional[float] = None
    tif: str = "Ioc"
    reduce_only: bool = False
    slippage: Optional[float] = None
    client_order_id: Optional[str] = None

    @property
    def is_buy(self) -> bool:
        side = self.side.strip().upper()
        if side in {"BUY", "LONG"}:
            return True
        if side in {"SELL", "SHORT"}:
            return False
        raise ValueError(f"Unsupported side: {self.side}")


class HyperliquidPrivateClient:
    def __init__(
        self,
        private_key: Optional[str] = None,
        api_wallet: Optional[str] = None,
        account_address: Optional[str] = None,
        vault_address: Optional[str] = None,
        testnet: Optional[bool] = None,
        timeout: float = 10.0,
        auto_connect: bool = False,
    ):
        self.private_key = (private_key or Config.HYPERLIQUID_PRIVATE_KEY).strip()
        self.api_wallet = (api_wallet or Config.HYPERLIQUID_API_WALLET).strip()
        self.account_address = (account_address or Config.HYPERLIQUID_ACCOUNT_ADDRESS).strip()
        self.vault_address = (vault_address or Config.HYPERLIQUID_VAULT_ADDRESS).strip() or None
        self.testnet = Config.HYPERLIQUID_TESTNET if testnet is None else bool(testnet)
        self.market_type = Config.EXCHANGE_MARKET_TYPE
        self.timeout = timeout

        self._deps: Optional[Dict[str, Any]] = None
        self._nonce_throttle = NonceThrottle()
        self.wallet_address: Optional[str] = None
        self.base_url: Optional[str] = None
        self.info = None
        self.exchange = None

        if auto_connect and self.is_configured():
            self.connect()

    def is_configured(self) -> bool:
        return bool(self.private_key and self.api_wallet)

    def _load_deps(self) -> Dict[str, Any]:
        if self._deps is not None:
            return self._deps

        try:
            from eth_account import Account
            from hyperliquid.exchange import Exchange
            from hyperliquid.info import Info
            from hyperliquid.utils.constants import MAINNET_API_URL, TESTNET_API_URL
            from hyperliquid.utils.types import Cloid
        except Exception as exc:
            raise RuntimeError(
                "hyperliquid-python-sdk not installed. Run: .venv\\Scripts\\python.exe -m pip install hyperliquid-python-sdk"
            ) from exc

        self._deps = {
            "Account": Account,
            "Exchange": Exchange,
            "Info": Info,
            "Cloid": Cloid,
            "MAINNET_API_URL": MAINNET_API_URL,
            "TESTNET_API_URL": TESTNET_API_URL,
        }
        return self._deps

    def connect(self):
        if not self.is_configured():
            raise RuntimeError("Missing Hyperliquid private credentials. Set HYPERLIQUID_API_WALLET and HYPERLIQUID_PRIVATE_KEY.")

        deps = self._load_deps()
        wallet = deps["Account"].from_key(self.private_key)
        self.wallet_address = wallet.address
        if self.api_wallet and self.wallet_address.lower() != self.api_wallet.lower():
            raise ValueError(
                "HYPERLIQUID_PRIVATE_KEY does not match HYPERLIQUID_API_WALLET."
            )

        self.base_url = deps["TESTNET_API_URL"] if self.testnet else deps["MAINNET_API_URL"]
        account_address = self.account_address or self.api_wallet

        self.info = deps["Info"](base_url=self.base_url, skip_ws=True, timeout=self.timeout)
        self.exchange = deps["Exchange"](
            wallet=wallet,
            base_url=self.base_url,
            account_address=account_address,
            vault_address=self.vault_address,
            timeout=self.timeout,
        )
        logger.info(
            "Hyperliquid private client connected (%s, account=%s)",
            "testnet" if self.testnet else "mainnet",
            account_address,
        )
        return self

    def _ensure_connected(self):
        if self.exchange is None or self.info is None:
            self.connect()

    def _effective_account_address(self) -> str:
        return self.account_address or self.api_wallet

    def _cloid(self, client_order_id: Optional[str]):
        if not client_order_id:
            return None
        deps = self._load_deps()
        Cloid = deps["Cloid"]

        raw = client_order_id.strip().lower()
        if raw.startswith("0x") and len(raw) == 34:
            return Cloid.from_str(raw)

        digest = hashlib.md5(raw.encode("utf-8")).hexdigest()[:32]
        return Cloid.from_str(f"0x{digest}")

    @staticmethod
    def parse_exchange_response(response: Any) -> Dict[str, Any]:
        payload: Dict[str, Any] = {
            "ok": False,
            "status": "unknown",
            "raw": response,
        }
        if not isinstance(response, dict):
            return payload

        status = response.get("status")
        payload["status"] = str(status) if status is not None else "unknown"
        payload["ok"] = status == "ok"

        statuses = (
            response.get("response", {})
            .get("data", {})
            .get("statuses", [])
        )
        if isinstance(statuses, list) and statuses:
            first = statuses[0]
            if isinstance(first, dict):
                if "resting" in first and isinstance(first["resting"], dict):
                    payload["order_status"] = "resting"
                    payload["oid"] = first["resting"].get("oid")
                elif "filled" in first and isinstance(first["filled"], dict):
                    payload["order_status"] = "filled"
                    payload["filled"] = first["filled"]
                    payload["oid"] = first["filled"].get("oid")
                    avg_px = first["filled"].get("avgPx") or first["filled"].get("px")
                    if avg_px is not None:
                        try:
                            payload["fill_price"] = float(avg_px)
                        except Exception:
                            pass
                elif "error" in first:
                    payload["order_status"] = "error"
                    payload["error"] = first["error"]
                    payload["ok"] = False

        if "error" in response and not payload.get("error"):
            payload["error"] = response.get("error")
            payload["ok"] = False

        return payload

    @staticmethod
    def _normalize_tif(tif: str) -> str:
        tif_norm = (tif or "Ioc").strip().capitalize()
        allowed = {"Ioc", "Gtc", "Alo"}
        if tif_norm not in allowed:
            raise ValueError(f"Unsupported TIF '{tif}'. Allowed: {sorted(allowed)}")
        return tif_norm

    def _serialized_call(self, fn, *args, **kwargs):
        self._nonce_throttle.reserve_slot()
        return fn(*args, **kwargs)

    def connectivity_snapshot(self) -> Dict[str, Any]:
        self._ensure_connected()
        address = self._effective_account_address()
        result: Dict[str, Any] = {
            "ok": True,
            "base_url": self.base_url,
            "wallet_address": self.wallet_address,
            "account_address": address,
        }

        try:
            result["rate_limit"] = self.info.user_rate_limit(address)
        except Exception as exc:
            result["ok"] = False
            result["rate_limit_error"] = str(exc)

        try:
            state = self.info.user_state(address)
            result["asset_positions"] = len(state.get("assetPositions", [])) if isinstance(state, dict) else None
        except Exception as exc:
            result["ok"] = False
            result["user_state_error"] = str(exc)

        try:
            open_orders = self.info.open_orders(address)
            result["open_orders"] = len(open_orders) if isinstance(open_orders, list) else None
        except Exception as exc:
            result["ok"] = False
            result["open_orders_error"] = str(exc)

        return result

    def fetch_position_sizes(self) -> Dict[str, float]:
        """
        Returns signed position size by coin, e.g. {"BTC": 0.12, "ETH": -0.4}.
        """
        self._ensure_connected()
        address = self._effective_account_address()
        state = self.info.user_state(address)
        result: Dict[str, float] = {}
        if not isinstance(state, dict):
            return result
        for row in state.get("assetPositions", []):
            pos = row.get("position", {}) if isinstance(row, dict) else {}
            coin = pos.get("coin")
            if not coin:
                continue
            try:
                result[str(coin)] = float(pos.get("szi", 0.0))
            except Exception:
                continue
        return result

    def place_order(self, request: HyperliquidOrderRequest) -> Dict[str, Any]:
        if request.size <= 0:
            raise ValueError("Order size must be positive.")
        self._ensure_connected()

        coin = symbol_to_hyperliquid_coin(request.symbol, self.market_type)
        cloid = self._cloid(request.client_order_id)
        slippage = float(request.slippage if request.slippage is not None else Config.HYPERLIQUID_ORDER_SLIPPAGE)

        if request.limit_price is None:
            raw = self._serialized_call(
                self.exchange.market_open,
                name=coin,
                is_buy=request.is_buy,
                sz=float(request.size),
                px=None,
                slippage=slippage,
                cloid=cloid,
            )
        else:
            order_type = {"limit": {"tif": self._normalize_tif(request.tif)}}
            raw = self._serialized_call(
                self.exchange.order,
                name=coin,
                is_buy=request.is_buy,
                sz=float(request.size),
                limit_px=float(request.limit_price),
                order_type=order_type,
                reduce_only=bool(request.reduce_only),
                cloid=cloid,
            )

        parsed = self.parse_exchange_response(raw)
        parsed["coin"] = coin
        parsed["symbol"] = request.symbol
        parsed["requested_size"] = float(request.size)
        return parsed

    def cancel_order(self, symbol: str, oid: int) -> Dict[str, Any]:
        self._ensure_connected()
        coin = symbol_to_hyperliquid_coin(symbol, self.market_type)
        raw = self._serialized_call(self.exchange.cancel, coin, int(oid))
        parsed = self.parse_exchange_response(raw)
        parsed["coin"] = coin
        parsed["oid"] = int(oid)
        return parsed

    def modify_order(
        self,
        symbol: str,
        oid: int,
        side: str,
        size: float,
        limit_price: float,
        tif: str = "Gtc",
        reduce_only: bool = False,
        client_order_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        if size <= 0:
            raise ValueError("Modified order size must be positive.")
        self._ensure_connected()
        coin = symbol_to_hyperliquid_coin(symbol, self.market_type)
        order_type = {"limit": {"tif": self._normalize_tif(tif)}}
        is_buy = HyperliquidOrderRequest(symbol=symbol, side=side, size=size).is_buy
        cloid = self._cloid(client_order_id)

        raw = self._serialized_call(
            self.exchange.modify_order,
            int(oid),
            coin,
            is_buy,
            float(size),
            float(limit_price),
            order_type,
            bool(reduce_only),
            cloid,
        )
        parsed = self.parse_exchange_response(raw)
        parsed["coin"] = coin
        parsed["oid"] = int(oid)
        return parsed


def create_hyperliquid_private_client(auto_connect: bool = False) -> HyperliquidPrivateClient:
    return HyperliquidPrivateClient(auto_connect=auto_connect)
