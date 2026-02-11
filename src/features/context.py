import numpy as np
import pandas as pd


class ContextFeatures:
    @staticmethod
    def calc_volatility_expansion(close: pd.Series, short_span: int = 10, long_span: int = 50) -> pd.Series:
        close = pd.to_numeric(close, errors="coerce").astype(float)
        rets = close.pct_change().fillna(0.0)
        short_vol = rets.ewm(span=max(2, short_span), adjust=False).std().abs()
        long_vol = rets.ewm(span=max(short_span + 1, long_span), adjust=False).std().abs()
        out = (short_vol / long_vol.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan).fillna(0.0)
        out.name = "vol_expansion"
        return out

    @staticmethod
    def calc_funding_divergence(funding_rate: pd.Series, price: pd.Series, window: int = 20) -> pd.Series:
        funding = pd.to_numeric(funding_rate, errors="coerce").fillna(0.0)
        rets = pd.to_numeric(price, errors="coerce").pct_change().fillna(0.0)
        corr = funding.rolling(window=window, min_periods=max(5, window // 4)).corr(rets).fillna(0.0)
        # Divergence = inverse correlation (higher means funding disagrees with price move)
        out = -corr
        out.name = "funding_divergence"
        return out
