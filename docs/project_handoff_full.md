# Project Handoff (Full Technical Context)

Generated: 2026-02-17  
Repository: `basecoin`  
Purpose: give another LLM complete context on how this bot is built, how it trades, and how it learns.

## 1) What This Project Is

This is an adaptive multi-asset crypto trading system with:
- Rule-based strategy selection and gating.
- ML confidence scoring (ensemble by market regime).
- Portfolio/risk controls and execution routing.
- Meta-learning from closed trades.
- Agent-orchestrated governance and staged auto-rollout.
- Exchange support via CCXT, with deeper Hyperliquid private+websocket integration.

Primary runtime entrypoint:
- `main.py`

Primary runtime mode used recently:
- `TRADING_MODE=paper` on `EXCHANGE_ID=hyperliquid` (with optional active orchestration and auto-rollout).

## 2) High-Level Architecture

Core runtime path:
- `src/data/feeder.py` builds `MarketState` from OHLCV+indicators.
- `src/engine/system.py` (`TradingEngine`) chooses action + confidence.
- `src/core/risk.py` validates/scales trade risk.
- `main.py` applies portfolio-level risk/exposure checks and opens/closes positions.
- `src/core/portfolio.py` tracks positions, equity, and trade history.
- `src/database/storage.py` logs decisions and later resolution updates.
- `src/core/meta_learner.py` learns from resolved trades and adjusts behavior.
- `scripts/learning_scheduler.py` + `src/ml/pipeline.py` retrain models on new resolved logs.
- `src/agent/orchestrator.py` + `src/agent/rollout_manager.py` provide governance and staged policy rollout.

## 3) Runtime Modes and Execution Semantics

### 3.1 Main modes
- Live loop: `main.py` -> `run_live_mode(...)`.
- Replay mode: `main.py --replay ...` -> `run_replay_mode(...)`.
- Backtest engine: `scripts/backtest.py` -> `src/backtest/engine.py`.

### 3.2 Important execution behavior
- In normal paper mode, orders are simulated through `src/execution/paper.py`.
- Real signed execution is implemented for Hyperliquid in:
  - `src/exchange/hyperliquid_private.py`
  - `src/execution/hyperliquid_live.py`
- Signed live orders are only used when all are true:
  - `EXCHANGE_ID=hyperliquid`
  - `TRADING_MODE=live`
  - `HYPERLIQUID_ENABLE_PRIVATE_ORDERS=true`

If those are not true, bot logic runs but execution remains paper/simulated.

## 4) End-to-End Live Cycle (Detailed)

Observed live cycle in `main.py`:
1. Initialize connector using `create_exchange_connector()` (`src/exchange/factory.py`).
2. Initialize feeder, engine, paper executor, portfolio, dashboard.
3. Optionally initialize Hyperliquid private client and websocket user stream.
4. Initialize monitoring/governance layers:
- `DriftMonitor`
- `CanaryMonitor`
- `DivergenceMonitor`
- `StrategyPerformanceTracker`
- `BanditAllocator`
- `LearningScheduler` (if enabled)
- `AgentOrchestrator` (if enabled)
- `AutoRolloutManager` (if enabled)
5. Load top symbols by volume and refresh periodically.
6. For each symbol:
- Build `MarketState` from latest candles (`LiveFeeder.get_current_state`).
- Pull current ticker.
- Update drift monitor.
- Engine computes proposed action + confidence.
- Optional agent orchestration may override to `WAIT` or reduced-size execution.
- Apply portfolio-level risk/exposure caps.
- Compute leverage, TP/SL, position size, strategy weighting, bandit weighting.
- Execute entry (paper or Hyperliquid live).
- Update open-position metrics.
- Evaluate exits (TP/SL/trailing/sync-closure), close positions, log outcomes.
- Feed trade results to MetaLearner and rollout manager.
- Update dashboard.
7. Persist logs/state continuously.

## 5) Data Model Contracts

### 5.1 MarketState
Defined in `src/core/definitions.py`.
Contains:
- Regime/volatility/trend enums.
- Technical indicators: RSI, SMA spread, MACD, Bollinger, ATR.
- Execution-aware metrics: spread/body/gap/volume zscore/liquidity proxy.
- Funding/context metadata.
- HTF features.
- Regime stability/confidence/momentum-shift features.
- Position/risk context fields.

### 5.2 Action
Defined in `src/core/definitions.py`.
Contains:
- `strategy`, `direction`, `risk_level`
- risk fields (`base_risk`, `adjusted_risk`, `risk_multiplier`)
- execution targets (`tp`, `sl`, `target_weight`)
- reasoning string.

## 6) Strategy System

### 6.1 Strategy enum currently available
`src/core/definitions.py`:
- `MOMENTUM`
- `CROSS_SECTIONAL_MOMENTUM`
- `BREAKOUT`
- `VOLATILITY_BREAKOUT`
- `SHORT_MOMENTUM`
- `SCALP`
- `MEAN_REVERSION`
- `ARBITRAGE`
- `MARKET_MAKING`
- `WAIT`

### 6.2 Gating layer
`src/core/gating.py`:
- First hard stop: if drawdown <= -5%, no strategies allowed.
- Regime-based allowlist:
  - Bull: momentum, breakout, arbitrage, optional cross-sectional and vol breakout.
  - Bear: short momentum, arbitrage, optional cross-sectional and vol breakout.
  - Sideways: scalp, mean reversion, arbitrage; low-vol sideways can include market making.
- Low-vol regime additionally disables breakout/cross-sectional/vol-breakout.

### 6.3 Scoring logic
`src/engine/system.py::_basic_selector`:
- Pre-filters: spread, gap, candle body limits.
- Computes strategy scores from indicator conditions.
- Applies:
  - MetaLearner policy score multipliers.
  - Strategy performance weights.
  - Runtime rollout weights.
- Selects max score if above `MIN_SIGNAL_SCORE`.
- Repetition limiter can rotate strategy or force WAIT.
- Optional strategic random WAIT injection via `STRATEGIC_WAIT_PROB`.

## 7) Risk Stack

### 7.1 Action-level risk
`src/core/risk.py`:
- Maps `RiskLevel` to base risk %.
- Downgrades risk in DANGER or near drawdown threshold.
- Applies confidence-based risk multiplier (bounded).

### 7.2 Portfolio-level risk
`src/core/risk_controls.py` + `main.py`:
- Daily loss halt.
- Peak drawdown halt.
- Gross exposure cap.
- Correlation-cluster cap (`cluster_map.json` driven).
- Volatility targeting scaler.

### 7.3 Canary and governance veto
- `src/monitoring/canary.py`: canary win-rate/DD halt.
- `src/agent/orchestrator.py`: `RiskAgent` veto can force WAIT.
- `src/agent/rollout_manager.py`: risk veto streak can roll back candidate policy.

## 8) Position Lifecycle and PnL

Main state engine:
- `src/core/portfolio.py`

Open:
- Enforces per-symbol and total position limits.
- Deducts entry fee and margin.
- Stores TP/SL, leverage, strategy, decision_id, trail state.

Update:
- Calculates unrealized PnL and portfolio equity.
- Manages trailing stop activation/update.

Close:
- Applies exit fee.
- Calculates realized PnL.
- Restores margin and updates balance/equity.
- Assigns loss category for forensics:
  - `REGIME_SHIFT`
  - `VOLATILITY_SPIKE`
  - `BAD_TIMING`
  - `MARKET_MOVE`

Persistence:
- Uses exchange-scoped state file by default:
  - `data/portfolio_state_<exchange>_<quote>_<mode>.json`
- Legacy fallback supported for old Binance paper file.

## 9) Self-Learning: What Actually Learns

There are four independent learning/adaptation loops.

### 9.1 MetaLearner (online adaptation)
`src/core/meta_learner.py`:
- Updates from each closed trade.
- Tracks win rate and loss categories globally + by `strategy|regime`.
- Adapts confidence threshold every 10 trades.
- Produces bounded policy adjustments:
  - score multiplier
  - confidence buffer
  - size multiplier
- Engine consumes these adjustments during selection and gating.

### 9.2 Strategy weighting + blocking
`src/core/allocator.py`:
- `StrategyPerformanceTracker`: rolling win-rate/avg-pnl stats.
- `BanditAllocator`: exploration/exploitation weighting.
- Main loop multiplies size by these weights and can block poor strategies.
- State persisted in `STRATEGY_INTELLIGENCE_FILE`.

### 9.3 ML retraining pipeline
`scripts/learning_scheduler.py` + `src/ml/pipeline.py`:
- Counts newly resolved decisions.
- Rebuilds dataset from logs.
- Retrains regime experts (`bull`, `bear`, `sideways`).
- Promotes only if new expert outperforms old expert.
- Updates `models/registry.json` active version.

### 9.4 Agent governance + auto rollout
- `src/agent/orchestrator.py` gives final action packet from specialist agents.
- `src/agent/rollout_manager.py`:
  - Creates candidate policy from diagnostics/planner actions.
  - Runs staged canary (`PROBE -> SCALE -> FULL`).
  - Promotes or rolls back automatically based on metrics/risk events.
  - Keeps reject-memory cooldown to avoid repeating failed policies.

## 10) ML System Details

### 10.1 Inference
`src/ml/inference.py`:
- Loads active model(s) from registry.
- If active ensemble exists, routes by regime:
  - bull expert for bull regime.
  - bear expert for bear regime.
  - sideways expert for sideways/transition.
- Uses persisted feature maps from `models/feature_maps.json`.
- Outputs confidence `P(good_trade)`.

### 10.2 Dataset and labels
`src/ml/dataset_builder.py`:
- Converts resolved decision logs to ML-ready rows.
- Excludes WAIT actions from training.
- Label is strict profitability target (fee/noise aware) derived from final reward/outcome.
- Maintains consistent categorical maps (session/symbol).

### 10.3 Trainer
`src/ml/trainer.py`:
- Supports XGBoost and LightGBM.
- Computes validation metrics.
- Includes optional Optuna tuning.
- Fits probability calibrator (Platt scaling) when possible.

### 10.4 Registry
`src/ml/registry.py`:
- Tracks versions and active model.
- Tracks trained-record counters globally and per-log path.
- Prevents cross-log counter mismatch issues.

## 11) Exchange Integration

### 11.1 Generic connector
`src/exchange/ccxt_connector.py`:
- Symbol normalization and translation.
- Ticker/OHLCV caching.
- Funding-rate access.
- Top-volume symbol scanning.
- Rate-limit cooldown/degraded-mode fallback.

### 11.2 Hyperliquid private path
`src/exchange/hyperliquid_private.py`:
- API wallet + key wiring.
- Nonce throttling.
- Place/cancel/modify orders.
- Response normalization.

### 11.3 Hyperliquid websocket + reconciliation
- `src/exchange/hyperliquid_stream.py`: user stream + watchdog + dedupe.
- `src/exchange/hyperliquid_reconcile.py`: position/order state updates from websocket events.
- Main loop uses this for exchange/local sync checks.

## 12) Agent-Orchestration Protocol

Implemented schema set:
- `schemas/agents/message_envelope.schema.json`
- `schemas/agents/task_assignment.payload.schema.json`
- `schemas/agents/task_result.payload.schema.json`
- `schemas/agents/decision_packet.payload.schema.json`

Validation rules enforced in `src/agent/schema_validator.py`:
- Reject messages failing envelope/payload schema.
- Reject task results with claims but empty evidence.
- If risk veto is true, final action must be `WAIT` or `EXECUTE_REDUCED`.
- If disagreements + confidence < 0.55, final action must be `WAIT` or `INSUFFICIENT_DATA`.

## 13) Storage and File Map

Primary runtime artifacts:
- Portfolio state: `data/portfolio_state_<exchange>_<quote>_<mode>.json`
- Experience decisions: `data/experience_log_<exchange>_<quote>_<mode>.jsonl`
- Resolution sidecar: `...jsonl.resolved.jsonl`
- MetaLearner state: `data/meta_learner_state.json`
- Decision audit: `data/decision_audit.jsonl`
- Strategy intelligence: `data/strategy_intelligence_<exchange>_<quote>_<mode>.json`
- Agent decisions: `data/agent_decisions_<exchange>_<quote>_<mode>.jsonl`
- Auto-rollout state: `data/auto_rollout_state_<exchange>_<quote>_<mode>.json`
- Models registry: `models/registry.json`
- Feature maps: `models/feature_maps.json`

## 14) Configuration Surface (Complete Key Groups)

Source of truth: `src/config.py`.  
Do not rely on stale docs only.

### 14.1 Core venue/runtime
- `TRADING_MODE`, `EXCHANGE_ID`, `EXCHANGE_MARKET_TYPE`, `QUOTE_CURRENCY`, `SYMBOL`
- `PORTFOLIO_STATE_FILE`, `EXPERIENCE_LOG_FILE`, `STRATEGY_INTELLIGENCE_FILE`
- `LOG_LEVEL`, `DATA_PATH`, `STRICT_STARTUP`

### 14.2 Learning and ML
- `LEARNING_ENABLED`, `LEARNING_INTERVAL_HOURS`, `LEARNING_MIN_TRADES`
- `ML_CONFIDENCE_MIN`, `MIN_SIGNAL_SCORE`
- `EV_GATING`, `EV_THRESHOLD`

### 14.3 Agent and rollout
- `AGENT_ORCHESTRATION_ENABLED`, `AGENT_MODE`, `AGENT_MIN_CONFIDENCE`, `AGENT_REDUCED_SIZE_MULTIPLIER`, `AGENT_LOG_FILE`
- `AUTO_ROLLOUT_ENABLED`, `AUTO_ROLLOUT_ACTIVE_MODE`, `AUTO_ROLLOUT_STATE_FILE`
- `AUTO_ROLLOUT_TRIGGER_TRADES`, `AUTO_ROLLOUT_WINDOW_TRADES`
- `AUTO_ROLLOUT_STAGE_FRACTION_PROBE`, `AUTO_ROLLOUT_STAGE_FRACTION_SCALE`, `AUTO_ROLLOUT_STAGE_FRACTION_FULL`
- `AUTO_ROLLOUT_STAGE_TRADES_PROBE`, `AUTO_ROLLOUT_STAGE_TRADES_SCALE`, `AUTO_ROLLOUT_STAGE_TRADES_FULL`
- `AUTO_ROLLOUT_MAX_STAGE_DD_PCT`, `AUTO_ROLLOUT_MIN_WIN_RATE_DELTA`, `AUTO_ROLLOUT_MIN_SHARPE_DELTA`
- `AUTO_ROLLOUT_MAX_DD_INCREASE`, `AUTO_ROLLOUT_MAX_RISK_VETO_STREAK`, `AUTO_ROLLOUT_POLICY_COOLDOWN_TRADES`, `AUTO_ROLLOUT_MAX_REJECT_MEMORY`

### 14.4 Hyperliquid private/ws
- `HYPERLIQUID_TESTNET`, `HYPERLIQUID_API_WALLET`, `HYPERLIQUID_PRIVATE_KEY`
- `HYPERLIQUID_ACCOUNT_ADDRESS`, `HYPERLIQUID_VAULT_ADDRESS`
- `HYPERLIQUID_ENABLE_PRIVATE_ORDERS`, `HYPERLIQUID_ORDER_SLIPPAGE`
- `HYPERLIQUID_USER_WS_ENABLED`, `HYPERLIQUID_WS_STALE_SEC`, `HYPERLIQUID_WS_LOG_EVENTS`
- `HYPERLIQUID_ORDER_SYNC_GRACE_SEC`

### 14.5 Portfolio and risk
- `INITIAL_CAPITAL`, `FEE_RATE`, `RISK_PROFILE`
- `BASE_LEVERAGE`, `MAX_LEVERAGE`, `MIN_LEVERAGE`, `LEVERAGE_SCALING`
- `RISK_PER_TRADE`, `MAX_POSITION_PCT`, `MAX_CONCURRENT_POSITIONS`, `MAX_POSITIONS_PER_SYMBOL`
- `MAX_DAILY_LOSS_PCT`, `MAX_DRAWDOWN_PCT`, `VOL_TARGET_DAILY_PCT`
- `EXPOSURE_CAP_PCT`, `CORR_CLUSTER_CAP_PCT`
- `CANARY_MODE`, `CANARY_TRADE_LIMIT`, `CANARY_MIN_WIN_RATE`, `CANARY_MAX_DD_PCT`
- `ENTRY_COOLDOWN_MINUTES`

### 14.6 Universe and timing
- `ACTIVE_SYMBOLS`, `TOP_COINS_COUNT`, `COIN_REFRESH_MINUTES`
- `SCAN_TIMEFRAME`, `LTF_LOOKBACK`, `HTF_TIMEFRAME`, `HTF_LOOKBACK`

### 14.7 Strategy filters and adaptation
- `STRATEGY_MIN_SAMPLES`, `STRATEGY_WEIGHTING_ENABLED`, `STRATEGY_FILTER_ENABLED`, `STRATEGY_FILTER_REGIME_AWARE`
- `STRATEGY_FILTER_WINDOW`, `STRATEGY_FILTER_MIN_TRADES`, `STRATEGY_FILTER_MIN_WIN_RATE`, `STRATEGY_FILTER_MIN_AVG_PNL`
- `ADAPTIVE_POLICY_ENABLED`, `ADAPTIVE_POLICY_MIN_SAMPLES`, `ADAPTIVE_POLICY_MIN_DOMINANCE`
- `ADAPTIVE_POLICY_MAX_SCORE_PENALTY`, `ADAPTIVE_POLICY_MAX_THRESHOLD_BONUS`
- `ADAPTIVE_POLICY_MIN_SIZE_MULTIPLIER`, `ADAPTIVE_POLICY_MAX_SIZE_MULTIPLIER`, `ADAPTIVE_POLICY_RECOVERY_WIN_RATE`

### 14.8 Strategy-specific thresholds
- Cross-sectional:
  - `CROSS_SECTIONAL_MOMENTUM_ENABLED`
  - `CROSS_SECTIONAL_MIN_UNIVERSE`
  - `CROSS_SECTIONAL_TOP_PCT`
  - `CROSS_SECTIONAL_BOTTOM_PCT`
  - `CROSS_SECTIONAL_MIN_ABS_SPREAD`
- Volatility breakout:
  - `VOLATILITY_BREAKOUT_ENABLED`
  - `VOL_BREAKOUT_BBW_SQUEEZE_MAX`
  - `VOL_BREAKOUT_EXPANSION_RATIO_MIN`
  - `VOL_BREAKOUT_BASELINE_WINDOW`
  - `VOL_BREAKOUT_MIN_VOLUME_ZSCORE`
  - `VOL_BREAKOUT_MIN_ATR_PCT`
  - `VOL_BREAKOUT_ADMISSION_ENABLED`
  - `VOL_BREAKOUT_ADMISSION_MIN_TRADES`
  - `VOL_BREAKOUT_ADMISSION_MIN_WIN_RATE`
  - `VOL_BREAKOUT_ADMISSION_MIN_AVG_PNL`
  - `VOL_BREAKOUT_WARMUP_SIZE_MULTIPLIER`
- General indicator thresholds:
  - `RSI_OVERBOUGHT`, `RSI_OVERSOLD`
  - `TREND_SPREAD_MIN`, `HTF_TREND_SPREAD_MIN`
  - `MIN_VOLUME_ZSCORE`
  - `MAX_SPREAD_PCT`, `MAX_GAP_PCT`, `MAX_BODY_PCT`
  - `NEAR_LEVEL_PCT`
  - `FUNDING_ARB_THRESHOLD`, `MM_MAX_SPREAD_PCT`, `MM_MAX_BODY_PCT`
- TP/SL and trailing:
  - `ATR_TP_SL_ENABLED`
  - `ATR_TP_MULTIPLIER_SCALP`, `ATR_SL_MULTIPLIER_SCALP`
  - `ATR_TP_MULTIPLIER_SWING`, `ATR_SL_MULTIPLIER_SWING`
  - `SCALP_TP_PCT`, `SCALP_SL_PCT`, `SWING_TP_PCT`, `SWING_SL_PCT`
  - `TRAILING_STOP_ENABLED`, `TRAILING_ACTIVATION_MODE`, `TRAILING_ATR_MULTIPLIER`

## 15) Test and Validation Status (Current Snapshot)

As checked now:
- `python -m pytest -q` -> 69 passed.
- `python scripts/startup_checks.py` -> all checks passed.

Pytest scope:
- `pytest.ini` limits discovery to `src` and `tests`.

## 16) Known Caveats / Technical Debt (Important for Next LLM)

1. Main-loop indentation defect in `main.py`.
- In current file, runtime policy + decide/act block is dedented outside the per-symbol `for sym in active_symbols:` loop.
- This can cause only the last scanned symbol state to drive decisions/execution each cycle.
- This explains symptoms like “bot scanning many symbols but taking very few trades”.

2. Unicode logging issues still possible on some Windows consoles.
- Even with encoding guards, some components still contain emoji/unicode text.
- cp1252 terminals can throw `UnicodeEncodeError` in some paths.

3. Some modules are production path, some are legacy/research path.
- Active path is primarily `main.py` + `src/core`, `src/engine`, `src/ml`, `src/agent`, `src/exchange`, `src/data`.
- Additional modules in `src/portfolio`, `src/risk`, `src/deployment`, `src/models`, and some scripts are partially legacy or research utilities.

4. Context data ingestors are mostly placeholders.
- `src/data/context/sentiment.py` and `src/data/context/onchain.py` currently use mock/placeholder data flow.
- `src/data/macro.py` returns static fallback values by default.

5. Live signed execution is Hyperliquid-specific.
- For non-Hyperliquid live runs, strategy loop can still execute in paper semantics unless custom live execution path is added.

6. `scripts/reset_paper.py` is legacy-targeted.
- It resets old fixed filenames and may not clear newer exchange-scoped state files.

## 17) Operational Commands

Environment:
- `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`

Validation:
- `.\.venv\Scripts\python.exe -m pytest -q`
- `.\.venv\Scripts\python.exe scripts/startup_checks.py`

Run bot:
- `.\.venv\Scripts\python.exe main.py`
- `.\.venv\Scripts\python.exe main.py --once`
- Replay:
  - `.\.venv\Scripts\python.exe main.py --replay data/BTC_USDT_2020_2026.csv --symbol BTC/USDT`

Backtest:
- `.\.venv\Scripts\python.exe scripts/backtest.py --csv data/BTC_USDT_2020_2026.csv --symbol BTC/USDT --fast`

Manual training:
- `.\.venv\Scripts\python.exe scripts/build_dataset.py`
- `.\.venv\Scripts\python.exe scripts/train_policy.py`
- `.\.venv\Scripts\python.exe scripts/train_ensemble.py`

Hyperliquid private smoke:
- `.\.venv\Scripts\python.exe scripts/hyperliquid_private_smoke.py --testnet`

## 18) Security Notes

- Never share real `.env` content with API keys/private keys.
- Share `.env.example` and `src/config.py` for configuration structure.
- If sharing logs externally, scrub wallet addresses/order ids if needed.

## 19) Ready-to-Use Prompt for Another LLM

Use this with the attached repo/files:

```text
You are auditing and extending a Python trading system in this repository.
Read docs/project_handoff_full.md first, then verify all claims against code before changing anything.

Goals:
1) Explain current behavior exactly as implemented (not as intended).
2) Identify critical correctness issues in live loop, risk, and learning pipeline wiring.
3) Propose minimal safe fixes with tests.
4) Preserve existing interfaces and exchange-scoped file behavior.
5) Do not remove risk controls.

Constraints:
- Keep changes backward compatible with Binance defaults.
- Keep Hyperliquid private execution gated behind env flags.
- Use existing schema-based agent protocol.
- Add/adjust tests for every behavior change.

Output format:
- Findings by severity.
- Proposed patch plan.
- Exact files to modify.
- Validation commands and expected pass criteria.
```

