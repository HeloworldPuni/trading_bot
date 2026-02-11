import pandas as pd

from src.strategies.base import AbstractBaseStrategy, StrategySignal


class MeanReversionStrategy(AbstractBaseStrategy):
    def __init__(self, rsi_buy: float = 30.0, rsi_sell: float = 70.0, model_threshold: float = 0.5):
        self.rsi_buy = float(rsi_buy)
        self.rsi_sell = float(rsi_sell)
        super().__init__(name="MeanReversion", model_threshold=model_threshold)

    def generate_signal(self, row: pd.Series, context: pd.Series | None = None) -> StrategySignal:
        context = context if context is not None else pd.Series(dtype=float)
        trend_regime = int(context.get("trend_regime", 0))
        if trend_regime == 1:
            return StrategySignal(0, 0.0, {"reason": "Regime blocked"})

        close = float(row.get("close", 0.0))
        bb_upper = float(row.get("bb_upper", close))
        bb_lower = float(row.get("bb_lower", close))
        rsi = float(row.get("rsi", 50.0))

        if close < bb_lower and rsi <= self.rsi_buy:
            raw = StrategySignal(1, min(1.0, 0.55 + (self.rsi_buy - rsi) / 100.0), {"direction": "LONG"})
        elif close > bb_upper and rsi >= self.rsi_sell:
            raw = StrategySignal(-1, min(1.0, 0.55 + (rsi - self.rsi_sell) / 100.0), {"direction": "SHORT"})
        else:
            raw = StrategySignal(0, 0.0, {"reason": "No reversion setup"})

        return self.apply_model_filter(raw, row)
