
import pandas as pd
import numpy as np
from statistics import NormalDist

class RiskMetrics:
    """
    Phase 9: Institutional Risk Metrics (VaR, ES, Kelly).
    """
    @staticmethod
    def calculate_var_historical(returns: pd.Series, confidence: float = 0.95) -> float:
        if len(returns) < 30: return 0.0
        cutoff = 1.0 - confidence
        var_val = returns.quantile(cutoff)
        return abs(var_val) if var_val < 0 else 0.0

    @staticmethod
    def calculate_expected_shortfall(returns: pd.Series, confidence: float = 0.95) -> float:
        if len(returns) < 30: return 0.0
        cutoff = 1.0 - confidence
        var_cutoff = returns.quantile(cutoff)
        tail_losses = returns[returns <= var_cutoff]
        if tail_losses.empty: return 0.0
        return abs(tail_losses.mean())

    @staticmethod
    def calculate_parametric_var(returns: pd.Series, confidence: float = 0.95) -> float:
        """
        Gaussian (parametric) VaR using sample mean and std dev.
        Returns positive loss magnitude.
        """
        if len(returns) < 30:
            return 0.0
        mu = float(np.mean(returns))
        sigma = float(np.std(returns, ddof=1))
        if sigma <= 0:
            return 0.0
        z = float(NormalDist().inv_cdf(1.0 - confidence))
        var_val = mu + z * sigma
        return abs(var_val) if var_val < 0 else 0.0

    @staticmethod
    def calculate_kelly(win_rate: float, avg_win: float, avg_loss: float) -> float:
        if avg_loss == 0: return 1.0
        win_loss_ratio = abs(avg_win / avg_loss)
        if win_loss_ratio == 0: return 0.0
        kelly = win_rate - ((1.0 - win_rate) / win_loss_ratio)
        return max(0.0, kelly)
