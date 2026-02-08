
from src.core.definitions import MarketState

class RewardCalculator:
    @staticmethod
    def calculate_reward(
        state: MarketState, 
        realized_pnl_percent: float, 
        rule_violation: bool = False, 
        regime_mismatch: bool = False
    ) -> float:
        """
        Original method (kept for backward compatibility or estimates).
        """
        reward = realized_pnl_percent
        if rule_violation:
            reward -= 10.0
        if state.current_drawdown_percent < -2.0 and realized_pnl_percent < 0:
            reward -= abs(realized_pnl_percent) * 0.5
        if regime_mismatch:
            reward -= 2.0
        return round(reward, 4)

    @staticmethod
    def calculate_final_reward(
        exit_reason: str,
        realized_pnl: float,
        duration_candles: int,
        is_wait_action: bool = False,
        market_change_during_wait: float = 0.0,
        repetition_count: int = 0
    ) -> float:
        """
        Computes FINAL REWARD for Closed Loop Learning.
        Includes Diminishing Returns for Repetition.
        """
        reward = 0.0

        # 1. HANDLE WAIT ACTIONS
        if is_wait_action:
            # If we waited and market crashed -> Big Positive Reward (Savior)
            if market_change_during_wait < -1.0: # Market dropped > 1%
                reward += 1.0 # Good wait
            # If we waited and market pumped -> Negative Reward (Missed Opportunity)
            elif market_change_during_wait > 2.0: # Market pumped > 2%
                reward -= 0.5 # Missed out
            else:
                reward += 0.05 # Tiny reward for patience in noise
            return round(reward, 4)

        # 2. HANDLE TRADES
        reward = realized_pnl

        # Bonus for quick TP
        if exit_reason == "TP" and duration_candles < 5:
            reward += 0.5

        # Penalty for Timeouts (Stagnant capital)
        if exit_reason in ("TIME", "TIME_EXIT"):
            reward -= 0.1

        # Penalty for SL
        if exit_reason == "SL":
            # Standard PnL capture handles this, but maybe extra pain?
            pass

        return round(reward, 4) if is_wait_action else RewardCalculator._apply_diminishing_returns(reward, repetition_count)

    @staticmethod
    def _apply_diminishing_returns(base_reward: float, repeats: int) -> float:
        """
        Rules:
        0 (1st exec): 1.0x
        1 (2nd exec): 0.8x
        2 (3rd exec): 0.5x
        3+ (Further): 0.2x
        """
        if base_reward <= 0: return round(base_reward, 4) # Don't diminish penalties
        
        scale = 1.0
        if repeats == 1: scale = 0.8
        elif repeats == 2: scale = 0.5
        elif repeats >= 3: scale = 0.2
        
        return round(base_reward * scale, 4)
