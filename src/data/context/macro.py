import os
from datetime import datetime, UTC

import pandas as pd

from src.config import Config
from src.data.macro import MacroProvider


class MacroIngestor:
    """
    Compatibility wrapper for periodic macro snapshot persistence.
    """

    def __init__(self, fred_api_key: str | None = None):
        self.provider = MacroProvider(fred_api_key=fred_api_key)

    def save_snapshot(self):
        metrics = self.provider.fetch_latest()
        path = os.path.join(Config.DATA_PATH, "context")
        os.makedirs(path, exist_ok=True)
        outfile = os.path.join(path, "macro.csv")
        row = {
            "timestamp": int(datetime.now(UTC).timestamp() * 1000),
            "interest_rate": float(metrics.interest_rate),
            "cpi_yoy": float(metrics.cpi_yoy),
            "dxy_index": float(metrics.dxy_index),
            "spx_corr": float(metrics.spx_corr),
            "risk_environment": metrics.risk_environment,
        }
        exists = os.path.exists(outfile)
        pd.DataFrame([row]).to_csv(outfile, mode="a", index=False, header=not exists)
        return row

    def run_cycle(self):
        return self.save_snapshot()
