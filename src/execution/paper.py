
import logging
from src.core.definitions import Action, ActionDirection, StrategyType

logger = logging.getLogger(__name__)

class PaperExecutor:
    def __init__(self):
        logger.info("Paper Executor Initialized")

    def execute(self, action: Action, symbol: str, current_price: float, atr: float) -> bool:
        """
        Simulates order execution with dynamic TP/SL.
        Returns True if successful.
        """
        if action.strategy == StrategyType.WAIT:
            return True

        if action.direction == ActionDirection.FLAT:
            return True

        # Calculate Dynamic TP/SL (Phase 32)
        # 2:1 Reward:Risk Ratio
        sl_dist = 1.5 * atr
        tp_dist = 3.0 * atr

        if action.direction == ActionDirection.LONG:
            action.sl = current_price - sl_dist
            action.tp = current_price + tp_dist
        else:
            action.sl = current_price + sl_dist
            action.tp = current_price - tp_dist

        logger.info(f"PAPER ORDER: {action.direction.name} {symbol} ({action.risk_level.name}) | TP: {action.tp:.2f} | SL: {action.sl:.2f}")
        return True
