import glob
import os
from typing import Optional

import pandas as pd

from src.config import Config


class FeatureStore:
    """
    Lightweight file-backed feature store used by research scripts.
    """

    def __init__(self, symbol: str, data_path: Optional[str] = None):
        self.symbol = symbol
        self.data_path = data_path or Config.DATA_PATH
        self.symbol_key = symbol.replace("/", "_").replace(":", "_")
        self.base = os.path.join(self.data_path, "raw", self.symbol_key)

    def _latest_csv(self, category: str) -> Optional[str]:
        pattern = os.path.join(self.base, category, "*.csv")
        files = glob.glob(pattern)
        if not files:
            return None
        return max(files, key=os.path.getctime)

    def load_trades(self) -> pd.DataFrame:
        path = self._latest_csv("trades")
        if not path:
            return pd.DataFrame()
        df = pd.read_csv(path)
        if df.empty:
            return df

        # Support both [trade_id, timestamp, ...] and [timestamp, ...] layouts.
        ts_col = "timestamp"
        if ts_col not in df.columns:
            if len(df.columns) >= 2:
                ts_col = df.columns[1]
            else:
                return pd.DataFrame()

        df["timestamp"] = pd.to_numeric(df[ts_col], errors="coerce")
        df = df.dropna(subset=["timestamp"])
        df["timestamp"] = df["timestamp"].astype("int64")

        if "price" not in df.columns and len(df.columns) >= 3:
            df["price"] = pd.to_numeric(df.iloc[:, 2], errors="coerce")
        if "amount" not in df.columns and len(df.columns) >= 4:
            df["amount"] = pd.to_numeric(df.iloc[:, 3], errors="coerce")
        if "side" not in df.columns and len(df.columns) >= 5:
            df["side"] = df.iloc[:, 4]

        df["price"] = pd.to_numeric(df.get("price"), errors="coerce").fillna(0.0)
        df["amount"] = pd.to_numeric(df.get("amount"), errors="coerce").fillna(0.0)
        df["side"] = df.get("side", "").fillna("").astype(str)
        return df.sort_values("timestamp").reset_index(drop=True)

    def load_orderbook(self) -> pd.DataFrame:
        path = self._latest_csv("orderbook")
        if not path:
            return pd.DataFrame()
        df = pd.read_csv(path)
        if "timestamp" in df.columns:
            df["timestamp"] = pd.to_numeric(df["timestamp"], errors="coerce")
            df = df.dropna(subset=["timestamp"])
            df["timestamp"] = df["timestamp"].astype("int64")
        return df

    def resample_trades(self, trades_df: pd.DataFrame, rule: str = "1min") -> pd.DataFrame:
        if trades_df is None or trades_df.empty:
            return pd.DataFrame()

        df = trades_df.copy()
        if "timestamp" not in df.columns:
            return pd.DataFrame()
        df["ts"] = pd.to_datetime(df["timestamp"], unit="ms", errors="coerce")
        df = df.dropna(subset=["ts"]).set_index("ts").sort_index()
        if df.empty:
            return pd.DataFrame()

        price = pd.to_numeric(df["price"], errors="coerce").fillna(method="ffill")
        vol = pd.to_numeric(df["amount"], errors="coerce").fillna(0.0)

        bars = pd.DataFrame(index=price.resample(rule).last().dropna().index)
        bars["open"] = price.resample(rule).first()
        bars["high"] = price.resample(rule).max()
        bars["low"] = price.resample(rule).min()
        bars["close"] = price.resample(rule).last()
        bars["volume"] = vol.resample(rule).sum()
        bars = bars.dropna(subset=["open", "high", "low", "close"])
        return bars
