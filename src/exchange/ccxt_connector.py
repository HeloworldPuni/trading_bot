import functools
import logging
import os
import time
from collections import deque
from typing import Any, Dict, List, Optional

import ccxt

from src.config import Config
from src.marketdata import sanitize_ticker_payload

logger = logging.getLogger(__name__)


def retry_with_backoff(max_retries: int = 3, base_delay: float = 1.0):
    """
    Decorator for exponential backoff retry on transient exchange failures.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            for attempt in range(max_retries):
                try:
                    result = func(self, *args, **kwargs)
                    self._consecutive_failures = 0
                    return result
                except Exception as exc:
                    delay = base_delay * (2 ** attempt)
                    self._consecutive_failures += 1
                    if self._consecutive_failures >= 5:
                        logger.error(
                            "EXCHANGE HEALTH: %s consecutive API failures",
                            self._consecutive_failures,
                        )
                    if attempt < max_retries - 1:
                        logger.warning(
                            "API call failed (attempt %s/%s): %s. Retrying in %.1fs...",
                            attempt + 1,
                            max_retries,
                            exc,
                            delay,
                        )
                        time.sleep(delay)
                    else:
                        logger.error("API call failed after %s attempts: %s", max_retries, exc)
                        raise

        return wrapper

    return decorator


class CCXTConnector:
    """
    Reusable CCXT connector with symbol normalization and cache helpers.
    """

    TICKER_CACHE_TTL = 30
    OHLCV_CACHE_TTL = 60
    MAX_RATE_LIMIT_BACKOFF_SEC = 90

    DEFAULT_EXCLUDED_BASES = {
        "USDC",
        "BUSD",
        "DAI",
        "TUSD",
        "USDP",
        "FDUSD",
        "USDT",
        "USD0",
    }

    def __init__(
        self,
        exchange_id: Optional[str] = None,
        quote_currency: Optional[str] = None,
        market_type: Optional[str] = None,
        settlement_currency: Optional[str] = None,
    ):
        self.exchange_id = (exchange_id or Config.EXCHANGE_ID or "binance").lower()
        self.quote_currency = (quote_currency or Config.QUOTE_CURRENCY or "USDT").upper()
        self.market_type = (market_type or Config.EXCHANGE_MARKET_TYPE or "").lower()
        self.settlement_currency = (settlement_currency or self.quote_currency).upper()

        self.exchange = None
        self._ticker_cache: Dict[str, Dict[str, Any]] = {}
        self._ticker_cache_time: float = 0
        self._ohlcv_cache: Dict[str, List[List[Any]]] = {}
        self._ohlcv_cache_time: Dict[str, float] = {}
        self._consecutive_failures: int = 0
        self._rate_limit_hits: int = 0
        self._degraded_until_ts: float = 0.0
        self._last_degraded_log_ts: float = 0.0
        self._error_window: deque[float] = deque(maxlen=20)
        self._slow_warning_ts: Dict[str, float] = {}
        self._rate_guard_enabled = bool(getattr(Config, "RATE_GUARD_ENABLED", True))
        self._rate_guard_window_sec = max(30, int(getattr(Config, "RATE_GUARD_WINDOW_SEC", 60)))
        self._rate_guard_429_escalate_hits = max(1, int(getattr(Config, "RATE_GUARD_429_ESCALATE_HITS", 6)))
        self._rate_guard_success_recovery = max(10, int(getattr(Config, "RATE_GUARD_SUCCESS_RECOVERY", 120)))
        self._rate_guard_max_level = max(0, int(getattr(Config, "RATE_GUARD_MAX_LEVEL", 3)))
        self._rate_guard_level = 0
        self._rate_guard_success_streak = 0
        self._rate_guard_429_times: deque[float] = deque(maxlen=500)
        self._rate_guard_last_change_ts = 0.0
        self._rate_guard_last_log_ts = 0.0
        self._endpoint_call_times: Dict[str, deque[float]] = {
            ep: deque(maxlen=5000) for ep in self.RATE_GUARD_ENDPOINTS
        }
        self._rate_guard_budgets_per_min: Dict[str, int] = {
            "ohlcv": max(1, int(getattr(Config, "RATE_GUARD_BUDGET_OHLCV_PER_MIN", 20))),
            "orderbook": max(0, int(getattr(Config, "RATE_GUARD_BUDGET_ORDERBOOK_PER_MIN", 6))),
            "ticker_snapshot": max(1, int(getattr(Config, "RATE_GUARD_BUDGET_TICKER_SNAPSHOT_PER_MIN", 30))),
            "batch_tickers": max(0, int(getattr(Config, "RATE_GUARD_BUDGET_BATCH_TICKERS_PER_MIN", 4))),
            "funding": max(0, int(getattr(Config, "RATE_GUARD_BUDGET_FUNDING_PER_MIN", 20))),
            "top_symbols": max(0, int(getattr(Config, "RATE_GUARD_BUDGET_TOP_SYMBOLS_PER_MIN", 4))),
        }
        self._connect()

    def _build_exchange_params(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "enableRateLimit": True,
            "enableRateLimit": True,
            "timeout": 5000,
            "options": {},
        }

        if Config.EXCHANGE_API_KEY:
            params["apiKey"] = Config.EXCHANGE_API_KEY
        if Config.EXCHANGE_SECRET:
            params["secret"] = Config.EXCHANGE_SECRET
        if self.market_type:
            params["options"]["defaultType"] = self.market_type
        if not params["options"]:
            params.pop("options", None)
        return params

    def _connect(self):
        try:
            exchange_class = getattr(ccxt, self.exchange_id)
            params = self._build_exchange_params()
            self.exchange = exchange_class(params)
            logger.info("Connected to %s", self.exchange_id)
        except AttributeError as exc:
            raise RuntimeError(f"Unsupported exchange_id '{self.exchange_id}' in ccxt") from exc
        except Exception as exc:
            logger.error("Failed to connect to exchange %s: %s", self.exchange_id, exc)
            raise

    def _ensure_markets_loaded(self):
        if self.exchange is None:
            return
        if not getattr(self.exchange, "markets", None):
            self.exchange.load_markets()

    @staticmethod
    def normalize_symbol(symbol: str) -> str:
        if not symbol:
            return symbol
        return symbol.split(":")[0] if ":" in symbol else symbol

    def _normalize_ticker(self, ticker: Dict[str, Any], exchange_symbol: str) -> Dict[str, Any]:
        return sanitize_ticker_payload(
            exchange_symbol=exchange_symbol,
            normalized_symbol=self.normalize_symbol(exchange_symbol),
            ticker=ticker,
        )

    def to_exchange_symbol(self, symbol: str) -> str:
        """
        Convert normalized symbols (e.g. BTC/USDC) to venue-specific market symbols
        (e.g. BTC/USDC:USDC) when needed.
        """
        if not symbol:
            return symbol

        normalized = self.normalize_symbol(symbol)
        self._ensure_markets_loaded()
        markets = getattr(self.exchange, "markets", {}) or {}

        if symbol in markets:
            return symbol
        if normalized in markets:
            return normalized

        if "/" in normalized:
            base, quote = normalized.split("/", 1)
            candidates = [
                f"{base}/{quote}:{self.settlement_currency}",
                f"{base}/{quote}",
            ]
            if quote != self.quote_currency:
                candidates.extend(
                    [
                        f"{base}/{self.quote_currency}:{self.settlement_currency}",
                        f"{base}/{self.quote_currency}",
                    ]
                )
            for candidate in candidates:
                if candidate in markets:
                    return candidate

        for market_symbol in markets.keys():
            if self.normalize_symbol(market_symbol) == normalized:
                return market_symbol

        return symbol

    def fallback_symbols(self, limit: int = 5) -> List[str]:
        if self.exchange_id == "hyperliquid" and self.quote_currency == "USDC":
            # Hyperliquid-safe defaults to avoid unavailable pairs during fallback.
            majors = ["BTC", "ETH", "SOL", "HYPE", "XRP", "DOGE", "AVAX", "INJ"]
        else:
            majors = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
        return [f"{base}/{self.quote_currency}" for base in majors[: max(1, int(limit))]]

    def _extract_quote_volume(self, ticker: Dict[str, Any]) -> float:
        if not isinstance(ticker, dict):
            return 0.0
        direct = ticker.get("quoteVolume")
        if direct is not None:
            try:
                return float(direct)
            except Exception:
                return 0.0
        info = ticker.get("info") or {}
        for key in ("quoteVolume", "turnover24h", "notionalVolume", "volumeUsd24h"):
            val = info.get(key)
            if val is not None:
                try:
                    return float(val)
                except Exception:
                    continue
        return 0.0

    @staticmethod
    def _is_rate_limited_error(exc: Exception) -> bool:
        msg = str(exc).lower()
        rate_limit_classes = tuple(
            cls
            for cls in (
                getattr(ccxt, "RateLimitExceeded", None),
                getattr(ccxt, "DDoSProtection", None),
            )
            if isinstance(cls, type)
        )
        if rate_limit_classes and isinstance(exc, rate_limit_classes):
            return True
        return (
            "429" in msg
            or "too many requests" in msg
            or "rate limit" in msg
            or "throttle" in msg
        )

    @staticmethod
    def _is_transient_error(exc: Exception) -> bool:
        transient_classes = tuple(
            cls
            for cls in (
                getattr(ccxt, "NetworkError", None),
                getattr(ccxt, "RequestTimeout", None),
                getattr(ccxt, "ExchangeNotAvailable", None),
            )
            if isinstance(cls, type)
        )
        if transient_classes and isinstance(exc, transient_classes):
            return True
        msg = str(exc).lower()
        return any(
            token in msg
            for token in (
                "timeout",
                "temporarily unavailable",
                "connection reset",
                "connection aborted",
                "max retries exceeded",
            )
        )

    def _ensure_rate_guard_state(self):
        """
        Backward-compatible lazy init for tests that instantiate the connector with __new__.
        """
        if not hasattr(self, "_rate_guard_enabled"):
            self._rate_guard_enabled = bool(getattr(Config, "RATE_GUARD_ENABLED", True))
        if not hasattr(self, "_rate_guard_window_sec"):
            self._rate_guard_window_sec = max(30, int(getattr(Config, "RATE_GUARD_WINDOW_SEC", 60)))
        if not hasattr(self, "_rate_guard_429_escalate_hits"):
            self._rate_guard_429_escalate_hits = max(1, int(getattr(Config, "RATE_GUARD_429_ESCALATE_HITS", 6)))
        if not hasattr(self, "_rate_guard_success_recovery"):
            self._rate_guard_success_recovery = max(10, int(getattr(Config, "RATE_GUARD_SUCCESS_RECOVERY", 120)))
        if not hasattr(self, "_rate_guard_max_level"):
            self._rate_guard_max_level = max(0, int(getattr(Config, "RATE_GUARD_MAX_LEVEL", 3)))
        if not hasattr(self, "_rate_guard_level"):
            self._rate_guard_level = 0
        if not hasattr(self, "_rate_guard_success_streak"):
            self._rate_guard_success_streak = 0
        if not hasattr(self, "_rate_guard_429_times"):
            self._rate_guard_429_times = deque(maxlen=500)
        if not hasattr(self, "_rate_guard_last_change_ts"):
            self._rate_guard_last_change_ts = 0.0
        if not hasattr(self, "_rate_guard_last_log_ts"):
            self._rate_guard_last_log_ts = 0.0
        if not hasattr(self, "_endpoint_call_times"):
            self._endpoint_call_times = {
                ep: deque(maxlen=5000) for ep in self.RATE_GUARD_ENDPOINTS
            }
        if not hasattr(self, "_rate_guard_budgets_per_min"):
            self._rate_guard_budgets_per_min = {
                "ohlcv": max(1, int(getattr(Config, "RATE_GUARD_BUDGET_OHLCV_PER_MIN", 20))),
                "orderbook": max(0, int(getattr(Config, "RATE_GUARD_BUDGET_ORDERBOOK_PER_MIN", 6))),
                "ticker_snapshot": max(1, int(getattr(Config, "RATE_GUARD_BUDGET_TICKER_SNAPSHOT_PER_MIN", 30))),
                "batch_tickers": max(0, int(getattr(Config, "RATE_GUARD_BUDGET_BATCH_TICKERS_PER_MIN", 4))),
                "funding": max(0, int(getattr(Config, "RATE_GUARD_BUDGET_FUNDING_PER_MIN", 20))),
                "top_symbols": max(0, int(getattr(Config, "RATE_GUARD_BUDGET_TOP_SYMBOLS_PER_MIN", 4))),
            }

    def _rate_guard_prune(self, q: deque[float], now_ts: float):
        cutoff = now_ts - float(self._rate_guard_window_sec)
        while q and q[0] < cutoff:
            q.popleft()

    def _rate_guard_level_multiplier(self) -> float:
        level = int(getattr(self, "_rate_guard_level", 0))
        max_level = max(0, int(getattr(self, "_rate_guard_max_level", 3)))
        level = max(0, min(max_level, level))
        return float(self.RATE_GUARD_LEVEL_MULTIPLIERS.get(level, 0.30))

    def _rate_guard_budget(self, endpoint: str) -> int:
        self._ensure_rate_guard_state()
        base_per_min = int(self._rate_guard_budgets_per_min.get(endpoint, 0))
        if base_per_min <= 0:
            return 0
        level = int(self._rate_guard_level)
        # Endpoint-specific hard disables under heavy stress.
        if endpoint == "orderbook" and level >= 2:
            return 0
        if endpoint in {"batch_tickers", "top_symbols"} and level >= 3:
            return 0
        window_scale = float(self._rate_guard_window_sec) / 60.0
        budget = int(base_per_min * window_scale * self._rate_guard_level_multiplier())
        return max(1, budget)

    def _rate_guard_note_call(self, endpoint: str):
        self._ensure_rate_guard_state()
        q = self._endpoint_call_times.setdefault(endpoint, deque(maxlen=5000))
        now_ts = time.time()
        self._rate_guard_prune(q, now_ts)
        q.append(now_ts)

    def _rate_guard_allow(self, endpoint: str) -> bool:
        self._ensure_rate_guard_state()
        if not self._rate_guard_enabled:
            return True
        budget = self._rate_guard_budget(endpoint)
        if budget <= 0:
            return False
        q = self._endpoint_call_times.setdefault(endpoint, deque(maxlen=5000))
        now_ts = time.time()
        self._rate_guard_prune(q, now_ts)
        if len(q) >= budget:
            if now_ts - float(self._rate_guard_last_log_ts) >= 20.0:
                logger.warning(
                    "[RATE-GUARD] %s budget exhausted (%s/%s in %ss).",
                    endpoint,
                    len(q),
                    budget,
                    self._rate_guard_window_sec,
                )
                self._rate_guard_last_log_ts = now_ts
            return False
        return True

    def _rate_guard_escalate_if_needed(self):
        self._ensure_rate_guard_state()
        if not self._rate_guard_enabled:
            return
        now_ts = time.time()
        self._rate_guard_prune(self._rate_guard_429_times, now_ts)
        hits = len(self._rate_guard_429_times)
        threshold = int(self._rate_guard_429_escalate_hits) * (int(self._rate_guard_level) + 1)
        if hits >= threshold and self._rate_guard_level < self._rate_guard_max_level:
            self._rate_guard_level += 1
            self._rate_guard_success_streak = 0
            self._rate_guard_last_change_ts = now_ts
            logger.warning(
                "[RATE-GUARD] Escalated to level %s after %s rate-limit hits in %ss.",
                self._rate_guard_level,
                hits,
                self._rate_guard_window_sec,
            )

    def _rate_guard_recover_if_needed(self):
        self._ensure_rate_guard_state()
        if not self._rate_guard_enabled or self._rate_guard_level <= 0:
            return
        now_ts = time.time()
        self._rate_guard_prune(self._rate_guard_429_times, now_ts)
        if self._rate_guard_429_times:
            return
        if self._rate_guard_success_streak >= self._rate_guard_success_recovery:
            self._rate_guard_level = max(0, self._rate_guard_level - 1)
            self._rate_guard_success_streak = 0
            self._rate_guard_last_change_ts = now_ts
            logger.info("[RATE-GUARD] Recovered to level %s.", self._rate_guard_level)

    def get_rate_guard_profile(self) -> Dict[str, Any]:
        self._ensure_rate_guard_state()
        level = int(self._rate_guard_level)
        mult = self._rate_guard_level_multiplier()
        # Main loop can use these hints to shrink scan pressure under stress.
        scan_multiplier = {0: 1.0, 1: 0.85, 2: 0.65, 3: 0.45}.get(level, 0.45)
        return {
            "enabled": bool(self._rate_guard_enabled),
            "level": level,
            "window_sec": int(self._rate_guard_window_sec),
            "multiplier": mult,
            "allow_orderbook": self._rate_guard_budget("orderbook") > 0,
            "allow_batch_ticker": self._rate_guard_budget("batch_tickers") > 0,
            "max_refresh_symbols_per_cycle": max(0, int(round(getattr(Config, "MARKETDATA_REFRESH_SYMBOLS_PER_CYCLE", 0) * scan_multiplier))),
            "scan_symbol_multiplier": float(scan_multiplier),
            "429_hits_window": len(self._rate_guard_429_times),
        }

    def _record_api_success(self):
        self._ensure_rate_guard_state()
        self._consecutive_failures = 0
        self._rate_limit_hits = max(0, self._rate_limit_hits - 1)
        self._rate_guard_success_streak += 1
        self._rate_guard_recover_if_needed()

    def _record_api_failure(self, exc: Exception):
        self._ensure_rate_guard_state()
        self._consecutive_failures += 1
        self._error_window.append(time.time())
        self._rate_guard_success_streak = 0

        if self._is_rate_limited_error(exc):
            self._rate_limit_hits += 1
            self._rate_guard_429_times.append(time.time())
            self._rate_guard_escalate_if_needed()
            backoff = min(
                self.MAX_RATE_LIMIT_BACKOFF_SEC,
                float(2 ** min(self._rate_limit_hits, 6)),
            )
            self._degraded_until_ts = max(self._degraded_until_ts, time.time() + backoff)
            logger.warning(
                "Rate limit hit on %s. Entering cooldown %.0fs.",
                self.exchange_id,
                backoff,
            )
            return

        # Even non-429 transient failures can spiral into API storms; apply a short cooldown.
        transient_backoff = min(
            10.0,
            float(1 + min(self._consecutive_failures, 5)),
        )
        self._degraded_until_ts = max(self._degraded_until_ts, time.time() + transient_backoff)

    def _log_slow_once(self, key: str, message: str, cooldown_sec: int = 180):
        now = time.time()
        last_ts = self._slow_warning_ts.get(key, 0.0)
        if now - last_ts >= max(1, cooldown_sec):
            logger.warning(message)
            self._slow_warning_ts[key] = now

    def _is_degraded(self) -> bool:
        now = time.time()
        degraded = now < self._degraded_until_ts
        if degraded and now - self._last_degraded_log_ts > 15:
            remaining = max(0.0, self._degraded_until_ts - now)
            logger.warning(
                "Exchange %s in temporary cooldown (%.1fs remaining). Using cached/fallback data.",
                self.exchange_id,
                remaining,
            )
            self._last_degraded_log_ts = now
        return degraded

    def get_degraded_remaining(self) -> float:
        return max(0.0, self._degraded_until_ts - time.time())

    def fetch_ohlcv(self, symbol: str, timeframe: str, limit: int = 100) -> List[List[Any]]:
        cache_key = f"{self.normalize_symbol(symbol)}_{timeframe}_{limit}"
        now = time.time()

        if cache_key in self._ohlcv_cache:
            cached_at = self._ohlcv_cache_time.get(cache_key, 0.0)
            if now - cached_at < self.OHLCV_CACHE_TTL:
                return self._ohlcv_cache[cache_key]

        if self._is_degraded():
            return self._ohlcv_cache.get(cache_key, [])
        if not self._rate_guard_allow("ohlcv"):
            return self._ohlcv_cache.get(cache_key, [])

        t0 = time.time()
        try:
            self._rate_guard_note_call("ohlcv")
            exchange_symbol = self.to_exchange_symbol(symbol)
            data = self.exchange.fetch_ohlcv(exchange_symbol, timeframe, limit=limit)
            
            elapsed = time.time() - t0
            if elapsed > 2.0:
                self._log_slow_once(
                    key=f"ohlcv:{symbol}",
                    message=f"SLOW API: fetch_ohlcv({symbol}) took {elapsed:.2f}s",
                )

            self._ohlcv_cache[cache_key] = data
            self._ohlcv_cache_time[cache_key] = now
            self._record_api_success()
            return data
        except Exception as exc:
            elapsed = time.time() - t0
            self._record_api_failure(exc)
            
            # Enhanced logging for debugging freeze
            log_level = logging.WARNING if elapsed < 5.0 else logging.ERROR
            logger.log(log_level, f"API FAIL: fetch_ohlcv({symbol}) took {elapsed:.2f}s: {exc}")
            
            return self._ohlcv_cache.get(cache_key, [])

    ORDERBOOK_CACHE_TTL = 30
    RATE_GUARD_ENDPOINTS = (
        "ohlcv",
        "orderbook",
        "ticker_snapshot",
        "batch_tickers",
        "funding",
        "top_symbols",
    )
    RATE_GUARD_LEVEL_MULTIPLIERS = {
        0: 1.00,
        1: 0.75,
        2: 0.50,
        3: 0.30,
    }

    def fetch_order_book(self, symbol: str, depth: int = 20) -> Dict[str, Any]:
        """Fetch L2 orderbook snapshot via ccxt. Returns {"bids": [...], "asks": [...]}."""
        cache_key = f"ob_{self.normalize_symbol(symbol)}_{depth}"
        now = time.time()

        if not hasattr(self, "_ob_cache"):
            self._ob_cache: Dict[str, Dict[str, Any]] = {}
            self._ob_cache_time: Dict[str, float] = {}

        if cache_key in self._ob_cache:
            cached_at = self._ob_cache_time.get(cache_key, 0.0)
            if now - cached_at < self.ORDERBOOK_CACHE_TTL:
                return self._ob_cache[cache_key]

        if self._is_degraded():
            return self._ob_cache.get(cache_key, {})
        if not self._rate_guard_allow("orderbook"):
            return self._ob_cache.get(cache_key, {})

        t0 = time.time()
        try:
            self._rate_guard_note_call("orderbook")
            exchange_symbol = self.to_exchange_symbol(symbol)
            book = self.exchange.fetch_order_book(exchange_symbol, limit=depth)
            elapsed = time.time() - t0
            if elapsed > 2.0:
                self._log_slow_once(
                    key=f"orderbook:{symbol}",
                    message=f"SLOW API: fetch_order_book({symbol}) took {elapsed:.2f}s",
                )

            result = {
                "bids": book.get("bids", []),
                "asks": book.get("asks", []),
            }
            self._ob_cache[cache_key] = result
            self._ob_cache_time[cache_key] = now
            self._record_api_success()
            return result
        except Exception as exc:
            self._record_api_failure(exc)
            logger.debug(f"fetch_order_book({symbol}) failed: {exc}")
            return self._ob_cache.get(cache_key, {})

    def fetch_ticker_snapshot(self, symbol: str) -> Dict[str, Any]:
        normalized_symbol = self.normalize_symbol(symbol)
        cached = self._ticker_cache.get(symbol) or self._ticker_cache.get(normalized_symbol)
        if cached and (time.time() - self._ticker_cache_time) < self.TICKER_CACHE_TTL:
            return cached

        if self._is_degraded():
            if cached:
                return cached
        if not self._rate_guard_allow("ticker_snapshot"):
            return cached or {}
        try:
            self._rate_guard_note_call("ticker_snapshot")
            exchange_symbol = self.to_exchange_symbol(symbol)
            ticker = self.exchange.fetch_ticker(exchange_symbol)
            self._record_api_success()
            normalized = self._normalize_ticker(ticker, exchange_symbol)
            self._ticker_cache[normalized_symbol] = normalized
            self._ticker_cache[exchange_symbol] = normalized
            return normalized
        except Exception as exc:
            self._record_api_failure(exc)
            if self._is_rate_limited_error(exc):
                logger.warning("Ticker snapshot rate-limited for %s. Using cache/fallback.", symbol)
            elif self._is_transient_error(exc):
                self._log_slow_once(
                    key=f"ticker-snapshot-transient:{symbol}",
                    message=f"Ticker snapshot transient failure for {symbol}. Using cache/fallback.",
                    cooldown_sec=60,
                )
            else:
                logger.error("Error fetching ticker snapshot for %s: %s", symbol, exc)
            return cached or {}

    def fetch_balance(self) -> Dict[str, Any]:
        if self._is_degraded():
            return {}
        try:
            bal = self.exchange.fetch_balance()
            self._record_api_success()
            return bal
        except Exception as exc:
            self._record_api_failure(exc)
            logger.error("Error fetching balance: %s", exc)
            return {}

    def refresh_all_tickers(self) -> Dict[str, Dict[str, Any]]:
        now = time.time()
        if now - self._ticker_cache_time < self.TICKER_CACHE_TTL and self._ticker_cache:
            return self._ticker_cache

        if self._is_degraded():
            return self._ticker_cache
        if not self._rate_guard_allow("batch_tickers"):
            return self._ticker_cache

        try:
            self._rate_guard_note_call("batch_tickers")
            raw_tickers = self.exchange.fetch_tickers()
            normalized: Dict[str, Dict[str, Any]] = {}
            for exchange_symbol, ticker in (raw_tickers or {}).items():
                row = self._normalize_ticker(ticker, exchange_symbol)
                normalized[exchange_symbol] = row
                normalized.setdefault(self.normalize_symbol(exchange_symbol), row)

            self._ticker_cache = normalized
            self._ticker_cache_time = now
            self._record_api_success()
            logger.debug("Refreshed %s tickers (%s aliases)", len(raw_tickers or {}), len(normalized))
            return self._ticker_cache
        except Exception as exc:
            self._record_api_failure(exc)
            if self._is_rate_limited_error(exc):
                logger.warning("Batch ticker refresh rate-limited. Reusing cached tickers.")
            elif self._is_transient_error(exc):
                self._log_slow_once(
                    key="batch-ticker-transient",
                    message="Batch ticker refresh transient failure. Reusing cached tickers.",
                    cooldown_sec=60,
                )
            else:
                logger.error("Error batch fetching tickers: %s", exc)
            return self._ticker_cache

    def get_market_structure(self, symbol: str) -> Optional[Dict[str, Any]]:
        now = time.time()
        if self._ticker_cache and now - self._ticker_cache_time < self.TICKER_CACHE_TTL:
            cached = self._ticker_cache.get(symbol)
            if cached:
                return cached
            cached = self._ticker_cache.get(self.normalize_symbol(symbol))
            if cached:
                return cached

        ticker = self.fetch_ticker_snapshot(symbol)
        if ticker:
            normalized_symbol = self.normalize_symbol(symbol)
            exchange_symbol = ticker.get("_exchange_symbol", normalized_symbol)
            self._ticker_cache[normalized_symbol] = ticker
            self._ticker_cache[exchange_symbol] = ticker
        return ticker or None

    def fetch_funding_rate(self, symbol: str) -> float:
        if self._is_degraded():
            return 0.0
        if not self._rate_guard_allow("funding"):
            return 0.0
        try:
            self._rate_guard_note_call("funding")
            exchange_symbol = self.to_exchange_symbol(symbol)
            funding = self.exchange.fetch_funding_rate(exchange_symbol)
            if funding:
                for key in ("fundingRate", "funding_rate"):
                    if key in funding and funding[key] is not None:
                        return float(funding[key]) * 100.0
                info = funding.get("info") if isinstance(funding, dict) else None
                if isinstance(info, dict):
                    for key in ("fundingRate", "funding_rate"):
                        if key in info and info[key] is not None:
                            return float(info[key]) * 100.0
            self._record_api_success()
            return 0.0
        except Exception as exc:
            self._record_api_failure(exc)
            return 0.0

    @retry_with_backoff(max_retries=3, base_delay=0.8)
    def fetch_top_symbols_by_volume(self, limit: int = 15) -> List[str]:
        if self._is_degraded():
            if self._ticker_cache:
                # Use last known snapshot while cooling down.
                entries: List[tuple[str, float]] = []
                for symbol, ticker in self._ticker_cache.items():
                    normalized = self.normalize_symbol(symbol)
                    if "/" not in normalized:
                        continue
                    base, quote = normalized.split("/", 1)
                    if quote.upper() != self.quote_currency:
                        continue
                    if base.upper() in self.DEFAULT_EXCLUDED_BASES:
                        continue
                    vol = self._extract_quote_volume(ticker)
                    if vol > 0:
                        entries.append((normalized, vol))
                entries = sorted(entries, key=lambda x: x[1], reverse=True)
                if entries:
                    seen = set()
                    ranked = []
                    for sym, _ in entries:
                        if sym not in seen:
                            seen.add(sym)
                            ranked.append(sym)
                        if len(ranked) >= max(1, int(limit)):
                            break
                    if ranked:
                        return ranked
            return self.fallback_symbols(limit=limit)

        if not self._rate_guard_allow("top_symbols"):
            return self.fallback_symbols(limit=limit)

        try:
            self._rate_guard_note_call("top_symbols")
            self._ensure_markets_loaded()
            tickers = self.exchange.fetch_tickers()
            entries: List[tuple[str, float]] = []
            excluded = set(self.DEFAULT_EXCLUDED_BASES)
            excluded.add(self.quote_currency)

            for exchange_symbol, ticker in (tickers or {}).items():
                normalized = self.normalize_symbol(exchange_symbol)
                if "/" not in normalized:
                    continue
                base, quote = normalized.split("/", 1)
                if quote.upper() != self.quote_currency:
                    continue
                if base.upper() in excluded:
                    continue
                if base.upper().startswith("XYZ"):
                    continue
                vol = self._extract_quote_volume(ticker)
                if vol > 0:
                    entries.append((normalized, vol))

            deduped: Dict[str, float] = {}
            for normalized, vol in entries:
                if normalized not in deduped or vol > deduped[normalized]:
                    deduped[normalized] = vol

            ordered = sorted(deduped.items(), key=lambda item: item[1], reverse=True)
            top = [sym for sym, _ in ordered[: max(1, int(limit))]]
            if not top:
                return self.fallback_symbols(limit=limit)

            logger.info(
                "Top %s %s pairs by 24h volume: %s",
                limit,
                self.quote_currency,
                ", ".join(sym.split("/")[0] for sym in top),
            )
            self._record_api_success()
            return top
        except Exception as exc:
            self._record_api_failure(exc)
            if self._is_rate_limited_error(exc):
                logger.warning("Top-symbol scan rate-limited. Falling back to cached/major symbols.")
            else:
                logger.error("Error fetching top symbols: %s", exc)
            return self.fallback_symbols(limit=limit)


class BinanceConnector(CCXTConnector):
    def __init__(self):
        super().__init__(
            exchange_id="binance",
            quote_currency=os.getenv("QUOTE_CURRENCY", "USDT"),
            market_type=os.getenv("EXCHANGE_MARKET_TYPE", "future"),
            settlement_currency=os.getenv("QUOTE_CURRENCY", "USDT"),
        )


class HyperliquidConnector(CCXTConnector):
    def __init__(self):
        super().__init__(
            exchange_id="hyperliquid",
            quote_currency=os.getenv("QUOTE_CURRENCY", "USDC"),
            market_type=os.getenv("EXCHANGE_MARKET_TYPE", "swap"),
            settlement_currency=os.getenv("QUOTE_CURRENCY", "USDC"),
        )

    def _build_exchange_params(self) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "enableRateLimit": True,
            "options": {"defaultType": self.market_type or "swap"},
        }

        api_wallet = os.getenv("HYPERLIQUID_API_WALLET", "").strip()
        private_key = os.getenv("HYPERLIQUID_PRIVATE_KEY", "").strip()
        if api_wallet and private_key:
            params["walletAddress"] = api_wallet
            params["privateKey"] = private_key

        return params
