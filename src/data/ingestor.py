
import logging
from typing import List, Optional
import pandas as pd
from datetime import datetime

logger = logging.getLogger(__name__)

class DataIngestor:
    """
    Phase 1 Retrofit: Unified Data Ingestor.
    """
    def __init__(self, exchange_connector):
        self.exchange = exchange_connector

    def fetch_ohlcv(self, symbol: str, timeframe: str = '1h', limit: int = 1000) -> pd.DataFrame:
        """Fetch OHLCV Data."""
        try:
            return self.exchange.fetch_ohlcv(symbol, timeframe, limit)
        except Exception as e:
            logger.error(f"Ingestion Failed for {symbol}: {e}")
            return pd.DataFrame()
            
    def fetch_trades(self, symbol: str, limit: int = 1000) -> pd.DataFrame:
        """Fetch Recent Trades."""
        try:
            return self.exchange.fetch_trades(symbol, limit)
        except Exception as e:
            logger.error(f"Trade Ingestion Failed for {symbol}: {e}")
            return pd.DataFrame()
