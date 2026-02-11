import math
from typing import Any, List, Tuple


def validate_ohlcv(ohlcv: List[List[Any]], min_len: int = 50) -> Tuple[bool, List[str]]:
    """
    Basic OHLCV sanity checks.
    Returns (ok, issues).
    """
    issues: List[str] = []

    if not ohlcv:
        return False, ["Empty OHLCV data"]

    if min_len and len(ohlcv) < min_len:
        return False, [f"Insufficient candles: {len(ohlcv)} < {min_len}"]

    prev_ts = None
    for i, row in enumerate(ohlcv):
        if row is None or len(row) < 6:
            issues.append(f"Row {i}: invalid length")
            continue

        ts, op, hi, lo, cl, vol = row[:6]

        try:
            ts = int(ts)
            op = float(op)
            hi = float(hi)
            lo = float(lo)
            cl = float(cl)
            vol = float(vol)
        except (TypeError, ValueError):
            issues.append(f"Row {i}: non-numeric values")
            continue

        if prev_ts is not None and ts <= prev_ts:
            issues.append(f"Row {i}: non-monotonic timestamp")
        prev_ts = ts

        if any(math.isnan(x) or math.isinf(x) for x in [op, hi, lo, cl, vol]):
            issues.append(f"Row {i}: NaN/Inf values")
            continue

        if op <= 0 or hi <= 0 or lo <= 0 or cl <= 0:
            issues.append(f"Row {i}: non-positive price")

        if lo > hi:
            issues.append(f"Row {i}: low > high")

        if hi < max(op, cl) or lo > min(op, cl):
            issues.append(f"Row {i}: OHLC inconsistent")

        if vol < 0:
            issues.append(f"Row {i}: negative volume")

    return len(issues) == 0, issues


def validate_orderbook(orderbook_rows: List[List[Any]], min_len: int = 1) -> Tuple[bool, List[str]]:
    """
    Basic orderbook snapshot checks.
    Expects rows like:
    [timestamp, bid1_p, bid1_v, ask1_p, ask1_v, ...]
    """
    issues: List[str] = []

    if not orderbook_rows:
        return False, ["Empty orderbook data"]
    if len(orderbook_rows) < min_len:
        return False, [f"Insufficient orderbook rows: {len(orderbook_rows)} < {min_len}"]

    prev_ts = None
    for i, row in enumerate(orderbook_rows):
        if row is None or len(row) < 5:
            issues.append(f"Row {i}: invalid length")
            continue
        try:
            ts = int(float(row[0]))
            bid = float(row[1])
            ask = float(row[3])
        except (TypeError, ValueError):
            issues.append(f"Row {i}: invalid numeric values")
            continue

        if prev_ts is not None and ts < prev_ts:
            issues.append(f"Row {i}: non-monotonic timestamp")
        prev_ts = ts

        if bid <= 0 or ask <= 0:
            issues.append(f"Row {i}: non-positive best price")
        if bid >= ask:
            issues.append(f"Row {i}: crossed book (bid >= ask)")

    return len(issues) == 0, issues
