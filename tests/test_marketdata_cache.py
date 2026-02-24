import time

from src.core.definitions import MarketRegime, MarketState, TrendStrength, VolatilityLevel
from src.marketdata.cache import MarketDataCache


def _state(symbol: str = "BTC/USDC", price: float = 100.0) -> MarketState:
    return MarketState(
        symbol=symbol,
        market_regime=MarketRegime.BULL_TREND,
        volatility_level=VolatilityLevel.NORMAL,
        trend_strength=TrendStrength.MODERATE,
        time_of_day="12",
        trading_session="NY",
        day_type="WEEKDAY",
        week_phase="MID",
        time_remaining_days=10.0,
        distance_to_key_levels=1.0,
        current_price=price,
        rsi=55.0,
        atr=1.0,
        current_risk_state="SAFE",
        raw_timestamp="2026-02-23T00:00:00+00:00",
    )


def test_marketdata_cache_upsert_and_get():
    cache = MarketDataCache()
    cache.upsert("BTC/USDC", state=_state(), ticker={"last": 101.0}, source="test")

    st = cache.get_state("BTC/USDC", max_age_sec=60)
    tk = cache.get_ticker("BTC/USDC", max_age_sec=60)
    assert st is not None
    assert st.symbol == "BTC/USDC"
    assert tk is not None
    assert tk.get("last") == 101.0


def test_marketdata_cache_respects_age_limits():
    cache = MarketDataCache()
    cache.upsert("ETH/USDC", state=_state("ETH/USDC"), ticker={"last": 200.0}, source="test")
    time.sleep(0.02)
    assert cache.get_state("ETH/USDC", max_age_sec=0.0) is None
    assert cache.get_ticker("ETH/USDC", max_age_sec=0.0) is None


def test_marketdata_cache_health_snapshot():
    cache = MarketDataCache()
    cache.upsert("SOL/USDC", state=_state("SOL/USDC"), source="test")
    cache.upsert("SOL/USDC", ticker={"last": 150.0}, source="test")
    health = cache.snapshot_health()
    assert health["symbols"] == 1
    assert health["with_state"] == 1
    assert health["with_ticker"] == 1
    assert health["max_state_age_sec"] is not None
    assert health["max_ticker_age_sec"] is not None

