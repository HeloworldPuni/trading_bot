
import logging
from typing import Optional, List, Tuple

from src.core.definitions import MarketState, Action, StrategyType, ActionDirection, RiskLevel, MarketRegime
from src.core.validation import StateValidator, ValidationException
from src.core.gating import StrategyGater
from src.core.risk import RiskManager
from src.database.storage import ExperienceDB
from src.ml.inference import PolicyInference

logger = logging.getLogger(__name__)

class TradingEngine:
    def __init__(self, log_suffix: Optional[str] = None):
        self.db = ExperienceDB(log_suffix=log_suffix)
        self.policy = PolicyInference()
        
    def run_analysis(self, state: MarketState, data_source: str = "live", market_period_id: str = None) -> Tuple[Action, str, int]:
        """
        The Main Loop:
        Returns: (Action, decision_id, repetition_count)
        """
        try:
            # 1. Validation
            StateValidator.validate_state(state)
            
            # 2. Gating
            allowed_strategies = StrategyGater.get_allowed_strategies(state)
            
            # 3. Decision (Cold Start Rule Logic)
            raw_action, repeats = self._basic_selector(state, allowed_strategies)
            
            # 4. Confidence Prediction (Now before RiskManager to allow Scaling)
            confidence = self.policy.predict_confidence(state, raw_action, repeats=repeats)
            self.last_confidence = confidence
            
            # 5. Risk Scaling Bands
            # Adjust trade risk dynamically based on ML confidence
            risk_multiplier = 1.0
            original_action_record = None
            
            if raw_action.strategy != StrategyType.WAIT:
                if confidence < 0.50:
                    logger.info(f"ML BLOCK: Confidence {confidence:.4f} < 0.50. Blocking trade.")
                    original_action_record = raw_action.to_dict()
                    raw_action = Action.wait(reason=f"Blocked by ML Confidence ({confidence:.4f} < 0.50)")
                elif 0.50 <= confidence < 0.60:
                    risk_multiplier = 0.5
                elif 0.60 <= confidence < 0.70:
                    risk_multiplier = 0.75
                elif confidence >= 0.70:
                    risk_multiplier = 1.25

            # 6. Risk Management (Validation & Scaling)
            # Pass the multiplier to RiskManager to apply it to base risk
            final_action = RiskManager.validate_action(state, raw_action, risk_multiplier=risk_multiplier)
            
            # 7. Logging (Pending Reward)
            # Store repeats, ML scores, and risks in metadata
            decision_id = self.db.log_decision(
                state, 
                final_action, 
                reward=0.0, 
                data_source=data_source, 
                market_period_id=market_period_id,
                repetition_count=repeats,
                ml_confidence=confidence,
                original_action=original_action_record
            )
            
            return final_action, decision_id, repeats

        except ValidationException as e:
            logger.error(f"State Validation Failed: {e}")
            fallback = Action.wait(reason=f"Validation Error: {e}")
            decision_id = self.db.log_decision(state, fallback, reward=0.0, data_source=data_source, repetition_count=0)
            return fallback, decision_id, 0
            
        except Exception as e:
            logger.error(f"System Error: {e}")
            fallback = Action.wait(reason=f"System Error: {e}")
            decision_id = self.db.log_decision(state, fallback, reward=0.0, repetition_count=0)
            return fallback, decision_id, 0

    def _basic_selector(self, state: MarketState, allowed: List[StrategyType]) -> Tuple[Action, int]:
        """
        A simple rule-based selector for Cold Start.
        Includes Logic to prevent excessive repetition (Max 3 consecutive same actions).
        Returns (Action, RepetitionCount for Diminishing Rewards)
        """
        if not allowed:
            return Action.wait(reason="No strategies allowed by Gating Protocol"), 0

        # 1. Fetch History
        history = self.db.get_recent_records(limit=3)
        
        # 2. Identify proposed primary strategy
        # Default: Pick first allowed
        proposed_strategy = allowed[0]

        # 2.5 Strategic Wait Injection (10% Chance)
        # "In strong trends, WAIT must still be chosen occasionally."
        import random
        if random.random() < 0.10:
             return Action.wait(reason="Strategic WAIT injection to gather inaction data."), 0
        
        # 3. Check Repetition
        # Count how many times we've done this EXACT strategy in the SAME context
        repeats = 0
        current_context = (state.market_regime.value, state.volatility_level.value)
        
        for record in reversed(history):
            recorded_action = record.get("action_taken", {})
            recorded_state = record.get("market_state", {})
            
            # Construct context from record
            # Note: Enums are stored as strings in JSON
            record_context = (recorded_state.get("market_regime"), recorded_state.get("volatility_level"))
            
            # Check for IDENTITY: Same Strategy AND Same Context
            is_same_strategy = recorded_action.get("strategy") == proposed_strategy.value
            is_same_context = record_context == current_context
            
            if is_same_strategy and is_same_context:
                repeats += 1
            else:
                break # Sequence broken (different strategy OR different context)
        
        # 4. Enforce Variety Rule
        if repeats >= 3:
            # We have done this 3 times in a row.
            # Try to find an alternative in 'allowed'
            alternatives = [s for s in allowed if s != proposed_strategy]
            
            if alternatives:
                # Pick the alternative
                proposed_strategy = alternatives[0]
                logger.info(f"Switching strategy to {proposed_strategy.name} to avoid repetition.")
                repeats = 0 # Reset repeats for new strategy
            else:
                # No alternatives?
                # Force WAIT
                return Action.wait(reason="Max consecutive repetitions reached. Forcing WAIT for diversity."), 0

        strategy = proposed_strategy
        
        direction = ActionDirection.FLAT
        if state.market_regime == MarketRegime.BULL_TREND:
            direction = ActionDirection.LONG
        elif state.market_regime == MarketRegime.BEAR_TREND:
            direction = ActionDirection.SHORT
        else:
            direction = ActionDirection.LONG 

        return Action(
            strategy=strategy,
            direction=direction,
            risk_level=RiskLevel.LOW, 
            reasoning=f"Selected {strategy.name} based on {state.market_regime.name}"
        ), repeats
