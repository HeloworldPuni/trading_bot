import pandas as pd


class MetaLabeler:
    @staticmethod
    def get_meta_labels(events: pd.DataFrame, close_prices: pd.Series) -> pd.DataFrame:
        if events is None or events.empty:
            return pd.DataFrame(columns=["ret", "bin"])

        close = pd.to_numeric(close_prices, errors="coerce").astype(float)
        out = events.copy()
        side = pd.to_numeric(out.get("side", 1), errors="coerce").fillna(1.0)
        t1 = out.get("t1")

        rets = []
        for t0, end in zip(out.index, t1):
            if t0 not in close.index:
                rets.append(0.0)
                continue
            t_end = end if end in close.index else close.index[close.index.searchsorted(end, side="right") - 1] if pd.notna(end) else close.index[-1]
            p0 = float(close.loc[t0])
            p1 = float(close.loc[t_end]) if t_end in close.index else p0
            rets.append((p1 / p0 - 1.0) if p0 > 0 else 0.0)

        out["ret"] = pd.Series(rets, index=out.index) * side.values
        out["bin"] = (out["ret"] > 0).astype(int)
        return out
