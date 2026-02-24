from __future__ import annotations

import threading
import time
from collections import deque
from typing import Any, Deque, Dict, List, Optional


def _tf_to_minutes(tf: str) -> int:
    if not tf:
        return 0
    s = str(tf).strip().lower()
    if s.endswith("m"):
        try:
            return int(s[:-1])
        except ValueError:
            return 0
    if s.endswith("h"):
        try:
            return int(s[:-1]) * 60
        except ValueError:
            return 0
    if s.endswith("d"):
        try:
            return int(s[:-1]) * 60 * 24
        except ValueError:
            return 0
    return 0


class CandleStore:
    """
    Build and maintain rolling 1m OHLCV candles from price ticks, with on-demand
    aggregation to higher timeframes.
    """

    def __init__(self, max_1m_bars: int = 4000):
        self.max_1m_bars = max(200, int(max_1m_bars))
        self._lock = threading.Lock()
        self._bars_1m: Dict[str, Deque[List[float]]] = {}
        self._open_1m: Dict[str, Dict[str, float]] = {}

    @staticmethod
    def _bucket_sec(ts: float, bucket_minutes: int = 1) -> int:
        sec = int(ts)
        step = max(1, int(bucket_minutes)) * 60
        return (sec // step) * step

    def ingest_tick(self, symbol: str, price: float, ts: Optional[float] = None):
        if not symbol:
            return
        try:
            px = float(price)
        except (TypeError, ValueError):
            return
        if px <= 0:
            return

        now_ts = float(ts) if ts is not None else time.time()
        bucket = self._bucket_sec(now_ts, 1)

        with self._lock:
            bars = self._bars_1m.setdefault(symbol, deque(maxlen=self.max_1m_bars))
            current = self._open_1m.get(symbol)

            if current is None:
                self._open_1m[symbol] = {
                    "bucket": float(bucket),
                    "open": px,
                    "high": px,
                    "low": px,
                    "close": px,
                    "volume": 1.0,
                }
                return

            curr_bucket = int(current["bucket"])
            if bucket == curr_bucket:
                current["high"] = max(current["high"], px)
                current["low"] = min(current["low"], px)
                current["close"] = px
                current["volume"] += 1.0
                return

            # Flush completed bucket and start a new one.
            bars.append(
                [
                    float(curr_bucket * 1000),
                    float(current["open"]),
                    float(current["high"]),
                    float(current["low"]),
                    float(current["close"]),
                    float(current["volume"]),
                ]
            )
            self._open_1m[symbol] = {
                "bucket": float(bucket),
                "open": px,
                "high": px,
                "low": px,
                "close": px,
                "volume": 1.0,
            }

    def _snapshot_1m(self, symbol: str) -> List[List[float]]:
        with self._lock:
            bars = list(self._bars_1m.get(symbol, []))
            open_bar = self._open_1m.get(symbol)
            if open_bar is not None:
                bars.append(
                    [
                        float(int(open_bar["bucket"]) * 1000),
                        float(open_bar["open"]),
                        float(open_bar["high"]),
                        float(open_bar["low"]),
                        float(open_bar["close"]),
                        float(open_bar["volume"]),
                    ]
                )
            return bars

    @staticmethod
    def _aggregate_rows(rows: List[List[float]]) -> List[float]:
        return [
            float(rows[0][0]),
            float(rows[0][1]),
            float(max(r[2] for r in rows)),
            float(min(r[3] for r in rows)),
            float(rows[-1][4]),
            float(sum(r[5] for r in rows)),
        ]

    def get_recent_ohlcv(self, symbol: str, timeframe: str, limit: int) -> List[List[float]]:
        rows_1m = self._snapshot_1m(symbol)
        if not rows_1m:
            return []

        tf_min = _tf_to_minutes(timeframe)
        if tf_min <= 1:
            return rows_1m[-max(1, int(limit)) :]

        bucket_ms = tf_min * 60 * 1000
        grouped: Dict[int, List[List[float]]] = {}
        for row in rows_1m:
            ts = int(row[0])
            bucket = (ts // bucket_ms) * bucket_ms
            grouped.setdefault(bucket, []).append(row)

        aggregated: List[List[float]] = []
        for bucket in sorted(grouped.keys()):
            rows = grouped[bucket]
            if not rows:
                continue
            agg = self._aggregate_rows(rows)
            agg[0] = float(bucket)
            aggregated.append(agg)
        return aggregated[-max(1, int(limit)) :]

    def symbols_with_min_bars(self, symbols: List[str], timeframe: str, min_bars: int) -> int:
        target = max(1, int(min_bars))
        count = 0
        for sym in symbols:
            if len(self.get_recent_ohlcv(sym, timeframe, target)) >= target:
                count += 1
        return count

