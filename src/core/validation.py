
from src.core.definitions import MarketState, MarketRegime, VolatilityLevel, TrendStrength

class ValidationException(Exception):
    """Raised when data integrity is compromised."""
    pass

class StateValidator:
    @staticmethod
    def validate_state(state: MarketState) -> bool:
        """
        Strictly validates constraints.
        Raises ValidationException on failure.
        """
        # 1. Null Checks
        if state.market_regime is None:
            raise ValidationException("Market Regime cannot be None")
        if state.volatility_level is None:
            raise ValidationException("Volatility Level cannot be None")
        
        # 2. Type Checks
        if not isinstance(state.market_regime, MarketRegime):
            raise ValidationException(f"Invalid Regime Type: {type(state.market_regime)}")
        
        # 3. Value Constraints
        if state.current_drawdown_percent > 0:
            # Drawdown should be negative or zero (e.g. -5.0)
            raise ValidationException(f"Drawdown must be <= 0, got {state.current_drawdown_percent}")
        
        if state.current_drawdown_percent < -100:
            raise ValidationException(f"Drawdown cannot be less than -100%, got {state.current_drawdown_percent}")

        if state.time_remaining_days < 0:
            raise ValidationException(f"Time remaining cannot be negative: {state.time_remaining_days}")

        # 4. Consistency Checks
        if state.market_regime == MarketRegime.SIDEWAYS_LOW_VOL and state.volatility_level == VolatilityLevel.HIGH:
            raise ValidationException("Contradiction: Regime is SIDEWAYS_LOW_VOL but Volatility is HIGH")

        return True
