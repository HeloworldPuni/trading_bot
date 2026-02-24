# Hyperliquid Rollout Playbook

This playbook defines the final deployment path from testnet/shadow to constrained live.
Use it exactly in order; do not skip gates.

## 1. Preconditions

- Branch is clean enough to run without unknown local edits.
- `python -m pytest` passes.
- `python scripts/startup_checks.py` passes.
- Hyperliquid credentials are loaded in `.env`:
  - `HYPERLIQUID_API_WALLET`
  - `HYPERLIQUID_PRIVATE_KEY`
  - `HYPERLIQUID_ACCOUNT_ADDRESS` (recommended)
- Keep private orders disabled until Stage 3:
  - `HYPERLIQUID_ENABLE_PRIVATE_ORDERS=false`

## 2. Stage 1 - Hyperliquid Paper/Shadow (No Signed Orders)

Goal: prove market-data + strategy loop stability on Hyperliquid symbols.

Recommended `.env` profile:

```env
EXCHANGE_ID=hyperliquid
EXCHANGE_MARKET_TYPE=swap
QUOTE_CURRENCY=USDC
TRADING_MODE=paper
HYPERLIQUID_TESTNET=true
HYPERLIQUID_ENABLE_PRIVATE_ORDERS=false
HYPERLIQUID_USER_WS_ENABLED=true
TOP_COINS_COUNT=10
```

Run:

```powershell
.venv\Scripts\python.exe scripts/startup_checks.py
.venv\Scripts\python.exe main.py --once --skip-checks
```

Gate to pass:

- No connector symbol-format errors.
- No crash in the main scan cycle.
- Top-volume universe resolves to tradable Hyperliquid symbols.

## 3. Stage 2 - Private API Connectivity Smoke (Testnet)

Goal: verify wallet/auth/signing path before enabling automated entries.

Keep:

- `TRADING_MODE=live`
- `HYPERLIQUID_TESTNET=true`
- `HYPERLIQUID_ENABLE_PRIVATE_ORDERS=true`

Run connectivity-only smoke:

```powershell
.venv\Scripts\python.exe scripts/hyperliquid_private_smoke.py --testnet
```

Optional signed action smoke (only if safe and intentional):

```powershell
.venv\Scripts\python.exe scripts/hyperliquid_private_smoke.py --testnet --place-order --symbol BTC/USDC --side BUY --size 0.001 --confirm-live
```

Gate to pass:

- `connectivity_snapshot` returns `"ok": true`.
- No nonce/signing errors.
- If signed smoke is used: order acknowledgement is received and cancel/close path works.

## 4. Stage 3 - Testnet Constrained Live (Automated Signed Orders)

Goal: run full loop with real signed actions in a tightly constrained risk box.

Recommended risk profile:

```env
TRADING_MODE=live
HYPERLIQUID_TESTNET=true
HYPERLIQUID_ENABLE_PRIVATE_ORDERS=true
BASE_LEVERAGE=1
MAX_LEVERAGE=2
MAX_POSITION_PCT=0.01
MAX_CONCURRENT_POSITIONS=1
MAX_POSITIONS_PER_SYMBOL=1
TOP_COINS_COUNT=5
HYPERLIQUID_ORDER_SYNC_GRACE_SEC=90
```

Run:

```powershell
.venv\Scripts\python.exe scripts/startup_checks.py
.venv\Scripts\python.exe main.py --skip-checks
```

Minimum soak window before promotion: **48 hours**.

Gate to pass:

- No unresolved local/exchange position divergence.
- Websocket reconciliation remains healthy (no repeated stale/looping reconnect behavior).
- No repeated order rejections caused by local state mismatches.
- No critical runtime exceptions.

## 5. Stage 4 - Mainnet Constrained Live (Capital Protection First)

Goal: small-capital production rollout with strict risk limits.

Change only these from Stage 3:

```env
HYPERLIQUID_TESTNET=false
```

Keep the same constrained risk caps for at least the first 7 days.

Gate to pass before scaling:

- 7-day stability with no critical incidents.
- Drawdown within policy.
- Exchange/local reconciliation stable during fills, exits, and reconnects.

## 6. Escalation Policy (Scale Up Slowly)

Scale one dimension at a time, max once every 7 days:

1. Increase `TOP_COINS_COUNT` (coverage).
2. Increase `MAX_CONCURRENT_POSITIONS` (parallelism).
3. Increase `MAX_POSITION_PCT` (size).
4. Increase leverage caps last.

Never scale if the previous 7-day window has:

- unresolved reconciliation incidents,
- emergency manual intervention,
- or abnormal rejection/reconnect spikes.

## 7. Rollback Procedure

If any critical issue appears:

1. Stop process immediately.
2. Set:
   - `HYPERLIQUID_ENABLE_PRIVATE_ORDERS=false`
   - `TRADING_MODE=paper`
3. Restart in paper mode and collect logs.
4. Run:
   - `python scripts/startup_checks.py`
   - `python -m pytest`
5. Re-enable live only after root cause + fix + clean soak.

## 8. Runtime Checks Per Session

Before each live session:

- `startup_checks.py` returns all green.
- Reconciliation bootstrap succeeds.
- Account address, vault, and environment (testnet/mainnet) are correct.
- Risk caps are explicitly reviewed in `.env`.

