from src.core.definitions import ActionDirection
from src.execution.hyperliquid_live import HyperliquidLiveExecutor


class _FakeClient:
    def __init__(self):
        self.calls = []

    def place_order(self, request):
        self.calls.append(request)
        return {
            "ok": True,
            "order_status": "filled",
            "oid": 123,
            "fill_price": 100.5,
            "requested_size": request.size,
        }

    def fetch_position_sizes(self):
        return {"BTC": 0.25}


def test_place_entry_maps_direction_and_qty():
    client = _FakeClient()
    executor = HyperliquidLiveExecutor(client)

    resp = executor.place_entry(
        symbol="BTC/USDC",
        direction=ActionDirection.LONG,
        size_usd=1000.0,
        reference_price=100.0,
        decision_id="dec-1",
    )

    assert resp["ok"] is True
    assert abs(resp["requested_qty"] - 10.0) < 1e-9
    assert client.calls[0].side == "BUY"
    assert client.calls[0].client_order_id == "dec-1"


def test_place_exit_sets_reduce_only_and_opposite_side():
    client = _FakeClient()
    executor = HyperliquidLiveExecutor(client)
    position = {
        "symbol": "ETH/USDC",
        "direction": "SHORT",
        "size_qty": 2.5,
        "decision_id": "abc",
    }
    resp = executor.place_exit(position, current_price=2000.0, reason="TP")
    assert resp["ok"] is True
    assert client.calls[0].side == "BUY"
    assert client.calls[0].reduce_only is True


def test_fetch_exchange_position_sizes_passthrough():
    client = _FakeClient()
    executor = HyperliquidLiveExecutor(client)
    assert executor.fetch_exchange_position_sizes()["BTC"] == 0.25
