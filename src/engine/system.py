import logging
import time
from collections import defaultdict, deque
from typing import Optional, List, Tuple, Dict, Any

from src.core.definitions import MarketState, Action, StrategyType, ActionDirection, RiskLevel, MarketRegime
from src.core.validation import StateValidator, ValidationException
from src.core.gating import StrategyGater
from src.core.risk import RiskManager
from src.config import Config
from src.core.trade_utils import get_trade_mode, expected_value
from src.database.storage import ExperienceDB
from src.ml.inference import PolicyInference
from src.monitoring.decision_audit import get_auditor, DecisionAudit
from src.core.meta_learner import MetaLearner
from src.strategies.arbitrage import ArbitrageStrategy
from src.strategies.market_making import InventoryStrategy

logger = logging.getLogger(__name__)

class TradingEngine:
    def __init__(self, log_suffix: Optional[str] = None):
        self.db = ExperienceDB(log_suffix=log_suffix)
        self.policy = PolicyInference()
        self.meta_learner = MetaLearner() # Phase D: Autonomous behavioral steering
        self.arbitrage = ArbitrageStrategy(min_profit_pct=0.0005, fee_rate=Config.FEE_RATE)
        self.market_maker = InventoryStrategy(max_inventory_usd=1000.0, risk_aversion=0.10)
        self.strategy_weights: Dict[StrategyType, float] = {}
        self.blocked_strategies: set[StrategyType] = set()
        self.auditor = get_auditor()
        self.last_policy_adjustment = self._policy_baseline()
        self.runtime_policy: Dict[str, Any] = {}
        self.cross_section_scores: Dict[str, float] = {}
        self.vol_breakout_bbw_history: Dict[str, deque] = defaultdict(lambda: deque(maxlen=120))

    @staticmethod
    def _policy_baseline() -> Dict[str, Any]:
        return {
            "score_multiplier": 1.0,
            "confidence_buffer": 0.0,
            "size_multiplier": 1.0,
            "dominant_loss_category": "NONE",
            "sample_size": 0,
            "applied": False,
        }

    def set_strategy_overrides(self, strategy_weights: Optional[Dict[StrategyType, float]] = None,
                                blocked_strategies: Optional[set] = None) -> None:
        self.strategy_weights = strategy_weights or {}
        self.blocked_strategies = blocked_strategies or set()

    def set_runtime_policy(self, policy: Optional[Dict[str, Any]] = None) -> None:
        self.runtime_policy = dict(policy or {})

    def update_cross_section_snapshot(self, symbol: str, state: MarketState) -> None:
        """
        Maintains a rolling universe-relative momentum score used by
        CROSS_SECTIONAL_MOMENTUM selection.
        """
        trend = max(-3.0, min(3.0, float(state.trend_spread)))
        htf_trend = max(-3.0, min(3.0, float(state.htf_trend_spread)))
        volume = max(-3.0, min(3.0, float(state.volume_zscore)))
        shift = max(-1.0, min(1.0, float(state.momentum_shift_score)))

        score = (0.50 * trend) + (0.35 * htf_trend) + (0.10 * volume) + (0.05 * shift)
        self.cross_section_scores[str(symbol)] = score
        # Keep memory bounded in case symbol universe rotates heavily.
        if len(self.cross_section_scores) > 120:
            stale_keys = list(self.cross_section_scores.keys())[:-120]
            for key in stale_keys:
                self.cross_section_scores.pop(key, None)

    def update_volatility_snapshot(self, symbol: str, state: MarketState) -> None:
        """
        Stores rolling Bollinger bandwidth history per symbol for squeeze/expansion logic.
        """
        bb_mid = float(state.bb_mid or 0.0)
        if bb_mid <= 0:
            return
        bbw_pct = ((float(state.bb_upper) - float(state.bb_lower)) / max(bb_mid, 1e-9)) * 100.0
        history = self.vol_breakout_bbw_history[str(symbol)]
        history.append(max(0.0, bbw_pct))

    def _vol_breakout_snapshot(self, symbol: str, state: MarketState) -> Dict[str, float]:
        symbol = str(symbol)
        history = list(self.vol_breakout_bbw_history.get(symbol, []))

        bb_mid = float(state.bb_mid or 0.0)
        current_bbw = 0.0
        if bb_mid > 0:
            current_bbw = ((float(state.bb_upper) - float(state.bb_lower)) / max(bb_mid, 1e-9)) * 100.0

        if history and abs(history[-1] - current_bbw) < 1e-9:
            prev_series = history[:-1]
        else:
            prev_series = history

        window = max(5, int(Config.VOL_BREAKOUT_BASELINE_WINDOW))
        baseline_slice = prev_series[-window:]
        baseline_bbw = sum(baseline_slice) / len(baseline_slice) if baseline_slice else current_bbw
        prev_bbw = prev_series[-1] if prev_series else baseline_bbw
        expansion_ratio = current_bbw / max(prev_bbw, 1e-9)
        baseline_ratio = current_bbw / max(baseline_bbw, 1e-9)

        return {
            "current_bbw": max(0.0, current_bbw),
            "prev_bbw": max(0.0, prev_bbw),
            "baseline_bbw": max(0.0, baseline_bbw),
            "expansion_ratio": max(0.0, expansion_ratio),
            "baseline_ratio": max(0.0, baseline_ratio),
            "sample_size": float(len(prev_series)),
        }

    def _cross_section_percentile(self, symbol: str) -> float:
        if symbol not in self.cross_section_scores:
            return 0.5
        values = list(self.cross_section_scores.values())
        if len(values) < 2:
            return 0.5
        values.sort()
        target = self.cross_section_scores[symbol]
        rank = sum(1 for value in values if value <= target)
        return rank / len(values)
        
        
    def run_analysis(self, state: MarketState, data_source: str = "live", market_period_id: str = None) -> Tuple[Action, str, int]:
        """
        The Main Loop:
        Returns: (Action, decision_id, repetition_count)
        """
        try:
            t0 = time.time()
            # 1. Validation
            StateValidator.validate_state(state)
            t1 = time.time()
            
            # 2. Gating
            allowed_strategies = StrategyGater.get_allowed_strategies(state)
            
            # 3. Decision (Cold Start Rule Logic)
            raw_action, repeats = self._basic_selector(state, allowed_strategies)
            selected_policy = self.last_policy_adjustment if raw_action.strategy != StrategyType.WAIT else self._policy_baseline()
            t2 = time.time()
            
            # 4. Confidence Prediction (Now before RiskManager to allow Scaling)
            confidence = self.policy.predict_confidence(state, raw_action, repeats=repeats)
            self.last_confidence = confidence
            t3 = time.time()
            
            # 5. Risk Scaling Bands (Weighted by MetaLearner)
            # Adjust trade risk dynamically based on ML confidence
            risk_multiplier = 1.0
            original_action_record = None
            applied_meta_threshold = self.meta_learner.confidence_threshold
            
            if raw_action.strategy != StrategyType.WAIT:
                # Use MetaLearner's adaptive threshold instead of hardcoded config
                policy_threshold_buffer = float(selected_policy.get("confidence_buffer", 0.0))
                runtime_threshold_buffer = float(self.runtime_policy.get("confidence_buffer", 0.0))
                
                # Enforce Config Minimum
                base_threshold = max(self.meta_learner.confidence_threshold, Config.ML_CONFIDENCE_MIN)
                
                applied_meta_threshold = base_threshold + policy_threshold_buffer + runtime_threshold_buffer
                if not state.regime_stable:
                    applied_meta_threshold += 0.1

                if confidence < applied_meta_threshold:
                    logger.info(f"META BLOCK: Confidence {confidence:.4f} < {applied_meta_threshold:.2f}. Blocking trade.")
                    original_action_record = raw_action.to_dict()
                    raw_action = Action.wait(reason=f"Blocked by MetaLearner Threshold ({confidence:.4f} < {applied_meta_threshold:.2f})")
                else:
                    # Use MetaLearner for position scaling
                    risk_multiplier = self.meta_learner.get_position_scaling(confidence)
                    risk_multiplier *= float(selected_policy.get("size_multiplier", 1.0))
                    risk_multiplier *= float(self.runtime_policy.get("size_multiplier", 1.0))
                    risk_multiplier = max(0.5, min(1.5, risk_multiplier))

            # 5.5 Expected Value gating (probability-calibrated)
            if Config.EV_GATING and raw_action.strategy != StrategyType.WAIT:
                trade_mode, tp_pct, sl_pct = get_trade_mode(
                    state.market_regime.value,
                    state.trend_strength.value
                )
                ev = expected_value(confidence, tp_pct, sl_pct)
                if ev < Config.EV_THRESHOLD:
                    logger.info(f"EV BLOCK: {trade_mode} EV {ev:.3f} < {Config.EV_THRESHOLD:.3f}. Blocking trade.")
                    original_action_record = raw_action.to_dict()
                    raw_action = Action.wait(reason=f"Blocked by EV ({ev:.3f} < {Config.EV_THRESHOLD:.3f})")
            
            t4 = time.time()

            # 6. Risk Management (Validation & Scaling)
            # Pass the multiplier to RiskManager to apply it to base risk
            final_action = RiskManager.validate_action(state, raw_action, risk_multiplier=risk_multiplier)
            t5 = time.time()
            
            # 7. Logging (Pending Reward)
            # Store repeats, ML scores, and risks in metadata
            decision_id = self.db.log_decision(
                state, 
                final_action, 
                reward=0.0, 
                data_source=data_source, 
                market_period_id=market_period_id,
                repetition_count=repeats,
                ml_confidence=confidence,
                original_action=original_action_record
            )
            t6 = time.time()
            
            # 8. Decision Audit (for debugging)
            try:
                audit = self.auditor.create_audit(decision_id, state.symbol)
                self.auditor.log_ml_result(audit, confidence, applied_meta_threshold)
                if Config.EV_GATING:
                    trade_mode, tp_pct, sl_pct = get_trade_mode(state.market_regime.value, state.trend_strength.value)
                    ev_val = expected_value(confidence, tp_pct, sl_pct)
                    self.auditor.log_ev_result(audit, ev_val, Config.EV_THRESHOLD)
                
                strat_weight = self.strategy_weights.get(raw_action.strategy, 1.0) if raw_action.strategy != StrategyType.WAIT else 1.0
                strat_blocked = raw_action.strategy in self.blocked_strategies
                self.auditor.log_strategy_filter(audit, raw_action.strategy.name if hasattr(raw_action.strategy, 'name') else str(raw_action.strategy), strat_weight, strat_blocked)
                self.auditor.log_risk_state(audit, state.current_risk_state, state.current_drawdown_percent, state.current_open_positions, Config.MAX_CONCURRENT_POSITIONS)
                self.auditor.log_market_context(audit, state.market_regime.value, state.regime_confidence, state.rsi, state.trend_spread, state.htf_trend_spread, state.volume_zscore)
                self.auditor.log_final_action(audit, final_action.strategy.name, final_action.direction.name)
                self.auditor.save(audit)
            except Exception as audit_err:
                logger.debug(f"Audit logging failed: {audit_err}")
            
            t7 = time.time()
            if t7 - t0 > 1.0:
                logger.warning(f"SLOW ENGINE ({state.symbol}): Total {t7-t0:.2f}s | Val {t1-t0:.2f}s | Sel {t2-t1:.2f}s | Conf {t3-t2:.2f}s | Logic {t4-t3:.2f}s | Risk {t5-t4:.2f}s | DB {t6-t5:.2f}s | Audit {t7-t6:.2f}s")
            
            return final_action, decision_id, repeats

        except ValidationException as e:
            logger.error(f"State Validation Failed: {e}")
            fallback = Action.wait(reason=f"Validation Error: {e}")
            decision_id = self.db.log_decision(state, fallback, reward=0.0, data_source=data_source, repetition_count=0)
            return fallback, decision_id, 0
            
        except Exception as e:
            logger.error(f"System Error: {e}")
            fallback = Action.wait(reason=f"System Error: {e}")
            decision_id = self.db.log_decision(state, fallback, reward=0.0, repetition_count=0)
            return fallback, decision_id, 0

    def _basic_selector(self, state: MarketState, allowed: List[StrategyType]) -> Tuple[Action, int]:
        """
        Rule-based signal selector with multi-timeframe + execution-aware filters.
        Returns (Action, repetition_count).
        """
        self.last_policy_adjustment = self._policy_baseline()
        if not allowed:
            return Action.wait(reason="No strategies allowed by Gating Protocol"), 0
        runtime_blocked = {
            str(name).upper() for name in self.runtime_policy.get("blocked_strategies", [])
        }
        merged_blocked = set(self.blocked_strategies)
        if runtime_blocked:
            for strat in list(allowed):
                if strat.name.upper() in runtime_blocked:
                    merged_blocked.add(strat)

        if merged_blocked:
            allowed = [s for s in allowed if s not in merged_blocked]
            if not allowed:
                return Action.wait(reason="All strategies blocked by performance filter."), 0

        # 1. Fetch History (for repetition)
        history = self.db.get_recent_records(limit=3)

        # 2. Strategic WAIT injection (data diversity)
        import random
        if Config.STRATEGIC_WAIT_PROB > 0 and random.random() < Config.STRATEGIC_WAIT_PROB:
            return Action.wait(reason="Strategic WAIT injection to gather inaction data."), 0

        # Runtime regime gates (auto-rollout policy controls)
        if bool(self.runtime_policy.get("require_regime_stable", False)) and not state.regime_stable:
            return Action.wait(reason="Blocked by runtime policy: unstable regime"), 0
        min_regime_conf = min(
            float(self.runtime_policy.get("min_regime_confidence", 0.0)),
            0.20,  # Cap: auto-rollout can't demand regime confidence above 20%
        )
        if min_regime_conf > 0 and state.regime_confidence < min_regime_conf:
            return Action.wait(
                reason=f"Blocked by runtime policy: regime_confidence {state.regime_confidence:.2f} < {min_regime_conf:.2f}"
            ), 0

        # 3. Execution risk filters
        if state.spread_pct > Config.MAX_SPREAD_PCT:
            return Action.wait(reason=f"Blocked by spread {state.spread_pct:.2f}%"), 0
        if abs(state.gap_pct) > Config.MAX_GAP_PCT:
            return Action.wait(reason=f"Blocked by gap {state.gap_pct:.2f}%"), 0
        if state.body_pct > Config.MAX_BODY_PCT:
            return Action.wait(reason=f"Blocked by body {state.body_pct:.2f}%"), 0

        # 4. Compute signal scores
        trend_up_ltf = state.trend_spread >= Config.TREND_SPREAD_MIN
        trend_down_ltf = state.trend_spread <= -Config.TREND_SPREAD_MIN
        trend_up_htf = state.htf_trend_spread >= Config.HTF_TREND_SPREAD_MIN
        trend_down_htf = state.htf_trend_spread <= -Config.HTF_TREND_SPREAD_MIN
        trend_up = trend_up_ltf or trend_up_htf
        trend_down = trend_down_ltf or trend_down_htf

        rsi_momentum_up = max(55.0, Config.RSI_OVERBOUGHT - 10.0)
        rsi_momentum_down = min(45.0, Config.RSI_OVERSOLD + 10.0)

        momentum_bias = 0
        if state.macd_hist > 0:
            momentum_bias += 1
        elif state.macd_hist < 0:
            momentum_bias -= 1
        if state.rsi >= rsi_momentum_up:
            momentum_bias += 1
        elif state.rsi <= rsi_momentum_down:
            momentum_bias -= 1

        momentum_up = momentum_bias >= 1
        momentum_down = momentum_bias <= -1
        volume_spike = state.volume_zscore >= Config.MIN_VOLUME_ZSCORE
        near_high = state.dist_to_high <= Config.NEAR_LEVEL_PCT
        near_low = state.dist_to_low <= Config.NEAR_LEVEL_PCT
        low_vol = state.volatility_level.value == "LOW"
        high_vol = state.volatility_level.value == "HIGH"

        scores: Dict[StrategyType, float] = {}
        directions: Dict[StrategyType, ActionDirection] = {}
        policy_adjustments: Dict[StrategyType, Dict[str, Any]] = {}

        for strat in allowed:
            score = 0.0
            direction = ActionDirection.FLAT

            if strat == StrategyType.MOMENTUM:
                if not (trend_up or momentum_up):
                    score = 0.0
                else:
                    score = 0.3
                    if trend_up_ltf:
                        score += 0.2
                    if momentum_up:
                        score += 0.2
                    if trend_up_htf:
                        score += 0.1
                    if near_high:
                        score += 0.1
                    direction = ActionDirection.LONG

            elif strat == StrategyType.CROSS_SECTIONAL_MOMENTUM:
                if not Config.CROSS_SECTIONAL_MOMENTUM_ENABLED:
                    score = 0.0
                elif len(self.cross_section_scores) < max(2, Config.CROSS_SECTIONAL_MIN_UNIVERSE):
                    score = 0.0
                else:
                    percentile = self._cross_section_percentile(state.symbol)
                    top_cut = 1.0 - max(0.01, min(0.49, Config.CROSS_SECTIONAL_TOP_PCT))
                    bottom_cut = max(0.01, min(0.49, Config.CROSS_SECTIONAL_BOTTOM_PCT))
                    abs_spread = max(abs(state.trend_spread), abs(state.htf_trend_spread))
                    spread_ok = abs_spread >= max(0.0, Config.CROSS_SECTIONAL_MIN_ABS_SPREAD)

                    if percentile >= top_cut and (trend_up or momentum_up) and spread_ok:
                        edge = (percentile - top_cut) / max(0.01, (1.0 - top_cut))
                        score = 0.42 + min(0.25, edge * 0.25)
                        direction = ActionDirection.LONG
                        if volume_spike:
                            score += 0.05
                    elif percentile <= bottom_cut and (trend_down or momentum_down) and spread_ok:
                        edge = (bottom_cut - percentile) / max(0.01, bottom_cut)
                        score = 0.42 + min(0.25, edge * 0.25)
                        direction = ActionDirection.SHORT
                        if volume_spike:
                            score += 0.05
                    else:
                        score = 0.0

            elif strat == StrategyType.SHORT_MOMENTUM:
                if not (trend_down or momentum_down):
                    score = 0.0
                else:
                    score = 0.3
                    if trend_down_ltf:
                        score += 0.2
                    if momentum_down:
                        score += 0.2
                    if trend_down_htf:
                        score += 0.1
                    if near_low:
                        score += 0.1
                    direction = ActionDirection.SHORT

            elif strat == StrategyType.BREAKOUT:
                # Breakout with volume confirmation
                if volume_spike and high_vol and (trend_up or trend_down):
                    score = 0.45
                    if trend_up:
                        direction = ActionDirection.LONG
                        if near_high:
                            score += 0.15
                        if trend_up_htf:
                            score += 0.1
                    elif trend_down:
                        direction = ActionDirection.SHORT
                        if near_low:
                            score += 0.15
                        if trend_down_htf:
                            score += 0.1
                else:
                    score = 0.0

            elif strat == StrategyType.VOLATILITY_BREAKOUT:
                snap = self._vol_breakout_snapshot(state.symbol, state)
                current_bbw = snap["current_bbw"]
                prev_bbw = snap["prev_bbw"]
                baseline_bbw = snap["baseline_bbw"]
                expansion_ratio = snap["expansion_ratio"]
                baseline_ratio = snap["baseline_ratio"]
                sample_size = int(snap["sample_size"])

                squeeze_ok = (
                    sample_size >= max(5, Config.VOL_BREAKOUT_BASELINE_WINDOW // 2)
                    and prev_bbw <= Config.VOL_BREAKOUT_BBW_SQUEEZE_MAX
                    and baseline_bbw <= (Config.VOL_BREAKOUT_BBW_SQUEEZE_MAX * 1.15)
                )
                expansion_ok = (
                    expansion_ratio >= Config.VOL_BREAKOUT_EXPANSION_RATIO_MIN
                    and baseline_ratio >= Config.VOL_BREAKOUT_EXPANSION_RATIO_MIN
                )
                atr_pct = (state.atr / max(state.current_price, 1e-9)) * 100.0 if state.current_price > 0 else 0.0
                volatility_ok = atr_pct >= Config.VOL_BREAKOUT_MIN_ATR_PCT
                volume_ok = state.volume_zscore >= Config.VOL_BREAKOUT_MIN_VOLUME_ZSCORE

                if squeeze_ok and expansion_ok and volatility_ok and volume_ok:
                    expansion_edge = max(0.0, baseline_ratio - Config.VOL_BREAKOUT_EXPANSION_RATIO_MIN)
                    score = 0.48 + min(0.22, expansion_edge * 0.20)
                    if trend_up or momentum_up or state.macd_hist > 0:
                        direction = ActionDirection.LONG
                        if near_high:
                            score += 0.05
                    elif trend_down or momentum_down or state.macd_hist < 0:
                        direction = ActionDirection.SHORT
                        if near_low:
                            score += 0.05
                    else:
                        score = 0.0
                else:
                    score = 0.0

            elif strat == StrategyType.MEAN_REVERSION:
                if low_vol:
                    if state.rsi >= Config.RSI_OVERBOUGHT and near_high:
                        score = 0.5
                        direction = ActionDirection.SHORT
                    elif state.rsi <= Config.RSI_OVERSOLD and near_low:
                        score = 0.5
                        direction = ActionDirection.LONG

            elif strat == StrategyType.ARBITRAGE:
                funding_threshold = getattr(Config, "FUNDING_ARB_THRESHOLD", 0.08)
                funding_opps = self.arbitrage.scan_funding({state.symbol: state.funding_rate / 100.0})
                if funding_opps and abs(state.funding_rate) >= funding_threshold:
                    # Positive funding -> crowded longs -> prefer short; inverse for negative funding.
                    direction = ActionDirection.SHORT if state.funding_rate > 0 else ActionDirection.LONG
                    score = 0.45 + min(0.25, abs(state.funding_rate) / max(funding_threshold, 1e-9) * 0.1)
                    if low_vol:
                        score += 0.05

            elif strat == StrategyType.MARKET_MAKING:
                mm_max_spread = getattr(Config, "MM_MAX_SPREAD_PCT", 0.12)
                mm_max_body = getattr(Config, "MM_MAX_BODY_PCT", Config.MAX_BODY_PCT * 0.6)
                if low_vol and state.spread_pct <= mm_max_spread and state.body_pct <= mm_max_body:
                    skew = self.market_maker.get_skew(state.current_open_positions * 100.0)
                    score = 0.35
                    if near_low:
                        direction = ActionDirection.LONG
                        score += 0.10
                    elif near_high:
                        direction = ActionDirection.SHORT
                        score += 0.10
                    else:
                        # Inventory-aware fallback direction.
                        if skew > 0:
                            direction = ActionDirection.LONG
                        elif skew < 0:
                            direction = ActionDirection.SHORT
                        else:
                            direction = ActionDirection.LONG if state.momentum_shift_score >= 0 else ActionDirection.SHORT

            elif strat == StrategyType.SCALP:
                if not high_vol and state.body_pct < (Config.MAX_BODY_PCT * 0.75):
                    score = 0.35
                    if momentum_up:
                        score += 0.15
                        direction = ActionDirection.LONG
                    elif momentum_down:
                        score += 0.15
                        direction = ActionDirection.SHORT

            # Regime stability adjustment
            if score > 0:
                confidence = max(0.0, min(1.0, state.regime_confidence))
                score *= (0.85 + 0.15 * confidence)
                if not state.regime_stable:
                    score *= 0.9

            if direction != ActionDirection.FLAT:
                policy_adj = self.meta_learner.get_policy_adjustments(
                    strategy=strat.name,
                    regime=state.market_regime.value,
                    regime_stable=state.regime_stable,
                )
                score *= float(policy_adj.get("score_multiplier", 1.0))
                weight = self.strategy_weights.get(strat, 1.0)
                runtime_weight = float(self.runtime_policy.get("strategy_weights", {}).get(strat.name.upper(), 1.0))
                scores[strat] = score * max(0.0, weight) * max(0.0, runtime_weight)
                directions[strat] = direction
                policy_adjustments[strat] = policy_adj

        if not scores:
            return Action.wait(reason="No strategy met signal criteria."), 0

        # 5. Select best strategy
        proposed_strategy = max(scores, key=scores.get)
        best_score = scores[proposed_strategy]
        min_signal_score = max(
            float(self.runtime_policy.get("min_signal_score", Config.MIN_SIGNAL_SCORE)),
            Config.MIN_SIGNAL_SCORE,  # Floor: never below .env-configured minimum
        )
        if best_score < min_signal_score:
            return Action.wait(reason=f"Signal score {best_score:.2f} below threshold"), 0

        # 6. Repetition check
        repeats = 0
        current_context = (state.market_regime.value, state.volatility_level.value)
        for record in reversed(history):
            recorded_action = record.get("action_taken", {})
            recorded_state = record.get("market_state", {})
            record_context = (recorded_state.get("market_regime"), recorded_state.get("volatility_level"))
            is_same_strategy = recorded_action.get("strategy") == proposed_strategy.value
            is_same_context = record_context == current_context
            if is_same_strategy and is_same_context:
                repeats += 1
            else:
                break

        if repeats >= 3:
            alternatives = [s for s in scores.keys() if s != proposed_strategy and scores[s] >= min_signal_score]
            if alternatives:
                proposed_strategy = alternatives[0]
                repeats = 0
            else:
                return Action.wait(reason="Max consecutive repetitions reached."), 0

        direction = directions.get(proposed_strategy, ActionDirection.FLAT)
        selected_policy = policy_adjustments.get(proposed_strategy, self._policy_baseline())
        self.last_policy_adjustment = selected_policy
        policy_note = ""
        if selected_policy.get("applied"):
            policy_note = (
                f" | policy={selected_policy.get('dominant_loss_category')} "
                f"(x{selected_policy.get('score_multiplier', 1.0):.2f})"
            )
        return Action(
            strategy=proposed_strategy,
            direction=direction,
            risk_level=RiskLevel.LOW,
            reasoning=f"Signal {proposed_strategy.name} score={best_score:.2f}{policy_note}"
        ), repeats
