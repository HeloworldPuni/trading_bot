import time

from src.exchange.hyperliquid_public_stream import HyperliquidPublicStream


def test_public_stream_parses_allmids_payload():
    stream = HyperliquidPublicStream(quote_currency="USDC", testnet=True, stale_timeout_sec=30)
    stream._on_event(
        {
            "channel": "allMids",
            "data": {"mids": {"BTC": "100000.5", "ETH": "2800.25", "BAD": "x"}},
        }
    )

    snap = stream.snapshot_tickers(max_age_sec=60)
    assert "BTC/USDC" in snap
    assert "ETH/USDC" in snap
    assert snap["BTC/USDC"]["last"] == 100000.5
    assert snap["BTC/USDC"]["_price_source"] == "hl_ws_mid"


def test_public_stream_health_flag_uses_staleness():
    stream = HyperliquidPublicStream(quote_currency="USDC", testnet=True, stale_timeout_sec=5)
    stream._running = True
    stream._last_event_ts = time.time()
    assert stream.is_healthy() is True
    stream._last_event_ts = time.time() - 10
    assert stream.is_healthy() is False


def test_public_stream_snapshot_age_filter():
    stream = HyperliquidPublicStream(quote_currency="USDC", testnet=True, stale_timeout_sec=30)
    stream._on_event({"channel": "allMids", "data": {"mids": {"SOL": "150.0"}}})
    assert "SOL/USDC" in stream.snapshot_tickers(max_age_sec=60)
    # Very strict age filter should drop stale rows.
    time.sleep(0.02)
    assert "SOL/USDC" not in stream.snapshot_tickers(max_age_sec=0.0)


def test_public_stream_pop_price_updates():
    stream = HyperliquidPublicStream(quote_currency="USDC", testnet=True, stale_timeout_sec=30)
    stream._on_event({"channel": "allMids", "data": {"mids": {"BTC": "100000", "ETH": "2500"}}})

    updates = stream.pop_price_updates(max_items=10)
    symbols = {u["symbol"] for u in updates}
    assert "BTC/USDC" in symbols
    assert "ETH/USDC" in symbols
    assert all(float(u["price"]) > 0 for u in updates)
    # Queue should be drained after pop.
    assert stream.pop_price_updates(max_items=10) == []
