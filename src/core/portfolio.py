
import logging
import json
import os
from datetime import datetime, UTC
from typing import Dict, List, Any, Optional
from src.config import Config

logger = logging.getLogger(__name__)

PORTFOLIO_STATE_FILE = "data/portfolio_state.json"

class Portfolio:
    def __init__(self, initial_balance: float = Config.INITIAL_CAPITAL, load_state: bool = True):
        self.initial_capital = initial_balance
        self.state_file = PORTFOLIO_STATE_FILE
        self._equity_peak = initial_balance
        self._daily_equity_start = initial_balance
        self._daily_date = datetime.now(UTC).date()
        
        # Phase 2: Cooldown tracking
        self.last_entry_times: Dict[str, datetime] = {}  # symbol -> last entry time
        
        # Try to load existing state
        if load_state and self._load_state():
            logger.info(f"💾 Portfolio Restored from disk! Balance: ${self.balance:,.2f}, Active: {len(self.get_all_positions())} positions")
        else:
            # Fresh start
            self.balance = initial_balance
            self.equity = initial_balance
            self.active_positions: Dict[str, List[Dict[str, Any]]] = {}  # Changed to List for multi-position
            self.trade_history: List[Dict[str, Any]] = []
            logger.info(f"Portfolio Initialized FRESH with ${initial_balance:,.2f}")
    
    def count_positions_for_symbol(self, symbol: str) -> int:
        """Count how many positions we have for a given symbol."""
        if symbol not in self.active_positions:
            return 0
        positions = self.active_positions[symbol]
        if isinstance(positions, list):
            return len(positions)
        else:
            # Legacy single-position format
            return 1

    def get_all_positions(self) -> List[Dict[str, Any]]:
        """Flatten all active positions into a single list."""
        flattened: List[Dict[str, Any]] = []
        for positions in self.active_positions.values():
            if isinstance(positions, list):
                flattened.extend(positions)
            else:
                flattened.append(positions)
        return flattened
    
    def can_open_position(self, symbol: str) -> tuple:
        """
        Phase 2: Check if we can open a new position on this symbol.
        Returns (can_open: bool, reason: str)
        """
        # Check max positions per symbol
        current_count = self.count_positions_for_symbol(symbol)
        if current_count >= Config.MAX_POSITIONS_PER_SYMBOL:
            return False, f"Max {Config.MAX_POSITIONS_PER_SYMBOL} positions per symbol"
        
        # Check cooldown
        if symbol in self.last_entry_times:
            elapsed = (datetime.now() - self.last_entry_times[symbol]).total_seconds() / 60
            if elapsed < Config.ENTRY_COOLDOWN_MINUTES:
                remaining = Config.ENTRY_COOLDOWN_MINUTES - elapsed
                return False, f"Cooldown: {remaining:.0f}m remaining"
        
        # Check total concurrent positions
        total_positions = sum(self.count_positions_for_symbol(s) for s in self.active_positions)
        if total_positions >= Config.MAX_CONCURRENT_POSITIONS:
            return False, f"Max {Config.MAX_CONCURRENT_POSITIONS} total positions"
        
        return True, "OK"
    
    def _load_state(self) -> bool:
        """Load portfolio state from disk."""
        if not os.path.exists(self.state_file):
            return False
        try:
            with open(self.state_file, "r") as f:
                state = json.load(f)
            self.balance = state.get("balance", self.initial_capital)
            self.equity = state.get("equity", self.initial_capital)
            raw_positions = state.get("active_positions", {})
            normalized: Dict[str, List[Dict[str, Any]]] = {}
            for sym, pos in raw_positions.items():
                if isinstance(pos, list):
                    normalized[sym] = pos
                else:
                    normalized[sym] = [pos]
            self.active_positions = normalized
            self.trade_history = state.get("trade_history", [])
            return True
        except Exception as e:
            logger.warning(f"Could not load portfolio state: {e}")
            return False
    
    def save_state(self):
        """Save portfolio state to disk."""
        try:
            os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
            state = {
                "balance": self.balance,
                "equity": self.equity,
                "initial_capital": self.initial_capital,
                "active_positions": self.active_positions,
                "trade_history": self.trade_history[-100:]  # Keep last 100 trades
            }
            with open(self.state_file, "w") as f:
                json.dump(state, f, indent=2)
            logger.debug("Portfolio state saved to disk")
        except Exception as e:
            logger.warning(f"Could not save portfolio state: {e}")

    def open_position(self, symbol: str, direction: str, entry_price: float, size_usd: float, 
                       tp: float, sl: float, decision_id: str, 
                       entry_regime: str = "UNKNOWN", entry_atr: float = 0.0,
                       leverage: int = 1):
        """
        Records a new position and deducts fees.
        Phase B: Also tracks entry regime and ATR for loss forensics.
        Phase 35: Tracks leverage for margin calculation.
        """
        # Calculate margin required (capital locked)
        margin_used = size_usd / leverage
        
        if margin_used > self.balance:
            logger.warning(f"Insufficient margin! Needed ${margin_used:.2f}, have ${self.balance:.2f}")
            return False

        # Enforce per-symbol position limit
        current_positions = self.active_positions.get(symbol, [])
        if not isinstance(current_positions, list):
            current_positions = [current_positions]
        if len(current_positions) >= Config.MAX_POSITIONS_PER_SYMBOL:
            logger.warning(f"Cannot open {symbol}: Max {Config.MAX_POSITIONS_PER_SYMBOL} positions reached.")
            return False

        # Apply Entry Fee and lock margin
        fee = size_usd * Config.FEE_RATE
        self.balance -= (fee + margin_used)  # Deduct fee AND margin
        
        new_pos = {
            "symbol": symbol,
            "direction": direction,
            "entry_price": entry_price,
            "size_usd": size_usd,
            "leverage": leverage,
            "margin_used": margin_used,
            "tp": tp,
            "sl": sl,
            "decision_id": decision_id,
            "strategy": None,
            "entry_fee": fee,
            "unrealized_pnl_usd": 0.0,
            "unrealized_pnl_pct": 0.0,
            # Phase B: Loss Forensics Metadata
            "entry_regime": entry_regime,
            "entry_atr": entry_atr,
        }
        
        if symbol not in self.active_positions:
            self.active_positions[symbol] = []
        if not isinstance(self.active_positions[symbol], list):
            self.active_positions[symbol] = [self.active_positions[symbol]]
        self.active_positions[symbol].append(new_pos)
        
        logger.info(f"Position OPEN: {direction} {symbol} @ {entry_price:.2f} | Size: ${size_usd:.2f} | Margin: ${margin_used:.2f} ({leverage}x) | Regime: {entry_regime}")
        
        # Phase 2: Record entry time for cooldown
        self.last_entry_times[symbol] = datetime.now()
        
        self.save_state()  # Persist after position change
        return True

    def update_metrics(self, symbol: str, current_price: float):
        """
        Updates unrealized P&L for a specific symbol.
        """
        if symbol not in self.active_positions:
            return

        positions = self.active_positions[symbol]
        if not isinstance(positions, list):
            positions = [positions]
            self.active_positions[symbol] = positions

        for pos in positions:
            entry = pos["entry_price"]
            direction = pos["direction"]
            size = pos["size_usd"]

            if direction == "LONG":
                pnl_pct = (current_price - entry) / entry
            else:
                pnl_pct = (entry - current_price) / entry

            pos["unrealized_pnl_pct"] = pnl_pct * 100
            pos["unrealized_pnl_usd"] = size * pnl_pct
        
        # Update Total Equity (Balance + PnL of all positions)
        total_pnl = sum(p["unrealized_pnl_usd"] for p in self.get_all_positions())
        self.equity = self.balance + total_pnl

    def close_position(self, symbol: str, exit_price: float, reason: str = "EXIT",
                        exit_regime: str = "UNKNOWN", exit_atr: float = 0.0,
                        decision_id: Optional[str] = None):
        """
        Closes a position, applies exit fees, and updates history.
        Phase B: Detects loss category based on regime/volatility changes.
        """
        if symbol not in self.active_positions:
            return None

        positions = self.active_positions[symbol]
        if not isinstance(positions, list):
            positions = [positions]

        pos = None
        if decision_id:
            for i, p in enumerate(positions):
                if p.get("decision_id") == decision_id:
                    pos = positions.pop(i)
                    break
        else:
            pos = positions.pop(0) if positions else None

        if pos is None:
            return None

        if not positions:
            self.active_positions.pop(symbol, None)
        else:
            self.active_positions[symbol] = positions
        
        # Apply Exit Fee (on the current value of the position)
        current_value = pos["size_usd"] + pos["unrealized_pnl_usd"]
        exit_fee = current_value * Config.FEE_RATE
        
        realized_pnl = pos["unrealized_pnl_usd"] - pos["entry_fee"] - exit_fee
        # Return margin + PnL to balance
        margin_used = pos.get("margin_used", pos["size_usd"])  # Fallback for old positions
        self.balance += (margin_used + realized_pnl)
        
        # Phase B: Loss Category Detection
        loss_category = None
        if realized_pnl < 0:
            entry_regime = pos.get("entry_regime", "UNKNOWN")
            entry_atr = pos.get("entry_atr", 0.0)
            
            # Regime Shift Detection
            if entry_regime != exit_regime and entry_regime != "UNKNOWN":
                loss_category = "REGIME_SHIFT"
            # Volatility Spike Detection (ATR jumped 50%+)
            elif entry_atr > 0 and exit_atr > entry_atr * 1.5:
                loss_category = "VOLATILITY_SPIKE"
            # Bad Timing (quick SL hit)
            elif reason == "SL":
                loss_category = "BAD_TIMING"
            else:
                loss_category = "MARKET_MOVE"
        
        history_entry = {
            **pos,
            "strategy": pos.get("strategy"),
            "exit_price": exit_price,
            "exit_reason": reason,
            "exit_fee": exit_fee,
            "realized_pnl_usd": realized_pnl,
            "realized_pnl_pct": (realized_pnl / pos["size_usd"]) * 100,
            # Phase B: Forensics Data
            "exit_regime": exit_regime,
            "exit_atr": exit_atr,
            "loss_category": loss_category,
        }
        
        self.trade_history.append(history_entry)
        # Sync equity after close (include remaining unrealized PnL)
        total_unrealized = sum(p.get("unrealized_pnl_usd", 0.0) for p in self.get_all_positions())
        self.equity = self.balance + total_unrealized
        
        if loss_category:
            logger.warning(f"📊 LOSS FORENSICS: {symbol} | Category: {loss_category} | Regime: {pos.get('entry_regime')} → {exit_regime}")
        
        logger.info(f"Position CLOSED: {symbol} | PnL: ${realized_pnl:.2f} ({history_entry['realized_pnl_pct']:.2f}%) | Reason: {reason}")
        self.save_state()  # Persist after position change
        return history_entry

    def get_summary(self):
        roi = ((self.equity - self.initial_capital) / self.initial_capital) * 100
        total_positions = sum(self.count_positions_for_symbol(s) for s in self.active_positions)
        if self.equity > self._equity_peak:
            self._equity_peak = self.equity
        today = datetime.now(UTC).date()
        if today != self._daily_date:
            self._daily_date = today
            self._daily_equity_start = self.equity
        drawdown_pct = (self._equity_peak - self.equity) / max(1e-9, self._equity_peak) * 100
        daily_loss_pct = (self._daily_equity_start - self.equity) / max(1e-9, self._daily_equity_start) * 100
        return {
            "initial_capital": self.initial_capital,
            "balance": self.balance,
            "equity": self.equity,
            "total_pnl": self.equity - self.initial_capital,
            "roi_pct": roi,
            "drawdown_pct": drawdown_pct,
            "daily_loss_pct": daily_loss_pct,
            "active_count": total_positions,
            "history_count": len(self.trade_history)
        }
