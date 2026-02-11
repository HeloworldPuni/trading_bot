
import logging
from src.core.definitions import Action, ActionDirection, StrategyType
from src.execution.router import OrderType, ExecutionStatus, ExecutionReport

logger = logging.getLogger(__name__)

class PaperExecutor:
    def __init__(self):
        logger.info("Paper Executor Initialized")

    def execute(self, action: Action, symbol: str, current_price: float, atr: float) -> bool:
        """
        Validates trade execution.
        Returns True if trade should proceed.
        
        Note: TP/SL is calculated in main.py using trade mode (SCALP/SWING).
        """
        if action.strategy == StrategyType.WAIT:
            return True

        if action.direction == ActionDirection.FLAT:
            return True

        # Executor just validates, actual TP/SL set in main.py via get_trade_mode()
        logger.info(f"PAPER ORDER: {action.direction.name} {symbol} ({action.risk_level.name})")
        return True


class PaperExchange:
    """
    Compatibility paper exchange used by legacy execution tests.
    """

    def __init__(self, latency_ms: int = 0):
        self.latency_ms = max(0, int(latency_ms))
        self.pending_orders = []

    def execute(self, request, current_price: float) -> ExecutionReport:
        if request.order_type == OrderType.MARKET:
            return ExecutionReport(
                action_id=request.action_id,
                status=ExecutionStatus.FILLED,
                filled_qty=float(request.quantity),
                avg_price=float(current_price),
            )

        if request.order_type == OrderType.LIMIT:
            if request.limit_price is None:
                return ExecutionReport(request.action_id, ExecutionStatus.REJECTED, 0.0, 0.0)

            should_fill = False
            if request.direction == ActionDirection.LONG and current_price <= request.limit_price:
                should_fill = True
            if request.direction == ActionDirection.SHORT and current_price >= request.limit_price:
                should_fill = True

            if should_fill:
                return ExecutionReport(
                    action_id=request.action_id,
                    status=ExecutionStatus.FILLED,
                    filled_qty=float(request.quantity),
                    avg_price=float(request.limit_price),
                )

            self.pending_orders.append(request)
            return ExecutionReport(request.action_id, ExecutionStatus.PENDING, 0.0, 0.0)

        # TWAP requests are accepted as pending in this simplified simulator.
        self.pending_orders.append(request)
        return ExecutionReport(request.action_id, ExecutionStatus.PENDING, 0.0, 0.0)

    def update(self, current_price: float):
        fills = []
        remaining = []
        for req in self.pending_orders:
            if req.order_type != OrderType.LIMIT:
                remaining.append(req)
                continue

            should_fill = False
            if req.direction == ActionDirection.LONG and current_price <= req.limit_price:
                should_fill = True
            if req.direction == ActionDirection.SHORT and current_price >= req.limit_price:
                should_fill = True

            if should_fill:
                fills.append(
                    ExecutionReport(
                        action_id=req.action_id,
                        status=ExecutionStatus.FILLED,
                        filled_qty=float(req.quantity),
                        avg_price=float(req.limit_price),
                    )
                )
            else:
                remaining.append(req)

        self.pending_orders = remaining
        return fills
