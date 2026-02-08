"""
Unit tests for replay mode and reward calculation logic.
Covers issue #16 from code review.
"""

import unittest
from src.core.reward import RewardCalculator
from src.core.definitions import MarketState, MarketRegime, VolatilityLevel, TrendStrength


class TestRewardCalculator(unittest.TestCase):
    """Tests for RewardCalculator"""
    
    def test_tp_quick_exit_bonus(self):
        """TP within 5 candles should get +0.5 bonus"""
        reward = RewardCalculator.calculate_final_reward(
            exit_reason="TP",
            realized_pnl=1.5,
            duration_candles=3,  # Quick exit
        )
        # 1.5 base + 0.5 bonus = 2.0
        self.assertEqual(reward, 2.0)
    
    def test_tp_slow_exit_no_bonus(self):
        """TP after 5+ candles should NOT get bonus"""
        reward = RewardCalculator.calculate_final_reward(
            exit_reason="TP",
            realized_pnl=1.5,
            duration_candles=10,  # Slow exit
        )
        # 1.5 base, no bonus
        self.assertEqual(reward, 1.5)
    
    def test_time_exit_penalty(self):
        """TIME_EXIT should apply -0.1 penalty"""
        reward = RewardCalculator.calculate_final_reward(
            exit_reason="TIME_EXIT",
            realized_pnl=0.5,
            duration_candles=50,
        )
        # 0.5 - 0.1 = 0.4
        self.assertEqual(reward, 0.4)
    
    def test_time_exit_legacy_format(self):
        """TIME (legacy format) should also apply penalty"""
        reward = RewardCalculator.calculate_final_reward(
            exit_reason="TIME",
            realized_pnl=0.5,
            duration_candles=50,
        )
        # 0.5 - 0.1 = 0.4
        self.assertEqual(reward, 0.4)
    
    def test_sl_exit_no_extra_penalty(self):
        """SL exit should just capture PnL loss, no extra penalty"""
        reward = RewardCalculator.calculate_final_reward(
            exit_reason="SL",
            realized_pnl=-1.0,
            duration_candles=5,
        )
        # -1.0 (no extra penalty)
        self.assertEqual(reward, -1.0)
    
    def test_wait_action_market_crash(self):
        """Waiting during market crash should be rewarded"""
        reward = RewardCalculator.calculate_final_reward(
            exit_reason="",
            realized_pnl=0,
            duration_candles=0,
            is_wait_action=True,
            market_change_during_wait=-2.5,  # Market crashed 2.5%
        )
        # Good wait = +1.0
        self.assertEqual(reward, 1.0)
    
    def test_wait_action_missed_pump(self):
        """Waiting during pump should be penalized"""
        reward = RewardCalculator.calculate_final_reward(
            exit_reason="",
            realized_pnl=0,
            duration_candles=0,
            is_wait_action=True,
            market_change_during_wait=3.0,  # Market pumped 3%
        )
        # Missed opportunity = -0.5
        self.assertEqual(reward, -0.5)
    
    def test_wait_action_neutral_market(self):
        """Waiting during flat market should get small reward"""
        reward = RewardCalculator.calculate_final_reward(
            exit_reason="",
            realized_pnl=0,
            duration_candles=0,
            is_wait_action=True,
            market_change_during_wait=0.5,  # Flat
        )
        # Patience in noise = +0.05
        self.assertEqual(reward, 0.05)
    
    def test_diminishing_returns_first_execution(self):
        """First execution (repeats=0) gets full reward"""
        reward = RewardCalculator.calculate_final_reward(
            exit_reason="TP",
            realized_pnl=1.0,
            duration_candles=10,
            repetition_count=0,
        )
        # 1.0 * 1.0 = 1.0
        self.assertEqual(reward, 1.0)
    
    def test_diminishing_returns_second_execution(self):
        """Second execution (repeats=1) gets 80% reward"""
        reward = RewardCalculator.calculate_final_reward(
            exit_reason="TP",
            realized_pnl=1.0,
            duration_candles=10,
            repetition_count=1,
        )
        # 1.0 * 0.8 = 0.8
        self.assertEqual(reward, 0.8)
    
    def test_diminishing_returns_third_execution(self):
        """Third execution (repeats=2) gets 50% reward"""
        reward = RewardCalculator.calculate_final_reward(
            exit_reason="TP",
            realized_pnl=1.0,
            duration_candles=10,
            repetition_count=2,
        )
        # 1.0 * 0.5 = 0.5
        self.assertEqual(reward, 0.5)
    
    def test_diminishing_returns_many_executions(self):
        """4+ executions (repeats>=3) gets 20% reward"""
        reward = RewardCalculator.calculate_final_reward(
            exit_reason="TP",
            realized_pnl=1.0,
            duration_candles=10,
            repetition_count=5,
        )
        # 1.0 * 0.2 = 0.2
        self.assertEqual(reward, 0.2)
    
    def test_no_diminishing_on_losses(self):
        """Losses should NOT be diminished (full penalty)"""
        reward = RewardCalculator.calculate_final_reward(
            exit_reason="SL",
            realized_pnl=-2.0,
            duration_candles=10,
            repetition_count=5,  # Many repeats
        )
        # -2.0 (unchanged, losses not diminished)
        self.assertEqual(reward, -2.0)


if __name__ == '__main__':
    unittest.main()
