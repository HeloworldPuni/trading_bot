import pandas as pd

from src.strategies.base import AbstractBaseStrategy, StrategySignal


class TrendFollowingStrategy(AbstractBaseStrategy):
    def __init__(self, adx_threshold: float = 20.0, model_threshold: float = 0.5):
        self.adx_threshold = float(adx_threshold)
        super().__init__(name="TrendFollowing", model_threshold=model_threshold)

    def generate_signal(self, row: pd.Series, context: pd.Series | None = None) -> StrategySignal:
        context = context if context is not None else pd.Series(dtype=float)

        trend_regime = int(context.get("trend_regime", 1))
        if trend_regime != 1:
            return StrategySignal(0, 0.0, {"reason": "Regime blocked"})

        ema_20 = float(row.get("ema_20", 0.0))
        ema_50 = float(row.get("ema_50", 0.0))
        adx = float(row.get("adx", 0.0))
        if adx < self.adx_threshold:
            return StrategySignal(0, 0.0, {"reason": "ADX below threshold"})

        if ema_20 > ema_50:
            raw = StrategySignal(1, min(1.0, 0.5 + (adx / 100.0)), {"direction": "LONG"})
        elif ema_20 < ema_50:
            raw = StrategySignal(-1, min(1.0, 0.5 + (adx / 100.0)), {"direction": "SHORT"})
        else:
            raw = StrategySignal(0, 0.0, {"reason": "No EMA edge"})

        return self.apply_model_filter(raw, row)
