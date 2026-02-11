from dataclasses import dataclass
from enum import Enum
from typing import Optional

from src.core.definitions import ActionDirection, StrategyType


class OrderType(Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    TWAP = "TWAP"


class ExecutionStatus(Enum):
    PENDING = "PENDING"
    FILLED = "FILLED"
    REJECTED = "REJECTED"


@dataclass
class OrderRequest:
    action_id: str
    direction: ActionDirection
    order_type: OrderType
    quantity: float
    limit_price: Optional[float] = None
    twap_minutes: int = 0


@dataclass
class ExecutionReport:
    action_id: str
    status: ExecutionStatus
    filled_qty: float = 0.0
    avg_price: float = 0.0


class SmartRouter:
    """
    Compatibility smart router for execution scripts.
    """

    def __init__(self):
        self.large_order_threshold = 0.30
        self.limit_spread_threshold = 0.05

    def route(self, action, state) -> OrderRequest:
        spread = float(getattr(state, "spread_pct", 0.0))
        current_price = float(getattr(state, "current_price", 0.0) or 0.0)
        target_weight = float(getattr(action, "target_weight", 0.0) or 0.0)
        direction = getattr(action, "direction", ActionDirection.FLAT)
        action_id = getattr(action, "reasoning", "") or f"route_{id(action)}"

        high_urgency = action.strategy in {StrategyType.MOMENTUM, StrategyType.SHORT_MOMENTUM, StrategyType.BREAKOUT}
        if abs(target_weight) >= self.large_order_threshold:
            return OrderRequest(action_id, direction, OrderType.TWAP, quantity=abs(target_weight), twap_minutes=60)

        if (not high_urgency) and spread >= self.limit_spread_threshold:
            if direction == ActionDirection.LONG:
                limit_price = current_price * 0.999 if current_price > 0 else None
            elif direction == ActionDirection.SHORT:
                limit_price = current_price * 1.001 if current_price > 0 else None
            else:
                limit_price = None
            return OrderRequest(action_id, direction, OrderType.LIMIT, quantity=max(abs(target_weight), 0.01), limit_price=limit_price)

        return OrderRequest(action_id, direction, OrderType.MARKET, quantity=max(abs(target_weight), 0.01))
