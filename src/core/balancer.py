import logging
from typing import Dict, Any, Tuple

logger = logging.getLogger(__name__)

class BalanceSupervisor:
    """
    Monitors distribution of experience data.
    """
    THRESHOLD = 0.60
    MIN_SAMPLES = 100  # Startup period

    @staticmethod
    def check(stats: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Checks current stats for imbalance.
        Returns: (throttle_needed, warning_message)
        """
        total = stats.get("total", 0)
        
        if total < BalanceSupervisor.MIN_SAMPLES:
            return False, ""

        # Check Strategies
        for strat, count in stats.get("strategies", {}).items():
            ratio = count / total
            if ratio > BalanceSupervisor.THRESHOLD:
                return True, f"Strategy Imbalance: {strat} is {ratio:.1%} of data."

        # Check Regimes
        for regime, count in stats.get("regimes", {}).items():
            ratio = count / total
            if ratio > BalanceSupervisor.THRESHOLD:
                return True, f"Regime Imbalance: {regime} is {ratio:.1%} of data."
                
        # Check Actions
        for action, count in stats.get("actions", {}).items():
            ratio = count / total
            if ratio > BalanceSupervisor.THRESHOLD:
                # Exception: WAIT action often dominates naturally. 
                # But requirement says "action types" are tracked.
                # If WAIT is > 60%, we might want to slow down?
                # User said: "action types (LONG, SHORT, WAIT)".
                # Let's enforce it strictly per requirement.
                return True, f"Action Imbalance: {action} is {ratio:.1%} of data."
                
        return False, ""
