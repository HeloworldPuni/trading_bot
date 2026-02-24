from src.exchange.hyperliquid_reconcile import HyperliquidRealtimeState


def test_seed_positions_normalizes_and_drops_zero():
    state = HyperliquidRealtimeState()
    state.seed_positions({"btc": 0.25, "eth": 0.0, "SOL": -1.5})
    snap = state.snapshot_position_sizes()
    assert snap == {"BTC": 0.25, "SOL": -1.5}
    assert state.position_state_ready is True


def test_userfills_apply_position_transitions():
    state = HyperliquidRealtimeState()
    events = [
        {
            "ts": 1.0,
            "channel": "userFills",
            "data": {
                "fills": [
                    {"coin": "BTC", "side": "buy", "sz": "0.10", "startPosition": "0", "time": 1000, "hash": "h1", "tid": 1},
                    {"coin": "BTC", "side": "sell", "sz": "0.04", "startPosition": "0.10", "time": 1001, "hash": "h2", "tid": 2},
                    {"coin": "ETH", "side": "A", "sz": "1.0", "startPosition": "0", "time": 1002, "hash": "h3", "tid": 3},
                ]
            },
        }
    ]
    stats = state.apply_events(events)
    snap = state.snapshot_position_sizes()
    assert stats["fills_applied"] == 3
    assert round(snap["BTC"], 8) == 0.06
    assert round(snap["ETH"], 8) == -1.0


def test_fill_dedupes_between_user_and_userfills_channels():
    state = HyperliquidRealtimeState()
    fill = {"coin": "BTC", "side": "buy", "sz": "0.2", "startPosition": "0", "time": 1000, "hash": "h1", "tid": 7}
    events = [
        {"ts": 1.0, "channel": "userFills", "data": {"fills": [fill]}},
        {"ts": 1.1, "channel": "user", "data": {"fills": [fill]}},
    ]
    stats = state.apply_events(events)
    snap = state.snapshot_position_sizes()
    assert stats["fills_seen"] == 2
    assert stats["fills_applied"] == 1
    assert round(snap["BTC"], 8) == 0.2


def test_older_fill_update_is_ignored():
    state = HyperliquidRealtimeState()
    events = [
        {"ts": 1.0, "channel": "userFills", "data": {"fills": [{"coin": "BTC", "side": "buy", "sz": "1", "startPosition": "0", "time": 200, "hash": "h2", "tid": 2}]}},
        {"ts": 1.1, "channel": "userFills", "data": {"fills": [{"coin": "BTC", "side": "buy", "sz": "2", "startPosition": "0", "time": 100, "hash": "h1", "tid": 1}]}},
    ]
    state.apply_events(events)
    snap = state.snapshot_position_sizes()
    assert round(snap["BTC"], 8) == 1.0


def test_order_updates_tracking_and_status_helpers():
    state = HyperliquidRealtimeState()
    events = [
        {
            "ts": 2.0,
            "channel": "orderUpdates",
            "data": [
                {
                    "order": {
                        "coin": "BTC",
                        "side": "B",
                        "limitPx": "50000",
                        "sz": "0.1",
                        "origSz": "0.1",
                        "oid": 11,
                        "timestamp": 1000,
                        "cloid": "abc",
                    },
                    "status": "open",
                    "statusTimestamp": 1001,
                },
                {
                    "order": {
                        "coin": "BTC",
                        "side": "B",
                        "limitPx": "50000",
                        "sz": "0.1",
                        "origSz": "0.1",
                        "oid": 12,
                        "timestamp": 1000,
                        "cloid": "def",
                    },
                    "status": "rejected",
                    "statusTimestamp": 1002,
                },
            ],
        }
    ]
    stats = state.apply_events(events)
    assert stats["order_updates_applied"] == 2

    open_order = state.get_order(11)
    rejected_order = state.get_order(12)
    assert open_order is not None and open_order["status"] == "open"
    assert rejected_order is not None and rejected_order["status"] == "rejected"
    assert HyperliquidRealtimeState.is_pending_order_status(open_order["status"]) is True
    assert HyperliquidRealtimeState.is_reject_or_cancel_status(rejected_order["status"]) is True
    assert HyperliquidRealtimeState.is_terminal_order_status("filled") is True
