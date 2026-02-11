import pandas as pd


class SampleWeights:
    @staticmethod
    def get_sample_weights(t1: pd.Series, close_index: pd.Index) -> pd.Series:
        if t1 is None or t1.empty:
            return pd.Series(dtype=float)

        close_index = pd.Index(close_index)
        concurrency = pd.Series(0.0, index=close_index)

        for t0, end in t1.items():
            if pd.isna(t0):
                continue
            if pd.isna(end):
                end = close_index[-1]
            mask = (close_index >= t0) & (close_index <= end)
            concurrency.loc[mask] += 1.0

        weights = pd.Series(index=t1.index, dtype=float)
        for t0, end in t1.items():
            if pd.isna(end):
                end = close_index[-1]
            mask = (close_index >= t0) & (close_index <= end)
            avg_conc = concurrency.loc[mask].mean() if mask.any() else 1.0
            weights.loc[t0] = 1.0 / max(avg_conc, 1.0)

        return weights.fillna(1.0)
