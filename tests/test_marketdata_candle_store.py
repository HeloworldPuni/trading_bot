from src.marketdata.candle_store import CandleStore


def test_candle_store_builds_1m_bars_from_ticks():
    store = CandleStore(max_1m_bars=200)
    base_ts = 1_700_000_400  # minute aligned

    store.ingest_tick("BTC/USDC", 100.0, base_ts + 1)
    store.ingest_tick("BTC/USDC", 105.0, base_ts + 20)
    store.ingest_tick("BTC/USDC", 99.0, base_ts + 40)
    # Cross minute to flush first bar.
    store.ingest_tick("BTC/USDC", 101.0, base_ts + 61)

    rows = store.get_recent_ohlcv("BTC/USDC", "1m", limit=10)
    assert len(rows) >= 2
    first = rows[-2]
    assert first[1] == 100.0  # open
    assert first[2] == 105.0  # high
    assert first[3] == 99.0   # low
    assert first[4] == 99.0   # close


def test_candle_store_aggregates_timeframes():
    store = CandleStore(max_1m_bars=500)
    base_ts = 1_700_000_400

    for i in range(8):
        # One price update per minute.
        store.ingest_tick("ETH/USDC", 2000.0 + i, base_ts + (i * 60) + 1)
    # Flush final minute bucket.
    store.ingest_tick("ETH/USDC", 2010.0, base_ts + (8 * 60) + 1)

    rows_5m = store.get_recent_ohlcv("ETH/USDC", "5m", limit=10)
    assert len(rows_5m) >= 1
    assert rows_5m[-1][1] > 0
    assert rows_5m[-1][2] >= rows_5m[-1][3]


def test_candle_store_symbols_with_min_bars():
    store = CandleStore(max_1m_bars=500)
    base_ts = 1_700_000_400

    for i in range(55):
        store.ingest_tick("SOL/USDC", 100.0 + i * 0.1, base_ts + (i * 60) + 1)
    store.ingest_tick("SOL/USDC", 120.0, base_ts + (56 * 60) + 1)

    count = store.symbols_with_min_bars(["SOL/USDC", "BTC/USDC"], "1m", min_bars=50)
    assert count == 1
