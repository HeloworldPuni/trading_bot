from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

from src.core.definitions import MarketRegime, MarketState, TrendStrength, VolatilityLevel


VALID_RISK_STATES = {"SAFE", "DANGER"}
VALID_PRICE_SOURCES = {"ticker", "ohlcv_fallback", "portfolio_state", "hl_ws_mid", "unknown"}


def _safe_float(value: Any) -> Optional[float]:
    try:
        num = float(value)
    except (TypeError, ValueError):
        return None
    if num != num:  # NaN guard
        return None
    return num


def extract_ticker_last_price(ticker: Dict[str, Any]) -> Optional[float]:
    """
    Best-effort extraction of a usable last price from heterogeneous exchange payloads.
    Returns None when no positive numeric price is available.
    """
    if not isinstance(ticker, dict):
        return None

    direct_keys = (
        "last",
        "close",
        "mark",
        "markPrice",
        "indexPrice",
        "price",
    )
    for key in direct_keys:
        num = _safe_float(ticker.get(key))
        if num is not None and num > 0.0:
            return num

    bid = _safe_float(ticker.get("bid"))
    ask = _safe_float(ticker.get("ask"))
    if bid is not None and ask is not None and bid > 0.0 and ask > 0.0:
        mid = (bid + ask) / 2.0
        if mid > 0.0:
            return mid

    info = ticker.get("info")
    if isinstance(info, dict):
        for key in ("markPx", "markPrice", "indexPx", "price", "last", "close"):
            num = _safe_float(info.get(key))
            if num is not None and num > 0.0:
                return num

    return None


def sanitize_ticker_payload(
    exchange_symbol: str,
    normalized_symbol: str,
    ticker: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Normalize ticker payload into a stable runtime contract.
    Guarantees:
    - `symbol` and `_exchange_symbol` are set
    - `last` is populated only when a positive price exists
    """
    row: Dict[str, Any] = dict(ticker or {})
    row["_exchange_symbol"] = exchange_symbol
    row["symbol"] = normalized_symbol

    last = extract_ticker_last_price(row)
    if last is not None and last > 0.0:
        row["last"] = last
    else:
        row.pop("last", None)
    return row


def validate_market_state(state: MarketState, expected_symbol: str) -> Tuple[bool, List[str]]:
    """
    Validate MarketState invariants before entering decision engine.
    """
    reasons: List[str] = []
    if state is None:
        return False, ["state is None"]

    state_symbol = str(getattr(state, "symbol", "") or "").strip()
    expected = str(expected_symbol or "").strip()
    if not state_symbol:
        reasons.append("state.symbol missing")
    elif expected and state_symbol != expected:
        reasons.append(f"state.symbol mismatch ({state_symbol} != {expected})")

    price = _safe_float(getattr(state, "current_price", None))
    if price is None or price < 0.0:
        reasons.append("state.current_price invalid")

    rsi = _safe_float(getattr(state, "rsi", None))
    if rsi is None or rsi < 0.0 or rsi > 100.0:
        reasons.append("state.rsi out of bounds")

    atr = _safe_float(getattr(state, "atr", None))
    if atr is None or atr < 0.0:
        reasons.append("state.atr invalid")

    risk_state = str(getattr(state, "current_risk_state", "") or "").upper()
    if risk_state and risk_state not in VALID_RISK_STATES:
        reasons.append(f"state.current_risk_state invalid ({risk_state})")

    return len(reasons) == 0, reasons


def is_safe_state_signature(state: Optional[MarketState]) -> bool:
    """
    Detect feeder SAFE-state fallback signature.
    """
    if state is None:
        return False
    risk_state = str(getattr(state, "current_risk_state", "") or "").upper()
    price = _safe_float(getattr(state, "current_price", None))
    atr = _safe_float(getattr(state, "atr", None))
    raw_ts = getattr(state, "raw_timestamp", None)
    regime = str(getattr(getattr(state, "market_regime", None), "value", "") or "")
    return (
        risk_state == "DANGER"
        and (price is None or price <= 0.0)
        and (atr is None or atr <= 0.0)
        and (raw_ts is None or str(raw_ts).strip() == "")
        and regime == "SIDEWAYS_LOW_VOL"
    )


def _enum_or_default(enum_cls, value: Any, default):
    try:
        return enum_cls(str(value))
    except Exception:
        return default


def market_state_from_payload(payload: Dict[str, Any]) -> Optional[MarketState]:
    """
    Best-effort reconstruction of MarketState from persisted market_state payload.
    Returns None on hard parse failures.
    """
    if not isinstance(payload, dict):
        return None

    regime = _enum_or_default(
        MarketRegime,
        payload.get("market_regime"),
        MarketRegime.SIDEWAYS_LOW_VOL,
    )
    vol = _enum_or_default(
        VolatilityLevel,
        payload.get("volatility_level"),
        VolatilityLevel.NORMAL,
    )
    strength = _enum_or_default(
        TrendStrength,
        payload.get("trend_strength"),
        TrendStrength.WEAK,
    )

    symbol = str(payload.get("symbol") or "").strip() or "BTC/USDT"
    rsi = _safe_float(payload.get("rsi"))
    atr = _safe_float(payload.get("atr"))
    current_price = _safe_float(payload.get("current_price"))

    try:
        return MarketState(
            symbol=symbol,
            market_regime=regime,
            volatility_level=vol,
            trend_strength=strength,
            time_of_day=str(payload.get("time_of_day") or "DEAD_ZONE"),
            trading_session=str(payload.get("trading_session") or "ASIA"),
            day_type=str(payload.get("day_type") or "WEEKDAY"),
            week_phase=str(payload.get("week_phase") or "MID"),
            time_remaining_days=_safe_float(payload.get("time_remaining_days")) or 0.0,
            distance_to_key_levels=_safe_float(payload.get("distance_to_key_levels")) or 0.0,
            current_price=current_price or 0.0,
            rsi=rsi if rsi is not None else 50.0,
            trend_spread=_safe_float(payload.get("trend_spread")) or 0.0,
            dist_to_high=_safe_float(payload.get("dist_to_high")) or 0.0,
            dist_to_low=_safe_float(payload.get("dist_to_low")) or 0.0,
            macd=_safe_float(payload.get("macd")) or 0.0,
            macd_signal=_safe_float(payload.get("macd_signal")) or 0.0,
            macd_hist=_safe_float(payload.get("macd_hist")) or 0.0,
            bb_upper=_safe_float(payload.get("bb_upper")) or 0.0,
            bb_lower=_safe_float(payload.get("bb_lower")) or 0.0,
            bb_mid=_safe_float(payload.get("bb_mid")) or 0.0,
            atr=atr if atr is not None else 0.0,
            volume_delta=_safe_float(payload.get("volume_delta")) or 0.0,
            spread_pct=_safe_float(payload.get("spread_pct")) or 0.0,
            body_pct=_safe_float(payload.get("body_pct")) or 0.0,
            gap_pct=_safe_float(payload.get("gap_pct")) or 0.0,
            volume_zscore=_safe_float(payload.get("volume_zscore")) or 0.0,
            liquidity_proxy=_safe_float(payload.get("liquidity_proxy")) or 0.0,
            funding_rate=_safe_float(payload.get("funding_rate")) or 0.0,
            funding_extreme=bool(payload.get("funding_extreme", False)),
            raw_timestamp=payload.get("raw_timestamp"),
            current_risk_state=str(payload.get("current_risk_state") or "SAFE"),
            current_drawdown_percent=_safe_float(payload.get("current_drawdown_percent")) or 0.0,
            current_open_positions=int(_safe_float(payload.get("current_open_positions")) or 0),
            regime_confidence=_safe_float(payload.get("regime_confidence")) or 1.0,
            regime_stable=bool(payload.get("regime_stable", True)),
            momentum_shift_score=_safe_float(payload.get("momentum_shift_score")) or 0.0,
            htf_trend_spread=_safe_float(payload.get("htf_trend_spread")) or 0.0,
            htf_rsi=_safe_float(payload.get("htf_rsi")) or 50.0,
            htf_atr=_safe_float(payload.get("htf_atr")) or 0.0,
        )
    except Exception:
        return None


def build_market_input_snapshot(
    symbol: str,
    state: MarketState,
    ticker: Optional[Dict[str, Any]],
    current_price: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Build normalized market-input envelope used by runtime validation gates.
    """
    ticker = ticker or {}
    px = _safe_float(current_price)
    if px is None or px <= 0.0:
        px = _safe_float(ticker.get("last"))

    state_price = _safe_float(getattr(state, "current_price", None))
    price_source = str(ticker.get("_price_source") or "ticker")

    return {
        "schema_version": "market_input_v1",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "symbol": symbol,
        "state_symbol": str(getattr(state, "symbol", "") or ""),
        "current_price": px,
        "state_current_price": state_price,
        "price_source": price_source,
        "market_regime": str(getattr(getattr(state, "market_regime", None), "value", "")),
        "risk_state": str(getattr(state, "current_risk_state", "") or "").upper(),
        "rsi": _safe_float(getattr(state, "rsi", None)),
        "atr": _safe_float(getattr(state, "atr", None)),
        "raw_timestamp": getattr(state, "raw_timestamp", None),
    }


def validate_market_input_snapshot(
    snapshot: Dict[str, Any],
    max_price_divergence_pct: float = 5.0,
) -> Tuple[bool, List[str]]:
    """
    Validate runtime market-input snapshot.
    Reject path is safe: caller should skip trading that symbol for the cycle.
    """
    reasons: List[str] = []
    if not isinstance(snapshot, dict):
        return False, ["snapshot is not a dict"]

    symbol = str(snapshot.get("symbol") or "").strip()
    if not symbol or "/" not in symbol:
        reasons.append("symbol missing or malformed")

    state_symbol = str(snapshot.get("state_symbol") or "").strip()
    if state_symbol and symbol and state_symbol != symbol:
        reasons.append(f"state_symbol mismatch ({state_symbol} != {symbol})")

    price = _safe_float(snapshot.get("current_price"))
    if price is None or price <= 0.0:
        reasons.append("current_price missing or non-positive")

    price_source = str(snapshot.get("price_source") or "unknown")
    if price_source not in VALID_PRICE_SOURCES:
        reasons.append(f"price_source invalid ({price_source})")

    rsi = _safe_float(snapshot.get("rsi"))
    if rsi is None or rsi < 0.0 or rsi > 100.0:
        reasons.append("rsi out of bounds")

    atr = _safe_float(snapshot.get("atr"))
    if atr is None or atr < 0.0:
        reasons.append("atr invalid")

    risk_state = str(snapshot.get("risk_state") or "").upper()
    if risk_state and risk_state not in VALID_RISK_STATES:
        reasons.append(f"risk_state invalid ({risk_state})")
    if risk_state == "DANGER":
        reasons.append("risk_state DANGER")

    regime = str(snapshot.get("market_regime") or "").strip()
    if not regime:
        reasons.append("market_regime missing")

    ts = str(snapshot.get("timestamp_utc") or "").strip()
    if ts:
        try:
            datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except ValueError:
            reasons.append("timestamp_utc invalid")

    state_px = _safe_float(snapshot.get("state_current_price"))
    if (
        state_px is not None
        and state_px > 0.0
        and price is not None
        and price > 0.0
        and max_price_divergence_pct > 0
    ):
        divergence = abs(price - state_px) / state_px * 100.0
        if divergence > max_price_divergence_pct:
            reasons.append(
                f"price divergence too high ({divergence:.2f}% > {max_price_divergence_pct:.2f}%)"
            )

    return len(reasons) == 0, reasons
