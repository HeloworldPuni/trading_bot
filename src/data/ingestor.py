import logging
import os
from datetime import datetime, UTC
from typing import Iterable, Optional

import pandas as pd

from src.config import Config

logger = logging.getLogger(__name__)


class DataIngestor:
    """
    Unified market-data ingestor.
    Supports OHLCV, trades, orderbook snapshots and open interest snapshots.
    """

    def __init__(self, exchange_connector, data_path: Optional[str] = None, orderbook_depth: int = 5):
        self.exchange = exchange_connector
        self.data_path = data_path or Config.DATA_PATH
        self.orderbook_depth = max(1, int(orderbook_depth))

    def _ccxt(self):
        if self.exchange is None:
            return None
        if hasattr(self.exchange, "exchange"):
            return self.exchange.exchange
        return self.exchange

    def fetch_ohlcv(self, symbol: str, timeframe: str = "1m", limit: int = 1000) -> pd.DataFrame:
        """
        Returns DataFrame:
        timestamp, open, high, low, close, volume
        """
        try:
            raw = None
            if hasattr(self.exchange, "fetch_ohlcv"):
                raw = self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
            else:
                ccxt_ex = self._ccxt()
                raw = ccxt_ex.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit) if ccxt_ex else []

            if isinstance(raw, pd.DataFrame):
                return raw
            if not raw:
                return pd.DataFrame(columns=["timestamp", "open", "high", "low", "close", "volume"])

            df = pd.DataFrame(raw, columns=["timestamp", "open", "high", "low", "close", "volume"])
            return df
        except Exception as e:
            logger.error("OHLCV ingestion failed for %s: %s", symbol, e)
            return pd.DataFrame(columns=["timestamp", "open", "high", "low", "close", "volume"])

    def fetch_trades(self, symbol: str, limit: int = 1000) -> pd.DataFrame:
        """
        Returns DataFrame:
        trade_id, timestamp, price, amount, side
        """
        try:
            ccxt_ex = self._ccxt()
            raw = ccxt_ex.fetch_trades(symbol, limit=limit) if ccxt_ex else []
            if not raw:
                return pd.DataFrame(columns=["trade_id", "timestamp", "price", "amount", "side"])

            rows = []
            for t in raw:
                rows.append(
                    {
                        "trade_id": t.get("id") or "",
                        "timestamp": int(t.get("timestamp") or 0),
                        "price": float(t.get("price") or 0.0),
                        "amount": float(t.get("amount") or 0.0),
                        "side": t.get("side") or "",
                    }
                )
            return pd.DataFrame(rows)
        except Exception as e:
            logger.error("Trade ingestion failed for %s: %s", symbol, e)
            return pd.DataFrame(columns=["trade_id", "timestamp", "price", "amount", "side"])

    def fetch_orderbook(self, symbol: str, depth: Optional[int] = None) -> pd.DataFrame:
        """
        Returns one-row orderbook snapshot with columns:
        timestamp, bid1_p, bid1_v, ask1_p, ask1_v, ...
        """
        try:
            ccxt_ex = self._ccxt()
            depth = int(depth or self.orderbook_depth)
            ob = ccxt_ex.fetch_order_book(symbol, limit=depth) if ccxt_ex else {}
            ts = int(ob.get("timestamp") or datetime.now(UTC).timestamp() * 1000)
            bids = ob.get("bids") or []
            asks = ob.get("asks") or []

            row = {"timestamp": ts}
            for i in range(depth):
                b = bids[i] if i < len(bids) else [None, None]
                a = asks[i] if i < len(asks) else [None, None]
                row[f"bid{i+1}_p"] = b[0]
                row[f"bid{i+1}_v"] = b[1]
                row[f"ask{i+1}_p"] = a[0]
                row[f"ask{i+1}_v"] = a[1]
            return pd.DataFrame([row])
        except Exception as e:
            logger.error("Orderbook ingestion failed for %s: %s", symbol, e)
            return pd.DataFrame()

    def fetch_open_interest(self, symbol: str) -> pd.DataFrame:
        """
        Returns one-row open interest snapshot if exchange supports it.
        """
        try:
            ccxt_ex = self._ccxt()
            if not ccxt_ex or not hasattr(ccxt_ex, "fetch_open_interest"):
                return pd.DataFrame()

            oi = ccxt_ex.fetch_open_interest(symbol)
            if not oi:
                return pd.DataFrame()

            ts = int(oi.get("timestamp") or datetime.now(UTC).timestamp() * 1000)
            value = float(oi.get("openInterestAmount") or oi.get("openInterestValue") or oi.get("openInterest") or 0.0)
            return pd.DataFrame([{"timestamp": ts, "open_interest": value}])
        except Exception:
            return pd.DataFrame()

    def _symbol_path(self, symbol: str, category: str) -> str:
        symbol_dir = symbol.replace("/", "_").replace(":", "_")
        path = os.path.join(self.data_path, "raw", symbol_dir, category)
        os.makedirs(path, exist_ok=True)
        return path

    @staticmethod
    def _append_dataframe(path: str, df: pd.DataFrame):
        if df is None or df.empty:
            return
        exists = os.path.exists(path)
        df.to_csv(path, mode="a", index=False, header=not exists)

    @staticmethod
    def _today_filename() -> str:
        return datetime.now(UTC).strftime("%Y-%m-%d") + ".csv"

    def run_cycle(self, symbols: Iterable[str], timeframe: str = "1m", ohlcv_limit: int = 300, trade_limit: int = 500):
        """
        Pull one ingestion cycle for all symbols and persist under data/raw.
        """
        for symbol in symbols:
            try:
                date_file = self._today_filename()

                ohlcv = self.fetch_ohlcv(symbol, timeframe=timeframe, limit=ohlcv_limit)
                self._append_dataframe(
                    os.path.join(self._symbol_path(symbol, "ohlcv"), date_file),
                    ohlcv,
                )

                trades = self.fetch_trades(symbol, limit=trade_limit)
                self._append_dataframe(
                    os.path.join(self._symbol_path(symbol, "trades"), date_file),
                    trades,
                )

                orderbook = self.fetch_orderbook(symbol, depth=self.orderbook_depth)
                self._append_dataframe(
                    os.path.join(self._symbol_path(symbol, "orderbook"), date_file),
                    orderbook,
                )

                oi = self.fetch_open_interest(symbol)
                self._append_dataframe(
                    os.path.join(self._symbol_path(symbol, "open_interest"), date_file),
                    oi,
                )
            except Exception as e:
                logger.error("Ingestion cycle failed for %s: %s", symbol, e)
