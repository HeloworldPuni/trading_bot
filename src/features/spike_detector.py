import pandas as pd


class SpikeDetector:
    @staticmethod
    def detect_spikes(close_prices: pd.Series, sigma: float = 4.0, window: int = 50) -> pd.Series:
        close = pd.to_numeric(close_prices, errors="coerce")
        returns = close.pct_change().fillna(0.0)
        # Use prior-window volatility so current spike does not dilute its own threshold.
        rolling_std = returns.rolling(window=window, min_periods=max(10, window // 5)).std().shift(1)
        fallback_std = returns.expanding(min_periods=max(10, window // 5)).std().shift(1)
        effective_std = rolling_std.fillna(fallback_std).fillna(0.0)
        threshold = effective_std * float(sigma)
        spikes = returns.abs() > threshold
        return spikes.fillna(False)
