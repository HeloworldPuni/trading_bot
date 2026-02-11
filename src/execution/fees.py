
import logging

logger = logging.getLogger(__name__)

class FeeOptimizer:
    """
    Phase 8 Retrofit: Fee Optimization.
    Recommends 'MAKER' strategies to capture rebates.
    """
    def __init__(self, maker_fee: float = 0.0002, taker_fee: float = 0.0005):
        self.maker_fee = maker_fee
        self.taker_fee = taker_fee

    def should_use_maker(self, spread_pct: float, urgency: str) -> bool:
        """
        Decides whether to use Post-Only (Maker) or Market (Taker).
        """
        cost_diff = self.taker_fee - self.maker_fee
        
        # High urgency -> Take liquidity
        if urgency == "HIGH":
            return False
            
        # If spread is tight and we save fees, use Maker
        if spread_pct < cost_diff * 2:
            return True
            
        return True # Default to maker for cost saving
