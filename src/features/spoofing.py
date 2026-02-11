import logging
from typing import Dict, List, Tuple, Any

import pandas as pd

logger = logging.getLogger(__name__)


class SpoofingDetector:
    """
    Heuristic spoofing detector:
    flags if a large visible level disappears/reduces sharply between snapshots.
    """

    @staticmethod
    def _extract_side_levels(snapshot: Any, side: str, max_depth: int = 20) -> Dict[float, float]:
        levels: Dict[float, float] = {}
        if snapshot is None:
            return levels

        if isinstance(snapshot, dict) and side in snapshot and isinstance(snapshot[side], list):
            for row in snapshot[side][:max_depth]:
                if len(row) >= 2:
                    try:
                        levels[float(row[0])] = float(row[1])
                    except Exception:
                        continue
            return levels

        if isinstance(snapshot, pd.Series):
            row = snapshot
        elif isinstance(snapshot, pd.DataFrame) and not snapshot.empty:
            row = snapshot.iloc[-1]
        else:
            return levels

        prefix = "bid" if side == "bids" else "ask"
        for i in range(1, max_depth + 1):
            p = row.get(f"{prefix}{i}_p")
            q = row.get(f"{prefix}{i}_v")
            if p is None or q is None:
                continue
            try:
                levels[float(p)] = float(q)
            except Exception:
                continue
        return levels

    @staticmethod
    def detect_large_cancellations(t0_book, t1_book, threshold_size: float = 10.0) -> bool:
        """
        Returns True if a large level vanishes/reduces by threshold_size or more.
        """
        threshold = abs(float(threshold_size))
        events = SpoofingDetector.detect_events(t0_book, t1_book, threshold_size=threshold)
        return len(events) > 0

    @staticmethod
    def detect_events(t0_book, t1_book, threshold_size: float = 10.0) -> List[Tuple[str, float, float]]:
        threshold = abs(float(threshold_size))
        events: List[Tuple[str, float, float]] = []

        for side in ("bids", "asks"):
            before = SpoofingDetector._extract_side_levels(t0_book, side)
            after = SpoofingDetector._extract_side_levels(t1_book, side)
            for price, qty_before in before.items():
                qty_after = after.get(price, 0.0)
                canceled = qty_before - qty_after
                if canceled >= threshold:
                    events.append((side, price, canceled))

        if events:
            logger.debug("Potential spoofing events: %s", events[:3])
        return events
