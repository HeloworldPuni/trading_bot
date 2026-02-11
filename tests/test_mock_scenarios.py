
import unittest
import shutil
import os
from src.core.definitions import MarketState, MarketRegime, VolatilityLevel, TrendStrength, StrategyType, ActionDirection, RiskLevel
from src.engine.system import TradingEngine
from src.config import Config

class TestTradingEngine(unittest.TestCase):
    def setUp(self):
        # Use a temporary test data directory
        self.test_data_dir = "tests/data"
        if os.path.exists(self.test_data_dir):
            shutil.rmtree(self.test_data_dir)
        os.makedirs(self.test_data_dir)
        
        # Patch config data path for testing (simplified approach)
        # Ideally we'd mock Config, but for now we just instantiate the Engine which uses Config.
        # We'll rely on the Engine creating the DB.
        # Note: The DB writes to Config.DATA_PATH. 
        # For this mock test, we mainly care about the RETURNED ACTION, not the file persistence.
        self._orig_wait_prob = Config.STRATEGIC_WAIT_PROB
        Config.STRATEGIC_WAIT_PROB = 0.0
        self.engine = TradingEngine()
        # Force deterministic confidence to avoid ML model effects in unit tests
        self.engine.policy.predict_confidence = lambda *args, **kwargs: 0.75
    
    def tearDown(self):
        Config.STRATEGIC_WAIT_PROB = self._orig_wait_prob

    def create_mock_state(self, **kwargs):
        defaults = {
            "market_regime": MarketRegime.BULL_TREND,
            "volatility_level": VolatilityLevel.NORMAL,
            "trend_strength": TrendStrength.STRONG,
            "time_of_day": "MID",
            "trading_session": "NY",
            "day_type": "WEEKDAY",
            "week_phase": "MID",
            "time_remaining_days": 10.0,
            "distance_to_key_levels": 5.0,
            "funding_extreme": False,
            "current_risk_state": "SAFE",
            "current_drawdown_percent": 0.0,
            "current_open_positions": 0,
            "rsi": 60.0,
            "macd_hist": 5.0,
            "trend_spread": 1.0,
            "dist_to_high": 0.2,
            "dist_to_low": 1.0,
            "regime_confidence": 0.8,
            "regime_stable": True,
            "momentum_shift_score": 0.2,
            "htf_trend_spread": 0.8,
            "spread_pct": 0.1,
            "body_pct": 0.2,
            "gap_pct": 0.1,
            "volume_zscore": 1.2
        }
        defaults.update(kwargs)
        return MarketState(**defaults)

    def test_bull_market_logic(self):
        """Test 1: Bull Market -> Should allow Momentum -> Buy"""
        state = self.create_mock_state(market_regime=MarketRegime.BULL_TREND)
        action, _, _ = self.engine.run_analysis(state)
        
        # Expectation: Strategy MOMENTUM or BREAKOUT allowed.
        # Basic Selector picks first one.
        # Direction should be LONG.
        self.assertIn(action.strategy, [StrategyType.MOMENTUM, StrategyType.BREAKOUT])
        self.assertEqual(action.direction, ActionDirection.LONG)

    def test_crash_circuit_breaker(self):
        """Test 2: Crash (-6% Drawdown) -> Should STOP trading (WAIT)"""
        state = self.create_mock_state(current_drawdown_percent=-6.0)
        action, _, _ = self.engine.run_analysis(state)
        
        # Expectation: WAIT because Gating returns empty list.
        self.assertEqual(action.strategy, StrategyType.WAIT)
        self.assertIn("No strategies allowed", action.reasoning)

    def test_danger_risk_reduction(self):
        """Test 3: Danger State -> Should force LOW risk"""
        state = self.create_mock_state(current_risk_state="DANGER")
        action, _, _ = self.engine.run_analysis(state)
        
        # Expectation: Action might be valid, but Risk must be LOW.
        if action.strategy != StrategyType.WAIT:
            self.assertEqual(action.risk_level, RiskLevel.LOW)
            self.assertIn("Downgraded risk", action.reasoning)

    def test_invalid_data_rejection(self):
        """Test 4: Bad Data (Negative Time) -> Should Reject"""
        # Logic error: time cannot be negative
        state = self.create_mock_state(time_remaining_days=-5.0)
        action, _, _ = self.engine.run_analysis(state)
        
        self.assertEqual(action.strategy, StrategyType.WAIT)
        self.assertIn("Validation Error", action.reasoning)

    def test_bear_market_logic(self):
        """Test 5: Bear Market -> Should SHORT"""
        state = self.create_mock_state(
            market_regime=MarketRegime.BEAR_TREND,
            rsi=40.0,
            macd_hist=-5.0,
            trend_spread=-1.0,
            htf_trend_spread=-0.8,
            dist_to_low=0.2
        )
        action, _, _ = self.engine.run_analysis(state)
        
        self.assertEqual(action.strategy, StrategyType.SHORT_MOMENTUM)
        self.assertEqual(action.direction, ActionDirection.SHORT)

if __name__ == '__main__':
    unittest.main()
