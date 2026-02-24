import argparse
import logging
import os
import sys

sys.path.append(os.getcwd())

from src.config import Config
from src.data.ingestor import DataIngestor
from src.exchange import create_exchange_connector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SnapshotFetcher")


def main():
    parser = argparse.ArgumentParser(description="Fetch one market-data snapshot cycle")
    parser.add_argument("--symbol", default=Config.SYMBOL, help="Trading pair, e.g. BTC/USDT or BTC/USDC")
    parser.add_argument("--timeframe", default="1m", help="OHLCV timeframe")
    parser.add_argument("--ohlcv-limit", type=int, default=300, help="OHLCV rows")
    parser.add_argument("--trade-limit", type=int, default=300, help="Trade rows")
    args = parser.parse_args()

    symbol = args.symbol
    print(f"Fetching immediate snapshot for {symbol} on {Config.EXCHANGE_ID}...")

    connector = create_exchange_connector()
    ingestor = DataIngestor(connector)

    ticker = connector.fetch_ticker_snapshot(symbol)
    current_price = ticker.get("last", "Unknown")
    print(f"Connected. Current Price: {current_price}")

    ingestor.run_cycle(
        symbols=[symbol],
        timeframe=args.timeframe,
        ohlcv_limit=args.ohlcv_limit,
        trade_limit=args.trade_limit,
    )

    symbol_key = symbol.replace("/", "_").replace(":", "_")
    base_path = os.path.join("data", "raw", symbol_key)
    print("\nChecking files:")
    for dtype in ["ohlcv", "trades", "orderbook", "open_interest"]:
        path = os.path.join(base_path, dtype)
        has_files = os.path.exists(path) and len(os.listdir(path)) > 0
        status = "[OK]" if has_files else "[FAIL]"
        print(f"  {status} {dtype}")


if __name__ == "__main__":
    main()
