import json

with open("data/portfolio_state.json", "r") as f:
    data = json.load(f)

wins = [t for t in data["trade_history"] if t.get("realized_pnl_usd", 0) > 0]

print(f"{'#':<3} {'Symbol':<18} {'Dir':<6} {'Strategy':<16} {'Entry':>10} {'Exit':>10} {'PnL $':>10} {'PnL %':>8} {'Reason':<6}")
print("-" * 100)

total_profit = 0
for i, w in enumerate(wins, 1):
    sym = w.get("symbol", "?")
    d = w.get("direction", "?")
    strat = w.get("strategy") or "N/A"
    entry = w.get("entry_price", 0)
    exit_p = w.get("exit_price", 0)
    pnl = w.get("realized_pnl_usd", 0)
    pnl_pct = w.get("realized_pnl_pct", 0)
    reason = w.get("exit_reason", "?")
    total_profit += pnl
    print(f"{i:<3} {sym:<18} {d:<6} {strat:<16} {entry:>10} {exit_p:>10.4f} {pnl:>+10.2f} {pnl_pct:>+7.2f}% {reason:<6}")

print("-" * 100)
print(f"TOTAL WINS: {len(wins)}  |  TOTAL PROFIT: ${total_profit:,.2f}")
