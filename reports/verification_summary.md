# Verification Report

## 1. Environment Setup

- Python Version: 3.14 (Confirmed)
- Dependencies: Installed successfully (including `ccxt`, `scikit-learn`, `pandas`)
- Runtime Fixes Applied:
  - Repaired broken base Python layout by restoring `C:\Python314\DLLs` extension modules.
  - Confirmed stdlib path probe (`C:\Python314\Lib\encodings`) passes at startup.
- Status: READY

## 2. Unit Tests

- Import Check: Passed (`imports OK`)
- Pytest: Passed (19/19 tests), scoped to `src/` and `tests/` via `pytest.ini`
- Note: 1 warning from XGBoost about serialized model compatibility across versions

## 3. Backtest Results (Smoke Tests)

Backtests are complete (`scripts/backtest.py --fast`).

### BTC/USDT

- Status: Complete
- Final Balance: $10,601.21
- Net Return (vs $10,000 start): +$601.21 (+6.01%)
- Realized Trade PnL Sum: +$805.46
- Win Rate: 47.49% (478 trades)
- Check: Passed (positive expectancy)

### ETH/USDT

- Status: Complete
- Final Balance: $10,315.59
- Net Return (vs $10,000 start): +$315.59 (+3.16%)
- Realized Trade PnL Sum: +$414.00
- Win Rate: 46.03% (239 trades)
- Check: Passed (positive expectancy)

### SOL/USDT

- Status: Complete
- Final Balance: $9,972.57
- Net Return (vs $10,000 start): -$27.43 (-0.27%)
- Realized Trade PnL Sum: -$7.51
- Win Rate: 38.00% (50 trades)
- Check: Review (near breakeven, weaker edge than BTC/ETH)

## 4. Issues Log

- [x] `hmmlearn` installation issue handled (kept fallback path active)
- [x] Verified fallback in `src/features/hmm_regime.py` (`GaussianMixture` used when `hmmlearn` is unavailable)
- [x] `pip` missing in venv fixed (bootstrapped via `ensurepip`)
- [x] `scripts/startup_checks.py` import path issue fixed (`python scripts/startup_checks.py` now works from repo root)
- [x] `src/monitoring/drift.py` now degrades gracefully when `scipy` is unavailable/broken (z-score fallback)
- [x] `src/ml/staleness.py` output normalized to ASCII-safe status tags (`[OK]`, `[WARN]`, `[INFO]`)

## 5. Runtime Hardening

- [x] Fixed Windows startup check crash caused by console encoding (`scripts/startup_checks.py`, `src/core/config_validator.py`)
- [x] Added console encoding guard in `main.py` to prevent `UnicodeEncodeError` on cp1252 terminals
- [x] Startup checks run cleanly and return success
- [x] Live smoke run completed with `python main.py --once` (single-cycle scan finished)
