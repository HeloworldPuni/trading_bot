import numpy as np
import pandas as pd


class RelativeFeatures:
    @staticmethod
    def calc_relative_strength(asset_close: pd.Series, benchmark_close: pd.Series, window: int = 20) -> pd.Series:
        asset_ret = pd.to_numeric(asset_close, errors="coerce").pct_change()
        bench_ret = pd.to_numeric(benchmark_close, errors="coerce").pct_change()
        rs = (asset_ret - bench_ret).rolling(window=window, min_periods=max(5, window // 4)).mean().fillna(0.0)
        rs.name = "relative_strength"
        return rs

    @staticmethod
    def calc_beta(asset_close: pd.Series, benchmark_close: pd.Series, window: int = 50) -> pd.Series:
        asset_ret = pd.to_numeric(asset_close, errors="coerce").pct_change().fillna(0.0)
        bench_ret = pd.to_numeric(benchmark_close, errors="coerce").pct_change().fillna(0.0)
        cov = asset_ret.rolling(window=window, min_periods=max(10, window // 5)).cov(bench_ret)
        var = bench_ret.rolling(window=window, min_periods=max(10, window // 5)).var()
        beta = (cov / var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan).fillna(0.0)
        beta.name = "beta"
        return beta
