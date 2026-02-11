import pandas as pd

from src.features.regime import RegimeDetector


class StrategyDataset:
    def __init__(self, feature_store):
        self.store = feature_store

    def _add_indicators(self, bars: pd.DataFrame) -> pd.DataFrame:
        df = bars.copy()
        close = pd.to_numeric(df["close"], errors="coerce")
        df["ema_20"] = close.ewm(span=20, adjust=False).mean()
        df["ema_50"] = close.ewm(span=50, adjust=False).mean()
        sma = close.rolling(20).mean()
        std = close.rolling(20).std()
        df["bb_upper"] = sma + (2 * std)
        df["bb_lower"] = sma - (2 * std)
        delta = close.diff()
        up = delta.clip(lower=0).ewm(com=13, adjust=False).mean()
        down = (-delta.clip(upper=0)).ewm(com=13, adjust=False).mean()
        rs = up / down.replace(0.0, pd.NA)
        df["rsi"] = (100 - (100 / (1 + rs))).fillna(50.0)
        tr1 = df["high"] - df["low"]
        tr2 = (df["high"] - close.shift(1)).abs()
        tr3 = (df["low"] - close.shift(1)).abs()
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        df["atr"] = tr.rolling(14).mean().fillna(0.0)
        df["adx"] = 25.0
        df["funding_rate"] = 0.0
        df["vol_expansion"] = 1.0
        df["funding_divergence"] = 0.0
        df["spread_rel"] = 0.0
        df["ofi"] = 0.0
        return df

    def prepare_dataset(self, strategy) -> tuple[pd.DataFrame, pd.Series]:
        trades = self.store.load_trades()
        if trades.empty:
            return pd.DataFrame(), pd.Series(dtype=int)

        bars = self.store.resample_trades(trades, rule="5min")
        if bars.empty or len(bars) < 100:
            return pd.DataFrame(), pd.Series(dtype=int)

        bars = self._add_indicators(bars)
        ctx = pd.DataFrame(index=bars.index)
        ctx["trend_regime"] = RegimeDetector.get_trend_regime(bars["high"], bars["low"], bars["close"])
        ctx["vol_regime"] = RegimeDetector.get_volatility_regime(bars["close"]).clip(upper=1)

        fwd_ret = bars["close"].shift(-3) / bars["close"] - 1.0
        rows = []
        labels = []

        for i in range(60, len(bars) - 4):
            row = bars.iloc[i]
            c = ctx.iloc[i]
            sig = strategy.generate_signal(row, c)
            if sig.signal == 0:
                continue
            realized = float(fwd_ret.iloc[i])
            outcome = 1 if (sig.signal * realized) > 0 else 0
            rows.append(row)
            labels.append(outcome)

        if not rows:
            return pd.DataFrame(), pd.Series(dtype=int)

        X = pd.DataFrame(rows).fillna(0.0)
        y = pd.Series(labels, index=X.index).astype(int)
        return X, y
