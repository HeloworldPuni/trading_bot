import json
import logging
import time
from collections import deque
from threading import Lock
from typing import Any, Deque, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)


class HyperliquidRealtimeState:
    """
    Maintains exchange position/order state from websocket events.

    Position state is seeded once (REST bootstrap), then updated incrementally
    from `user`/`userFills` websocket feeds.
    """

    _ZERO_EPS = 1e-9

    # Order status normalization is intentionally permissive because formats can
    # vary slightly between API versions.
    _PENDING_ORDER_STATUSES = {
        "open",
        "new",
        "received",
        "resting",
        "triggered",
        "queued",
        "partiallyfilled",
        "partially_filled",
    }
    _TERMINAL_ORDER_STATUSES = {
        "filled",
        "canceled",
        "cancelled",
        "rejected",
        "margincanceled",
        "margin_canceled",
        "selftradecanceled",
        "self_trade_canceled",
    }

    def __init__(self, initial_positions: Optional[Dict[str, float]] = None):
        self._lock = Lock()
        self._positions: Dict[str, float] = {}
        self._orders_by_oid: Dict[int, Dict[str, Any]] = {}
        self._position_last_fill_ts: Dict[str, int] = {}
        self._position_state_ready = False

        self._seen_fill_order: Deque[str] = deque(maxlen=20000)
        self._seen_fill_set = set()

        self.last_event_ts = 0.0
        self.last_position_update_ts = 0.0
        self.last_order_update_ts = 0.0

        if initial_positions:
            self.seed_positions(initial_positions)

    @staticmethod
    def _to_float(value: Any, default: float = 0.0) -> float:
        try:
            return float(value)
        except Exception:
            return default

    @staticmethod
    def _normalize_coin(coin: Any) -> str:
        return str(coin or "").strip().upper()

    @staticmethod
    def _normalize_status(status: Any) -> str:
        return str(status or "").strip().lower().replace(" ", "").replace("-", "").replace(".", "")

    @classmethod
    def is_pending_order_status(cls, status: Any) -> bool:
        return cls._normalize_status(status) in cls._PENDING_ORDER_STATUSES

    @classmethod
    def is_terminal_order_status(cls, status: Any) -> bool:
        return cls._normalize_status(status) in cls._TERMINAL_ORDER_STATUSES

    @classmethod
    def is_reject_or_cancel_status(cls, status: Any) -> bool:
        normalized = cls._normalize_status(status)
        return normalized in {
            "canceled",
            "cancelled",
            "rejected",
            "margincanceled",
            "margin_canceled",
            "selftradecanceled",
            "self_trade_canceled",
        }

    @property
    def position_state_ready(self) -> bool:
        return self._position_state_ready

    def seed_positions(self, position_sizes: Dict[str, float]) -> None:
        normalized: Dict[str, float] = {}
        for coin, size in (position_sizes or {}).items():
            c = self._normalize_coin(coin)
            if not c:
                continue
            s = self._to_float(size, 0.0)
            if abs(s) >= self._ZERO_EPS:
                normalized[c] = s
        with self._lock:
            self._positions = normalized
            self._position_state_ready = True

    def snapshot_position_sizes(self) -> Dict[str, float]:
        with self._lock:
            return dict(self._positions)

    def get_order(self, oid: Optional[int]) -> Optional[Dict[str, Any]]:
        if oid is None:
            return None
        try:
            key = int(oid)
        except Exception:
            return None
        with self._lock:
            order = self._orders_by_oid.get(key)
            return dict(order) if isinstance(order, dict) else None

    def _track_fill_seen(self, fill_key: str) -> bool:
        if fill_key in self._seen_fill_set:
            return False
        self._seen_fill_set.add(fill_key)
        if len(self._seen_fill_order) == self._seen_fill_order.maxlen:
            old = self._seen_fill_order.popleft()
            self._seen_fill_set.discard(old)
        self._seen_fill_order.append(fill_key)
        return True

    @staticmethod
    def _stable_payload_key(payload: Dict[str, Any]) -> str:
        try:
            return json.dumps(payload, sort_keys=True, separators=(",", ":"))
        except Exception:
            return str(payload)

    def _fill_key(self, fill: Dict[str, Any]) -> str:
        tx_hash = str(fill.get("hash") or "")
        tid = str(fill.get("tid") or "")
        if tx_hash and tid:
            return f"{tx_hash}:{tid}"
        if tx_hash:
            return tx_hash
        return self._stable_payload_key(fill)

    @staticmethod
    def _side_to_signed_delta(side: Any, size: float) -> float:
        s = str(side or "").strip().lower()
        if s in {"b", "buy", "bid", "long"}:
            return abs(size)
        if s in {"a", "ask", "sell", "short"}:
            return -abs(size)
        # Unknown side: keep provided sign if any.
        return size

    def _extract_fills(self, channel: str, data: Any) -> List[Dict[str, Any]]:
        fills: List[Dict[str, Any]] = []
        if channel == "userFills":
            if isinstance(data, dict) and isinstance(data.get("fills"), list):
                fills.extend(x for x in data["fills"] if isinstance(x, dict))
            return fills

        if channel != "user":
            return fills

        # WsUserEvent can arrive as a dict (single event) or as a list of events.
        events = data if isinstance(data, list) else [data]
        for ev in events:
            if not isinstance(ev, dict):
                continue
            ev_fills = ev.get("fills")
            if isinstance(ev_fills, list):
                fills.extend(x for x in ev_fills if isinstance(x, dict))
        return fills

    def _apply_fill(self, fill: Dict[str, Any]) -> bool:
        fill_key = self._fill_key(fill)
        if not self._track_fill_seen(fill_key):
            return False

        coin = self._normalize_coin(fill.get("coin"))
        if not coin:
            return False

        fill_ts = int(self._to_float(fill.get("time"), 0.0))
        size = self._to_float(fill.get("sz"), 0.0)
        if abs(size) < self._ZERO_EPS:
            return False

        signed_delta = self._side_to_signed_delta(fill.get("side"), size)
        start_position_raw = fill.get("startPosition", None)
        has_start_position = start_position_raw is not None
        start_position = self._to_float(start_position_raw, 0.0)

        with self._lock:
            # Ignore stale fills that arrive out-of-order and would rewind state.
            prev_ts = self._position_last_fill_ts.get(coin, 0)
            if fill_ts and prev_ts and fill_ts < prev_ts:
                return False

            current_position = self._positions.get(coin, 0.0)
            next_position = (start_position + signed_delta) if has_start_position else (current_position + signed_delta)
            if abs(next_position) < self._ZERO_EPS:
                self._positions.pop(coin, None)
            else:
                self._positions[coin] = next_position

            if fill_ts:
                self._position_last_fill_ts[coin] = fill_ts
            self._position_state_ready = True
        return True

    @staticmethod
    def _extract_order_rows(data: Any) -> List[Dict[str, Any]]:
        if isinstance(data, list):
            return [row for row in data if isinstance(row, dict)]
        if isinstance(data, dict):
            if isinstance(data.get("orders"), list):
                return [row for row in data["orders"] if isinstance(row, dict)]
            if isinstance(data.get("order"), dict):
                return [data]
        return []

    def _apply_order_update(self, row: Dict[str, Any]) -> bool:
        order = row.get("order")
        if not isinstance(order, dict):
            return False

        oid_raw = order.get("oid")
        try:
            oid = int(oid_raw)
        except Exception:
            return False

        coin = self._normalize_coin(order.get("coin"))
        status = self._normalize_status(row.get("status"))
        update = {
            "oid": oid,
            "coin": coin,
            "status": status,
            "status_timestamp": int(self._to_float(row.get("statusTimestamp"), 0.0)),
            "side": str(order.get("side") or ""),
            "limit_px": self._to_float(order.get("limitPx"), 0.0),
            "sz": self._to_float(order.get("sz"), 0.0),
            "orig_sz": self._to_float(order.get("origSz"), 0.0),
            "timestamp": int(self._to_float(order.get("timestamp"), 0.0)),
            "cloid": order.get("cloid"),
        }
        with self._lock:
            self._orders_by_oid[oid] = update
        return True

    def apply_events(self, events: List[Dict[str, Any]]) -> Dict[str, int]:
        stats = {
            "events": 0,
            "fills_seen": 0,
            "fills_applied": 0,
            "order_updates_applied": 0,
            "unknown_events": 0,
        }
        now_ts = 0.0

        for ev in events or []:
            if not isinstance(ev, dict):
                continue
            stats["events"] += 1
            now_ts = max(now_ts, self._to_float(ev.get("ts"), 0.0))
            channel = str(ev.get("channel") or "")
            data = ev.get("data")

            fills = self._extract_fills(channel, data)
            if fills:
                stats["fills_seen"] += len(fills)
                # Use event order from venue; stale fill guard prevents rewinds.
                for fill in fills:
                    if self._apply_fill(fill):
                        stats["fills_applied"] += 1
                continue

            if channel == "orderUpdates":
                rows = self._extract_order_rows(data)
                for row in rows:
                    if self._apply_order_update(row):
                        stats["order_updates_applied"] += 1
                continue

            stats["unknown_events"] += 1

        if now_ts > 0:
            self.last_event_ts = now_ts
        if stats["fills_applied"] > 0:
            self.last_position_update_ts = max(self.last_position_update_ts, time.time())
        if stats["order_updates_applied"] > 0:
            self.last_order_update_ts = max(self.last_order_update_ts, time.time())
        return stats
