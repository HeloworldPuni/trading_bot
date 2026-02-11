import pandas as pd
import numpy as np


class TripleBarrierLabeler:
    """
    Triple-barrier labeling for event-driven supervision.
    Labels:
    -  1: profit barrier hit first
    - -1: stop barrier hit first
    -  0: vertical barrier reached first
    """

    def __init__(self, profit_take: float = 0.02, stop_loss: float = 0.01, time_limit: int = 10):
        self.pt = float(profit_take)
        self.sl = float(stop_loss)
        self.limit = int(time_limit)

    def label(self, prices: pd.Series) -> pd.Series:
        if prices is None or prices.empty:
            return pd.Series(dtype=int)

        if not isinstance(prices.index, pd.DatetimeIndex):
            idx = pd.date_range("1970-01-01", periods=len(prices), freq="min")
            prices = pd.Series(prices.values, index=idx)

        target = prices.pct_change().ewm(span=20, min_periods=5).std().abs().fillna(0.0)
        vertical = pd.Series(prices.index.to_series().shift(-self.limit), index=prices.index)
        events = TripleBarrierLabeler.get_events(
            close_prices=prices,
            t_events=prices.index,
            pt_sl=[self.pt, self.sl],
            target=target,
            min_ret=0.0,
            vertical_barrier_times=vertical,
        )
        return events["label"].reindex(prices.index).fillna(0).astype(int)

    @staticmethod
    def _resolve_barrier_time(close_prices: pd.Series, end_time) -> pd.Timestamp | None:
        if close_prices.empty:
            return None
        if pd.isna(end_time):
            return close_prices.index[-1]
        if end_time <= close_prices.index[0]:
            return close_prices.index[0]
        if end_time >= close_prices.index[-1]:
            return close_prices.index[-1]
        loc = close_prices.index.searchsorted(end_time, side="right") - 1
        if loc < 0:
            return None
        return close_prices.index[loc]

    @staticmethod
    def get_events(
        close_prices: pd.Series,
        t_events,
        pt_sl,
        target: pd.Series,
        min_ret: float = 0.0,
        vertical_barrier_times: pd.Series | None = None,
    ) -> pd.DataFrame:
        """
        Event labeling API used by training scripts.
        """
        if close_prices is None or close_prices.empty:
            return pd.DataFrame(columns=["t1", "trgt", "pt", "sl", "ret", "label"])

        close = close_prices.sort_index().astype(float)
        t_events = pd.Index(t_events).intersection(close.index)
        if len(t_events) == 0:
            return pd.DataFrame(columns=["t1", "trgt", "pt", "sl", "ret", "label"])

        if target is None or target.empty:
            target = close.pct_change().rolling(20, min_periods=5).std().abs()
        target = target.reindex(close.index).fillna(method="ffill").fillna(method="bfill").fillna(0.0)

        if vertical_barrier_times is None:
            # Fallback vertical barrier: 10 bars ahead.
            vertical_barrier_times = pd.Series(close.index.to_series().shift(-10), index=close.index)
        else:
            vertical_barrier_times = vertical_barrier_times.reindex(close.index)

        pt_mult = float(pt_sl[0]) if pt_sl and len(pt_sl) > 0 else 0.0
        sl_mult = float(pt_sl[1]) if pt_sl and len(pt_sl) > 1 else 0.0

        rows = []
        for t0 in t_events:
            trgt = float(target.loc[t0]) if t0 in target.index else 0.0
            if not np.isfinite(trgt) or trgt < float(min_ret):
                continue

            p0 = float(close.loc[t0])
            raw_t1 = vertical_barrier_times.loc[t0] if t0 in vertical_barrier_times.index else close.index[-1]
            t1 = TripleBarrierLabeler._resolve_barrier_time(close, raw_t1)
            if t1 is None or t1 < t0:
                continue

            path = close.loc[t0:t1]
            if path.empty:
                continue

            pt_price = p0 * (1.0 + pt_mult * trgt) if pt_mult > 0 else np.inf
            sl_price = p0 * (1.0 - sl_mult * trgt) if sl_mult > 0 else -np.inf

            label = 0
            t_end = t1
            for ts, px in path.iloc[1:].items():
                px = float(px)
                if px >= pt_price:
                    label = 1
                    t_end = ts
                    break
                if px <= sl_price:
                    label = -1
                    t_end = ts
                    break

            p_end = float(close.loc[t_end])
            ret = (p_end / p0) - 1.0 if p0 > 0 else 0.0
            rows.append({"t0": t0, "t1": t_end, "trgt": trgt, "pt": pt_price, "sl": sl_price, "ret": ret, "label": int(label)})

        if not rows:
            return pd.DataFrame(columns=["t1", "trgt", "pt", "sl", "ret", "label"])

        out = pd.DataFrame(rows).set_index("t0").sort_index()
        return out
