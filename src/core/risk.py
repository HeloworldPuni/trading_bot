
from src.core.definitions import MarketState, Action, RiskLevel, StrategyType

class RiskManager:
    @staticmethod
    def get_base_risk_percent(level: RiskLevel) -> float:
        """Maps RiskLevel to base percentage risk."""
        mapping = {
            RiskLevel.LOW: 0.5,
            RiskLevel.MEDIUM: 1.0,
            RiskLevel.HIGH: 2.0
        }
        return mapping.get(level, 0.5)

    @staticmethod
    def validate_action(state: MarketState, action: Action, risk_multiplier: float = 1.0) -> Action:
        """
        Validates and modifies the action's risk parameters based on state.
        
        WARNING: This method MUTATES the input action object directly.
        The same action is returned with updated risk fields.
        Caller should assume action is modified after this call.
        
        Applies risk_multiplier while ensuring hard caps are enforced.
        """
        if action.strategy == StrategyType.WAIT:
            return action

        # 1. Initialize Risks
        base_risk = RiskManager.get_base_risk_percent(action.risk_level)
        
        # 2. Enforcement of "DANGER" state (Downgrade)
        if state.current_risk_state == "DANGER":
            base_risk = RiskManager.get_base_risk_percent(RiskLevel.LOW)
            action.risk_level = RiskLevel.LOW
            action.reasoning = f"Downgraded risk due to DANGER state. (Original: {action.reasoning})"
        
        # 3. Drawdown Proximity (Downgrade)
        if state.current_drawdown_percent <= -4.0:
            if action.risk_level != RiskLevel.LOW:
                base_risk = RiskManager.get_base_risk_percent(RiskLevel.LOW)
                action.risk_level = RiskLevel.LOW
                action.reasoning = f"Downgraded risk due to Drawdown proximity. (Original: {action.reasoning})"

        # 4. Apply Multiplier
        # adjusted_risk = base_risk * risk_multiplier
        adjusted_risk = base_risk * risk_multiplier
        
        # Hard Cap: Never exceed 2.0% regardless of multiplier
        if adjusted_risk > 2.0:
            adjusted_risk = 2.0
            
        action.base_risk = base_risk
        action.adjusted_risk = adjusted_risk
        action.risk_multiplier = risk_multiplier
        
        return action
