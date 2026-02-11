from dataclasses import dataclass
import os
from typing import Any, Dict, List, Optional

from src.config import Config
from src.core.definitions import StrategyType, ActionDirection
from src.core.allocator import StrategyPerformanceTracker
from src.core.trade_utils import calculate_tp_sl
from src.core.reward import RewardCalculator
from src.data.replay_feeder import ReplayFeeder
from src.engine.system import TradingEngine


@dataclass
class BacktestConfig:
    initial_capital: float = Config.INITIAL_CAPITAL
    fee_rate: float = Config.FEE_RATE
    slippage_bps: float = 5.0
    latency_candles: int = 1
    funding_rate_per_interval: float = 0.0  # percent
    funding_interval_candles: int = 32
    max_position_pct: float = Config.MAX_POSITION_PCT
    leverage: int = 1
    max_positions_per_symbol: int = Config.MAX_POSITIONS_PER_SYMBOL


@dataclass
class BacktestPosition:
    symbol: str
    direction: str
    entry_price: float
    size_usd: float
    leverage: int
    tp: float
    sl: float
    entry_step: int
    decision_id: str
    strategy: str = ""
    entry_regime: str = "UNKNOWN"
    entry_fee: float = 0.0
    funding_accrued: float = 0.0


class BacktestPortfolio:
    def __init__(self, config: BacktestConfig):
        self.config = config
        self.balance = config.initial_capital
        self.equity = config.initial_capital
        self.positions: List[BacktestPosition] = []
        self.trade_history: List[Dict[str, Any]] = []

    def count_positions(self, symbol: str) -> int:
        return sum(1 for p in self.positions if p.symbol == symbol)

    def can_open(self, symbol: str) -> bool:
        if self.count_positions(symbol) >= self.config.max_positions_per_symbol:
            return False
        return True

    def open_position(self, pos: BacktestPosition) -> bool:
        margin_used = pos.size_usd / max(1, pos.leverage)
        if margin_used > self.balance:
            return False
        entry_fee = pos.size_usd * self.config.fee_rate
        pos.entry_fee = entry_fee
        self.balance -= (margin_used + entry_fee)
        self.positions.append(pos)
        return True

    def update_equity(self, current_price: float):
        unrealized = 0.0
        for p in self.positions:
            pnl_pct = (current_price - p.entry_price) / p.entry_price
            if p.direction == ActionDirection.SHORT.name:
                pnl_pct *= -1
            unrealized += p.size_usd * pnl_pct
        self.equity = self.balance + unrealized

    def apply_funding(self, step: int):
        if self.config.funding_rate_per_interval == 0:
            return
        if self.config.funding_interval_candles <= 0:
            return
        if step % self.config.funding_interval_candles != 0:
            return

        rate = self.config.funding_rate_per_interval / 100.0
        for p in self.positions:
            funding_fee = p.size_usd * rate
            if p.direction == ActionDirection.LONG.name:
                self.balance -= funding_fee
                p.funding_accrued -= funding_fee
            else:
                self.balance += funding_fee
                p.funding_accrued += funding_fee

    def close_position(self, pos: BacktestPosition, exit_price: float, reason: str, step: int):
        if pos not in self.positions:
            return None

        # Apply exit fee
        direction = pos.direction
        pnl_pct = (exit_price - pos.entry_price) / pos.entry_price
        if direction == ActionDirection.SHORT.name:
            pnl_pct *= -1
        unrealized = pos.size_usd * pnl_pct
        current_value = pos.size_usd + unrealized
        exit_fee = current_value * self.config.fee_rate

        realized_pnl = unrealized - pos.entry_fee - exit_fee + pos.funding_accrued
        margin_used = pos.size_usd / max(1, pos.leverage)
        self.balance += (margin_used + realized_pnl)

        self.positions.remove(pos)

        trade = {
            "symbol": pos.symbol,
            "direction": pos.direction,
            "entry_price": pos.entry_price,
            "exit_price": exit_price,
            "size_usd": pos.size_usd,
            "strategy": pos.strategy,
            "entry_regime": pos.entry_regime,
            "entry_fee": pos.entry_fee,
            "exit_fee": exit_fee,
            "funding": pos.funding_accrued,
            "realized_pnl_usd": realized_pnl,
            "realized_pnl_pct": (realized_pnl / pos.size_usd) * 100 if pos.size_usd > 0 else 0.0,
            "reason": reason,
            "entry_step": pos.entry_step,
            "exit_step": step,
            "decision_id": pos.decision_id
        }
        self.trade_history.append(trade)
        return trade


def _apply_slippage(price: float, direction: str, side: str, slippage_bps: float) -> float:
    if slippage_bps <= 0:
        return price
    slip = slippage_bps / 10000.0
    if side == "entry":
        return price * (1 + slip) if direction == ActionDirection.LONG.name else price * (1 - slip)
    # exit
    return price * (1 - slip) if direction == ActionDirection.LONG.name else price * (1 + slip)


class BacktestEngine:
    def __init__(self, csv_path: str, symbol: str, config: Optional[BacktestConfig] = None, log_suffix: str = "backtest", data_path: Optional[str] = None):
        self.csv_path = csv_path
        self.symbol = symbol
        self.config = config or BacktestConfig()
        self.engine = TradingEngine(log_suffix=log_suffix)
        if data_path:
            # Override DB path to avoid locks against active logs
            os.makedirs(data_path, exist_ok=True)
            self.engine.db.filepath = os.path.join(data_path, f"experience_log_{log_suffix}.jsonl")
            self.engine.db.lockpath = self.engine.db.filepath + ".lock"
        self.feeder = ReplayFeeder(csv_path, symbol=symbol)
        self.portfolio = BacktestPortfolio(self.config)
        self.pending_orders: List[Dict[str, Any]] = []
        self.perf_tracker = StrategyPerformanceTracker(window=Config.STRATEGY_FILTER_WINDOW)
        self.engine.db.enable_buffer_mode()

    def run(self) -> Dict[str, Any]:
        step = 0
        while True:
            state = self.feeder.get_next_state()
            if not state:
                break

            candle = self.feeder.get_latest_candle()
            if not candle:
                break

            open_price = float(candle[1])
            high_price = float(candle[2])
            low_price = float(candle[3])
            close_price = float(candle[4])

            # Execute pending orders after latency
            if self.pending_orders:
                ready = [o for o in self.pending_orders if step - o["created_step"] >= self.config.latency_candles]
                self.pending_orders = [o for o in self.pending_orders if o not in ready]
                for order in ready:
                    action = order["action"]
                    if action.strategy == StrategyType.WAIT:
                        continue
                    direction = action.direction.name
                    entry = _apply_slippage(open_price, direction, "entry", self.config.slippage_bps)
                    trade_mode, tp, sl, _, _ = calculate_tp_sl(
                        entry_price=entry,
                        direction=direction,
                        atr=order.get("atr", 0.0),
                        regime=order.get("regime", state.market_regime.value),
                        trend_strength=order.get("trend_strength", state.trend_strength.value)
                    )
                    size_usd = self.portfolio.balance * self.config.max_position_pct
                    pos = BacktestPosition(
                        symbol=self.symbol,
                        direction=direction,
                        entry_price=entry,
                        size_usd=size_usd,
                        leverage=self.config.leverage,
                        tp=tp,
                        sl=sl,
                        entry_step=step,
                        decision_id=order["decision_id"],
                        strategy=action.strategy.name,
                        entry_regime=order.get("regime", state.market_regime.value)
                    )
                    self.portfolio.open_position(pos)

            # Update funding and equity
            self.portfolio.apply_funding(step)
            self.portfolio.update_equity(close_price)

            # Check exits for open positions (TP/SL within candle)
            to_close: List[BacktestPosition] = []
            for pos in self.portfolio.positions:
                exit_price = None
                reason = None
                if pos.direction == ActionDirection.LONG.name:
                    if low_price <= pos.sl:
                        exit_price, reason = pos.sl, "SL"
                    if high_price >= pos.tp:
                        exit_price, reason = pos.tp, "TP"
                else:
                    if high_price >= pos.sl:
                        exit_price, reason = pos.sl, "SL"
                    if low_price <= pos.tp:
                        exit_price, reason = pos.tp, "TP"
                if exit_price:
                    exit_price = _apply_slippage(exit_price, pos.direction, "exit", self.config.slippage_bps)
                    to_close.append((pos, exit_price, reason))

            for pos, exit_price, reason in to_close:
                trade = self.portfolio.close_position(pos, exit_price, reason, step)
                if trade:
                    reward = RewardCalculator.calculate_final_reward(
                        exit_reason=reason,
                        realized_pnl=trade["realized_pnl_pct"],
                        duration_candles=step - pos.entry_step,
                        repetition_count=0
                    )
                    strat_name = trade.get("strategy")
                    entry_regime = trade.get("entry_regime")
                    pnl_pct = trade.get("realized_pnl_pct", 0.0)
                    if strat_name:
                        self.perf_tracker.record(strat_name, pnl_pct)
                        if entry_regime:
                            self.perf_tracker.record(f"{strat_name}|{entry_regime}", pnl_pct)
                    self.engine.db.finalize_record(
                        decision_id=pos.decision_id,
                        outcome_data={"exit_price": exit_price, "reason": reason, "pnl_usd": trade["realized_pnl_usd"]},
                        final_reward=reward
                    )

            # Decide next action
            if Config.STRATEGY_FILTER_ENABLED or Config.STRATEGY_WEIGHTING_ENABLED:
                strategy_weights = {}
                blocked = set()
                for strat in StrategyType:
                    if strat == StrategyType.WAIT:
                        continue
                    key = f"{strat.name}|{state.market_regime.value}" if Config.STRATEGY_FILTER_REGIME_AWARE else strat.name
                    if Config.STRATEGY_WEIGHTING_ENABLED:
                        strategy_weights[strat] = self.perf_tracker.get_weight(
                            key, min_samples=Config.STRATEGY_MIN_SAMPLES
                        )
                    if Config.STRATEGY_FILTER_ENABLED and self.perf_tracker.is_blocked(
                        key,
                        min_samples=Config.STRATEGY_FILTER_MIN_TRADES,
                        min_win_rate=Config.STRATEGY_FILTER_MIN_WIN_RATE,
                        min_avg_pnl=Config.STRATEGY_FILTER_MIN_AVG_PNL
                    ):
                        blocked.add(strat)
                self.engine.set_strategy_overrides(strategy_weights=strategy_weights, blocked_strategies=blocked)
            else:
                self.engine.set_strategy_overrides()

            action, decision_id, _ = self.engine.run_analysis(state, data_source="backtest")
            if action.strategy != StrategyType.WAIT and self.portfolio.can_open(self.symbol):
                self.pending_orders.append({
                    "action": action,
                    "decision_id": decision_id,
                    "created_step": step,
                    "atr": state.atr,
                    "regime": state.market_regime.value,
                    "trend_strength": state.trend_strength.value
                })

            if step % 1000 == 0:
                print(f"Backtest Progress: {step} steps processed...")
            
            step += 1

        # Final equity update
        if self.portfolio.positions:
            self.portfolio.update_equity(close_price)

        self.engine.db.flush_records()

        return {
            "final_balance": self.portfolio.balance,
            "final_equity": self.portfolio.equity,
            "trades": self.portfolio.trade_history,
            "trade_count": len(self.portfolio.trade_history)
        }


class FastBacktestEngine(BacktestEngine):
    """
    Faster variant that disables DB logging in the trading engine.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable logging to JSONL for speed
        self.engine.db.log_decision = lambda *a, **k: "noop"
        self.engine.db.finalize_record = lambda *a, **k: None
