import time
from collections import deque

from src.exchange.ccxt_connector import CCXTConnector


def _build_connector_stub() -> CCXTConnector:
    c = CCXTConnector.__new__(CCXTConnector)
    c.exchange_id = "hyperliquid"
    c.quote_currency = "USDC"
    c.market_type = "swap"
    c.settlement_currency = "USDC"
    c.exchange = None
    c._ticker_cache = {}
    c._ticker_cache_time = 0.0
    c._ohlcv_cache = {}
    c._ohlcv_cache_time = {}
    c._consecutive_failures = 0
    c._rate_limit_hits = 0
    c._degraded_until_ts = 0.0
    c._last_degraded_log_ts = 0.0
    c._error_window = deque(maxlen=20)
    c._slow_warning_ts = {}
    c._rate_guard_enabled = True
    c._rate_guard_window_sec = 60
    c._rate_guard_429_escalate_hits = 2
    c._rate_guard_success_recovery = 3
    c._rate_guard_max_level = 3
    c._rate_guard_level = 0
    c._rate_guard_success_streak = 0
    c._rate_guard_429_times = deque(maxlen=500)
    c._rate_guard_last_change_ts = 0.0
    c._rate_guard_last_log_ts = 0.0
    c._endpoint_call_times = {
        ep: deque(maxlen=5000) for ep in CCXTConnector.RATE_GUARD_ENDPOINTS
    }
    c._rate_guard_budgets_per_min = {
        "ohlcv": 5,
        "orderbook": 5,
        "ticker_snapshot": 5,
        "batch_tickers": 2,
        "funding": 5,
        "top_symbols": 2,
    }
    return c


def test_rate_limit_failure_enables_degraded_mode():
    c = _build_connector_stub()
    c._record_api_failure(Exception("429 Too Many Requests"))
    assert c._is_degraded() is True
    assert c._rate_limit_hits >= 1


def test_fetch_ticker_uses_cache_while_degraded():
    c = _build_connector_stub()
    c._ticker_cache = {"BTC/USDC": {"symbol": "BTC/USDC", "last": 123.45}}
    c._degraded_until_ts = time.time() + 60
    ticker = c.fetch_ticker_snapshot("BTC/USDC")
    assert ticker["last"] == 123.45


def test_top_volume_uses_cached_ranking_while_degraded():
    c = _build_connector_stub()
    c._degraded_until_ts = time.time() + 60
    c._ticker_cache = {
        "BTC/USDC": {"quoteVolume": 2000.0},
        "ETH/USDC": {"quoteVolume": 1500.0},
        "DOGE/USDC": {"quoteVolume": 500.0},
    }
    top = c.fetch_top_symbols_by_volume(limit=2)
    assert top == ["BTC/USDC", "ETH/USDC"]


def test_rate_guard_escalates_level_on_repeated_429():
    c = _build_connector_stub()
    assert c._rate_guard_level == 0
    c._record_api_failure(Exception("429 Too Many Requests"))
    c._record_api_failure(Exception("429 Too Many Requests"))
    assert c._rate_guard_level >= 1


def test_rate_guard_recovers_after_success_streak():
    c = _build_connector_stub()
    c._rate_guard_level = 2
    c._rate_guard_429_times.clear()
    c._rate_guard_success_recovery = 2
    c._record_api_success()
    c._record_api_success()
    assert c._rate_guard_level == 1


def test_rate_guard_budget_blocks_ohlcv_calls():
    c = _build_connector_stub()
    c._rate_guard_budgets_per_min["ohlcv"] = 1
    c._endpoint_call_times["ohlcv"].append(time.time())

    class DummyExchange:
        def __init__(self):
            self.called = 0

        def fetch_ohlcv(self, *args, **kwargs):
            self.called += 1
            return [[1, 1, 1, 1, 1, 1]]

    c.exchange = DummyExchange()
    out = c.fetch_ohlcv("BTC/USDC", "15m", limit=50)
    assert out == []
    assert c.exchange.called == 0


def test_rate_guard_profile_disables_orderbook_at_high_level():
    c = _build_connector_stub()
    c._rate_guard_level = 2
    profile = c.get_rate_guard_profile()
    assert profile["allow_orderbook"] is False
