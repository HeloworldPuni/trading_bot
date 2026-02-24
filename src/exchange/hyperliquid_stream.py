import hashlib
import json
import logging
import threading
import time
from collections import deque
from typing import Any, Deque, Dict, List, Optional

from src.config import Config

logger = logging.getLogger(__name__)


class HyperliquidUserStream:
    """
    User-stream wrapper with reconnection watchdog and event deduplication.
    """

    def __init__(
        self,
        user_address: str,
        testnet: bool = True,
        stale_timeout_sec: int = 120,
        queue_size: int = 2000,
    ):
        self.user_address = (user_address or "").strip()
        self.testnet = bool(testnet)
        self.stale_timeout_sec = max(30, int(stale_timeout_sec))

        self._lock = threading.Lock()
        self._events: Deque[Dict[str, Any]] = deque(maxlen=max(100, int(queue_size)))
        self._seen_order: Deque[str] = deque(maxlen=5000)
        self._seen_set = set()

        self._running = False
        self._watchdog_thread: Optional[threading.Thread] = None
        self._last_event_ts = time.time()

        self._info = None
        self._base_url = None

    def _load_sdk(self):
        try:
            from hyperliquid.info import Info
            from hyperliquid.utils.constants import MAINNET_API_URL, TESTNET_API_URL
        except Exception as exc:
            raise RuntimeError(
                "hyperliquid-python-sdk is required for websocket streaming."
            ) from exc
        return Info, MAINNET_API_URL, TESTNET_API_URL

    @staticmethod
    def _fingerprint(event: Dict[str, Any]) -> str:
        try:
            payload = json.dumps(event, sort_keys=True, separators=(",", ":"))
        except Exception:
            payload = str(event)
        return hashlib.sha1(payload.encode("utf-8")).hexdigest()

    def _dedupe_accept(self, event: Dict[str, Any]) -> bool:
        key = self._fingerprint(event)
        if key in self._seen_set:
            return False
        self._seen_set.add(key)
        if len(self._seen_order) == self._seen_order.maxlen:
            old = self._seen_order.popleft()
            self._seen_set.discard(old)
        self._seen_order.append(key)
        return True

    def _on_event(self, ws_msg: Dict[str, Any]):
        self._last_event_ts = time.time()
        if not isinstance(ws_msg, dict):
            return
        if not self._dedupe_accept(ws_msg):
            return
        normalized = {
            "ts": self._last_event_ts,
            "channel": ws_msg.get("channel"),
            "data": ws_msg.get("data"),
            "raw": ws_msg,
        }
        with self._lock:
            self._events.append(normalized)
        if Config.HYPERLIQUID_WS_LOG_EVENTS:
            logger.info("[HL-WS] %s event queued", normalized.get("channel"))

    def _disconnect(self):
        info = self._info
        self._info = None
        if not info:
            return
        try:
            info.disconnect_websocket()
        except Exception:
            pass

    def _connect(self):
        if not self.user_address:
            raise RuntimeError("Hyperliquid user stream requires user_address.")
        Info, MAINNET_API_URL, TESTNET_API_URL = self._load_sdk()
        self._base_url = TESTNET_API_URL if self.testnet else MAINNET_API_URL
        self._info = Info(base_url=self._base_url, skip_ws=False, timeout=10.0)

        self._info.subscribe({"type": "userEvents", "user": self.user_address}, self._on_event)
        self._info.subscribe({"type": "userFills", "user": self.user_address}, self._on_event)
        self._info.subscribe({"type": "orderUpdates", "user": self.user_address}, self._on_event)
        self._last_event_ts = time.time()
        logger.info("[HL-WS] Connected (%s) for %s", "testnet" if self.testnet else "mainnet", self.user_address)

    def _watchdog(self):
        while self._running:
            time.sleep(5)
            stale_for = time.time() - self._last_event_ts
            if stale_for <= self.stale_timeout_sec:
                continue
            logger.warning("[HL-WS] stale for %.1fs, reconnecting stream...", stale_for)
            try:
                self._disconnect()
                self._connect()
            except Exception as exc:
                logger.error("[HL-WS] reconnect failed: %s", exc)

    def start(self):
        if self._running:
            return
        self._running = True
        self._connect()
        self._watchdog_thread = threading.Thread(target=self._watchdog, daemon=True, name="hl-user-ws-watchdog")
        self._watchdog_thread.start()

    def stop(self):
        self._running = False
        self._disconnect()
        t = self._watchdog_thread
        if t and t.is_alive():
            t.join(timeout=2.0)

    def pop_events(self, max_items: int = 200) -> List[Dict[str, Any]]:
        out: List[Dict[str, Any]] = []
        cap = max(1, int(max_items))
        with self._lock:
            while self._events and len(out) < cap:
                out.append(self._events.popleft())
        return out
