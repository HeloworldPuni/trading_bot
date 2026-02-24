from src.exchange.hyperliquid_stream import HyperliquidUserStream


def test_stream_dedupes_repeated_events():
    stream = HyperliquidUserStream(user_address="0xabc", testnet=True, stale_timeout_sec=60)
    event = {"channel": "userFills", "data": {"user": "0xabc", "fills": [{"hash": "h1", "tid": 1}]}}
    stream._on_event(event)
    stream._on_event(event)
    pulled = stream.pop_events(max_items=10)
    assert len(pulled) == 1
    assert pulled[0]["channel"] == "userFills"


def test_stream_pop_events_respects_limit():
    stream = HyperliquidUserStream(user_address="0xabc", testnet=True, stale_timeout_sec=60)
    for idx in range(5):
        stream._on_event({"channel": "orderUpdates", "data": {"oid": idx, "status": "open"}})
    pulled = stream.pop_events(max_items=3)
    assert len(pulled) == 3
    remaining = stream.pop_events(max_items=10)
    assert len(remaining) == 2
