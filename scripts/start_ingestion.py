import time
import logging
import sys
import os
import argparse

# Ensure project root is in path
sys.path.append(os.getcwd())

from src.config import Config
from src.exchange import create_exchange_connector
from src.data.ingestor import DataIngestor
# Phase 1 Backfill: Contextual Ingestors
from src.data.context.macro import MacroIngestor
from src.data.context.sentiment import SentimentIngestor
from src.data.context.onchain import WhaleIngestor

# Setup Logging for Ingestion
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [INGEST] - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ingestion.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("IngestionRunner")

def main():
    parser = argparse.ArgumentParser(description="Institutional data ingestion runner")
    parser.add_argument("--once", action="store_true", help="Run one ingestion cycle and exit")
    parser.add_argument("--interval-sec", type=float, default=10.0, help="Target cycle interval seconds")
    parser.add_argument("--top-limit", type=int, default=5, help="Top symbols by volume to ingest when ACTIVE_SYMBOLS is empty")
    parser.add_argument(
        "--symbols",
        type=str,
        default="",
        help="Comma-separated symbols override, e.g. BTC/USDC,ETH/USDC",
    )
    args = parser.parse_args()

    logger.info("Starting Institutional Data Ingestion Service...")
    
    # 1. Initialize
    try:
        connector = create_exchange_connector()
        ingestor = DataIngestor(connector)
        
        # Initialize Context Ingestors
        macro_ingestor = MacroIngestor()
        sentiment_ingestor = SentimentIngestor()
        whale_ingestor = WhaleIngestor()
        
        last_macro_run = 0
        last_sentiment_run = 0
        last_whale_run = 0
    except Exception as e:
        logger.critical(f"Failed to initialize connector: {e}")
        return

    # 2. Get Symbols
    # In Phase 33 we added dynamic scanning. Here we can use that or a fixed list.
    # For Phase 1 validation, let's stick to the majors to avoid rate limits.
    symbols_override = [s.strip() for s in args.symbols.split(",") if s.strip()]
    symbols = symbols_override or Config.ACTIVE_SYMBOLS or connector.fetch_top_symbols_by_volume(limit=max(1, int(args.top_limit)))
    if not symbols:
        symbols = connector.fallback_symbols(limit=max(1, int(args.top_limit)))
    logger.info(f"Targeting Symbols: {symbols}")

    # 3. Loop
    try:
        while True:
            start_time = time.time()
            
            logger.info("Starting ingestion cycle...")
            ingestor.run_cycle(symbols)
            
            now = time.time()
            
            # Macro: Run once every 24 hours (86400s)
            if now - last_macro_run > 86400:
                logger.info("Running Macro Ingestion...")
                try:
                    macro_ingestor.save_snapshot()
                    last_macro_run = now
                except Exception as e:
                    logger.error(f"Macro ingestion failed: {e}")

            # Sentiment: Run every 8 hours (28800s) to respect 100 req/mo limit
            if now - last_sentiment_run > 28800:
                logger.info("Running Sentiment Ingestion...")
                try:
                    sentiment_ingestor.run_cycle()
                    last_sentiment_run = now
                except Exception as e:
                    logger.error(f"Sentiment ingestion failed: {e}")

            # Whale: Run every 1 hour (3600s)
            if now - last_whale_run > 3600:
                logger.info("Running Whale Ingestion...")
                try:
                    whale_ingestor.run_cycle()
                    last_whale_run = now
                except Exception as e:
                    logger.error(f"Whale ingestion failed: {e}")

            
            elapsed = time.time() - start_time
            logger.info(f"Cycle complete in {elapsed:.2f}s")

            if args.once:
                logger.info("One-shot mode complete. Exiting.")
                break

            # Rate limit / Interval
            sleep_time = max(0, float(args.interval_sec) - elapsed)
            time.sleep(sleep_time)
            
    except KeyboardInterrupt:
        logger.info("Ingestion stopped by user.")
    except Exception as e:
        logger.critical(f"Ingestion crashed: {e}")

if __name__ == "__main__":
    main()
