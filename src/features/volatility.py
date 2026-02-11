import numpy as np
import pandas as pd


class VolatilityEstimator:
    @staticmethod
    def get_daily_vol(close_prices: pd.Series, span: int = 100) -> pd.Series:
        close = pd.to_numeric(close_prices, errors="coerce").astype(float)
        returns = close.pct_change().fillna(0.0)
        vol = returns.ewm(span=max(2, span), adjust=False).std().abs()
        # Keep as per-bar estimate; scripts mostly use it as dynamic target.
        return vol.replace([np.inf, -np.inf], np.nan).fillna(0.0)
