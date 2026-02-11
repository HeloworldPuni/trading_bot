import os
import sys
import logging

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.backtest.engine import BacktestConfig, BacktestEngine, FastBacktestEngine

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("Backtest")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Backtest engine (realistic execution hooks)")
    parser.add_argument("--csv", required=True, help="Path to OHLCV CSV (timestamp, open, high, low, close, volume)")
    parser.add_argument("--symbol", default="BTC/USDT", help="Symbol name for logging")
    parser.add_argument("--slippage-bps", type=float, default=5.0, help="Slippage in basis points per trade")
    parser.add_argument("--latency", type=int, default=1, help="Latency in candles before execution")
    parser.add_argument("--funding-rate", type=float, default=0.0, help="Funding rate per interval (percent)")
    parser.add_argument("--funding-interval", type=int, default=32, help="Funding interval in candles")
    parser.add_argument("--leverage", type=int, default=1, help="Leverage for sizing")
    parser.add_argument("--max-position-pct", type=float, default=None, help="Position size as percent of balance")
    parser.add_argument("--initial-capital", type=float, default=None, help="Initial capital")
    parser.add_argument("--data-path", type=str, default="data", help="Data path for backtest logs")
    parser.add_argument("--fast", action="store_true", help="Disable DB logging for speed")
    parser.add_argument("--report", type=str, default=None, help="Optional JSON report output path")
    parser.add_argument("--log-suffix", type=str, default="backtest", help="Suffix for experience log file")

    args = parser.parse_args()

    config = BacktestConfig(
        initial_capital=args.initial_capital if args.initial_capital is not None else BacktestConfig.initial_capital,
        slippage_bps=args.slippage_bps,
        latency_candles=args.latency,
        funding_rate_per_interval=args.funding_rate,
        funding_interval_candles=args.funding_interval,
        leverage=args.leverage,
        max_position_pct=args.max_position_pct if args.max_position_pct is not None else BacktestConfig.max_position_pct
    )

    engine_cls = FastBacktestEngine if args.fast else BacktestEngine
    engine = engine_cls(args.csv, symbol=args.symbol, config=config, data_path=args.data_path, log_suffix=args.log_suffix)
    result = engine.run()
    trades = result.get("trades", [])

    # Compute basic metrics
    wins = sum(1 for t in trades if t.get("realized_pnl_usd", 0) > 0)
    total = len(trades)
    win_rate = wins / total if total else 0.0
    avg_pnl = sum(t.get("realized_pnl_pct", 0.0) for t in trades) / total if total else 0.0
    total_pnl = sum(t.get("realized_pnl_usd", 0.0) for t in trades)

    print("\n" + "=" * 40)
    print("BACKTEST SUMMARY")
    print("=" * 40)
    print(f"Final Balance: ${result['final_balance']:.2f}")
    print(f"Final Equity:  ${result['final_equity']:.2f}")
    print(f"Trades:        {result['trade_count']}")
    print(f"Win Rate:      {win_rate:.2%}")
    print(f"Avg PnL %:     {avg_pnl:.4f}")
    print(f"Total PnL:     ${total_pnl:.2f}")
    print("=" * 40)

    if args.report:
        report = {
            "final_balance": result["final_balance"],
            "final_equity": result["final_equity"],
            "trade_count": result["trade_count"],
            "win_rate": win_rate,
            "avg_pnl": avg_pnl,
            "total_pnl": total_pnl,
        }
        os.makedirs(os.path.dirname(args.report), exist_ok=True)
        import json
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"Report saved to {args.report}")


if __name__ == "__main__":
    main()
