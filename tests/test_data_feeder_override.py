from src.data.feeder import LiveFeeder


def _ohlcv_rows(count: int = 60, start_ts: int = 1_700_000_000_000):
    rows = []
    px = 100.0
    for i in range(count):
        ts = start_ts + (i * 60_000)
        op = px
        hi = px + 1.0
        lo = px - 1.0
        cl = px + 0.2
        vol = 1000.0 + i
        rows.append([ts, op, hi, lo, cl, vol])
        px += 0.1
    return rows


class _DummyConnector:
    def __init__(self, rows):
        self.rows = rows
        self.fetch_ohlcv_calls = 0

    def fetch_ohlcv(self, symbol, timeframe, limit=200):
        self.fetch_ohlcv_calls += 1
        return list(self.rows[-limit:])

    def fetch_funding_rate(self, symbol):
        return 0.0


def test_feeder_uses_ohlcv_override_without_rest_fetch():
    rows = _ohlcv_rows(70)
    connector = _DummyConnector(rows=rows)
    feeder = LiveFeeder(connector)

    state = feeder.get_current_state("BTC/USDC", open_positions=0, ohlcv_override=rows)
    assert state.symbol == "BTC/USDC"
    assert state.current_price > 0
    assert connector.fetch_ohlcv_calls == 0


def test_feeder_falls_back_to_rest_when_override_is_insufficient():
    rows = _ohlcv_rows(70)
    connector = _DummyConnector(rows=rows)
    feeder = LiveFeeder(connector)

    state = feeder.get_current_state("ETH/USDC", open_positions=1, ohlcv_override=rows[:10])
    assert state.symbol == "ETH/USDC"
    assert state.current_open_positions == 1
    assert connector.fetch_ohlcv_calls >= 1
