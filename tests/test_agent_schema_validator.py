from src.agent.schema_validator import AgentSchemaValidator


def _valid_envelope(message_type: str, payload: dict) -> dict:
    return {
        "message_id": "msg_12345678",
        "trace_id": "trace_12345678",
        "timestamp_utc": "2026-02-17T12:00:00Z",
        "sender": "Orchestrator",
        "recipient": "StrategyAgent",
        "message_type": message_type,
        "payload": payload,
    }


def test_valid_task_assignment_passes():
    validator = AgentSchemaValidator()
    payload = {
        "task_id": "task-1",
        "goal": "Analyze momentum degradation in transition regimes.",
        "constraints": {
            "deadline_utc": "2026-02-17T12:10:00Z",
            "risk_limits": {"max_drawdown_pct": 10.0, "max_exposure_pct": 0.6},
            "allowed_action_space": ["thresholds", "strategy_weights"],
        },
        "expected_output": {
            "schema_id": "task-result.payload.schema.json",
            "required_fields": ["claims", "evidence", "confidence"],
        },
    }
    msg = _valid_envelope("TASK_ASSIGNMENT", payload)

    result = validator.validate_message(msg)
    assert result.valid is True
    assert result.errors == []


def test_invalid_task_result_claims_without_evidence_fails():
    validator = AgentSchemaValidator()
    payload = {
        "task_id": "task-2",
        "status": "OK",
        "claims": ["Momentum fails in bull-to-sideways transitions."],
        "evidence": [],
        "confidence": {"score": 0.72, "calibration": "MEDIUM"},
        "data_gaps": [],
    }
    msg = _valid_envelope("TASK_RESULT", payload)

    result = validator.validate_message(msg)
    assert result.valid is False
    assert any("payload.evidence" in err for err in result.errors)


def test_decision_packet_respects_risk_veto_rule():
    validator = AgentSchemaValidator()
    payload = {
        "trace_id": "trace_12345678",
        "agent_inputs_summary": ["RiskAgent vetoed due to drawdown spike."],
        "agreements": ["Risk limit breached."],
        "disagreements": [],
        "final_reasoning": "Risk override was activated and execution should be blocked.",
        "confidence": 0.91,
        "data_gaps": [],
        "final_action": "EXECUTE",
        "risk_veto": {"vetoed": True, "reason": "DD > max threshold"},
    }
    msg = _valid_envelope("DECISION_PACKET", payload)

    result = validator.validate_message(msg)
    assert result.valid is False
    assert any("risk_veto.vetoed=true" in err for err in result.errors)


def test_decision_packet_low_confidence_disagreement_forces_wait_or_insufficient():
    validator = AgentSchemaValidator()
    payload = {
        "trace_id": "trace_12345678",
        "agent_inputs_summary": ["Strategy and validation agents disagree on signal quality."],
        "agreements": [],
        "disagreements": ["Entry timing confidence is weak."],
        "final_reasoning": "Evidence is conflicting and confidence is below threshold.",
        "confidence": 0.43,
        "data_gaps": ["Need more samples in current regime."],
        "final_action": "EXECUTE_REDUCED",
        "risk_veto": {"vetoed": False, "reason": ""},
    }
    msg = _valid_envelope("DECISION_PACKET", payload)

    result = validator.validate_message(msg)
    assert result.valid is False
    assert any("confidence < 0.55" in err for err in result.errors)
