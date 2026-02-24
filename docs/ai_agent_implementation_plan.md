# AI Agent Implementation Plan

## Goal
Upgrade the bot from adaptive rules to a constrained, self-improving agent that can diagnose, propose, test, and safely deploy improvements.

## Main Orchestrator (Trading Brain)
- The orchestrator does not trade directly.
- It coordinates specialist agents, resolves conflicts, and produces the final decision packet.
- No single specialist output is final without evidence comparison and orchestration.

### Orchestrator Responsibilities
1. **Agent Management**
- Assign tasks to specialists and enforce role boundaries.
- Prevent overlapping responsibilities.
- Request deeper analysis when evidence is weak.

2. **Communication Control**
- Collect structured outputs from all specialists.
- Force cross-check replies when agents disagree.
- Ensure all conclusions include supporting rationale or data source.

3. **Decision Orchestration**
- Resolve outcomes by consensus or evidence superiority.
- If conflict remains unresolved, return `INSUFFICIENT_DATA` or `WAIT`.

4. **Evidence-First Rule**
- No assumption-only conclusions.
- Every claim must map to observed data, model output, or explicit rule.

## Architecture Loop
1. **Observer**
- Continuously compute regime-wise performance, slippage, loss categories, drift, and execution quality.
- Produce daily diagnostics: what degraded, where, and since when.

2. **Analyst**
- Convert diagnostics into hypotheses.
- Example: `MOMENTUM` underperforms during `BULL -> SIDEWAYS` transitions.

3. **Planner**
- Map hypotheses into bounded actions only (no arbitrary code rewrites in production).
- Action space: thresholds, strategy weights, per-regime gates, symbol filters, position caps.

4. **Experimenter**
- Validate each proposal with walk-forward backtests and paper-shadow runs.
- Compare candidate vs champion on fixed metrics (Sharpe, max drawdown, win rate, tail loss).

5. **Governor**
- Promote only if candidate passes minimum sample and acceptance criteria.
- Canary rollout first; auto-rollback on risk breach.

6. **Memory**
- Persist what was tried, where it worked, and where it failed.
- Avoid repeating previously rejected adaptations.

## Default Specialist Agents
- `MarketDataAgent`: collects and validates market/feature/execution inputs.
- `StrategyAgent`: proposes trade hypotheses or parameter updates.
- `RiskAgent`: computes downside, exposure, cluster risk, and hard-limit checks.
- `ValidationAgent`: challenges assumptions, tests counter-cases, and flags weak evidence.
- `ExecutionAgent`: converts approved decisions into actionable instructions.

## Safety Constraints
- Keep autonomy inside a strict parameter action space.
- Require statistical significance thresholds before promotion.
- Enforce risk-first overrides (drawdown, exposure, cluster caps).
- Always support rollback to last known-good policy.
- `RiskAgent` has veto power on live actions.
- Enforce decision deadlines per cycle to avoid stale outputs in moving markets.
- If uncertainty/disagreement stays high, default to reduced size or `WAIT`.

## Initial Implementation Modules
- `agent/orchestrator.py`
- `agent/analyzer.py`
- `agent/planner.py`
- `agent/experiment_manager.py`
- `agent/governor.py`
- `agent/rollout_manager.py`

## Workflow
Goal -> Task Breakdown -> Agent Assignment -> Agent Communication -> Evidence Comparison -> Conflict Resolution -> Final Decision Summary

## Inter-Agent JSON Schema (Strict)
Use one envelope for all agent traffic. All messages must validate before being accepted by the orchestrator.

Implemented files:
- `schemas/agents/message_envelope.schema.json`
- `schemas/agents/task_assignment.payload.schema.json`
- `schemas/agents/task_result.payload.schema.json`
- `schemas/agents/decision_packet.payload.schema.json`

### 1) Common Envelope
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "agent-message.schema.json",
  "type": "object",
  "required": ["message_id", "trace_id", "timestamp_utc", "sender", "recipient", "message_type", "payload"],
  "properties": {
    "message_id": { "type": "string", "minLength": 8 },
    "trace_id": { "type": "string", "minLength": 8 },
    "timestamp_utc": { "type": "string", "format": "date-time" },
    "sender": { "type": "string" },
    "recipient": { "type": "string" },
    "message_type": {
      "type": "string",
      "enum": [
        "TASK_ASSIGNMENT",
        "TASK_RESULT",
        "CHALLENGE_REQUEST",
        "CHALLENGE_RESPONSE",
        "DECISION_PACKET"
      ]
    },
    "payload": { "type": "object" }
  },
  "additionalProperties": false
}
```

### 2) Task Assignment Payload
```json
{
  "$id": "task-assignment.payload.schema.json",
  "type": "object",
  "required": ["task_id", "goal", "constraints", "expected_output"],
  "properties": {
    "task_id": { "type": "string" },
    "goal": { "type": "string", "minLength": 10 },
    "constraints": {
      "type": "object",
      "required": ["deadline_utc", "risk_limits", "allowed_action_space"],
      "properties": {
        "deadline_utc": { "type": "string", "format": "date-time" },
        "risk_limits": {
          "type": "object",
          "required": ["max_drawdown_pct", "max_exposure_pct"],
          "properties": {
            "max_drawdown_pct": { "type": "number" },
            "max_exposure_pct": { "type": "number" }
          },
          "additionalProperties": true
        },
        "allowed_action_space": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "thresholds",
              "strategy_weights",
              "regime_gates",
              "symbol_filters",
              "position_caps"
            ]
          },
          "minItems": 1
        }
      },
      "additionalProperties": false
    },
    "expected_output": {
      "type": "object",
      "required": ["schema_id", "required_fields"],
      "properties": {
        "schema_id": { "type": "string" },
        "required_fields": { "type": "array", "items": { "type": "string" }, "minItems": 1 }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

### 3) Specialist Task Result Payload
```json
{
  "$id": "task-result.payload.schema.json",
  "type": "object",
  "required": ["task_id", "status", "claims", "evidence", "confidence", "data_gaps"],
  "properties": {
    "task_id": { "type": "string" },
    "status": { "type": "string", "enum": ["OK", "PARTIAL", "INSUFFICIENT_DATA", "FAILED"] },
    "claims": {
      "type": "array",
      "items": { "type": "string", "minLength": 5 },
      "minItems": 1
    },
    "evidence": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["evidence_id", "source", "metric", "value", "window"],
        "properties": {
          "evidence_id": { "type": "string" },
          "source": { "type": "string" },
          "metric": { "type": "string" },
          "value": { "type": ["number", "string", "boolean"] },
          "window": { "type": "string" }
        },
        "additionalProperties": false
      }
    },
    "confidence": {
      "type": "object",
      "required": ["score", "calibration"],
      "properties": {
        "score": { "type": "number", "minimum": 0, "maximum": 1 },
        "calibration": { "type": "string", "enum": ["LOW", "MEDIUM", "HIGH"] }
      },
      "additionalProperties": false
    },
    "proposed_actions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["action_type", "params"],
        "properties": {
          "action_type": {
            "type": "string",
            "enum": [
              "set_threshold",
              "set_strategy_weight",
              "set_regime_gate",
              "set_symbol_filter",
              "set_position_cap"
            ]
          },
          "params": { "type": "object" }
        },
        "additionalProperties": false
      }
    },
    "data_gaps": { "type": "array", "items": { "type": "string" } }
  },
  "additionalProperties": false
}
```

### 4) Final Decision Packet Payload
```json
{
  "$id": "decision-packet.payload.schema.json",
  "type": "object",
  "required": [
    "trace_id",
    "agent_inputs_summary",
    "agreements",
    "disagreements",
    "final_reasoning",
    "confidence",
    "data_gaps",
    "final_action",
    "risk_veto"
  ],
  "properties": {
    "trace_id": { "type": "string" },
    "agent_inputs_summary": { "type": "array", "items": { "type": "string" } },
    "agreements": { "type": "array", "items": { "type": "string" } },
    "disagreements": { "type": "array", "items": { "type": "string" } },
    "final_reasoning": { "type": "string", "minLength": 20 },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
    "data_gaps": { "type": "array", "items": { "type": "string" } },
    "final_action": {
      "type": "string",
      "enum": ["EXECUTE", "EXECUTE_REDUCED", "WAIT", "INSUFFICIENT_DATA"]
    },
    "risk_veto": {
      "type": "object",
      "required": ["vetoed", "reason"],
      "properties": {
        "vetoed": { "type": "boolean" },
        "reason": { "type": "string" }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

### Validation Rules
- Reject any message that fails schema validation.
- Reject `TASK_RESULT` payloads with claims but empty evidence.
- If `RiskAgent` sends veto, orchestrator must force final action to `WAIT` or `EXECUTE_REDUCED`.
- If disagreement remains unresolved and confidence < 0.55, final action must be `INSUFFICIENT_DATA` or `WAIT`.

## Final Decision Packet (Required Output)
- Summary of specialist inputs
- Points of agreement
- Points of disagreement
- Final reasoning
- Confidence level
- Data gaps / uncertainties
- Final action (`EXECUTE`, `EXECUTE_REDUCED`, `WAIT`, `INSUFFICIENT_DATA`)

## Integration Path
1. Build `orchestrator.py` and standardize specialist message schema.
2. Integrate Observer + Analyst with current telemetry and logs.
3. Add Planner with constrained action schema.
4. Add Experimenter and benchmark harness.
5. Add Governor (canary + rollback + veto handling).
6. Wire Memory into scheduler for continuous learning cycles.

## Phase 2 Status (Implemented)
- Automatic candidate creation from diagnostics + planner actions.
- Persistent champion/candidate policy registry with versioning.
- Staged canary rollout (`PROBE -> SCALE -> FULL`) with automatic rollback on stage drawdown breach.
- Stage-gate evaluation using experiment criteria (`win_rate_delta`, `sharpe_delta`, `drawdown_increase`) and governor decisions.
- Automatic champion promotion after all canary stages pass.
- Runtime policy deployment wired into trading engine via bounded controls:
  - `min_signal_score`
  - `confidence_buffer`
  - `size_multiplier`
  - `strategy_weights`
  - `blocked_strategies`
  - regime gates (`require_regime_stable`, `min_regime_confidence`)
