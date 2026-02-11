import numpy as np
import pandas as pd

from src.portfolio.risk import RiskManager


class PortfolioAllocator:
    def __init__(self, risk_manager: RiskManager):
        self.risk = risk_manager

    def _apply_correlation_penalty(self, weights: dict[str, float], strategy_returns: pd.DataFrame | None) -> dict[str, float]:
        if strategy_returns is None or strategy_returns.empty or len(weights) < 2:
            return weights

        corr = strategy_returns.corr().fillna(0.0).abs()
        penalized = dict(weights)
        keys = list(weights.keys())
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                a, b = keys[i], keys[j]
                if a not in corr.index or b not in corr.columns:
                    continue
                if corr.loc[a, b] >= 0.7:
                    penalized[a] *= 0.75
                    penalized[b] *= 0.75
        return penalized

    def allocate(
        self,
        signals: dict,
        current_prices: dict[str, float],
        historical_prices: dict[str, pd.Series],
        strategy_returns: pd.DataFrame | None = None,
    ) -> dict[str, float]:
        if not signals:
            return {}

        # Base weights: direction * confidence
        weights = {}
        for name, sig in signals.items():
            direction = float(getattr(sig, "signal", 0.0))
            confidence = float(getattr(sig, "confidence", 0.0))
            weights[name] = direction * confidence

        # Volatility targeting from first available asset history.
        price_series = next(iter(historical_prices.values())) if historical_prices else None
        vol_scale = self.risk.volatility_scaler(price_series) if price_series is not None else 1.0
        weights = {k: v * vol_scale for k, v in weights.items()}

        # Correlation-aware haircut.
        weights = self._apply_correlation_penalty(weights, strategy_returns)

        # Final hard caps.
        return self.risk.cap_positions(weights)
