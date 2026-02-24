
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
        self.state_file = self._resolve_state_file()
        self._equity_peak = initial_balance
        self._daily_equity_start = initial_balance
        self._daily_date = datetime.now(UTC).date()
        
        # Phase 2: Cooldown tracking
        self.last_entry_times: Dict[str, datetime] = {}  # symbol -> last entry time
        
        # Try to load existing state
        if load_state and self._load_state():
            logger.info(
                "Portfolio restored from disk. Balance: $%s, Active: %s positions",
                f"{self.balance:,.2f}",
                len(self.get_all_positions()),
            )
        else:
            # Fresh start
            self.balance = initial_balance
            self.equity = initial_balance
            self.active_positions: Dict[str, List[Dict[str, Any]]] = {}  # Changed to List for multi-position
            self.trade_history: List[Dict[str, Any]] = []
            logger.info(f"Portfolio Initialized FRESH with ${initial_balance:,.2f}")

    def _resolve_state_file(self) -> str:
        """
        Use venue-scoped portfolio state by default to avoid cross-exchange contamination.
        Keep backward compatibility for legacy Binance/USDT paper file.
        """
        configured = getattr(Config, "PORTFOLIO_STATE_FILE", None)
        default_scoped = os.path.join(
            "data",
            f"portfolio_state_{Config.EXCHANGE_ID}_{Config.QUOTE_CURRENCY}_{Config.TRADING_MODE}.json",
        )
        target = configured or default_scoped
        legacy = PORTFOLIO_STATE_FILE

        # Backward compatibility only for historical default setup.
        if (
            target == default_scoped
            and not os.path.exists(target)
            and Config.EXCHANGE_ID == "binance"
            and Config.QUOTE_CURRENCY == "USDT"
            and Config.TRADING_MODE == "paper"
            and os.path.exists(legacy)
        ):
            return legacy
        return target

    @staticmethod
    def _compute_unrealized_pnl(pos: Dict[str, Any], current_price: float) -> float:
        entry = float(pos.get("entry_price", 0.0) or 0.0)
        size = float(pos.get("size_usd", 0.0) or 0.0)
        if entry <= 0.0 or size <= 0.0:
            return 0.0
        direction = str(pos.get("direction", "LONG") or "LONG").upper()
        if direction == "LONG":
            pnl_pct = (float(current_price) - entry) / entry
        else:
            pnl_pct = (entry - float(current_price)) / entry
        return size * pnl_pct

    @staticmethod
    def _estimate_liquidation_price(entry_price: float, direction: str, leverage: int) -> Optional[float]:
        lev = int(leverage) if leverage else 0
        if entry_price <= 0 or lev <= 0:
            return None
        direction = str(direction or "LONG").upper()
        if direction == "LONG":
            px = entry_price * (1.0 - (1.0 / lev))
        else:
            px = entry_price * (1.0 + (1.0 / lev))
        return px if px > 0 else None
    
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
                       leverage: int = 1, size_qty: float = 0.0,
                       exchange_order_id: Optional[int] = None,
                       trade_mode: str = "SCALP",
                       exchange_order_status: Optional[str] = None,
                       strategy: Optional[str] = None):
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
            "size_qty": size_qty,
            "leverage": leverage,
            "margin_used": margin_used,
            "tp": tp,
            "sl": sl,
            "decision_id": decision_id,
            "entry_time": datetime.now(UTC).isoformat(),
            "strategy": strategy,
            "entry_fee": fee,
            "unrealized_pnl_usd": 0.0,
            "unrealized_pnl_pct": 0.0,
            "raw_unrealized_pnl_usd": 0.0,
            "liquidation_flag": False,
            "liquidation_price": self._estimate_liquidation_price(entry_price, direction, leverage),
            "exchange_order_id": exchange_order_id,
            "exchange_order_status": exchange_order_status,
            # Phase B: Loss Forensics Metadata
            "entry_regime": entry_regime,
            "entry_atr": entry_atr,
            # Trailing Stop Fields
            "trade_mode": trade_mode,
            "trail_active": False,
            "trail_high": entry_price,
            "trail_sl": None,
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

    def backfill_open_position_strategies(self, experience_log_path: Optional[str] = None) -> int:
        """
        Fill missing strategy on restored open positions using decision ids from experience log.
        Returns number of positions patched.
        """
        missing_refs: List[tuple] = []
        for sym, positions in self.active_positions.items():
            rows = positions if isinstance(positions, list) else [positions]
            for idx, pos in enumerate(rows):
                if pos.get("strategy"):
                    continue
                decision_id = pos.get("decision_id")
                if decision_id:
                    missing_refs.append((decision_id, sym, idx))

        if not missing_refs:
            return 0

        log_path = experience_log_path or getattr(Config, "EXPERIENCE_LOG_FILE", "")
        if not log_path or not os.path.exists(log_path):
            return 0

        remaining = {did for did, _, _ in missing_refs}
        found: Dict[str, str] = {}
        try:
            with open(log_path, "r", encoding="utf-8") as f:
                for line in f:
                    if not remaining:
                        break
                    try:
                        rec = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    rec_id = rec.get("id")
                    if rec_id not in remaining:
                        continue
                    strategy = (rec.get("action_taken") or {}).get("strategy")
                    if strategy:
                        found[rec_id] = strategy
                        remaining.discard(rec_id)
        except Exception as e:
            logger.warning(f"Could not backfill open-position strategies: {e}")
            return 0

        patched = 0
        for decision_id, sym, idx in missing_refs:
            strategy = found.get(decision_id)
            if not strategy:
                continue
            positions = self.active_positions.get(sym, [])
            if isinstance(positions, list) and idx < len(positions):
                positions[idx]["strategy"] = strategy
                patched += 1

        if patched > 0:
            logger.info(f"Backfilled strategy for {patched} restored open positions from experience log.")
            self.save_state()
        return patched

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
            size = float(pos.get("size_usd", 0.0) or 0.0)
            margin_used = float(pos.get("margin_used", size) or size)
            raw_unrealized = self._compute_unrealized_pnl(pos, current_price)
            capped_unrealized = max(raw_unrealized, -margin_used)
            pos["raw_unrealized_pnl_usd"] = raw_unrealized
            pos["liquidation_flag"] = raw_unrealized <= (-margin_used + 1e-9)
            pos["unrealized_pnl_usd"] = capped_unrealized
            if size > 0:
                pos["unrealized_pnl_pct"] = (capped_unrealized / size) * 100.0
            else:
                pos["unrealized_pnl_pct"] = 0.0
            pos["current_price"] = current_price
        
        # Update Total Equity (Balance + PnL + Margin)
        all_pos = self.get_all_positions()
        total_pnl = sum(p.get("unrealized_pnl_usd", 0.0) for p in all_pos)
        total_margin = sum(p.get("margin_used", 0.0) for p in all_pos)
        self.equity = self.balance + total_pnl + total_margin

    def update_trailing_stop(self, symbol: str, current_price: float, current_atr: float):
        """
        Update trailing stop for positions in trailing mode.
        Returns list of positions that should be closed (trail_sl hit).
        """
        if not Config.TRAILING_STOP_ENABLED:
            return []
        
        if symbol not in self.active_positions:
            return []
        
        positions = self.active_positions[symbol]
        if not isinstance(positions, list):
            positions = [positions]
        
        to_trail_close = []
        for pos in positions:
            trade_mode = pos.get("trade_mode", "SCALP")
            direction = pos["direction"]
            
            # Only trail on eligible trade modes
            if trade_mode != Config.TRAILING_ACTIVATION_MODE:
                continue
            
            if pos.get("trail_active"):
                # Already trailing — update trail high and trail_sl
                if direction == "LONG":
                    if current_price > pos["trail_high"]:
                        pos["trail_high"] = current_price
                        trail_dist = current_atr * Config.TRAILING_ATR_MULTIPLIER
                        pos["trail_sl"] = pos["trail_high"] - trail_dist
                    # Check if trail_sl hit
                    if current_price <= pos["trail_sl"]:
                        to_trail_close.append(pos)
                else:  # SHORT
                    if current_price < pos["trail_high"]:  # trail_high = trail_low for shorts
                        pos["trail_high"] = current_price
                        trail_dist = current_atr * Config.TRAILING_ATR_MULTIPLIER
                        pos["trail_sl"] = pos["trail_high"] + trail_dist
                    if current_price >= pos["trail_sl"]:
                        to_trail_close.append(pos)
            else:
                # Not trailing yet — check if TP hit to activate
                tp = pos.get("tp")
                if tp is None:
                    continue
                
                should_activate = False
                if direction == "LONG" and current_price >= tp:
                    should_activate = True
                elif direction == "SHORT" and current_price <= tp:
                    should_activate = True
                
                if should_activate:
                    pos["trail_active"] = True
                    pos["trail_high"] = current_price
                    trail_dist = current_atr * Config.TRAILING_ATR_MULTIPLIER
                    if direction == "LONG":
                        pos["trail_sl"] = current_price - trail_dist
                    else:
                        pos["trail_sl"] = current_price + trail_dist
                    logger.info(
                        "Trailing stop activated: %s %s | Price: %s | Trail SL: %.6f",
                        symbol,
                        direction,
                        current_price,
                        pos["trail_sl"],
                    )
        
        return to_trail_close

    def close_position(self, symbol: str, exit_price: float, reason: str = "EXIT",
                        exit_regime: str = "UNKNOWN", exit_atr: float = 0.0,
                        decision_id: Optional[str] = None,
                        exchange_exit_order_id: Optional[int] = None):
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
        
        size_usd = float(pos.get("size_usd", 0.0) or 0.0)
        margin_used = float(pos.get("margin_used", size_usd) or size_usd)
        entry_fee = max(0.0, float(pos.get("entry_fee", 0.0) or 0.0))

        # Recompute with exit price and cap loss by posted margin (paper liquidation model).
        raw_unrealized = self._compute_unrealized_pnl(pos, exit_price)
        capped_unrealized = max(raw_unrealized, -margin_used)
        liquidated = bool(pos.get("liquidation_flag")) or raw_unrealized <= (-margin_used + 1e-9)
        exit_notional = max(0.0, size_usd + capped_unrealized)
        exit_fee = exit_notional * Config.FEE_RATE

        # Realized PnL is net of both fees. Cash release excludes entry fee (already deducted at open).
        realized_pnl = capped_unrealized - entry_fee - exit_fee
        cash_release = margin_used + capped_unrealized - exit_fee
        self.balance += cash_release
        
        # Phase B: Loss Category Detection
        loss_category = None
        if realized_pnl < 0:
            entry_regime = pos.get("entry_regime", "UNKNOWN")
            entry_atr = pos.get("entry_atr", 0.0)

            if liquidated:
                loss_category = "LIQUIDATION"
            # Regime Shift Detection
            elif entry_regime != exit_regime and entry_regime != "UNKNOWN":
                loss_category = "REGIME_SHIFT"
            # Volatility Spike Detection (ATR jumped 50%+)
            elif entry_atr > 0 and exit_atr > entry_atr * 1.5:
                loss_category = "VOLATILITY_SPIKE"
            # Bad Timing (quick SL hit)
            elif reason == "SL":
                loss_category = "BAD_TIMING"
            else:
                loss_category = "MARKET_MOVE"

        effective_reason = reason
        if liquidated and not str(reason).upper().startswith("LIQ"):
            effective_reason = "LIQUIDATED"

        pos["raw_unrealized_pnl_usd"] = raw_unrealized
        pos["unrealized_pnl_usd"] = capped_unrealized
        if size_usd > 0:
            pos["unrealized_pnl_pct"] = (capped_unrealized / size_usd) * 100.0
        pos["liquidation_flag"] = liquidated
        
        history_entry = {
            **pos,
            "strategy": pos.get("strategy"),
            "exit_price": exit_price,
            "exit_reason": effective_reason,
            "exit_time": datetime.now(UTC).isoformat(),
            "exchange_exit_order_id": exchange_exit_order_id,
            "exit_fee": exit_fee,
            "realized_pnl_usd": realized_pnl,
            "realized_pnl_pct": (realized_pnl / size_usd * 100.0) if size_usd > 0 else 0.0,
            "liquidated": liquidated,
            # Phase B: Forensics Data
            "exit_regime": exit_regime,
            "exit_atr": exit_atr,
            "loss_category": loss_category,
        }
        
        self.trade_history.append(history_entry)
        # Sync equity after close (include remaining unrealized PnL + Margin)
        all_pos = self.get_all_positions()
        total_unrealized = sum(p.get("unrealized_pnl_usd", 0.0) for p in all_pos)
        total_margin = sum(p.get("margin_used", 0.0) for p in all_pos)
        self.equity = self.balance + total_unrealized + total_margin
        
        if loss_category:
            logger.warning(
                "Loss forensics: %s | Category: %s | Regime: %s -> %s",
                symbol,
                loss_category,
                pos.get("entry_regime"),
                exit_regime,
            )
        
        logger.info(
            f"Position CLOSED: {symbol} | PnL: ${realized_pnl:.2f} "
            f"({history_entry['realized_pnl_pct']:.2f}%) | Reason: {effective_reason}"
        )
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
