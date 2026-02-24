"""
Governor
Promotion and rollout decision logic with risk-first overrides.
"""

from __future__ import annotations

from typing import Any, Dict


class DeploymentGovernor:
    def decide(
        self,
        experiment_result: Dict[str, Any],
        risk_veto: bool = False,
        canary_failed: bool = False,
    ) -> Dict[str, Any]:
        if risk_veto:
            return {"promote": False, "mode": "hold", "reason": "Risk veto active"}
        if canary_failed:
            return {"promote": False, "mode": "rollback", "reason": "Canary failed"}
        if not bool(experiment_result.get("approved", False)):
            return {"promote": False, "mode": "hold", "reason": "Experiment did not pass"}
        return {"promote": True, "mode": "canary", "reason": "Approved for staged rollout"}

