from typing import Dict, Optional


class DivergenceMonitor:
    """
    Tracks live vs backtest metrics divergence in a lightweight way.
    """
    def __init__(self):
        self.baseline = {}

    def set_baseline(self, metrics: Dict[str, float]):
        self.baseline = metrics or {}

    def check(self, live_metrics: Dict[str, float], thresholds: Optional[Dict[str, float]] = None) -> Optional[str]:
        if not self.baseline:
            return None
        thresholds = thresholds or {"win_rate": 0.15, "avg_pnl": 0.5}
        for key, tol in thresholds.items():
            if key in live_metrics and key in self.baseline:
                diff = abs(live_metrics[key] - self.baseline[key])
                if diff > tol:
                    return f"Divergence on {key}: live {live_metrics[key]:.3f} vs base {self.baseline[key]:.3f}"
        return None
