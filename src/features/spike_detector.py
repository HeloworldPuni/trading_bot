import pandas as pd


class SpikeDetector:
    @staticmethod
    def detect_spikes(close_prices: pd.Series, sigma: float = 4.0, window: int = 50) -> pd.Series:
        close = pd.to_numeric(close_prices, errors="coerce")
        returns = close.pct_change().fillna(0.0)
        rolling_std = returns.rolling(window=window, min_periods=max(10, window // 5)).std()
        spikes = returns.abs() > (rolling_std * float(sigma))
        return spikes.fillna(False)
