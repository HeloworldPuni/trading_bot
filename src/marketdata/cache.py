from __future__ import annotations

import threading
import time
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from src.core.definitions import MarketState


@dataclass
class SymbolSnapshot:
    symbol: str
    state: Optional[MarketState] = None
    ticker: Dict[str, Any] = field(default_factory=dict)
    orderbook: Dict[str, Any] = field(default_factory=dict)
    state_updated_at: float = 0.0
    ticker_updated_at: float = 0.0
    orderbook_updated_at: float = 0.0
    source: str = "unknown"


class MarketDataCache:
    """
    In-memory symbol snapshot cache.
    Used to decouple decision loop from transient API failures.
    """

    def __init__(self):
        self._lock = threading.Lock()
        self._snapshots: Dict[str, SymbolSnapshot] = {}

    def upsert(
        self,
        symbol: str,
        *,
        state: Optional[MarketState] = None,
        ticker: Optional[Dict[str, Any]] = None,
        orderbook: Optional[Dict[str, Any]] = None,
        source: str = "runtime",
    ) -> SymbolSnapshot:
        now_ts = time.time()
        with self._lock:
            snap = self._snapshots.get(symbol)
            if snap is None:
                snap = SymbolSnapshot(symbol=symbol)
                self._snapshots[symbol] = snap

            if state is not None:
                snap.state = state
                snap.state_updated_at = now_ts
            if ticker is not None:
                snap.ticker = dict(ticker)
                snap.ticker_updated_at = now_ts
            if orderbook is not None:
                snap.orderbook = dict(orderbook)
                snap.orderbook_updated_at = now_ts
            snap.source = source
            return snap

    def get_snapshot(self, symbol: str) -> Optional[SymbolSnapshot]:
        with self._lock:
            return self._snapshots.get(symbol)

    def get_state(self, symbol: str, max_age_sec: float) -> Optional[MarketState]:
        with self._lock:
            snap = self._snapshots.get(symbol)
            if snap is None or snap.state is None:
                return None
            age = time.time() - snap.state_updated_at
            if age > max(0.0, float(max_age_sec)):
                return None
            return snap.state

    def get_ticker(self, symbol: str, max_age_sec: float) -> Optional[Dict[str, Any]]:
        with self._lock:
            snap = self._snapshots.get(symbol)
            if snap is None or not snap.ticker:
                return None
            age = time.time() - snap.ticker_updated_at
            if age > max(0.0, float(max_age_sec)):
                return None
            return dict(snap.ticker)

    def get_orderbook(self, symbol: str, max_age_sec: float) -> Optional[Dict[str, Any]]:
        with self._lock:
            snap = self._snapshots.get(symbol)
            if snap is None or not snap.orderbook:
                return None
            age = time.time() - snap.orderbook_updated_at
            if age > max(0.0, float(max_age_sec)):
                return None
            return dict(snap.orderbook)

    def snapshot_health(self, now_ts: Optional[float] = None) -> Dict[str, Any]:
        now_ts = now_ts or time.time()
        with self._lock:
            total = len(self._snapshots)
            with_state = sum(1 for s in self._snapshots.values() if s.state is not None)
            with_ticker = sum(1 for s in self._snapshots.values() if bool(s.ticker))
            state_ages = [
                max(0.0, now_ts - s.state_updated_at)
                for s in self._snapshots.values()
                if s.state_updated_at > 0
            ]
            ticker_ages = [
                max(0.0, now_ts - s.ticker_updated_at)
                for s in self._snapshots.values()
                if s.ticker_updated_at > 0
            ]
        return {
            "symbols": total,
            "with_state": with_state,
            "with_ticker": with_ticker,
            "max_state_age_sec": max(state_ages) if state_ages else None,
            "max_ticker_age_sec": max(ticker_ages) if ticker_ages else None,
        }

