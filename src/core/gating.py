
from typing import List, Set
from src.core.definitions import MarketState, StrategyType, MarketRegime, VolatilityLevel

class StrategyGater:
    @staticmethod
    def get_allowed_strategies(state: MarketState) -> List[StrategyType]:
        """
        Determines which strategies are PERMITTED based on the Master Protocol.
        """
        
        # 1. Circuit Breaker (Hard Rule)
        # "If current_drawdown_percent <= -5: Disallow ALL strategies."
        if state.current_drawdown_percent <= -5.0:
            return []

        allowed: Set[StrategyType] = set()

        # 2. Regime-Based Rules
        if state.market_regime == MarketRegime.BULL_TREND:
            allowed.add(StrategyType.MOMENTUM)
            allowed.add(StrategyType.BREAKOUT)
            allowed.add(StrategyType.ARBITRAGE)
            
        elif state.market_regime == MarketRegime.BEAR_TREND:
            allowed.add(StrategyType.SHORT_MOMENTUM)
            allowed.add(StrategyType.ARBITRAGE)
            
        elif state.market_regime in [MarketRegime.SIDEWAYS_LOW_VOL, MarketRegime.SIDEWAYS_HIGH_VOL]:
            allowed.add(StrategyType.SCALP)
            allowed.add(StrategyType.MEAN_REVERSION)
            allowed.add(StrategyType.ARBITRAGE)
            if state.market_regime == MarketRegime.SIDEWAYS_LOW_VOL:
                allowed.add(StrategyType.MARKET_MAKING)
            
        # TRANSITION regime usually implies caution; strictly following protocol implies NO strategies allowed
        # unless explicitly stated. Protocol says:
        # "If a strategy is not explicitly allowed, it must NOT be considered."
        # So TRANSITION -> Empty list (WAIT).

        # 3. Volatility Rules
        if state.volatility_level == VolatilityLevel.LOW:
            # "Disallow BREAKOUT (False break risk high)"
            if StrategyType.BREAKOUT in allowed:
                allowed.remove(StrategyType.BREAKOUT)

        return list(allowed)
