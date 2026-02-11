from dataclasses import dataclass
from typing import Optional

from src.config import Config


@dataclass
class CanaryState:
    trades: int = 0
    wins: int = 0
    peak_equity: float = 0.0
    halted: bool = False
    reason: Optional[str] = None


class CanaryMonitor:
    def __init__(self, initial_equity: float):
        self.state = CanaryState(peak_equity=initial_equity)

    def record_trade(self, pnl_pct: float):
        self.state.trades += 1
        if pnl_pct > 0:
            self.state.wins += 1

    def update_equity(self, equity: float):
        if equity > self.state.peak_equity:
            self.state.peak_equity = equity

    def check(self, equity: float) -> Optional[str]:
        if not Config.CANARY_MODE:
            return None
        self.update_equity(equity)
        if self.state.trades < Config.CANARY_TRADE_LIMIT:
            return None
        win_rate = self.state.wins / max(1, self.state.trades)
        drawdown = (self.state.peak_equity - equity) / max(1e-9, self.state.peak_equity) * 100
        if win_rate < Config.CANARY_MIN_WIN_RATE:
            self.state.halted = True
            self.state.reason = f"Canary win rate {win_rate:.2f} < {Config.CANARY_MIN_WIN_RATE:.2f}"
            return self.state.reason
        if drawdown > Config.CANARY_MAX_DD_PCT:
            self.state.halted = True
            self.state.reason = f"Canary DD {drawdown:.2f}% > {Config.CANARY_MAX_DD_PCT:.2f}%"
            return self.state.reason
        return None
