
import logging
import time
from typing import Dict, Optional
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class ShadowPosition:
    symbol: str
    size: float
    entry_price: float
    unrealized_pnl: float = 0.0

class ShadowExecutor:
    """
    Phase 11 Retrofit: Shadow Mode Execution.
    Simulates trades against live market data.
    """
    def __init__(self, initial_capital: float = 10000.0, fee_rate: float = 0.0005):
        self.initial_capital = initial_capital
        self.balance = initial_capital
        self.fee_rate = fee_rate
        self.inventory: Dict[str, ShadowPosition] = {}
        self.trades = []
        logger.info(f"ShadowExecutor initialized with ${initial_capital:.2f}")

    def submit_order(self, order: Dict) -> str:
        """
        Simulate order execution.
        """
        symbol = order.get('symbol')
        side = order.get('side').upper()
        quantity = float(order.get('amount', 0))
        price = float(order.get('price', 0)) # Limit price or current market
        
        if quantity <= 0 or price <= 0:
            logger.error(f"Invalid shadow order: {order}")
            return "REJECTED"

        # Calculate cost
        cost = quantity * price
        fee = cost * self.fee_rate
        
        if side == 'BUY':
            if self.balance >= (cost + fee):
                self.balance -= (cost + fee)
                self._update_inventory(symbol, quantity, price, side)
                self._log_trade(symbol, side, quantity, price, fee)
                return "FILLED"
            else:
                logger.warning(f"Shadow Insufficient Funds: {self.balance} < {cost+fee}")
                return "REJECTED_FUNDS"
                
        elif side == 'SELL':
            # Allow Short Selling (Negative Inventory)
            revenue = cost - fee
            self.balance += revenue
            self._update_inventory(symbol, quantity, price, side)
            self._log_trade(symbol, side, quantity, price, fee)
            return "FILLED"
                
        return "REJECTED_UNKNOWN"

    def _update_inventory(self, symbol: str, quantity: float, price: float, side: str):
        if symbol not in self.inventory:
            self.inventory[symbol] = ShadowPosition(symbol, 0.0, 0.0)
            
        pos = self.inventory[symbol]
        
        if side == 'BUY':
            # Weighted average entry price
            total_cost = (pos.size * pos.entry_price) + (quantity * price)
            new_size = pos.size + quantity
            pos.entry_price = total_cost / new_size if new_size > 0 else 0.0
            pos.size = new_size
            
        elif side == 'SELL':
            pos.size = pos.size - quantity
            # Update entry price for short position if flipping from long or increasing short
            if pos.size < 0:
                 # Simplified: Just track size. 
                 # Real short logic needs separate liability tracking.
                 pass

    def _log_trade(self, symbol, side, qty, price, fee):
        t = {
            "timestamp": time.time(),
            "symbol": symbol,
            "side": side,
            "qty": qty,
            "price": price,
            "fee": fee
        }
        self.trades.append(t)
        logger.info(f"SHADOW TRADING: {side} {qty} {symbol} @ {price} (Fee: {fee:.4f})")

    def get_equity(self, current_prices: Dict[str, float]) -> float:
        """Calculate total equity (cash + position value)."""
        equity = self.balance
        for symbol, pos in self.inventory.items():
            price = current_prices.get(symbol, pos.entry_price)
            equity += pos.size * price
        return equity
