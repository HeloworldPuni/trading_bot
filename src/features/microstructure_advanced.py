from typing import Any, List

import pandas as pd

from src.features.microstructure import MicrostructureFeatures


class LiquidityAnalyzer:
    @staticmethod
    def _to_level_frames(orderbook_snapshot: Any):
        if isinstance(orderbook_snapshot, pd.DataFrame):
            if not orderbook_snapshot.empty and {"price", "quantity"}.issubset(orderbook_snapshot.columns):
                # If a single side DataFrame is passed, caller should use MicrostructureFeatures directly.
                return orderbook_snapshot, pd.DataFrame(columns=["price", "quantity"])

            row = orderbook_snapshot.iloc[-1] if not orderbook_snapshot.empty else pd.Series(dtype=float)
        elif isinstance(orderbook_snapshot, dict):
            row = pd.Series(orderbook_snapshot)
        else:
            row = pd.Series(dtype=float)

        bids = []
        asks = []
        for i in range(1, 21):
            bp = row.get(f"bid{i}_p")
            bv = row.get(f"bid{i}_v")
            ap = row.get(f"ask{i}_p")
            av = row.get(f"ask{i}_v")
            if bp is not None and bv is not None:
                bids.append({"price": bp, "quantity": bv})
            if ap is not None and av is not None:
                asks.append({"price": ap, "quantity": av})

        return pd.DataFrame(bids), pd.DataFrame(asks)

    @staticmethod
    def detect_liquidity_gaps(orderbook_snapshot: Any, threshold_pct: float = 0.5) -> List[dict]:
        bids, asks = LiquidityAnalyzer._to_level_frames(orderbook_snapshot)
        return MicrostructureFeatures.detect_liquidity_gaps(bids, asks, threshold_pct=threshold_pct)
