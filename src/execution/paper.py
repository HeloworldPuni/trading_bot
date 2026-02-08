
import logging
from src.core.definitions import Action, ActionDirection, StrategyType

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
