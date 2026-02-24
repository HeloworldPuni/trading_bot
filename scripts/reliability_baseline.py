import argparse
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.config import Config


LOCAL_TZ = datetime.now().astimezone().tzinfo or timezone.utc


def _now_utc() -> datetime:
    return datetime.now(timezone.utc)


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _ratio(num: float, den: float) -> Optional[float]:
    if den <= 0:
        return None
    return float(num) / float(den)


def _parse_iso_utc(raw: Any) -> Optional[datetime]:
    if not raw:
        return None
    text = str(raw).strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


LOG_PREFIX_RE = re.compile(r"^(?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - ")
COOLDOWN_RE = re.compile(r"Entering cooldown (?P<seconds>\d+)s")
ACTIVE_POS_RE = re.compile(r"Active:\s*(?P<count>\d+)\s*positions")
SCAN_COINS_RE = re.compile(r"Scanning\s+(?P<count>\d+)\s+coins")


def _parse_log_ts_utc(line: str) -> Optional[datetime]:
    m = LOG_PREFIX_RE.match(line)
    if not m:
        return None
    try:
        local_dt = datetime.strptime(m.group("ts"), "%Y-%m-%d %H:%M:%S,%f")
    except ValueError:
        return None
    return local_dt.replace(tzinfo=LOCAL_TZ).astimezone(timezone.utc)


def _percentile(values: List[float], p: float) -> Optional[float]:
    if not values:
        return None
    if p <= 0:
        return float(min(values))
    if p >= 100:
        return float(max(values))
    vals = sorted(float(v) for v in values)
    k = (len(vals) - 1) * (p / 100.0)
    f = int(k)
    c = min(f + 1, len(vals) - 1)
    if f == c:
        return vals[f]
    return vals[f] + (vals[c] - vals[f]) * (k - f)


def _is_safe_state_signature(state: Dict[str, Any]) -> bool:
    if not isinstance(state, dict):
        return False
    risk = str(state.get("current_risk_state", "")).upper()
    raw_ts = state.get("raw_timestamp")
    price = _safe_float(state.get("current_price"))
    atr = _safe_float(state.get("atr"))
    return risk == "DANGER" and price <= 0.0 and not raw_ts and atr <= 0.0


def collect_experience_metrics(path: str, window_start: datetime) -> Dict[str, Any]:
    metrics: Dict[str, Any] = {
        "path": path,
        "exists": os.path.exists(path),
        "lines_scanned": 0,
        "records_in_window": 0,
        "malformed_lines": 0,
        "resolved_records": 0,
        "unresolved_records": 0,
        "wait_records": 0,
        "non_wait_records": 0,
        "price_available_records": 0,
        "price_missing_records": 0,
        "safe_state_records": 0,
        "symbols_seen": 0,
        "top_symbols": [],
        "price_available_rate": None,
        "ohlcv_valid_rate": None,
        "safe_state_rate": None,
    }
    if not metrics["exists"]:
        return metrics

    symbol_counter: Counter = Counter()
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            metrics["lines_scanned"] += 1
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                metrics["malformed_lines"] += 1
                continue

            ts = _parse_iso_utc(rec.get("timestamp"))
            if not ts or ts < window_start:
                continue

            metrics["records_in_window"] += 1
            state = rec.get("market_state") if isinstance(rec.get("market_state"), dict) else {}
            action = rec.get("action_taken") if isinstance(rec.get("action_taken"), dict) else {}

            symbol = str(state.get("symbol") or "").strip()
            if symbol:
                symbol_counter[symbol] += 1

            strategy = str(action.get("strategy", "UNKNOWN")).upper()
            if strategy == "WAIT":
                metrics["wait_records"] += 1
            else:
                metrics["non_wait_records"] += 1

            if bool(rec.get("resolved")):
                metrics["resolved_records"] += 1
            else:
                metrics["unresolved_records"] += 1

            px = _safe_float(state.get("current_price"))
            if px > 0.0:
                metrics["price_available_records"] += 1
            else:
                metrics["price_missing_records"] += 1

            if _is_safe_state_signature(state):
                metrics["safe_state_records"] += 1

    metrics["symbols_seen"] = len(symbol_counter)
    metrics["top_symbols"] = symbol_counter.most_common(15)
    metrics["price_available_rate"] = _ratio(
        metrics["price_available_records"], metrics["records_in_window"]
    )
    safe_state_rate = _ratio(metrics["safe_state_records"], metrics["records_in_window"])
    metrics["safe_state_rate"] = safe_state_rate
    metrics["ohlcv_valid_rate"] = None if safe_state_rate is None else (1.0 - safe_state_rate)
    return metrics


def collect_decision_metrics(path: str, window_start: datetime) -> Dict[str, Any]:
    metrics: Dict[str, Any] = {
        "path": path,
        "exists": os.path.exists(path),
        "lines_scanned": 0,
        "records_in_window": 0,
        "malformed_lines": 0,
        "unique_decisions_in_window": 0,
        "duplicate_decision_records": 0,
        "wait_actions": 0,
        "non_wait_actions": 0,
        "top_block_reasons": [],
        "top_symbols": [],
    }
    if not metrics["exists"]:
        return metrics

    seen_ids = set()
    reason_counter: Counter = Counter()
    symbol_counter: Counter = Counter()
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            metrics["lines_scanned"] += 1
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                metrics["malformed_lines"] += 1
                continue

            ts = _parse_iso_utc(rec.get("timestamp"))
            if not ts or ts < window_start:
                continue

            metrics["records_in_window"] += 1
            decision_id = str(rec.get("decision_id") or "").strip()
            if decision_id:
                if decision_id in seen_ids:
                    metrics["duplicate_decision_records"] += 1
                else:
                    seen_ids.add(decision_id)

            symbol = str(rec.get("symbol") or "").strip()
            if symbol:
                symbol_counter[symbol] += 1

            action = str(rec.get("action", "WAIT")).upper()
            if action == "WAIT":
                metrics["wait_actions"] += 1
            else:
                metrics["non_wait_actions"] += 1

            blocked_reasons = rec.get("blocked_reasons")
            if isinstance(blocked_reasons, list):
                for reason in blocked_reasons:
                    reason_counter[str(reason)] += 1

    metrics["unique_decisions_in_window"] = len(seen_ids)
    metrics["top_block_reasons"] = reason_counter.most_common(10)
    metrics["top_symbols"] = symbol_counter.most_common(15)
    return metrics


def collect_runtime_log_metrics(path: str, window_start: datetime) -> Dict[str, Any]:
    metrics: Dict[str, Any] = {
        "path": path,
        "exists": os.path.exists(path),
        "lines_scanned": 0,
        "lines_in_window": 0,
        "rate_limit_hits": 0,
        "api_429_errors": 0,
        "ticker_last_unavailable": 0,
        "insufficient_ohlcv": 0,
        "data_quality_issue_lines": 0,
        "exchange_cooldown_lines": 0,
        "batch_ticker_rate_limited": 0,
        "slow_api_warnings": 0,
        "max_cooldown_seconds": 0,
        "startup_events": 0,
        "startup_ready_samples": 0,
        "startup_ready_seconds_p50": None,
        "startup_ready_seconds_p95": None,
        "last_restored_active_positions": None,
        "last_scan_universe_size": None,
    }
    if not metrics["exists"]:
        return metrics

    current_start_ts: Optional[datetime] = None
    startup_durations: List[float] = []

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            metrics["lines_scanned"] += 1
            ts = _parse_log_ts_utc(line)
            if not ts or ts < window_start:
                continue

            metrics["lines_in_window"] += 1

            if "Starting Adaptive Trading Assistant" in line:
                current_start_ts = ts
                metrics["startup_events"] += 1
            elif "Components initialized." in line and current_start_ts:
                startup_durations.append((ts - current_start_ts).total_seconds())
                current_start_ts = None

            if "Rate limit hit on" in line:
                metrics["rate_limit_hits"] += 1
                m = COOLDOWN_RE.search(line)
                if m:
                    seconds = int(m.group("seconds"))
                    if seconds > metrics["max_cooldown_seconds"]:
                        metrics["max_cooldown_seconds"] = seconds
            if "429 Too Many Requests" in line:
                metrics["api_429_errors"] += 1
            if "ticker last price unavailable" in line:
                metrics["ticker_last_unavailable"] += 1
            if "insufficient_ohlcv" in line:
                metrics["insufficient_ohlcv"] += 1
            if "Data quality issue for" in line:
                metrics["data_quality_issue_lines"] += 1
            if "temporary cooldown" in line:
                metrics["exchange_cooldown_lines"] += 1
            if "Batch ticker refresh rate-limited" in line:
                metrics["batch_ticker_rate_limited"] += 1
            if "SLOW API:" in line:
                metrics["slow_api_warnings"] += 1

            active_match = ACTIVE_POS_RE.search(line)
            if active_match:
                metrics["last_restored_active_positions"] = int(active_match.group("count"))
            scan_match = SCAN_COINS_RE.search(line)
            if scan_match:
                metrics["last_scan_universe_size"] = int(scan_match.group("count"))

    metrics["startup_ready_samples"] = len(startup_durations)
    metrics["startup_ready_seconds_p50"] = _percentile(startup_durations, 50)
    metrics["startup_ready_seconds_p95"] = _percentile(startup_durations, 95)
    return metrics


def evaluate_slos(metrics: Dict[str, Any]) -> Dict[str, Any]:
    experience = metrics.get("experience", {})
    decisions = metrics.get("decision_audit", {})
    runtime = metrics.get("runtime_log", {})

    decisions_den = decisions.get("unique_decisions_in_window") or 0
    if decisions_den <= 0:
        decisions_den = experience.get("records_in_window") or 0

    rate_limit_hits_per_1k = None
    ticker_unavailable_per_1k = None
    if decisions_den > 0:
        rate_limit_hits_per_1k = (runtime.get("rate_limit_hits", 0) / decisions_den) * 1000.0
        ticker_unavailable_per_1k = (runtime.get("ticker_last_unavailable", 0) / decisions_den) * 1000.0

    checks = [
        {
            "name": "price_available_rate",
            "target": 0.995,
            "operator": ">=",
            "value": experience.get("price_available_rate"),
        },
        {
            "name": "ohlcv_valid_rate",
            "target": 0.99,
            "operator": ">=",
            "value": experience.get("ohlcv_valid_rate"),
        },
        {
            "name": "rate_limit_hits_per_1000_decisions",
            "target": 1.0,
            "operator": "<=",
            "value": rate_limit_hits_per_1k,
        },
        {
            "name": "ticker_unavailable_per_1000_decisions",
            "target": 1.0,
            "operator": "<=",
            "value": ticker_unavailable_per_1k,
        },
        {
            "name": "startup_ready_seconds_p95",
            "target": 180.0,
            "operator": "<=",
            "value": runtime.get("startup_ready_seconds_p95"),
        },
    ]

    def _status(value: Optional[float], target: float, op: str) -> str:
        if value is None:
            return "UNKNOWN"
        if op == ">=":
            return "PASS" if value >= target else "FAIL"
        return "PASS" if value <= target else "FAIL"

    for check in checks:
        check["status"] = _status(check["value"], check["target"], check["operator"])

    statuses = [c["status"] for c in checks]
    if any(s == "FAIL" for s in statuses):
        overall = "FAIL"
    elif all(s == "PASS" for s in statuses):
        overall = "PASS"
    else:
        overall = "UNKNOWN"

    return {
        "overall_status": overall,
        "decisions_denominator": decisions_den,
        "checks": checks,
    }


def build_report(
    hours: int,
    experience_path: str,
    decision_path: str,
    runtime_log_path: str,
) -> Dict[str, Any]:
    now_utc = _now_utc()
    window_start = now_utc - timedelta(hours=hours)

    experience = collect_experience_metrics(experience_path, window_start)
    decision_audit = collect_decision_metrics(decision_path, window_start)
    runtime_log = collect_runtime_log_metrics(runtime_log_path, window_start)

    all_metrics = {
        "experience": experience,
        "decision_audit": decision_audit,
        "runtime_log": runtime_log,
    }
    slo = evaluate_slos(all_metrics)

    notes: List[str] = []
    if runtime_log.get("rate_limit_hits", 0) > 0:
        notes.append(
            f"Observed {runtime_log['rate_limit_hits']} rate-limit hits inside analysis window."
        )
    if runtime_log.get("ticker_last_unavailable", 0) > 0:
        notes.append(
            f"Observed {runtime_log['ticker_last_unavailable']} ticker-unavailable warnings."
        )
    if experience.get("safe_state_records", 0) > 0:
        notes.append(
            f"Observed {experience['safe_state_records']} SAFE-state records from feeder fallback."
        )
    if not notes:
        notes.append("No major reliability warnings detected in selected window.")

    report = {
        "phase": "phase_0_baseline_lock",
        "generated_at_utc": now_utc.isoformat(),
        "window": {
            "hours": hours,
            "start_utc": window_start.isoformat(),
            "end_utc": now_utc.isoformat(),
        },
        "config_snapshot": {
            "exchange_id": Config.EXCHANGE_ID,
            "trading_mode": Config.TRADING_MODE,
            "quote_currency": Config.QUOTE_CURRENCY,
            "top_coins_count": Config.TOP_COINS_COUNT,
            "hyperliquid_rate_safe_top_coins": getattr(Config, "HYPERLIQUID_RATE_SAFE_TOP_COINS", None),
            "effective_scan_limit": (
                min(Config.TOP_COINS_COUNT, getattr(Config, "HYPERLIQUID_RATE_SAFE_TOP_COINS", Config.TOP_COINS_COUNT))
                if Config.EXCHANGE_ID == "hyperliquid"
                else Config.TOP_COINS_COUNT
            ),
            "scan_timeframe": Config.SCAN_TIMEFRAME,
            "ltf_lookback": Config.LTF_LOOKBACK,
        },
        "metrics": all_metrics,
        "slo_evaluation": slo,
        "notes": notes,
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate reliability baseline report.")
    parser.add_argument("--hours", type=int, default=24, help="Lookback window in hours (default: 24)")
    parser.add_argument(
        "--experience-log",
        type=str,
        default=Config.EXPERIENCE_LOG_FILE,
        help="Path to experience JSONL",
    )
    parser.add_argument(
        "--decision-audit",
        type=str,
        default=os.path.join("data", "decision_audit.jsonl"),
        help="Path to decision audit JSONL",
    )
    parser.add_argument(
        "--runtime-log",
        type=str,
        default="adaptive_trader.log",
        help="Path to runtime log file",
    )
    parser.add_argument(
        "--report-path",
        type=str,
        default=os.path.join("reports", "reliability_baseline.json"),
        help="Output JSON report path",
    )
    args = parser.parse_args()

    report = build_report(
        hours=max(1, args.hours),
        experience_path=args.experience_log,
        decision_path=args.decision_audit,
        runtime_log_path=args.runtime_log,
    )

    os.makedirs(os.path.dirname(args.report_path), exist_ok=True)
    with open(args.report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"[OK] Reliability baseline written: {args.report_path}")
    print(f"      Overall SLO status: {report['slo_evaluation']['overall_status']}")
    print(f"      Window: last {report['window']['hours']}h")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
