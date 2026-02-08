import math
from dataclasses import dataclass
from datetime import datetime, date
from typing import Dict, Any, Optional, Tuple, List

from src.config import Config


@dataclass
class RiskState:
    peak_equity: float
    daily_start_equity: float
    daily_date: date
    halted: bool = False
    halt_reason: Optional[str] = None


class PortfolioRiskManager:
    """
    Portfolio-level risk controls.
    """
    def __init__(self, initial_equity: float):
        today = datetime.utcnow().date()
        self.state = RiskState(
            peak_equity=initial_equity,
            daily_start_equity=initial_equity,
            daily_date=today
        )

    def update_equity(self, equity: float):
        if equity > self.state.peak_equity:
            self.state.peak_equity = equity

        today = datetime.utcnow().date()
        if today != self.state.daily_date:
            self.state.daily_date = today
            self.state.daily_start_equity = equity
            self.state.halted = False
            self.state.halt_reason = None

    def check_limits(self, equity: float, initial_equity: float) -> Tuple[bool, Optional[str]]:
        """
        Returns (halted, reason).
        """
        self.update_equity(equity)

        # Max daily loss
        daily_loss = (self.state.daily_start_equity - equity) / max(1e-9, self.state.daily_start_equity) * 100
        if daily_loss >= Config.MAX_DAILY_LOSS_PCT:
            self.state.halted = True
            self.state.halt_reason = f"Daily loss {daily_loss:.2f}% >= {Config.MAX_DAILY_LOSS_PCT:.2f}%"
            return True, self.state.halt_reason

        # Max drawdown from peak
        drawdown = (self.state.peak_equity - equity) / max(1e-9, self.state.peak_equity) * 100
        if drawdown >= Config.MAX_DRAWDOWN_PCT:
            self.state.halted = True
            self.state.halt_reason = f"Drawdown {drawdown:.2f}% >= {Config.MAX_DRAWDOWN_PCT:.2f}%"
            return True, self.state.halt_reason

        return False, None

    def volatility_scaler(self, daily_vol_pct: float) -> float:
        """
        Returns a scaling factor based on realized daily vol.
        """
        if daily_vol_pct <= 0:
            return 1.0
        target = Config.VOL_TARGET_DAILY_PCT
        if target <= 0:
            return 1.0
        return max(0.25, min(1.5, target / daily_vol_pct))


def compute_daily_vol(returns: List[float]) -> float:
    if not returns:
        return 0.0
    mean = sum(returns) / len(returns)
    var = sum((r - mean) ** 2 for r in returns) / len(returns)
    return math.sqrt(var)


def compute_gross_exposure(open_positions: List[Dict[str, Any]], equity: float) -> float:
    if equity <= 0:
        return 0.0
    exposure = sum(p.get("size_usd", 0.0) for p in open_positions)
    return exposure / equity


def cluster_exposure(open_positions: List[Dict[str, Any]], equity: float, clusters: Dict[str, str]) -> Dict[str, float]:
    """
    Aggregate exposure by cluster using a simple symbol->cluster mapping.
    """
    totals: Dict[str, float] = {}
    if equity <= 0:
        return totals
    for p in open_positions:
        sym = p.get("symbol")
        cluster = clusters.get(sym, "OTHER")
        totals[cluster] = totals.get(cluster, 0.0) + p.get("size_usd", 0.0)
    return {k: v / equity for k, v in totals.items()}
