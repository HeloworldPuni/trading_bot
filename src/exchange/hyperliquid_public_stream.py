import logging
import threading
import time
from collections import deque
from typing import Any, Deque, Dict, List, Optional

from src.config import Config
from src.marketdata import sanitize_ticker_payload

logger = logging.getLogger(__name__)


class HyperliquidPublicStream:
    """
    Public websocket stream for Hyperliquid all-mids feed.
    Maintains an in-memory ticker snapshot map for runtime usage.
    """

    def __init__(
        self,
        quote_currency: str = "USDC",
        testnet: bool = True,
        stale_timeout_sec: int = 30,
        queue_size: int = 2000,
    ):
        self.quote_currency = (quote_currency or "USDC").upper()
        self.testnet = bool(testnet)
        self.stale_timeout_sec = max(5, int(stale_timeout_sec))

        self._lock = threading.Lock()
        self._tickers: Dict[str, Dict[str, Any]] = {}
        self._ticker_ts: Dict[str, float] = {}
        self._updates: Deque[Dict[str, Any]] = deque(maxlen=max(100, int(queue_size)))

        self._running = False
        self._watchdog_thread: Optional[threading.Thread] = None
        self._last_event_ts = 0.0
        self._last_connect_ts = 0.0

        self._info = None
        self._base_url = None

    def _load_sdk(self):
        try:
            from hyperliquid.info import Info
            from hyperliquid.utils.constants import MAINNET_API_URL, TESTNET_API_URL
        except Exception as exc:
            raise RuntimeError("hyperliquid-python-sdk is required for public websocket feed.") from exc
        return Info, MAINNET_API_URL, TESTNET_API_URL

    @staticmethod
    def _coin_to_symbol(coin: str, quote: str) -> str:
        coin = str(coin or "").strip().upper()
        return f"{coin}/{quote}" if coin else ""

    def _extract_mids(self, ws_msg: Dict[str, Any]) -> Dict[str, float]:
        data = ws_msg.get("data")
        mids_raw: Dict[str, Any] = {}
        if isinstance(data, dict):
            if isinstance(data.get("mids"), dict):
                mids_raw = data.get("mids") or {}
            elif isinstance(data.get("allMids"), dict):
                mids_raw = data.get("allMids") or {}
            else:
                # Some payloads send mids as direct key-value map.
                mids_raw = data
        elif isinstance(data, list):
            for row in data:
                if not isinstance(row, dict):
                    continue
                coin = row.get("coin") or row.get("symbol")
                mid = row.get("mid") or row.get("px") or row.get("price")
                if coin is not None and mid is not None:
                    mids_raw[str(coin)] = mid

        mids: Dict[str, float] = {}
        for coin, raw_px in mids_raw.items():
            try:
                px = float(raw_px)
            except (TypeError, ValueError):
                continue
            if px > 0:
                mids[str(coin)] = px
        return mids

    def _on_event(self, ws_msg: Dict[str, Any]):
        if not isinstance(ws_msg, dict):
            return
        channel = str(ws_msg.get("channel") or "").strip()
        if channel and channel.lower() not in {"allmids", "all_mids"}:
            return

        mids = self._extract_mids(ws_msg)
        if not mids:
            return

        now_ts = time.time()
        with self._lock:
            for coin, px in mids.items():
                symbol = self._coin_to_symbol(coin, self.quote_currency)
                if not symbol:
                    continue
                ticker = sanitize_ticker_payload(
                    exchange_symbol=symbol,
                    normalized_symbol=symbol,
                    ticker={
                        "last": px,
                        "mid": px,
                        "_price_source": "hl_ws_mid",
                        "info": {"coin": coin},
                    },
                )
                ticker["_price_source"] = "hl_ws_mid"
                self._tickers[symbol] = ticker
                self._ticker_ts[symbol] = now_ts
                self._updates.append(
                    {
                        "symbol": symbol,
                        "price": px,
                        "ts": now_ts,
                    }
                )
            self._last_event_ts = now_ts

        if Config.HYPERLIQUID_WS_LOG_EVENTS:
            logger.info("[HL-PUBLIC-WS] allMids update: %s symbols", len(mids))

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
        Info, MAINNET_API_URL, TESTNET_API_URL = self._load_sdk()
        self._base_url = TESTNET_API_URL if self.testnet else MAINNET_API_URL
        self._info = Info(base_url=self._base_url, skip_ws=False, timeout=10.0)
        self._info.subscribe({"type": "allMids"}, self._on_event)
        self._last_event_ts = time.time()
        self._last_connect_ts = self._last_event_ts
        logger.info(
            "[HL-PUBLIC-WS] Connected (%s, quote=%s).",
            "testnet" if self.testnet else "mainnet",
            self.quote_currency,
        )

    def _watchdog(self):
        while self._running:
            time.sleep(5)
            stale_for = time.time() - self._last_event_ts
            if stale_for <= self.stale_timeout_sec:
                continue
            logger.warning("[HL-PUBLIC-WS] stale for %.1fs, reconnecting...", stale_for)
            try:
                self._disconnect()
                self._connect()
            except Exception as exc:
                logger.error("[HL-PUBLIC-WS] reconnect failed: %s", exc)

    def start(self):
        if self._running:
            return
        self._running = True
        self._connect()
        self._watchdog_thread = threading.Thread(
            target=self._watchdog,
            daemon=True,
            name="hl-public-ws-watchdog",
        )
        self._watchdog_thread.start()

    def stop(self):
        self._running = False
        self._disconnect()
        t = self._watchdog_thread
        if t and t.is_alive():
            t.join(timeout=2.0)

    def is_healthy(self) -> bool:
        if not self._running:
            return False
        return (time.time() - self._last_event_ts) <= self.stale_timeout_sec

    def snapshot_tickers(self, max_age_sec: Optional[float] = None) -> Dict[str, Dict[str, Any]]:
        now_ts = time.time()
        max_age = float(max_age_sec) if max_age_sec is not None else float(self.stale_timeout_sec)
        out: Dict[str, Dict[str, Any]] = {}
        with self._lock:
            for symbol, ticker in self._tickers.items():
                ts = self._ticker_ts.get(symbol, 0.0)
                if ts <= 0.0:
                    continue
                if max_age >= 0 and (now_ts - ts) > max_age:
                    continue
                out[symbol] = dict(ticker)
        return out

    def pop_price_updates(self, max_items: int = 2000) -> List[Dict[str, Any]]:
        """
        Return and clear queued price updates captured from websocket events.
        """
        limit = max(1, int(max_items))
        updates: List[Dict[str, Any]] = []
        with self._lock:
            while self._updates and len(updates) < limit:
                updates.append(dict(self._updates.popleft()))
        return updates
