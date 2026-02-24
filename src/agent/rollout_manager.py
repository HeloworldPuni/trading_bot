"""
Automatic candidate promotion + canary rollback manager.

This manager closes the loop for bounded policy adaptation:
diagnostics -> candidate policy -> staged canary -> promote/rollback.
"""

from __future__ import annotations

import json
import math
import os
from copy import deepcopy
from datetime import UTC, datetime
from typing import Any, Dict, List, Optional

from src.agent.analyzer import ObserverAnalyzer
from src.agent.experiment_manager import ExperimentCriteria, ExperimentManager
from src.agent.governor import DeploymentGovernor
from src.agent.planner import AdaptivePlanner
from src.config import Config


def _now_iso() -> str:
    return datetime.now(UTC).isoformat()


class AutoRolloutManager:
    def __init__(
        self,
        state_file: Optional[str] = None,
        trigger_trades: Optional[int] = None,
        window_trades: Optional[int] = None,
        max_stage_dd_pct: Optional[float] = None,
        stages: Optional[List[Dict[str, Any]]] = None,
        min_win_rate_delta: Optional[float] = None,
        min_sharpe_delta: Optional[float] = None,
        max_dd_increase: Optional[float] = None,
        max_risk_veto_streak: Optional[int] = None,
        policy_cooldown_trades: Optional[int] = None,
        max_reject_memory: Optional[int] = None,
    ):
        self.state_file = state_file or Config.AUTO_ROLLOUT_STATE_FILE
        self.trigger_trades = int(trigger_trades if trigger_trades is not None else Config.AUTO_ROLLOUT_TRIGGER_TRADES)
        self.window_trades = int(window_trades if window_trades is not None else Config.AUTO_ROLLOUT_WINDOW_TRADES)
        self.max_stage_dd_pct = float(max_stage_dd_pct if max_stage_dd_pct is not None else Config.AUTO_ROLLOUT_MAX_STAGE_DD_PCT)
        self.min_win_rate_delta = float(min_win_rate_delta if min_win_rate_delta is not None else Config.AUTO_ROLLOUT_MIN_WIN_RATE_DELTA)
        self.min_sharpe_delta = float(min_sharpe_delta if min_sharpe_delta is not None else Config.AUTO_ROLLOUT_MIN_SHARPE_DELTA)
        self.max_dd_increase = float(max_dd_increase if max_dd_increase is not None else Config.AUTO_ROLLOUT_MAX_DD_INCREASE)
        self.max_risk_veto_streak = int(
            max_risk_veto_streak
            if max_risk_veto_streak is not None
            else Config.AUTO_ROLLOUT_MAX_RISK_VETO_STREAK
        )
        self.policy_cooldown_trades = int(
            policy_cooldown_trades
            if policy_cooldown_trades is not None
            else Config.AUTO_ROLLOUT_POLICY_COOLDOWN_TRADES
        )
        self.max_reject_memory = int(
            max_reject_memory if max_reject_memory is not None else Config.AUTO_ROLLOUT_MAX_REJECT_MEMORY
        )

        self.stages = stages or [
            {
                "name": "PROBE",
                "fraction": float(Config.AUTO_ROLLOUT_STAGE_FRACTION_PROBE),
                "min_trades": int(Config.AUTO_ROLLOUT_STAGE_TRADES_PROBE),
            },
            {
                "name": "SCALE",
                "fraction": float(Config.AUTO_ROLLOUT_STAGE_FRACTION_SCALE),
                "min_trades": int(Config.AUTO_ROLLOUT_STAGE_TRADES_SCALE),
            },
            {
                "name": "FULL",
                "fraction": float(Config.AUTO_ROLLOUT_STAGE_FRACTION_FULL),
                "min_trades": int(Config.AUTO_ROLLOUT_STAGE_TRADES_FULL),
            },
        ]

        self.analyzer = ObserverAnalyzer()
        self.planner = AdaptivePlanner()
        self.experiment = ExperimentManager()
        self.governor = DeploymentGovernor()

        self.state = self._load_or_init_state()

    def _default_policy(self) -> Dict[str, Any]:
        return {
            "min_signal_score": float(Config.MIN_SIGNAL_SCORE),
            "confidence_buffer": 0.0,
            "size_multiplier": 1.0,
            "strategy_weights": {},
            "blocked_strategies": [],
            "require_regime_stable": False,
            "min_regime_confidence": 0.0,
        }

    def _load_or_init_state(self) -> Dict[str, Any]:
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    loaded = json.load(f)
                    return self._ensure_state_defaults(loaded)
            except Exception:
                pass
        state = {
            "version_counter": 1,
            "champion": {
                "version": "champion_v1",
                "policy": self._default_policy(),
                "promoted_at": _now_iso(),
                "baseline_metrics": None,
            },
            "candidate": None,
            "last_candidate_trade_count": 0,
            "total_trade_count": 0,
            "reject_memory": [],
            "events": [],
        }
        state = self._ensure_state_defaults(state)
        self._save_state(state)
        return state

    def _ensure_state_defaults(self, state: Dict[str, Any]) -> Dict[str, Any]:
        state.setdefault("version_counter", 1)
        state.setdefault("candidate", None)
        state.setdefault("last_candidate_trade_count", 0)
        state.setdefault("total_trade_count", 0)
        state.setdefault("events", [])
        state.setdefault("history", [])
        state.setdefault("reject_memory", [])

        champion = state.setdefault("champion", {})
        champion.setdefault("version", "champion_v1")
        champion.setdefault("policy", self._default_policy())
        champion.setdefault("promoted_at", _now_iso())
        champion.setdefault("baseline_metrics", None)
        return state

    def _save_state(self, state: Optional[Dict[str, Any]] = None) -> None:
        payload = state if state is not None else self.state
        directory = os.path.dirname(self.state_file)
        if directory:
            os.makedirs(directory, exist_ok=True)
        tmp = self.state_file + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        os.replace(tmp, self.state_file)

    def _append_event(self, event: str) -> None:
        item = {"timestamp_utc": _now_iso(), "event": event}
        self.state.setdefault("events", []).append(item)
        self.state["events"] = self.state["events"][-500:]

    @staticmethod
    def _clamp(value: float, lo: float, hi: float) -> float:
        return max(lo, min(hi, value))

    @staticmethod
    def _policy_fingerprint(policy: Dict[str, Any]) -> str:
        return json.dumps(policy, sort_keys=True, separators=(",", ":"))

    def _in_reject_cooldown(self, policy_fingerprint: str, total_trades: int) -> bool:
        for item in self.state.get("reject_memory", []):
            if item.get("policy_fingerprint") != policy_fingerprint:
                continue
            rejected_at = int(item.get("rejected_at_trade_count", 0))
            if (total_trades - rejected_at) < self.policy_cooldown_trades:
                return True
        return False

    def _remember_rejected_policy(self, policy_fingerprint: str, reason: str) -> None:
        if not policy_fingerprint:
            return
        memory = self.state.setdefault("reject_memory", [])
        memory.append(
            {
                "policy_fingerprint": policy_fingerprint,
                "rejected_at_trade_count": int(self.state.get("total_trade_count", 0)),
                "reason": str(reason),
                "timestamp_utc": _now_iso(),
            }
        )
        if len(memory) > self.max_reject_memory:
            del memory[:-self.max_reject_memory]

    def _normalize_policy(self, policy: Dict[str, Any]) -> Dict[str, Any]:
        p = deepcopy(policy)
        p["min_signal_score"] = self._clamp(float(p.get("min_signal_score", Config.MIN_SIGNAL_SCORE)), 0.45, 0.80)
        p["confidence_buffer"] = self._clamp(float(p.get("confidence_buffer", 0.0)), 0.0, 0.15)
        p["size_multiplier"] = self._clamp(float(p.get("size_multiplier", 1.0)), 0.40, 1.20)
        p["require_regime_stable"] = bool(p.get("require_regime_stable", False))
        p["min_regime_confidence"] = self._clamp(float(p.get("min_regime_confidence", 0.0)), 0.0, 1.0)

        weights = {}
        for key, val in dict(p.get("strategy_weights", {})).items():
            weights[str(key).upper()] = self._clamp(float(val), 0.5, 1.5)
        p["strategy_weights"] = weights

        blocked = [str(x).upper() for x in p.get("blocked_strategies", [])]
        p["blocked_strategies"] = sorted(set(blocked))
        return p

    def _apply_action_to_policy(self, policy: Dict[str, Any], action: Dict[str, Any]) -> None:
        action_type = str(action.get("action_type", "")).strip()
        params = dict(action.get("params", {}))

        if action_type == "set_threshold":
            if "min_signal_score" in params:
                policy["min_signal_score"] = float(params["min_signal_score"])
            if "confidence_buffer" in params:
                policy["confidence_buffer"] = float(params["confidence_buffer"])
        elif action_type == "set_strategy_weight":
            strategy = str(params.get("strategy", "")).upper()
            weight = params.get("weight")
            if strategy and weight is not None:
                policy.setdefault("strategy_weights", {})[strategy] = float(weight)
        elif action_type == "set_regime_gate":
            if "require_regime_stable" in params:
                policy["require_regime_stable"] = bool(params["require_regime_stable"])
            if "min_regime_confidence" in params:
                policy["min_regime_confidence"] = float(params["min_regime_confidence"])
        elif action_type == "set_position_cap":
            if "size_multiplier" in params:
                policy["size_multiplier"] = float(params["size_multiplier"])
            elif "max_position_pct" in params:
                # Convert absolute cap hint into a multiplier against current config.
                cap = float(params["max_position_pct"])
                base = max(1e-9, float(Config.MAX_POSITION_PCT))
                policy["size_multiplier"] = cap / base
        elif action_type == "set_symbol_filter":
            # Placeholder for future symbol-level gates.
            pass

    def _build_candidate_policy(self, actions: List[Dict[str, Any]], champion_policy: Dict[str, Any]) -> Dict[str, Any]:
        policy = deepcopy(champion_policy)
        for action in actions:
            self._apply_action_to_policy(policy, action)
        return self._normalize_policy(policy)

    @staticmethod
    def _policy_equal(a: Dict[str, Any], b: Dict[str, Any]) -> bool:
        return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)

    def _metrics_from_pnls(self, pnl_pcts: List[float]) -> Dict[str, Any]:
        n = len(pnl_pcts)
        if n == 0:
            return {"trades": 0, "win_rate": 0.0, "avg_pnl": 0.0, "sharpe": 0.0, "max_drawdown": 0.0}

        wins = sum(1 for p in pnl_pcts if p > 0)
        avg = sum(pnl_pcts) / n
        var = sum((p - avg) ** 2 for p in pnl_pcts) / n
        std = math.sqrt(var)
        sharpe = 0.0
        if std > 1e-9:
            sharpe = (avg / std) * math.sqrt(n)
        elif avg > 0:
            sharpe = 3.0

        eq = 1.0
        peak = 1.0
        max_dd = 0.0
        for p in pnl_pcts:
            eq *= max(0.01, 1.0 + (p / 100.0))
            if eq > peak:
                peak = eq
            dd = (peak - eq) / max(peak, 1e-9) * 100.0
            if dd > max_dd:
                max_dd = dd

        return {
            "trades": n,
            "win_rate": wins / n,
            "avg_pnl": avg,
            "sharpe": sharpe,
            "max_drawdown": max_dd,
        }

    def _metrics_from_trade_history(self, trade_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        pnl = [float(t.get("realized_pnl_pct", 0.0)) for t in trade_history]
        return self._metrics_from_pnls(pnl)

    def maybe_create_candidate(self, trade_history: List[Dict[str, Any]]) -> Optional[str]:
        if self.state.get("candidate") is not None:
            return None
        total_trades = len(trade_history)
        self.state["total_trade_count"] = max(int(self.state.get("total_trade_count", 0)), total_trades)
        if total_trades < self.trigger_trades:
            return None

        last_mark = int(self.state.get("last_candidate_trade_count", 0))
        if (total_trades - last_mark) < self.trigger_trades:
            return None

        window = trade_history[-self.window_trades :]
        diagnostics = self.analyzer.build_diagnostics(window)
        actions = self.planner.propose_actions(diagnostics)
        if not actions:
            return None

        champion_policy = self.state["champion"]["policy"]
        candidate_policy = self._build_candidate_policy(actions, champion_policy)
        if self._policy_equal(candidate_policy, champion_policy):
            self.state["last_candidate_trade_count"] = total_trades
            self._save_state()
            return None

        policy_fingerprint = self._policy_fingerprint(candidate_policy)
        if self._in_reject_cooldown(policy_fingerprint, total_trades):
            self.state["last_candidate_trade_count"] = total_trades
            event = "Candidate creation skipped: identical policy is in cooldown memory."
            self._append_event(event)
            self._save_state()
            return event

        version_counter = int(self.state.get("version_counter", 1)) + 1
        version = f"candidate_v{version_counter}"
        baseline_metrics = self._metrics_from_trade_history(window)

        self.state["version_counter"] = version_counter
        self.state["last_candidate_trade_count"] = total_trades
        self.state["candidate"] = {
            "version": version,
            "created_at": _now_iso(),
            "policy": candidate_policy,
            "policy_fingerprint": policy_fingerprint,
            "source_actions": actions,
            "diagnostics": diagnostics,
            "baseline_metrics": baseline_metrics,
            "stage_index": 0,
            "stage_started_at": _now_iso(),
            "stage_trade_count": 0,
            "stage_pnls": [],
            "stage_equity_peak": None,
            "stage_equity_start": None,
            "total_canary_trades": 0,
            "risk_veto_count": 0,
            "risk_veto_streak": 0,
            "canary_failures": 0,
        }
        event = f"Candidate {version} created with {len(actions)} action(s)."
        self._append_event(event)
        self._save_state()
        return event

    def _rollback_candidate(self, reason: str) -> str:
        candidate = self.state.get("candidate")
        if not candidate:
            return reason
        self._remember_rejected_policy(candidate.get("policy_fingerprint", ""), reason)
        event = f"Candidate {candidate['version']} rolled back: {reason}"
        self.state.setdefault("history", []).append(
            {
                "type": "ROLLBACK",
                "timestamp_utc": _now_iso(),
                "candidate_version": candidate["version"],
                "candidate_stage": self.stages[int(candidate.get("stage_index", 0))]["name"],
                "reason": reason,
            }
        )
        self.state["candidate"] = None
        self._append_event(event)
        self._save_state()
        return event

    def _promote_candidate(self, reason: str) -> str:
        candidate = self.state.get("candidate")
        if not candidate:
            return reason
        old_version = self.state["champion"]["version"]
        self.state["champion"] = {
            "version": candidate["version"],
            "policy": candidate["policy"],
            "promoted_at": _now_iso(),
            "baseline_metrics": self._metrics_from_pnls(candidate.get("stage_pnls", [])),
            "source_actions": candidate.get("source_actions", []),
        }
        self.state.setdefault("history", []).append(
            {
                "type": "PROMOTION",
                "timestamp_utc": _now_iso(),
                "from_version": old_version,
                "to_version": candidate["version"],
                "reason": reason,
            }
        )
        self.state["candidate"] = None
        event = f"Candidate promoted to champion: {self.state['champion']['version']} (from {old_version})"
        self._append_event(event)
        self._save_state()
        return event

    def record_trade_result(self, pnl_pct: float, equity: float, active_mode: bool = True) -> Optional[str]:
        candidate = self.state.get("candidate")
        if not candidate:
            return None

        self.state["total_trade_count"] = int(self.state.get("total_trade_count", 0)) + 1
        if not active_mode:
            # Shadow mode: observe performance, but never advance rollout stages.
            candidate["shadow_trade_count"] = int(candidate.get("shadow_trade_count", 0)) + 1
            shadow_pnls = candidate.setdefault("shadow_pnls", [])
            shadow_pnls.append(float(pnl_pct))
            if len(shadow_pnls) > 500:
                del shadow_pnls[:-500]
            candidate["shadow_last_seen_at"] = _now_iso()
            self._save_state()
            return None

        if candidate.get("stage_equity_start") is None:
            candidate["stage_equity_start"] = float(equity)
            candidate["stage_equity_peak"] = float(equity)

        candidate["stage_trade_count"] += 1
        candidate["total_canary_trades"] += 1
        candidate["risk_veto_streak"] = 0
        candidate.setdefault("stage_pnls", []).append(float(pnl_pct))

        peak = float(candidate.get("stage_equity_peak") or equity)
        peak = max(peak, float(equity))
        candidate["stage_equity_peak"] = peak
        drawdown = (peak - float(equity)) / max(peak, 1e-9) * 100.0
        if drawdown > self.max_stage_dd_pct:
            return self._rollback_candidate(f"stage drawdown {drawdown:.2f}% > {self.max_stage_dd_pct:.2f}%")

        stage_index = int(candidate["stage_index"])
        stage = self.stages[stage_index]
        if candidate["stage_trade_count"] < int(stage["min_trades"]):
            self._save_state()
            return None

        candidate_metrics = self._metrics_from_pnls(candidate.get("stage_pnls", []))
        baseline_metrics = candidate.get("baseline_metrics") or self.state["champion"].get("baseline_metrics") or {
            "trades": 0,
            "win_rate": 0.0,
            "avg_pnl": 0.0,
            "sharpe": 0.0,
            "max_drawdown": 0.0,
        }
        criteria = ExperimentCriteria(
            min_trades=int(stage["min_trades"]),
            min_win_rate_delta=self.min_win_rate_delta,
            min_sharpe_delta=self.min_sharpe_delta,
            max_drawdown_increase=self.max_dd_increase,
        )
        exp_result = self.experiment.evaluate(candidate_metrics, baseline_metrics, criteria)
        gov = self.governor.decide(exp_result, risk_veto=False, canary_failed=False)
        if not gov.get("promote"):
            return self._rollback_candidate(gov.get("reason", "candidate failed stage criteria"))

        if stage_index < len(self.stages) - 1:
            candidate["stage_index"] = stage_index + 1
            candidate["stage_started_at"] = _now_iso()
            candidate["stage_trade_count"] = 0
            candidate["stage_pnls"] = []
            candidate["stage_equity_start"] = float(equity)
            candidate["stage_equity_peak"] = float(equity)
            stage_name = self.stages[candidate["stage_index"]]["name"]
            event = f"Candidate {candidate['version']} promoted to canary stage {stage_name}."
            self._append_event(event)
            self._save_state()
            return event

        return self._promote_candidate("passed all canary stages")

    def record_governance_signal(
        self,
        *,
        risk_veto: bool = False,
        canary_failed: bool = False,
        reason: str = "",
    ) -> Optional[str]:
        candidate = self.state.get("candidate")
        if not candidate:
            return None

        if canary_failed:
            candidate["canary_failures"] = int(candidate.get("canary_failures", 0)) + 1
            gov = self.governor.decide(
                {"approved": True, "reason": "canary failure"},
                risk_veto=False,
                canary_failed=True,
            )
            rollback_reason = gov.get("reason", "Canary failed")
            if reason:
                rollback_reason = f"{rollback_reason}: {reason}"
            return self._rollback_candidate(rollback_reason)

        if risk_veto:
            candidate["risk_veto_count"] = int(candidate.get("risk_veto_count", 0)) + 1
            candidate["risk_veto_streak"] = int(candidate.get("risk_veto_streak", 0)) + 1
            streak = int(candidate.get("risk_veto_streak", 0))
            if streak >= self.max_risk_veto_streak:
                gov = self.governor.decide(
                    {"approved": True, "reason": "risk veto streak"},
                    risk_veto=True,
                    canary_failed=False,
                )
                rollback_reason = gov.get(
                    "reason",
                    f"Risk veto streak {streak} >= {self.max_risk_veto_streak}",
                )
                if reason:
                    rollback_reason = f"{rollback_reason}: {reason}"
                return self._rollback_candidate(rollback_reason)
            self._append_event(
                f"Candidate {candidate['version']} risk veto observed (streak={streak}/{self.max_risk_veto_streak})."
            )
            self._save_state()
        return None

    def _blend_policy(self, champion: Dict[str, Any], candidate: Dict[str, Any], fraction: float) -> Dict[str, Any]:
        fraction = self._clamp(float(fraction), 0.0, 1.0)
        merged = deepcopy(champion)
        merged["min_signal_score"] = champion["min_signal_score"] + fraction * (
            candidate["min_signal_score"] - champion["min_signal_score"]
        )
        merged["confidence_buffer"] = champion["confidence_buffer"] + fraction * (
            candidate["confidence_buffer"] - champion["confidence_buffer"]
        )
        merged["size_multiplier"] = champion["size_multiplier"] + fraction * (
            candidate["size_multiplier"] - champion["size_multiplier"]
        )

        strategy_weights = {}
        all_keys = set(champion.get("strategy_weights", {}).keys()) | set(candidate.get("strategy_weights", {}).keys())
        for key in all_keys:
            c0 = float(champion.get("strategy_weights", {}).get(key, 1.0))
            c1 = float(candidate.get("strategy_weights", {}).get(key, 1.0))
            strategy_weights[key] = c0 + fraction * (c1 - c0)
        merged["strategy_weights"] = strategy_weights

        merged["require_regime_stable"] = bool(champion.get("require_regime_stable", False)) or (
            bool(candidate.get("require_regime_stable", False)) and fraction >= 0.5
        )
        merged["min_regime_confidence"] = champion.get("min_regime_confidence", 0.0) + fraction * (
            candidate.get("min_regime_confidence", 0.0) - champion.get("min_regime_confidence", 0.0)
        )
        if fraction >= 1.0:
            merged["blocked_strategies"] = candidate.get("blocked_strategies", [])
        else:
            merged["blocked_strategies"] = champion.get("blocked_strategies", [])

        merged["__rollout_fraction"] = fraction
        return self._normalize_policy(merged)

    def get_runtime_policy(self, active_mode: bool) -> Dict[str, Any]:
        champion = self._normalize_policy(self.state["champion"]["policy"])
        candidate = self.state.get("candidate")
        if not candidate or not active_mode:
            return champion

        stage = self.stages[int(candidate["stage_index"])]
        fraction = float(stage["fraction"])
        candidate_policy = self._normalize_policy(candidate["policy"])
        return self._blend_policy(champion, candidate_policy, fraction)

    def snapshot(self) -> Dict[str, Any]:
        candidate = self.state.get("candidate")
        return {
            "champion_version": self.state["champion"]["version"],
            "candidate_version": candidate.get("version") if candidate else None,
            "candidate_stage": self.stages[int(candidate["stage_index"])]["name"] if candidate else None,
            "candidate_risk_veto_streak": int(candidate.get("risk_veto_streak", 0)) if candidate else 0,
            "candidate_canary_failures": int(candidate.get("canary_failures", 0)) if candidate else 0,
            "events_tail": self.state.get("events", [])[-5:],
        }
