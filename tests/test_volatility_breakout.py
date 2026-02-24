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


class TestVolatilityBreakout(unittest.TestCase):
    def setUp(self):
        self._orig_wait_prob = Config.STRATEGIC_WAIT_PROB
        self._orig_vol_enabled = Config.VOLATILITY_BREAKOUT_ENABLED
        self._orig_vol_squeeze = Config.VOL_BREAKOUT_BBW_SQUEEZE_MAX
        self._orig_vol_expansion = Config.VOL_BREAKOUT_EXPANSION_RATIO_MIN
        self._orig_vol_window = Config.VOL_BREAKOUT_BASELINE_WINDOW
        self._orig_vol_z = Config.VOL_BREAKOUT_MIN_VOLUME_ZSCORE
        self._orig_vol_atr = Config.VOL_BREAKOUT_MIN_ATR_PCT

        Config.STRATEGIC_WAIT_PROB = 0.0
        Config.VOLATILITY_BREAKOUT_ENABLED = True
        Config.VOL_BREAKOUT_BBW_SQUEEZE_MAX = 2.0
        Config.VOL_BREAKOUT_EXPANSION_RATIO_MIN = 1.20
        Config.VOL_BREAKOUT_BASELINE_WINDOW = 12
        Config.VOL_BREAKOUT_MIN_VOLUME_ZSCORE = 1.0
        Config.VOL_BREAKOUT_MIN_ATR_PCT = 0.20

        self.engine = TradingEngine()
        self.engine.policy.predict_confidence = lambda *args, **kwargs: 0.78

    def tearDown(self):
        Config.STRATEGIC_WAIT_PROB = self._orig_wait_prob
        Config.VOLATILITY_BREAKOUT_ENABLED = self._orig_vol_enabled
        Config.VOL_BREAKOUT_BBW_SQUEEZE_MAX = self._orig_vol_squeeze
        Config.VOL_BREAKOUT_EXPANSION_RATIO_MIN = self._orig_vol_expansion
        Config.VOL_BREAKOUT_BASELINE_WINDOW = self._orig_vol_window
        Config.VOL_BREAKOUT_MIN_VOLUME_ZSCORE = self._orig_vol_z
        Config.VOL_BREAKOUT_MIN_ATR_PCT = self._orig_vol_atr

    @staticmethod
    def _state(
        symbol: str,
        upper: float,
        lower: float,
        trend_spread: float,
        htf_spread: float,
        volume_z: float = 1.4,
        atr: float = 0.35,
    ) -> MarketState:
        return MarketState(
            symbol=symbol,
            market_regime=MarketRegime.BULL_TREND,
            volatility_level=VolatilityLevel.HIGH,
            trend_strength=TrendStrength.STRONG,
            time_of_day="MID",
            trading_session="NY",
            day_type="WEEKDAY",
            week_phase="MID",
            time_remaining_days=5.0,
            distance_to_key_levels=1.0,
            current_price=100.0,
            rsi=61.0,
            trend_spread=trend_spread,
            dist_to_high=0.3,
            dist_to_low=1.2,
            macd=1.1,
            macd_signal=0.7,
            macd_hist=0.9,
            bb_upper=upper,
            bb_lower=lower,
            bb_mid=100.0,
            atr=atr,
            volume_delta=0.0,
            spread_pct=0.10,
            body_pct=0.25,
            gap_pct=0.05,
            volume_zscore=volume_z,
            liquidity_proxy=10.0,
            funding_rate=0.0,
            funding_extreme=False,
            current_risk_state="SAFE",
            current_drawdown_percent=0.0,
            current_open_positions=0,
            regime_confidence=0.82,
            regime_stable=True,
            momentum_shift_score=0.3,
            htf_trend_spread=htf_spread,
            htf_rsi=57.0,
            htf_atr=0.4,
        )

    def test_volatility_breakout_selected_after_squeeze_expansion(self):
        symbol = "VB/USDC"

        for _ in range(14):
            squeeze = self._state(symbol, upper=100.8, lower=99.2, trend_spread=0.6, htf_spread=0.5, volume_z=0.8)
            self.engine.update_volatility_snapshot(symbol, squeeze)

        expansion = self._state(symbol, upper=102.6, lower=97.4, trend_spread=1.1, htf_spread=0.8, volume_z=1.8)
        self.engine.update_volatility_snapshot(symbol, expansion)

        self.engine.set_strategy_overrides(
            strategy_weights={
                StrategyType.VOLATILITY_BREAKOUT: 2.0,
                StrategyType.MOMENTUM: 0.2,
                StrategyType.BREAKOUT: 0.2,
                StrategyType.ARBITRAGE: 0.2,
            }
        )
        action, _, _ = self.engine.run_analysis(expansion)

        self.assertEqual(action.strategy, StrategyType.VOLATILITY_BREAKOUT)
        self.assertEqual(action.direction, ActionDirection.LONG)

    def test_volatility_breakout_skips_when_no_expansion(self):
        symbol = "VB2/USDC"

        for _ in range(14):
            squeeze = self._state(symbol, upper=100.8, lower=99.2, trend_spread=0.6, htf_spread=0.5, volume_z=0.9)
            self.engine.update_volatility_snapshot(symbol, squeeze)

        # Still squeezed, no real expansion.
        flat = self._state(symbol, upper=100.95, lower=99.05, trend_spread=0.7, htf_spread=0.5, volume_z=1.3)
        self.engine.update_volatility_snapshot(symbol, flat)

        self.engine.set_strategy_overrides(
            strategy_weights={
                StrategyType.VOLATILITY_BREAKOUT: 2.0,
                StrategyType.MOMENTUM: 0.8,
                StrategyType.BREAKOUT: 0.8,
                StrategyType.ARBITRAGE: 0.8,
            }
        )
        action, _, _ = self.engine.run_analysis(flat)

        self.assertNotEqual(action.strategy, StrategyType.VOLATILITY_BREAKOUT)


if __name__ == "__main__":
    unittest.main()
