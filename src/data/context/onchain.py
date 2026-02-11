
import logging
import os
from datetime import datetime, UTC
from typing import List, Dict

import pandas as pd

from src.config import Config

logger = logging.getLogger(__name__)

class WhaleIngestor:
    """
    Phase 1 Retrofit: On-Chain Whale Alerting (Mock).
    """
    def fetch_large_transactions(self, threshold_usd: float = 1000000) -> List[Dict]:
        # Placeholder for real API (e.g., Whale Alert)
        return []

    def run_cycle(self, threshold_usd: float = 1_000_000) -> List[Dict]:
        txs = self.fetch_large_transactions(threshold_usd=threshold_usd)
        path = os.path.join(Config.DATA_PATH, "context")
        os.makedirs(path, exist_ok=True)
        outfile = os.path.join(path, "whale.csv")
        now_ms = int(datetime.now(UTC).timestamp() * 1000)

        rows = txs or [{"timestamp": now_ms, "amount_usd": 0.0, "asset": "N/A", "direction": "NONE"}]
        normalized = []
        for tx in rows:
            normalized.append(
                {
                    "timestamp": int(tx.get("timestamp", now_ms)),
                    "amount_usd": float(tx.get("amount_usd", 0.0)),
                    "asset": tx.get("asset", "N/A"),
                    "direction": tx.get("direction", "UNKNOWN"),
                }
            )

        exists = os.path.exists(outfile)
        pd.DataFrame(normalized).to_csv(outfile, mode="a", index=False, header=not exists)
        return txs
