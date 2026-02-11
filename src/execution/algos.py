
import logging
import time
from typing import Dict, List, Optional
import random

logger = logging.getLogger(__name__)

class OrderFactory:
    """Helper to create standard order inputs."""
    @staticmethod
    def create_limit_order(symbol: str, side: str, amount: float, price: float, 
                           post_only: bool = False) -> Dict:
        return {
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "amount": amount,
            "price": price,
            "params": {"postOnly": True} if post_only else {}
        }

class IcebergExecutor:
    """
    Splits large order into visible chunks to hide intent.
    """
    def __init__(self, total_qty: float, visible_qty: float, price_limit: float):
        self.total_qty = total_qty
        self.remaining_qty = total_qty
        self.visible_qty = visible_qty
        self.price_limit = price_limit
        self.executed_qty = 0.0

    def get_next_slice(self) -> float:
        if self.remaining_qty <= 0:
            return 0.0
        
        # Add random variance (+/- 20% to visible size)
        variance = self.visible_qty * 0.2
        slice_size = self.visible_qty + random.uniform(-variance, variance)
        slice_size = min(slice_size, self.remaining_qty)
        return round(slice_size, 6)

    def on_fill(self, qty: float):
        self.remaining_qty -= qty
        self.executed_qty += qty
        logger.info(f"Iceberg: Filled {qty}. Remaining: {self.remaining_qty}")

class POVExecutor:
    """
    Percent of Volume (POV) Execution.
    target_pct: Target participation rate (e.g. 0.10 for 10% of market volume).
    """
    def __init__(self, total_qty: float, target_pct: float, limit_price: float):
        self.total_qty = total_qty
        self.remaining_qty = total_qty
        self.target_pct = target_pct
        self.limit_price = limit_price
        self.market_volume_since_start = 0.0
        self.my_volume_since_start = 0.0

    def update_market_volume(self, recent_volume: float):
        self.market_volume_since_start += recent_volume

    def get_target_qty(self) -> float:
        # Target = (Total Market Vol including mine) * Target%
        # But we need to solve for *next* order size.
        # Simple approximation: Match recent volume * target_pct
        
        needed = self.market_volume_since_start * self.target_pct - self.my_volume_since_start
        if needed <= 0: return 0.0
        
        qty = min(needed, self.remaining_qty)
        return round(qty, 6)

class VWAPExecutor:
    """
    Volume Weighted Average Price (VWAP) Execution.
    Spreads execution over a time horizon based on historical volume profile.
    NOTE: Simplified implementation (linear time spread) for Phase 8.
    """
    def __init__(self, total_qty: float, duration_minutes: int):
        self.total_qty = total_qty
        self.remaining_qty = total_qty
        self.start_time = time.time()
        self.end_time = self.start_time + (duration_minutes * 60)
        self.duration_seconds = duration_minutes * 60

    def get_next_slice(self) -> float:
        now = time.time()
        if now >= self.end_time:
            return self.remaining_qty # Dump remaining at end
            
        remaining_time = self.end_time - now
        # Linear pace: qty_per_second
        rate = self.remaining_qty / remaining_time if remaining_time > 0 else 0
        
        # Return 1 minute worth of volume
        slice_qty = rate * 60
        slice_qty = min(slice_qty, self.remaining_qty)
        return round(slice_qty, 6)
