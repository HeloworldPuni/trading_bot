import sys
import os
import pandas as pd
import numpy as np
sys.path.append(os.getcwd())

from src.features.store import FeatureStore
from src.features.microstructure import MicrostructureFeatures
from src.features.context import ContextFeatures
from src.features.relative import RelativeFeatures
from src.features.labeler import TripleBarrierLabeler
from src.features.volatility import VolatilityEstimator

def audit_data_quality():
    print("\n--- 1. Data Quality Audit ---")
    store = FeatureStore("BTC/USDT")
    
    # Trades
    trades = store.load_trades()
    print(f"Trades Loaded: {len(trades)}")
    if trades.empty:
        print("FAIL: No trades found.")
        return False
        
    print(f"Trades Range: {trades['timestamp'].min()} to {trades['timestamp'].max()}")
    
    # Check for gaps > 1 minute
    trades['ts'] = pd.to_datetime(trades['timestamp'], unit='ms')
    gaps = trades['ts'].diff()
    large_gaps = gaps[gaps > pd.Timedelta(minutes=5)]
    if not large_gaps.empty:
        print(f"WARN: Found {len(large_gaps)} gaps > 5 mins.")
    else:
        print("PASS: No significant data gaps.")

    # Orderbook
    ob = store.load_orderbook()
    print(f"Orderbook Snapshots: {len(ob)}")
    if ob.empty:
        print("FAIL: No orderbook data.")
        return False
        
    # Check for stuck data (variance = 0)
    if ob['bid1_p'].var() == 0:
        print("FAIL: Bid price variance is 0 (Stuck feed).")
        return False
    else:
        print("PASS: Orderbook is dynamic.")
        
    return True

def audit_features():
    print("\n--- 2. Feature Calculation Audit ---")
    store = FeatureStore("BTC/USDT")
    trades = store.load_trades()
    ob = store.load_orderbook()
    
    # Microstructure
    ofi = MicrostructureFeatures.calc_ofi(ob)
    print(f"OFI Mean: {ofi.mean():.4f} (Should be near 0)")
    print(f"OFI Std: {ofi.std():.4f}")
    
    spread = MicrostructureFeatures.calc_spread(ob)
    print(f"Avg Spread (bps): {spread['spread_rel'].mean():.4f}")
    
    if spread['spread_rel'].min() < 0:
        print("FAIL: Negative spread detected.")
        return False
        
    # Context
    # Need bars
    bars = store.resample_trades(trades, rule='1min')
    close = bars['close']
    
    vol_regime = ContextFeatures.calc_volatility_expansion(close)
    print(f"Vol Expansion Ratio (Max): {vol_regime.max():.4f}")
    
    if vol_regime.isna().all():
         print("FAIL: Volatility calculation returned all NaNs.")
         return False
         
    return True

def audit_labels():
    print("\n--- 3. Label Distribution Audit ---")
    store = FeatureStore("BTC/USDT")
    trades = store.load_trades()
    bars = store.resample_trades(trades, rule='1min')
    close = bars['close']
    
    vol = VolatilityEstimator.get_daily_vol(close, span=20)
    
    # Barriers
    t_events = close.index
    vertical = t_events + pd.Timedelta(minutes=10)
    
    labels = TripleBarrierLabeler.get_events(
        close_prices=close,
        t_events=t_events,
        pt_sl=[1.0, 1.0],
        target=vol,
        min_ret=0.00001,
        vertical_barrier_times=pd.Series(vertical, index=t_events)
    )
    
    dist = labels['label'].value_counts(normalize=True)
    print("Label Distribution:")
    print(dist)
    
    # Check if we have both wins and losses
    if 1 not in dist and -1 not in dist:
         print("WARN: Imbalanced labels (All timeouts?).")
    
    return True

def audit_phase_4():
    print("\n--- 4. Regime Detection Audit (Phase 4) ---")
    store = FeatureStore("BTC/USDT")
    trades = store.load_trades()
    bars = store.resample_trades(trades, rule='5min')
    close = bars['close']
    
    # 1. HMM Separation Check
    # We want to confirm that State 0 and State 1 are actually different.
    from src.features.hmm_regime import HMMRegimeClassifier
    hmm = HMMRegimeClassifier(n_components=2)
    rets = np.log(close / close.shift(1)).dropna()
    
    try:
        states = hmm.fit_predict(rets)
        vol_0 = rets[states == 0].std()
        vol_1 = rets[states == 1].std()
        
        print(f"HMM State 0 Vol: {vol_0:.5f}")
        print(f"HMM State 1 Vol: {vol_1:.5f}")
        
        # Check for distinction (e.g. one is at least 1.2x the other)
        ratio = max(vol_0, vol_1) / (min(vol_0, vol_1) + 1e-9)
        print(f"Vol Ratio: {ratio:.2f}")
        
        if ratio < 1.1:
            print("WARN: HMM states are not distinct enough (Vol Ratio < 1.1).")
            # Not necessarily a failure if market was flat, but worth noting.
        else:
            print("PASS: HMM states are distinct.")
            
        # Check Probabilities
        probs = hmm.predict_proba(rets)
        if probs.empty:
             print("FAIL: predict_proba returned empty.")
             return False
        print("PASS: HMM Probabilities generated.")

    except Exception as e:
        print(f"FAIL: HMM Audit crash: {e}")
        return False
        
    # 2. Spike Detection Sensitivity
    # create synthetic spike
    from src.features.spike_detector import SpikeDetector
    
    # Create a copy with a massive spike at the end
    synthetic = close.copy()
    synthetic.iloc[-1] = synthetic.iloc[-2] * 1.05 # +5% jump
    
    spikes = SpikeDetector.detect_spikes(synthetic)
    if spikes.iloc[-1]:
        print("PASS: SpikeDetector caught synthetic +5% shock.")
    else:
        print("FAIL: SpikeDetector missed synthetic +5% shock.")
        return False
        
    # 3. Regime Stability (Trend)
    from src.features.regime import RegimeDetector
    high, low = bars['high'], bars['low']
    trend = RegimeDetector.get_trend_regime(high, low, close)
    
    # Count transitions
    transitions = (trend != trend.shift(1)).sum()
    print(f"Trend Transitions: {transitions} / {len(trend)}")
    
    if transitions > (len(trend) * 0.5):
        print("WARN: Trend regime finds too much chop (Flickering).")
    else:
        print("PASS: Trend regime is stable.")

    return True

def audit_phase_5():
    print("\n--- 5. Strategy Library Audit (Phase 5) ---")
    
    # 1. Interface Check
    from src.strategies.base import AbstractBaseStrategy, StrategySignal
    from src.strategies.trend import TrendFollowingStrategy
    from src.strategies.mean_reversion import MeanReversionStrategy
    from src.strategies.arbitrage import FundingArbitrageStrategy
    
    # Mock Data
    row = pd.Series({
        'close': 100.0, 'high': 102.0, 'low': 98.0, 
        'ema_20': 101.0, 'ema_50': 99.0, 'adx': 30.0, # Trend Up
        'bb_upper': 110.0, 'bb_lower': 90.0, 'rsi': 50.0,
        'funding_rate': 0.0001, 'atr': 1.0
    })
    
    # Mock Context
    ctx_trend = pd.Series({'trend_regime': 1, 'vol_regime': 1})
    ctx_range = pd.Series({'trend_regime': 0, 'vol_regime': 1})
    
    # Test Trend Strategy
    trend = TrendFollowingStrategy()
    sig_t_active = trend.generate_signal(row, ctx_trend)
    sig_t_blocked = trend.generate_signal(row, ctx_range)
    
    # Phase 6 Update: ML Model might kill the signal.
    # We accept Signal=1 OR (Signal=0 AND reason="ML Filter Rejected")
    is_active_valid = (sig_t_active.signal == 1) or \
                      (sig_t_active.signal == 0 and sig_t_active.metadata.get("reason") == "ML Filter Rejected")
    
    if is_active_valid and sig_t_blocked.signal == 0:
        print("PASS: TrendStrategy respects Regime (Active/ML-Filtered in Trend, Blocked in Range).")
    else:
        print(f"FAIL: TrendStrategy Logic Error. Active={sig_t_active.signal}, Blocked={sig_t_blocked.signal}, Meta={sig_t_active.metadata}")
        return False
        
    # Check Output Standard
    if not isinstance(sig_t_active, StrategySignal):
        print("FAIL: Strategy does not output StrategySignal dataclass.")
        return False

    # Test Mean Reversion Strategy
    # Need mean reversion data (Close < Lower BB)
    row_mr = row.copy()
    row_mr['close'] = 89.0 # Below BB lower (90)
    row_mr['rsi'] = 25.0
    
    mr = MeanReversionStrategy()
    sig_mr_active = mr.generate_signal(row_mr, ctx_range)
    sig_mr_blocked = mr.generate_signal(row_mr, ctx_trend)
    
    is_mr_valid = (sig_mr_active.signal == 1) or \
                  (sig_mr_active.signal == 0 and sig_mr_active.metadata.get("reason") == "ML Filter Rejected")
    
    if is_mr_valid and sig_mr_blocked.signal == 0:
        print("PASS: MeanReversionStrategy respects Regime (Active/ML-Filtered in Range, Blocked in Trend).")
    else:
        print(f"FAIL: MeanRev Logic Error. Active={sig_mr_active.signal}, Blocked={sig_mr_blocked.signal}, Meta={sig_mr_active.metadata}")
        return False

    # Test Arbitrage
    # Funding > 0.05
    row_arb = row.copy()
    row_arb['funding_rate'] = 0.06 
    arb = FundingArbitrageStrategy()
    sig_arb = arb.generate_signal(row_arb)
    
    if sig_arb.signal == -1:
        print("PASS: FundingArbitrage correctly shorts high funding.")
    else:
        print("FAIL: FundingArbitrage missed signal.")
        return False
        
    return True

def audit_phase_6():
    print("\n--- 6. Strategy ML Models Audit (Phase 6) ---")

    def _unwrap_model(model_obj):
        if isinstance(model_obj, dict) and "model" in model_obj:
            return model_obj["model"]
        return model_obj

    def _build_feature_row_for_model(model_obj) -> pd.Series:
        model = _unwrap_model(model_obj)
        feature_names = getattr(model, "feature_names_in_", None)
        cols = [str(c) for c in feature_names] if feature_names is not None else []

        if not cols:
            n_features = int(getattr(model, "n_features_in_", 0) or 0)
            if n_features <= 0:
                n_features = 8
            cols = [f"feature_{i+1}" for i in range(n_features)]

        values = {c: 0.0 for c in cols}
        # Inject sensible defaults when known feature names exist.
        defaults = {
            "spread_rel": 0.1,
            "ofi": 5.0,
            "funding_divergence": 0.0,
            "vol_buy": 1.0,
            "vol_sell": 1.0,
            "trend_regime": 1.0,
            "vol_regime": 1.0,
            "rsi": 50.0,
            "ema_20": 101.0,
            "ema_50": 100.0,
            "adx": 25.0,
            "close": 100.0,
            "high": 101.0,
            "low": 99.0,
            "bb_upper": 110.0,
            "bb_lower": 90.0,
            "funding_rate": 0.0,
            "atr": 1.0,
        }
        for k, v in defaults.items():
            if k in values:
                values[k] = v
        return pd.Series(values)

    # 1. Check Artifacts (legacy + current-compatible)
    legacy_features = os.path.exists("data/features/BTC_USDT_features.parquet")
    legacy_labels = os.path.exists("data/features/BTC_USDT_labels.parquet")
    modern_artifacts = os.path.exists("models/feature_maps.json") and os.path.exists("models/registry.json")

    if legacy_features and legacy_labels:
        print("PASS: Legacy datasets (Features + Labels) exist.")
    elif modern_artifacts:
        print("PASS: Modern model artifacts exist (registry + feature maps).")
    else:
        print("FAIL: No valid feature/label artifacts found.")
        return False

    # 2. Check Models
    if not os.path.exists("models/TrendFollowing.joblib"):
        print("FAIL: TrendFollowing model missing.")
        return False
    if not os.path.exists("models/MeanReversion.joblib"):
        print("FAIL: MeanReversion model missing.")
        return False
    print("PASS: Strategy model files exist.")

    # 3. Validation Logic
    from src.strategies.trend import TrendFollowingStrategy
    from src.strategies.mean_reversion import MeanReversionStrategy
    try:
        trend_strat = TrendFollowingStrategy()
        if trend_strat.ml_model is None:
            print("FAIL: TrendStrategy failed to load ML model.")
            return False
        print("PASS: TrendStrategy loaded ML model.")

        mr_strat = MeanReversionStrategy()
        if mr_strat.ml_model is None:
            print("FAIL: MeanReversionStrategy failed to load ML model.")
            return False
        print("PASS: MeanReversionStrategy loaded ML model.")

        # Build model-compatible feature rows.
        trend_features = _build_feature_row_for_model(trend_strat.ml_model)
        mr_features = _build_feature_row_for_model(mr_strat.ml_model)

        # Create raw signal and apply model filters
        from src.strategies.base import StrategySignal
        raw_sig = StrategySignal(1, 0.5)

        trend_filtered = trend_strat.apply_model_filter(raw_sig, trend_features)
        mr_filtered = mr_strat.apply_model_filter(raw_sig, mr_features)

        if "ml_probability" in trend_filtered.metadata:
            print(f"PASS: Trend ML filter applied. Prob: {trend_filtered.metadata['ml_probability']:.4f}")
        else:
            print("FAIL: Trend ML filter did not return probability metadata.")
            return False

        if "ml_probability" in mr_filtered.metadata:
            print(f"PASS: MeanReversion ML filter applied. Prob: {mr_filtered.metadata['ml_probability']:.4f}")
        else:
            print("FAIL: MeanReversion ML filter did not return probability metadata.")
            return False

    except Exception as e:
        print(f"FAIL: ML Audit Exception: {e}")
        return False
        
    return True

def audit_phase_7():
    print("\n--- 7. Portfolio Engine Audit (Phase 7) ---")
    
    # 1. Check Imports
    try:
        from src.portfolio.allocator import PortfolioAllocator
        from src.portfolio.risk import RiskManager
        from src.strategies.base import StrategySignal
    except ImportError as e:
        print(f"FAIL: Phase 7 Imports missing: {e}")
        return False
        
    # 2. Functional Test: Volatility Targeting
    try:
        # Use large max_pos to isolate vol targeting logic
        risk = RiskManager(max_leverage=2.0, max_position_size=1.0, target_volatility=0.40)
        allocator = PortfolioAllocator(risk)
        
        # Test Case: High Volatility
        # 80% annual vol -> Vol Scaler should be 0.5x
        # We simulate prices with High Vol
        # We need historical prices dict
        # Use cumprod for geometric returns (percentage changes)
        # 5% daily returns -> High Volatility
        returns = 1 + np.random.normal(0, 0.05, 100)
        prices = pd.Series(np.cumprod(returns)) * 100.0
        hist = {'BTC/USDT': prices}
        curr = {'BTC/USDT': prices.iloc[-1]}
        
        signals = {'TestStrat': StrategySignal(1, 1.0)} # Full confidence
        
        weights = allocator.allocate(signals, curr, hist)
        w = weights.get('TestStrat', 10.0)
        
        # Expected: 1.0 * (0.40 / 0.80) approx 0.5
        # Allow range 0.3 to 0.7 due to random noise in vol calc
        if 0.3 <= w <= 0.7:
             print(f"PASS: Volatility Targeting active. Weight {w:.2f} (Expected ~0.50)")
        else:
             print(f"FAIL: Volatility Targeting off. Weight {w:.2f} (Expected ~0.50)")
             return False
             
        # 3. Functional Test: Leverage Cap
        # Try to allocate 10 strategies with weight 1.0 each (Total 10.0)
        # Should be capped at 2.0 (0.2 each)
        many_signals = {f"Strat{i}": StrategySignal(1, 1.0) for i in range(10)}
        weights_caps = allocator.allocate(many_signals, curr, hist) # Re-uses high vol, so 0.5 scaler -> Total 5.0 -> Cap 2.0 -> 0.4x -> Final 0.2 each
        
        total_lev = sum(abs(x) for x in weights_caps.values())
        if 1.9 <= total_lev <= 2.1:
            print(f"PASS: Max Leverage Constraint active. Total {total_lev:.2f} (Limit 2.0)")
        else:
            print(f"FAIL: Max Leverage failed. Total {total_lev:.2f}")
            return False
            
        # 4. Functional Test: Correlation Penalty
        # Sim two strategies with 0.9 correlation
        rets_corr = pd.DataFrame({
            'StratA': np.random.normal(0, 0.01, 100),
            'StratB': np.random.normal(0, 0.01, 100)
        })
        # Force high correlation
        rets_corr['StratB'] = rets_corr['StratA'] * 0.9 + np.random.normal(0, 0.001, 100)
        
        # Use lower confidence so we don't hit Max Leverage Cap immediately
        # This allows us to see the reduction from penalty
        sigs_corr = {
            'StratA': StrategySignal(1, 0.4),
            'StratB': StrategySignal(1, 0.4)
        }
        
        # Current vol low enough to avoid vol scaling (or we pre-calculate expected)
        # We reuse the 'prices' from before which has low vol? Wait, no, 'prices' is High Vol.
        # We need a Low Vol asset to isolate Correlation effect.
        prices_low = pd.Series(np.cumprod(1 + np.random.normal(0, 0.001, 100))) * 100
        hist_low = {'BTC/USDT': prices_low}
        
        w_corr = allocator.allocate(sigs_corr, curr, hist_low, strategy_returns=rets_corr)
        
        # Expected: Both have raw 1.0. 
        # Vol Scaling: Low Vol -> maybe 2x cap.
        # Correlation: >0.7 -> Penalty 0.75.
        # Let's see result. Ideally < 2.0 (if capped) * 0.75 = 1.5.
        
        # Wait, exact calc:
        # Vol: very low -> scaler = 2.0 (Cap).
        # Raw Scaled = 2.0 each.
        # Correlation Penalty: 2.0 * 0.75 = 1.5 each.
        # Leverage Constraint: Total 3.0 > Limit 2.0.
        # Final Scale: 2.0 / 3.0 = 0.66.
        # Final Weight: 1.5 * 0.66 = 1.0 each.
        
        # This is complex to assert exact value due to layers.
        # Easier: Compare with Uncorrelated run.
        
        # Uncorrelated Run
        rets_uncorr = pd.DataFrame({
            'StratA': np.random.normal(0, 0.01, 100),
            'StratB': np.random.normal(0, 0.01, 100)
        })
        w_uncorr = allocator.allocate(sigs_corr, curr, hist_low, strategy_returns=rets_uncorr)
        
        sum_corr = sum(w_corr.values())
        sum_uncorr = sum(w_uncorr.values())
        
        if sum_corr < sum_uncorr:
             print(f"PASS: Correlation Penalty active. Correlated Sum {sum_corr:.2f} < Uncorrelated {sum_uncorr:.2f}")
        else:
             print(f"FAIL: Correlation Penalty inactive. {sum_corr:.2f} >= {sum_uncorr:.2f}")
             return False

    except Exception as e:
        print(f"FAIL: Portfolio Audit crash: {e}")
        return False
        
    return True

def audit_phase_8():
    print("\n--- 8. Execution Engine Audit (Phase 8) ---")
    try:
        from src.execution.router import SmartRouter, OrderType, ExecutionStatus, ActionDirection
        from src.execution.paper import PaperExchange
        from src.core.definitions import Action, StrategyType, RiskLevel, MarketState, VolatilityLevel, TrendStrength, MarketRegime
        
        router = SmartRouter()
        exchange = PaperExchange(latency_ms=0)
        
        # Mock State
        state = MarketState(
            market_regime=MarketRegime.BULL_TREND,
            volatility_level=VolatilityLevel.NORMAL,
            trend_strength=TrendStrength.MODERATE,
            time_of_day="MID",
            trading_session="NY",
            day_type="WEEKDAY",
            week_phase="MID",
            time_remaining_days=1.0,
            current_price=100.0,
            distance_to_key_levels=1.0,
            spread_pct=0.0001, # Tight spread
            funding_extreme=False
        )
        
        # 1. Test High Urgency Routing
        action_urgent = Action(StrategyType.MOMENTUM, ActionDirection.LONG, RiskLevel.HIGH, target_weight=0.1)
        req_urgent = router.route(action_urgent, state)
        if req_urgent.order_type == OrderType.MARKET:
            print("PASS: High Urgency routed to MARKET.")
        else:
            print(f"FAIL: High Urgency routed to {req_urgent.order_type.name}")
            return False
            
        # 2. Test Low Urgency Routing (Wide Spread)
        state_wide = MarketState(
            market_regime=MarketRegime.SIDEWAYS_LOW_VOL,
            volatility_level=VolatilityLevel.LOW,
            trend_strength=TrendStrength.WEAK,
            time_of_day="MID",
            trading_session="NY",
            day_type="WEEKDAY",
            week_phase="MID",
            time_remaining_days=1.0,
            current_price=100.0,
            distance_to_key_levels=1.0,
            spread_pct=0.10, # Wide spread
            funding_extreme=False
        )
        action_passive = Action(StrategyType.MEAN_REVERSION, ActionDirection.SHORT, RiskLevel.LOW, target_weight=0.1)
        req_passive = router.route(action_passive, state_wide)
        if req_passive.order_type == OrderType.LIMIT:
             print("PASS: Low Urgency/Wide Spread routed to LIMIT.")
        else:
             print(f"FAIL: Low Urgency routed to {req_passive.order_type.name}")
             return False
             
        # 3. Test Execution Lifecycle
        # Place Limit Buy @ 99 (Current 100) -> Pending
        req_limit = req_passive # Reuse object structure but modify
        req_limit.order_type = OrderType.LIMIT
        req_limit.limit_price = 99.0
        req_limit.direction = ActionDirection.LONG
        req_limit.action_id = "AUDIT_LIMIT_TEST"
        
        report = exchange.execute(req_limit, 100.0)
        if report.status == ExecutionStatus.PENDING:
             print("PASS: Limit Order is PENDING.")
        else:
             print(f"FAIL: Limit Order status {report.status}")
             return False
             
        # Drop price to 98 -> Fill
        fills = exchange.update(98.0)
        if len(fills) == 1 and fills[0].status == ExecutionStatus.FILLED:
             print(f"PASS: Limit Order FILLED on price drop. Price: {fills[0].avg_price}")
        else:
             print(f"FAIL: Limit Order not filled. Fills: {len(fills)}")
             return False
             
    except Exception as e:
        print(f"FAIL: Phase 8 Audit Crash: {e}")
        import traceback
        traceback.print_exc()
        return False
        
    return True

def main():
    try:
        # Sequential Audit
        if not audit_data_quality(): sys.exit(1)
        if not audit_features(): sys.exit(1)
        if not audit_labels(): sys.exit(1)
        if not audit_phase_4(): sys.exit(1)
        if not audit_phase_5(): sys.exit(1)
        if not audit_phase_6(): sys.exit(1)
        if not audit_phase_7(): sys.exit(1)
        if not audit_phase_8(): sys.exit(1)
        
        print("\n*** DEEP AUDIT PASSED ***")
        sys.exit(0)
    except Exception as e:
        print(f"Audit Crashed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
