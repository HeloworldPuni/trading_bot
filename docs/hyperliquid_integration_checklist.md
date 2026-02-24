# Hyperliquid Integration Checklist

This checklist is designed to add Hyperliquid support without breaking the current Binance workflow.

## 0) Guardrails (Do First)

- [x] Keep existing Binance imports and runtime paths backward compatible.
- [x] Keep `EXCHANGE_ID=binance` behavior unchanged by default.
- [x] Route all exchange-specific logic behind a connector factory.
- [x] Require passing startup checks + tests before declaring integration complete.

## 1) Exchange Abstraction Layer

- [x] Introduce a reusable CCXT connector base with:
- [x] OHLCV/ticker/funding/top-volume methods already used by the engine.
- [x] Symbol normalization (`BASE/QUOTE` vs `BASE/QUOTE:SETTLE`) to avoid venue format breaks.
- [x] Exchange symbol translation (`BTC/USDC` -> venue-specific symbol).
- [x] Cache-safe ticker/ohlcv handling (existing behavior retained).

Acceptance criteria:
- [x] Existing callers in `main.py`, feeders, and scripts still work without API changes.

## 2) Hyperliquid Connector

- [x] Add `HyperliquidConnector` with exchange-specific defaults:
- [x] `EXCHANGE_ID=hyperliquid`
- [x] `QUOTE_CURRENCY=USDC`
- [x] `EXCHANGE_MARKET_TYPE=swap`
- [x] Support public data flow immediately (no trade signing required for read paths).
- [x] Add stable fallback symbols (`BTC/USDC`, `ETH/USDC`, `SOL/USDC`).

Acceptance criteria:
- [x] `create_exchange_connector()` returns Hyperliquid connector when configured.
- [x] `fetch_top_symbols_by_volume()` returns normalized symbols for strategy engine use.

## 3) Runtime Wiring

- [x] Replace hardcoded `BinanceConnector()` construction with factory usage in:
- [x] `main.py`
- [x] `scripts/run_shadow.py`
- [x] `scripts/start_ingestion.py`
- [x] `scripts/fetch_snapshot.py`
- [x] Replace direct `connector.exchange.fetch_ticker(...)` calls with connector wrapper methods.
- [x] Remove hardcoded `USDT` fallback symbols from runtime flow.

Acceptance criteria:
- [x] Same commands still run with Binance defaults.
- [x] Hyperliquid mode can run in paper/shadow with `EXCHANGE_ID=hyperliquid`.

## 4) Config and Safety

- [x] Add exchange-aware defaults in `Config`:
- [x] `EXCHANGE_MARKET_TYPE`
- [x] `QUOTE_CURRENCY`
- [x] `SYMBOL` default aligned with quote currency.
- [x] Keep old env vars working.
- [x] Document env examples for both Binance and Hyperliquid.

Acceptance criteria:
- [x] No breaking changes for existing `.env`.

## 5) Validation and Regression Checks

- [x] Run `python -m pytest`.
- [x] Run `python scripts/startup_checks.py`.
- [x] Run `python main.py --once --skip-checks` for smoke verification.
- [x] Confirm no import/runtime regressions from connector changes.

Acceptance criteria:
- [x] Tests and startup checks pass.
- [x] Smoke run completes without connector errors.

## 6) Next Phase (Not in this patch)

- [x] Native Hyperliquid private trading client (nonces/signing/API wallet separation).
- [x] Exchange endpoint order placement/cancel/modify via signed actions.
- [x] Safe smoke tool for private connectivity/signed-action validation (`scripts/hyperliquid_private_smoke.py`).
- [x] Wire signed order lifecycle into the main strategy loop (entry + exit sync with exchange state).
- [x] WebSocket user stream with watchdog/reconnect policy (`src/exchange/hyperliquid_stream.py`) and main-loop consumption.
- [x] Rate-limit budgeter/cooldown guard for exchange polling (`src/exchange/ccxt_connector.py`).
- [x] Full idempotent order-state reconciliation using websocket events as source of truth.
- [x] Testnet shadow then constrained live rollout playbook (`docs/hyperliquid_rollout_playbook.md`).

## 7) Phase 4 Start (Stability)

- [x] Isolate portfolio state per venue/quote/mode to avoid loading Binance positions on Hyperliquid.
- [x] Preserve legacy default path compatibility for Binance/USDT paper mode.
- [x] Keep strategy universe logic unchanged: dynamic top-volume scan remains primary selection flow.
- [x] Reduce ticker request pressure by using batch ticker refresh + cache lookups in main loop.
- [x] Add websocket-driven user updates (fills/orders) with reconnect watchdog.
- [x] Add strict rate-limit budgeter for Hyperliquid `info` calls under degraded network/API periods.
- [x] Extend websocket handling to drive full local order/position state without periodic REST sync.
