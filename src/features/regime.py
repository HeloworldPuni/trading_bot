import numpy as np
import pandas as pd


class RegimeDetector:
    @staticmethod
    def get_volatility_regime(close: pd.Series, window: int = 50) -> pd.Series:
        returns = pd.to_numeric(close, errors="coerce").pct_change().fillna(0.0)
        vol = returns.rolling(window=window, min_periods=max(10, window // 5)).std().fillna(0.0)
        low = vol.quantile(0.33)
        high = vol.quantile(0.66)
        regime = pd.Series(1, index=vol.index, dtype=int)
        regime[vol <= low] = 0
        regime[vol >= high] = 2
        return regime

    @staticmethod
    def get_trend_regime(high: pd.Series, low: pd.Series, close: pd.Series, fast: int = 20, slow: int = 50) -> pd.Series:
        c = pd.to_numeric(close, errors="coerce").astype(float)
        ema_fast = c.ewm(span=fast, adjust=False).mean()
        ema_slow = c.ewm(span=slow, adjust=False).mean()
        spread = (ema_fast - ema_slow).abs() / ema_slow.replace(0.0, np.nan)
        trend = (spread > 0.002).astype(int).fillna(0)
        return trend

    @staticmethod
    def get_liquidity_regime(orderbook_df: pd.DataFrame) -> pd.Series:
        if orderbook_df is None or orderbook_df.empty:
            return pd.Series(dtype=int)

        bid = pd.to_numeric(orderbook_df.get("bid1_p"), errors="coerce")
        ask = pd.to_numeric(orderbook_df.get("ask1_p"), errors="coerce")
        mid = (bid + ask) / 2.0
        spread = (ask - bid).abs()
        spread_rel = (spread / mid.replace(0.0, np.nan)).fillna(1.0)
        liquid = (spread_rel < 0.0015).astype(int).fillna(0)
        return liquid
