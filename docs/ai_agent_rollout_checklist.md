# AI Agent Rollout Checklist

This is the operational runbook to resume the AI-agent track without destabilizing trading.

## Current State
- Reliability/data hardening: completed through Phase 3.
- AI-agent architecture: implemented through Phase 2 modules.
- Known gap before this checklist: shadow mode needed stricter separation from automatic promotion.

## Important Runtime Rule
- `AGENT_MODE` controls whether agent decisions can override trade actions (`shadow` vs `active`).
- `AUTO_ROLLOUT_ACTIVE_MODE` controls whether candidate policy can affect runtime policy.
- With current code, when `AUTO_ROLLOUT_ACTIVE_MODE=false`, candidate rollout no longer auto-promotes/rolls back from live trades. It stays observational.

## Phase A - Freeze Baseline (24-48h)
Goal: lock a stable baseline before agent changes influence execution.

Set in `.env`:
```env
AGENT_ORCHESTRATION_ENABLED=true
AGENT_MODE=shadow
AUTO_ROLLOUT_ENABLED=true
AUTO_ROLLOUT_ACTIVE_MODE=false
```

Run:
```powershell
.\.venv\Scripts\python.exe scripts/startup_checks.py
.\.venv\Scripts\python.exe main.py --skip-checks
```

Collect:
- `reports/reliability_baseline.json`
- `data/decision_audit.jsonl`
- `data/agent_decisions_hyperliquid_USDC_paper.jsonl`
- `data/auto_rollout_state_hyperliquid_USDC_paper.json`

Pass gate:
- No crashes/restart loops.
- No impossible accounting values (equity/balance remain coherent).
- Reliability trend stable or improving versus prior 24h report.

## Phase B - Shadow Agent Validation (24h)
Goal: validate agent quality while still non-invasive.

Keep same `.env` as Phase A.

Checks:
- Agent emits structured decisions in `data/agent_decisions_*.jsonl`.
- Risk vetoes are coherent (not constant false positives).
- Candidate creation events may occur, but runtime policy remains champion-only.

Pass gate:
- Agent `WAIT`/`EXECUTE_REDUCED` decisions correlate with weaker setups in audit logs.
- No unexplained veto storms.

## Phase C - Controlled Canary Activation
Goal: allow candidate policy impact with strict rollout constraints.

Change in `.env`:
```env
AGENT_MODE=active
AUTO_ROLLOUT_ACTIVE_MODE=true
AUTO_ROLLOUT_STAGE_FRACTION_PROBE=0.25
AUTO_ROLLOUT_STAGE_FRACTION_SCALE=0.60
AUTO_ROLLOUT_STAGE_FRACTION_FULL=1.00
AUTO_ROLLOUT_STAGE_TRADES_PROBE=6
AUTO_ROLLOUT_STAGE_TRADES_SCALE=12
AUTO_ROLLOUT_STAGE_TRADES_FULL=18
AUTO_ROLLOUT_MAX_STAGE_DD_PCT=3.5
AUTO_ROLLOUT_MAX_RISK_VETO_STREAK=6
```

Run:
```powershell
.\.venv\Scripts\python.exe scripts/startup_checks.py
.\.venv\Scripts\python.exe main.py --skip-checks
```

Monitor log lines:
- `[AUTO-ROLLOUT] Candidate ... created`
- `[AUTO-ROLLOUT] ... promoted to canary stage ...`
- `[AUTO-ROLLOUT] ... rolled back ...` (acceptable if risk criteria fail)

Pass gate:
- At least one full candidate cycle completes without runtime instability.
- No safety kills from accounting/data corruption.

## Phase D - Supervised Production Loop
Goal: keep automation bounded while reducing manual intervention.

Keep:
```env
AGENT_ORCHESTRATION_ENABLED=true
AGENT_MODE=active
AUTO_ROLLOUT_ENABLED=true
AUTO_ROLLOUT_ACTIVE_MODE=true
```

Operator policy:
- Review rollout events daily.
- Only adjust thresholds weekly unless hard safety events occur.
- Do not add new strategy families during this stabilization window.

## Rollback Profile (Immediate Safety)
If behavior degrades:
```env
AGENT_MODE=shadow
AUTO_ROLLOUT_ACTIVE_MODE=false
```
Then restart bot and continue paper soak until stable.

## Quick Phase Status Template
Use this before each session:
- Reliability phase: `Phase 3 complete / Phase 4 soak in progress`
- AI-agent phase: `A baseline`, `B shadow validation`, `C canary active`, or `D supervised production`

