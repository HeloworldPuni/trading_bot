
import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)

class InventoryStrategy:
    """
    Phase 5 Retrofit: Inventory Management / Market Making.
    Adjusts quotes based on current inventory lean.
    """
    def __init__(self, max_inventory_usd: float = 1000.0, risk_aversion: float = 0.1):
        self.max_inventory = max_inventory_usd
        self.risk_aversion = risk_aversion # Gamma

    def get_skew(self, current_inventory_usd: float) -> float:
        """
        Returns price skew in basis points.
        Positive inventory -> Skew lower (Sell cheaper to reduce inv).
        Negative inventory -> Skew higher (Buy higher to cover short).
        """
        normalized_inv = current_inventory_usd / self.max_inventory
        # Linear skew model: Skew = -Gamma * Inventory
        # If Inv = 1.0 (Max Long), Skew = -0.1 (-10bps)
        return -self.risk_aversion * normalized_inv

    def get_quotes(self, mid_price: float, inventory_usd: float, spread_bps: float = 0.001) -> Dict[str, float]:
        """
        Calculates Bid/Ask prices.
        """
        skew_pct = self.get_skew(inventory_usd)
        
        # Adjust mid with skew
        reservation_price = mid_price * (1 + skew_pct)
        
        half_spread = spread_bps / 2.0
        bid = reservation_price * (1 - half_spread)
        ask = reservation_price * (1 + half_spread)
        
        return {"bid": bid, "ask": ask}
