from src.core.definitions import MarketRegime, MarketState, TrendStrength, VolatilityLevel
from src.marketdata.contracts import (
    build_market_input_snapshot,
    is_safe_state_signature,
    market_state_from_payload,
    sanitize_ticker_payload,
    validate_market_input_snapshot,
    validate_market_state,
)


def _valid_state(symbol: str = "BTC/USDC") -> MarketState:
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
        current_price=100.0,
        rsi=55.0,
        atr=1.5,
        current_risk_state="SAFE",
        raw_timestamp="2026-02-22T12:00:00+00:00",
    )


def test_sanitize_ticker_payload_coerces_last_from_close():
    out = sanitize_ticker_payload(
        exchange_symbol="BTC/USDC:USDC",
        normalized_symbol="BTC/USDC",
        ticker={"close": 101.25},
    )
    assert out["symbol"] == "BTC/USDC"
    assert out["_exchange_symbol"] == "BTC/USDC:USDC"
    assert out["last"] == 101.25


def test_validate_market_state_accepts_valid_state():
    ok, issues = validate_market_state(_valid_state(), expected_symbol="BTC/USDC")
    assert ok is True
    assert issues == []


def test_market_input_snapshot_rejects_safe_state_signature():
    state = _valid_state(symbol="ETH/USDC")
    state.current_risk_state = "DANGER"
    state.current_price = 0.0
    state.raw_timestamp = None
    state.atr = 0.0

    snapshot = build_market_input_snapshot(
        symbol="ETH/USDC",
        state=state,
        ticker={"last": None},
        current_price=None,
    )
    ok, issues = validate_market_input_snapshot(snapshot)
    assert ok is False
    assert any("DANGER" in reason for reason in issues)


def test_market_input_snapshot_accepts_valid_payload():
    state = _valid_state(symbol="SOL/USDC")
    snapshot = build_market_input_snapshot(
        symbol="SOL/USDC",
        state=state,
        ticker={"last": 100.2},
        current_price=100.2,
    )
    ok, issues = validate_market_input_snapshot(snapshot, max_price_divergence_pct=10.0)
    assert ok is True
    assert issues == []


def test_safe_state_signature_detection():
    state = _valid_state("XRP/USDC")
    assert is_safe_state_signature(state) is False
    state.current_risk_state = "DANGER"
    state.current_price = 0.0
    state.atr = 0.0
    state.raw_timestamp = None
    state.market_regime = MarketRegime.SIDEWAYS_LOW_VOL
    assert is_safe_state_signature(state) is True


def test_market_state_from_payload_rebuilds_state():
    payload = {
        "symbol": "BTC/USDC",
        "market_regime": "BULL_TREND",
        "volatility_level": "NORMAL",
        "trend_strength": "MODERATE",
        "time_of_day": "12",
        "trading_session": "NY",
        "day_type": "WEEKDAY",
        "week_phase": "MID",
        "time_remaining_days": 12.0,
        "distance_to_key_levels": 1.0,
        "current_price": 123.45,
        "rsi": 56.0,
        "atr": 1.2,
        "current_risk_state": "SAFE",
        "raw_timestamp": "2026-02-23T00:00:00+00:00",
    }
    state = market_state_from_payload(payload)
    assert state is not None
    assert state.symbol == "BTC/USDC"
    assert state.current_price == 123.45
    assert state.market_regime == MarketRegime.BULL_TREND
