"""
Planner layer
Converts diagnostics into bounded adaptation actions.
"""

from __future__ import annotations

from typing import Any, Dict, List


class AdaptivePlanner:
    ALLOWED_ACTION_TYPES = {
        "set_threshold",
        "set_strategy_weight",
        "set_regime_gate",
        "set_symbol_filter",
        "set_position_cap",
    }

    def propose_actions(self, diagnostics: Dict[str, Any]) -> List[Dict[str, Any]]:
        actions: List[Dict[str, Any]] = []
        top_issue = diagnostics.get("top_issue")
        win_rate = float(diagnostics.get("win_rate", 0.0))

        if top_issue == "REGIME_SHIFT":
            actions.append(
                {
                    "action_type": "set_regime_gate",
                    "params": {"min_regime_confidence": 0.60, "require_regime_stable": True},
                    "rationale": "Frequent regime-shift losses require stricter regime gating.",
                }
            )
        elif top_issue == "BAD_TIMING":
            actions.append(
                {
                    "action_type": "set_threshold",
                    "params": {"min_signal_score": 0.62},
                    "rationale": "Entry timing losses suggest stronger confirmation threshold.",
                }
            )
        elif top_issue == "VOLATILITY_SPIKE":
            actions.append(
                {
                    "action_type": "set_position_cap",
                    "params": {"size_multiplier": 0.8},
                    "rationale": "Volatility spikes call for smaller position sizing.",
                }
            )

        if win_rate < 0.45:
            actions.append(
                {
                    "action_type": "set_position_cap",
                    "params": {"max_position_pct": 0.03},
                    "rationale": "Low system win-rate requires temporary defensive sizing.",
                }
            )

        return [a for a in actions if a.get("action_type") in self.ALLOWED_ACTION_TYPES]

