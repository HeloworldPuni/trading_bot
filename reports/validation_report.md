# Validation Report

Date: 2026-02-08

## Full Backtest (BTC_USDT_2020_2026.csv, fast)
- Final Balance: $10144.33
- Final Equity:  $10144.33
- Trades: 94
- Win Rate: 48.94%
- Avg PnL %: 0.1937
- Total PnL: $182.35

## Walk-Forward (ml_dataset.csv)
- Splits: 8
- Avg Test AUC: 0.8348
- Avg Test Acc: 0.7485

## Aggressive Profile Backtest (BTC_USDT_2020_2026.csv, fast)
- Final Balance: $10035.94
- Final Equity:  $10035.94
- Trades: 97
- Win Rate: 42.27%
- Avg PnL %: 0.0730
- Total PnL: $82.88

## Notes
- Backtest executed with `--fast` (DB logging disabled), slippage 5 bps, latency 1 candle.
- Signal gating: `MIN_SIGNAL_SCORE=0.60`, ML confidence gating: `ML_CONFIDENCE_MIN=0.65`.
- Strategy filter enabled (rolling window, regime-aware) and ATR-based TP/SL enabled.
 - Aggressive run used `RISK_PROFILE=aggressive` overrides.

## Next Tuning Options
1. Adjust confidence/EV thresholds to improve trade selectivity vs frequency.
2. Re-run backtests with funding fees and different slippage/latency assumptions.
3. Add regime-specific thresholds or dynamic thresholds based on volatility.
