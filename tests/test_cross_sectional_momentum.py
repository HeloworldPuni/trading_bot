import unittest

from src.config import Config
from src.core.definitions import (
    ActionDirection,
    MarketRegime,
    MarketState,
    StrategyType,
    TrendStrength,
    VolatilityLevel,
)
from src.engine.system import TradingEngine


class TestCrossSectionalMomentum(unittest.TestCase):
    def setUp(self):
        self._orig_wait_prob = Config.STRATEGIC_WAIT_PROB
        self._orig_cross_enabled = Config.CROSS_SECTIONAL_MOMENTUM_ENABLED
        self._orig_cross_min_universe = Config.CROSS_SECTIONAL_MIN_UNIVERSE
        self._orig_cross_top = Config.CROSS_SECTIONAL_TOP_PCT
        self._orig_cross_bottom = Config.CROSS_SECTIONAL_BOTTOM_PCT
        self._orig_cross_spread = Config.CROSS_SECTIONAL_MIN_ABS_SPREAD

        Config.STRATEGIC_WAIT_PROB = 0.0
        Config.CROSS_SECTIONAL_MOMENTUM_ENABLED = True
        Config.CROSS_SECTIONAL_MIN_UNIVERSE = 8
        Config.CROSS_SECTIONAL_TOP_PCT = 0.20
        Config.CROSS_SECTIONAL_BOTTOM_PCT = 0.20
        Config.CROSS_SECTIONAL_MIN_ABS_SPREAD = 0.20

        self.engine = TradingEngine()
        self.engine.policy.predict_confidence = lambda *args, **kwargs: 0.75

    def tearDown(self):
        Config.STRATEGIC_WAIT_PROB = self._orig_wait_prob
        Config.CROSS_SECTIONAL_MOMENTUM_ENABLED = self._orig_cross_enabled
        Config.CROSS_SECTIONAL_MIN_UNIVERSE = self._orig_cross_min_universe
        Config.CROSS_SECTIONAL_TOP_PCT = self._orig_cross_top
        Config.CROSS_SECTIONAL_BOTTOM_PCT = self._orig_cross_bottom
        Config.CROSS_SECTIONAL_MIN_ABS_SPREAD = self._orig_cross_spread

    @staticmethod
    def _state(
        symbol: str,
        trend_spread: float,
        htf_trend_spread: float,
        market_regime: MarketRegime = MarketRegime.BULL_TREND,
    ) -> MarketState:
        return MarketState(
            symbol=symbol,
            market_regime=market_regime,
            volatility_level=VolatilityLevel.NORMAL,
            trend_strength=TrendStrength.MODERATE,
            time_of_day="MID",
            trading_session="NY",
            day_type="WEEKDAY",
            week_phase="MID",
            time_remaining_days=7.0,
            distance_to_key_levels=1.0,
            current_price=100.0,
            rsi=60.0,
            trend_spread=trend_spread,
            dist_to_high=0.3,
            dist_to_low=1.1,
            macd=1.0,
            macd_signal=0.8,
            macd_hist=0.8,
            bb_upper=102.0,
            bb_lower=98.0,
            bb_mid=100.0,
            atr=1.2,
            volume_delta=0.0,
            spread_pct=0.08,
            body_pct=0.2,
            gap_pct=0.05,
            volume_zscore=1.4,
            liquidity_proxy=10.0,
            funding_rate=0.0,
            funding_extreme=False,
            current_risk_state="SAFE",
            current_drawdown_percent=0.0,
            current_open_positions=0,
            regime_confidence=0.8,
            regime_stable=True,
            momentum_shift_score=0.3,
            htf_trend_spread=htf_trend_spread,
            htf_rsi=58.0,
            htf_atr=1.4,
        )

    def test_cross_sectional_momentum_selected_for_top_ranked_symbol(self):
        base_scores = [-1.4, -1.0, -0.6, -0.2, 0.2, 0.6, 0.9, 1.1]
        for idx, score in enumerate(base_scores):
            sym = f"S{idx}/USDC"
            snap_state = self._state(sym, trend_spread=score, htf_trend_spread=score * 0.9)
            self.engine.update_cross_section_snapshot(sym, snap_state)

        target = self._state("TOP/USDC", trend_spread=1.8, htf_trend_spread=1.5)
        self.engine.update_cross_section_snapshot("TOP/USDC", target)

        self.engine.set_strategy_overrides(
            strategy_weights={
                StrategyType.CROSS_SECTIONAL_MOMENTUM: 2.0,
                StrategyType.MOMENTUM: 0.2,
                StrategyType.BREAKOUT: 0.2,
                StrategyType.ARBITRAGE: 0.2,
            }
        )
        action, _, _ = self.engine.run_analysis(target)

        self.assertEqual(action.strategy, StrategyType.CROSS_SECTIONAL_MOMENTUM)
        self.assertEqual(action.direction, ActionDirection.LONG)

    def test_cross_sectional_momentum_not_used_with_small_universe(self):
        for idx, score in enumerate([0.2, 0.4, 0.8]):
            sym = f"SM{idx}/USDC"
            snap_state = self._state(sym, trend_spread=score, htf_trend_spread=score * 0.9)
            self.engine.update_cross_section_snapshot(sym, snap_state)

        target = self._state("TARGET/USDC", trend_spread=1.0, htf_trend_spread=0.8)
        self.engine.update_cross_section_snapshot("TARGET/USDC", target)

        self.engine.set_strategy_overrides(
            strategy_weights={
                StrategyType.CROSS_SECTIONAL_MOMENTUM: 3.0,
                StrategyType.MOMENTUM: 0.8,
                StrategyType.BREAKOUT: 0.8,
                StrategyType.ARBITRAGE: 0.8,
            }
        )
        action, _, _ = self.engine.run_analysis(target)

        self.assertNotEqual(action.strategy, StrategyType.CROSS_SECTIONAL_MOMENTUM)


if __name__ == "__main__":
    unittest.main()
