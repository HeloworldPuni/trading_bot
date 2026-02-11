
import logging
from typing import Dict, List

logger = logging.getLogger(__name__)

class PerformanceMonitor:
    """
    Phase 10 Retrofit: Performance Decay Monitoring.
    Tracks Sharpe Ratio and Drawdown in real-time.
    """
    def __init__(self, window_size: int = 100):
        self.daily_pnls: List[float] = []
        self.window_size = window_size

    def update(self, daily_pnl_pct: float):
        self.daily_pnls.append(daily_pnl_pct)
        if len(self.daily_pnls) > self.window_size:
            self.daily_pnls.pop(0)

    def get_sharpe_ratio(self) -> float:
        if len(self.daily_pnls) < 2:
            return 0.0
        
        # Simple annualized sharpe approximation
        import numpy as np
        returns = np.array(self.daily_pnls)
        mean_ret = np.mean(returns)
        std_dev = np.std(returns)
        
        if std_dev == 0:
            return 0.0
            
        # Annualized (assuming daily returns)
        return (mean_ret / std_dev) * np.sqrt(252)
