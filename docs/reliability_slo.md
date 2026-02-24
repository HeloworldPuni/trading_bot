# Reliability SLO (Phase 0 Baseline Lock)

This document defines reliability metrics and pass/fail gates for the trading runtime.

## Scope
- Exchange: current runtime venue (example: Hyperliquid paper)
- Data sources:
- `data/experience_log_*.jsonl`
- `data/decision_audit.jsonl`
- `adaptive_trader.log`

## Metrics
1. `price_available_rate`
- Definition: fraction of experience records with `market_state.current_price > 0`.
- Formula: `price_available_records / records_in_window`
- Target: `>= 0.995`

2. `ohlcv_valid_rate`
- Definition: fraction of records not in feeder SAFE-state signature.
- SAFE-state signature currently means:
- `current_risk_state == "DANGER"`
- `current_price == 0`
- `raw_timestamp is null`
- `atr == 0`
- Formula: `1 - (safe_state_records / records_in_window)`
- Target: `>= 0.99`

3. `rate_limit_hits_per_1000_decisions`
- Definition: rate-limit warnings normalized by decision volume.
- Formula: `(rate_limit_hits / decision_count) * 1000`
- Target: `<= 1.0`

4. `ticker_unavailable_per_1000_decisions`
- Definition: "ticker last price unavailable" warnings normalized by decision volume.
- Formula: `(ticker_last_unavailable / decision_count) * 1000`
- Target: `<= 1.0`

5. `startup_ready_seconds_p95`
- Definition: p95 time from startup banner to `Components initialized.` log line.
- Formula: p95 of startup duration samples in analysis window.
- Target: `<= 180 seconds`

## Phase 0 Gate
- Run baseline collector.
- Persist report to `reports/reliability_baseline.json`.
- Gate status:
- `PASS` if all checks pass
- `FAIL` if any check fails
- `UNKNOWN` if data is insufficient for one or more checks

## Command
```powershell
.\.venv\Scripts\python.exe scripts/reliability_baseline.py --hours 24
```

Optional output path:
```powershell
.\.venv\Scripts\python.exe scripts/reliability_baseline.py --hours 24 --report-path reports/reliability_baseline.json
```

## Notes
- Phase 0 is measurement-only. It does not modify trading logic.
- This baseline is the reference before deeper reliability architecture changes in later phases.
