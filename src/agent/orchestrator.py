"""
Trading Brain Orchestrator
Coordinates specialist agents and emits a validated final decision packet.

This is intentionally bounded:
- No direct strategy rewrites
- No unrestricted parameter mutation
- Risk veto can force WAIT/EXECUTE_REDUCED
"""

from __future__ import annotations

import json
import os
import uuid
from datetime import UTC, datetime, timedelta
from typing import Any, Dict, List, Optional

from src.config import Config
from src.core.definitions import Action, StrategyType, MarketState
from src.agent.schema_validator import AgentSchemaValidator, SchemaValidationError


def _utc_now_iso() -> str:
    return datetime.now(UTC).isoformat()


class _SpecialistBase:
    def __init__(self, name: str):
        self.name = name

    def run(self, task: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

    @staticmethod
    def _conf(score: float, calibration: str = "MEDIUM") -> Dict[str, Any]:
        score = max(0.0, min(1.0, float(score)))
        calibration = calibration if calibration in {"LOW", "MEDIUM", "HIGH"} else "MEDIUM"
        return {"score": score, "calibration": calibration}


class MarketDataAgent(_SpecialistBase):
    def __init__(self):
        super().__init__("MarketDataAgent")

    def run(self, task: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        state: MarketState = context["state"]
        spread_ok = state.spread_pct <= 0.8
        body_ok = state.body_pct <= 2.0
        gap_ok = abs(state.gap_pct) <= 1.0
        regime_ok = state.regime_stable and state.regime_confidence >= 0.55

        checks_ok = [spread_ok, body_ok, gap_ok, regime_ok]
        quality_score = sum(1 for x in checks_ok if x) / len(checks_ok)

        status = "OK"
        if quality_score < 0.75:
            status = "PARTIAL"
        if quality_score < 0.5:
            status = "FAILED"

        claims = []
        if status == "OK":
            claims.append("Market data quality is acceptable for decisioning.")
        else:
            claims.append("Market data context is noisy or unstable for reliable execution.")

        proposed_actions = []
        if not regime_ok:
            proposed_actions.append(
                {
                    "action_type": "set_regime_gate",
                    "params": {
                        "require_regime_stable": True,
                        "min_regime_confidence": 0.60,
                    },
                }
            )

        return {
            "task_id": task["task_id"],
            "status": status,
            "claims": claims,
            "evidence": [
                {"evidence_id": "mkt_01", "source": "market_state", "metric": "spread_pct", "value": state.spread_pct, "window": "latest"},
                {"evidence_id": "mkt_02", "source": "market_state", "metric": "body_pct", "value": state.body_pct, "window": "latest"},
                {"evidence_id": "mkt_03", "source": "market_state", "metric": "gap_pct", "value": state.gap_pct, "window": "latest"},
                {"evidence_id": "mkt_04", "source": "market_state", "metric": "regime_stable", "value": state.regime_stable, "window": "latest"},
                {"evidence_id": "mkt_05", "source": "market_state", "metric": "regime_confidence", "value": state.regime_confidence, "window": "latest"},
            ],
            "confidence": self._conf(quality_score, "HIGH" if quality_score >= 0.75 else "MEDIUM"),
            "proposed_actions": proposed_actions,
            "data_gaps": [],
        }


class StrategyAgent(_SpecialistBase):
    def __init__(self):
        super().__init__("StrategyAgent")

    def run(self, task: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        action: Action = context["proposed_action"]
        confidence: float = float(context.get("model_confidence", 0.5))
        state: MarketState = context["state"]
        min_conf = float(Config.AGENT_MIN_CONFIDENCE)

        if action.strategy == StrategyType.WAIT:
            return {
                "task_id": task["task_id"],
                "status": "OK",
                "claims": ["No execution proposed; strategy posture is defensive (WAIT)."],
                "evidence": [
                    {"evidence_id": "str_01", "source": "engine", "metric": "strategy", "value": "WAIT", "window": "latest"},
                    {"evidence_id": "str_02", "source": "engine", "metric": "model_confidence", "value": confidence, "window": "latest"},
                ],
                "confidence": self._conf(0.7, "MEDIUM"),
                "proposed_actions": [],
                "data_gaps": [],
            }

        status = "OK"
        if confidence < min_conf:
            status = "PARTIAL"

        claims = [f"Proposed strategy is {action.strategy.value} with direction {action.direction.value}."]
        if status == "PARTIAL":
            claims.append("Model confidence is below preferred threshold for full-size execution.")

        proposed_actions = []
        if status == "PARTIAL":
            proposed_actions.append(
                {
                    "action_type": "set_threshold",
                    "params": {"confidence_min": min_conf, "symbol": state.symbol},
                }
            )

        return {
            "task_id": task["task_id"],
            "status": status,
            "claims": claims,
            "evidence": [
                {"evidence_id": "str_01", "source": "engine", "metric": "strategy", "value": action.strategy.value, "window": "latest"},
                {"evidence_id": "str_02", "source": "engine", "metric": "direction", "value": action.direction.value, "window": "latest"},
                {"evidence_id": "str_03", "source": "model", "metric": "confidence", "value": confidence, "window": "latest"},
            ],
            "confidence": self._conf(max(0.0, min(1.0, confidence)), "MEDIUM"),
            "proposed_actions": proposed_actions,
            "data_gaps": [],
        }


class RiskAgent(_SpecialistBase):
    def __init__(self):
        super().__init__("RiskAgent")

    def run(self, task: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        state: MarketState = context["state"]
        open_positions = int(context.get("open_positions", 0))
        max_positions = int(context.get("max_positions", 1))
        gross_exposure = float(context.get("gross_exposure", 0.0))
        exposure_cap = float(context.get("exposure_cap", 1.0))

        veto = False
        reasons: List[str] = []

        # Drawdown field is negative in current state wiring.
        if float(state.current_drawdown_percent) <= -5.0:
            veto = True
            reasons.append("drawdown breach")
        if open_positions >= max_positions:
            veto = True
            reasons.append("max positions reached")
        if gross_exposure >= exposure_cap:
            veto = True
            reasons.append("exposure cap reached")

        status = "FAILED" if veto else "OK"
        claims = []
        if veto:
            claims.append(f"Risk veto active: {', '.join(reasons)}.")
        else:
            claims.append("Risk posture acceptable; no hard veto triggered.")

        proposed_actions = []
        if not veto and gross_exposure > exposure_cap * 0.8:
            status = "PARTIAL"
            claims.append("Risk is elevated; recommend reduced execution size.")
            proposed_actions.append(
                {
                    "action_type": "set_position_cap",
                    "params": {"size_multiplier": 0.75},
                }
            )

        risk_conf = 0.95 if veto else 0.8
        return {
            "task_id": task["task_id"],
            "status": status,
            "claims": claims,
            "evidence": [
                {"evidence_id": "risk_01", "source": "market_state", "metric": "current_drawdown_percent", "value": state.current_drawdown_percent, "window": "latest"},
                {"evidence_id": "risk_02", "source": "portfolio", "metric": "open_positions", "value": open_positions, "window": "latest"},
                {"evidence_id": "risk_03", "source": "portfolio", "metric": "max_positions", "value": max_positions, "window": "config"},
                {"evidence_id": "risk_04", "source": "portfolio", "metric": "gross_exposure", "value": gross_exposure, "window": "latest"},
                {"evidence_id": "risk_05", "source": "portfolio", "metric": "exposure_cap", "value": exposure_cap, "window": "config"},
            ],
            "confidence": self._conf(risk_conf, "HIGH"),
            "proposed_actions": proposed_actions,
            "data_gaps": [],
        }


class ValidationAgent(_SpecialistBase):
    def __init__(self):
        super().__init__("ValidationAgent")

    def run(self, task: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        market_status = context.get("market_status", "OK")
        strategy_status = context.get("strategy_status", "OK")
        risk_status = context.get("risk_status", "OK")
        confidence = float(context.get("model_confidence", 0.5))
        min_conf = float(Config.AGENT_MIN_CONFIDENCE)

        disagreements: List[str] = []
        if strategy_status == "OK" and market_status in {"PARTIAL", "FAILED"}:
            disagreements.append("Strategy signals execution while market quality is degraded.")
        if strategy_status == "OK" and confidence < min_conf:
            disagreements.append("Strategy confidence is weak for full execution.")
        if risk_status == "FAILED":
            disagreements.append("Risk veto conflicts with execution intent.")

        status = "OK" if not disagreements else "PARTIAL"
        claims = ["Validation cross-check completed."]
        claims.extend(disagreements or ["No major cross-agent contradictions detected."])

        return {
            "task_id": task["task_id"],
            "status": status,
            "claims": claims,
            "evidence": [
                {"evidence_id": "val_01", "source": "cross_agent", "metric": "market_status", "value": market_status, "window": "latest"},
                {"evidence_id": "val_02", "source": "cross_agent", "metric": "strategy_status", "value": strategy_status, "window": "latest"},
                {"evidence_id": "val_03", "source": "cross_agent", "metric": "risk_status", "value": risk_status, "window": "latest"},
                {"evidence_id": "val_04", "source": "model", "metric": "confidence", "value": confidence, "window": "latest"},
            ],
            "confidence": self._conf(0.7 if not disagreements else 0.55, "MEDIUM"),
            "proposed_actions": [],
            "data_gaps": [],
        }


class ExecutionAgent(_SpecialistBase):
    def __init__(self):
        super().__init__("ExecutionAgent")

    def run(self, task: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        final_action = context.get("final_action", "WAIT")
        claims = [f"Execution mapping generated for final action {final_action}."]
        return {
            "task_id": task["task_id"],
            "status": "OK",
            "claims": claims,
            "evidence": [
                {"evidence_id": "exe_01", "source": "orchestrator", "metric": "final_action", "value": final_action, "window": "latest"}
            ],
            "confidence": self._conf(0.8, "MEDIUM"),
            "proposed_actions": [],
            "data_gaps": [],
        }


class AgentOrchestrator:
    """
    Main orchestration layer (Trading Brain).
    """

    def __init__(
        self,
        log_path: str = "data/agent_decisions.jsonl",
        min_confidence: float = 0.55,
        reduced_size_multiplier: float = 0.5,
    ):
        self.validator = AgentSchemaValidator()
        self.log_path = log_path
        self.min_confidence = float(min_confidence)
        self.reduced_size_multiplier = max(0.1, min(1.0, float(reduced_size_multiplier)))

        self.market_data_agent = MarketDataAgent()
        self.strategy_agent = StrategyAgent()
        self.risk_agent = RiskAgent()
        self.validation_agent = ValidationAgent()
        self.execution_agent = ExecutionAgent()

    def orchestrate(
        self,
        symbol: str,
        state: MarketState,
        proposed_action: Action,
        model_confidence: float,
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        context = dict(context or {})
        context.update(
            {
                "symbol": symbol,
                "state": state,
                "proposed_action": proposed_action,
                "model_confidence": float(model_confidence),
            }
        )
        trace_id = f"trace_{uuid.uuid4().hex[:12]}"

        specialist_results: Dict[str, Dict[str, Any]] = {}
        specialist_results["MarketDataAgent"] = self._run_specialist(
            trace_id=trace_id,
            specialist=self.market_data_agent,
            goal=f"Validate data quality and regime stability for {symbol}.",
            context=context,
        )
        specialist_results["StrategyAgent"] = self._run_specialist(
            trace_id=trace_id,
            specialist=self.strategy_agent,
            goal=f"Assess strategy suitability for {proposed_action.strategy.value}.",
            context=context,
        )
        specialist_results["RiskAgent"] = self._run_specialist(
            trace_id=trace_id,
            specialist=self.risk_agent,
            goal="Evaluate downside, exposure, and hard risk constraints.",
            context=context,
        )

        specialist_results["ValidationAgent"] = self._run_specialist(
            trace_id=trace_id,
            specialist=self.validation_agent,
            goal="Challenge assumptions and identify cross-agent contradictions.",
            context={
                **context,
                "market_status": specialist_results["MarketDataAgent"]["status"],
                "strategy_status": specialist_results["StrategyAgent"]["status"],
                "risk_status": specialist_results["RiskAgent"]["status"],
            },
        )

        decision_payload = self._build_decision_payload(
            trace_id=trace_id,
            specialist_results=specialist_results,
            model_confidence=float(model_confidence),
            proposed_action=proposed_action,
        )

        specialist_results["ExecutionAgent"] = self._run_specialist(
            trace_id=trace_id,
            specialist=self.execution_agent,
            goal="Prepare final execution directive.",
            context={**context, "final_action": decision_payload["final_action"]},
        )

        decision_envelope = self._envelope(
            trace_id=trace_id,
            sender="Orchestrator",
            recipient="Controller",
            message_type="DECISION_PACKET",
            payload=decision_payload,
        )
        self.validator.assert_valid_message(decision_envelope)

        self._save_record(
            {
                "trace_id": trace_id,
                "timestamp_utc": _utc_now_iso(),
                "symbol": symbol,
                "proposed_strategy": proposed_action.strategy.value,
                "proposed_direction": proposed_action.direction.value,
                "model_confidence": float(model_confidence),
                "decision": decision_payload,
                "specialists": specialist_results,
            }
        )
        return decision_payload

    def _run_specialist(
        self,
        trace_id: str,
        specialist: _SpecialistBase,
        goal: str,
        context: Dict[str, Any],
    ) -> Dict[str, Any]:
        assignment_payload = self._assignment_payload(goal=goal)
        assignment_envelope = self._envelope(
            trace_id=trace_id,
            sender="Orchestrator",
            recipient=specialist.name,
            message_type="TASK_ASSIGNMENT",
            payload=assignment_payload,
        )
        self.validator.assert_valid_message(assignment_envelope)

        result_payload = specialist.run(task=assignment_payload, context=context)
        result_envelope = self._envelope(
            trace_id=trace_id,
            sender=specialist.name,
            recipient="Orchestrator",
            message_type="TASK_RESULT",
            payload=result_payload,
        )
        self.validator.assert_valid_message(result_envelope)
        return result_payload

    def _assignment_payload(self, goal: str) -> Dict[str, Any]:
        deadline = datetime.now(UTC) + timedelta(seconds=20)
        return {
            "task_id": f"task_{uuid.uuid4().hex[:10]}",
            "goal": goal,
            "constraints": {
                "deadline_utc": deadline.isoformat(),
                "risk_limits": {"max_drawdown_pct": 15.0, "max_exposure_pct": 1.0},
                "allowed_action_space": [
                    "thresholds",
                    "strategy_weights",
                    "regime_gates",
                    "symbol_filters",
                    "position_caps",
                ],
            },
            "expected_output": {
                "schema_id": "task-result.payload.schema.json",
                "required_fields": ["status", "claims", "evidence", "confidence"],
            },
        }

    @staticmethod
    def _envelope(
        trace_id: str,
        sender: str,
        recipient: str,
        message_type: str,
        payload: Dict[str, Any],
    ) -> Dict[str, Any]:
        return {
            "message_id": f"msg_{uuid.uuid4().hex[:12]}",
            "trace_id": trace_id,
            "timestamp_utc": _utc_now_iso(),
            "sender": sender,
            "recipient": recipient,
            "message_type": message_type,
            "payload": payload,
        }

    def _build_decision_payload(
        self,
        trace_id: str,
        specialist_results: Dict[str, Dict[str, Any]],
        model_confidence: float,
        proposed_action: Action,
    ) -> Dict[str, Any]:
        mkt = specialist_results["MarketDataAgent"]
        strat = specialist_results["StrategyAgent"]
        risk = specialist_results["RiskAgent"]
        val = specialist_results["ValidationAgent"]

        risk_veto = risk["status"] == "FAILED"
        disagreements: List[str] = []
        agreements: List[str] = []

        if risk_veto:
            disagreements.append("RiskAgent vetoed execution due to hard risk constraints.")
        else:
            agreements.append("RiskAgent reported no hard veto.")

        if strat["status"] == "OK":
            agreements.append("StrategyAgent supports current strategy posture.")
        else:
            disagreements.append("StrategyAgent flagged low-confidence posture.")

        if mkt["status"] == "OK":
            agreements.append("MarketDataAgent quality checks are acceptable.")
        else:
            disagreements.append("MarketDataAgent detected unstable/noisy market context.")

        validation_claims = val.get("claims", [])
        for claim in validation_claims:
            if "disagreement" in claim.lower() or "conflict" in claim.lower():
                disagreements.append(claim)

        combined_confidence = min(
            float(model_confidence),
            float(mkt["confidence"]["score"]),
            float(strat["confidence"]["score"]),
            float(val["confidence"]["score"]),
        )

        if proposed_action.strategy == StrategyType.WAIT:
            final_action = "WAIT"
            reasoning = "Engine proposed WAIT; orchestrator keeps defensive posture."
        elif risk_veto:
            final_action = "WAIT"
            reasoning = "Risk veto has priority over execution."
        elif disagreements and combined_confidence < self.min_confidence:
            final_action = "INSUFFICIENT_DATA"
            reasoning = "Conflicting signals with low confidence; no reliable edge."
        elif mkt["status"] == "PARTIAL" or strat["status"] == "PARTIAL" or val["status"] == "PARTIAL":
            final_action = "EXECUTE_REDUCED"
            reasoning = "Execution is allowed but reduced due to partial-quality signals."
        else:
            final_action = "EXECUTE"
            reasoning = "Cross-agent evidence supports execution."

        data_gaps: List[str] = []
        for key in ["MarketDataAgent", "StrategyAgent", "RiskAgent", "ValidationAgent"]:
            data_gaps.extend(specialist_results[key].get("data_gaps", []))

        payload = {
            "trace_id": trace_id,
            "agent_inputs_summary": [
                f"MarketDataAgent={mkt['status']}",
                f"StrategyAgent={strat['status']}",
                f"RiskAgent={risk['status']}",
                f"ValidationAgent={val['status']}",
            ],
            "agreements": agreements,
            "disagreements": disagreements,
            "final_reasoning": reasoning,
            "confidence": max(0.0, min(1.0, combined_confidence)),
            "data_gaps": data_gaps,
            "final_action": final_action,
            "risk_veto": {
                "vetoed": bool(risk_veto),
                "reason": risk["claims"][0] if risk_veto and risk.get("claims") else "",
            },
        }
        return payload

    def _save_record(self, record: Dict[str, Any]) -> None:
        try:
            directory = os.path.dirname(self.log_path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            with open(self.log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(record) + "\n")
        except Exception as exc:
            # Keep orchestration non-fatal for live loop.
            _ = exc
