
import logging
import sys
import os
from datetime import datetime

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ml.inference import PolicyInference
from src.core.definitions import MarketState, MarketRegime, VolatilityLevel, TrendStrength, Action, StrategyType, ActionDirection, RiskLevel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TestInference")

def test():
    print("Testing PolicyInference loading...")
    inf = PolicyInference()
    
    # Remove mismatch warning guard to see the error
    if hasattr(inf, "_mismatch_warned"):
        delattr(inf, "_mismatch_warned")

    print(f"Active Version: {inf.registry.data.get('active_version')}")
    print(f"Ensemble loaded: {list(inf.ensemble.keys())}")
    
    if not inf.ensemble:
        print("ERROR: No ensemble models loaded!")
        return

    # Mock a state compatible with definitions.py
    state = MarketState(
        market_regime=MarketRegime.BULL_TREND,
        volatility_level=VolatilityLevel.NORMAL,
        trend_strength=TrendStrength.STRONG,
        time_of_day="MID",
        trading_session="NY",
        day_type="WEEKDAY",
        week_phase="MID",
        time_remaining_days=3.5,
        distance_to_key_levels=0.05,
        rsi=60.0,
        trend_spread=0.01,
        dist_to_high=0.01,
        dist_to_low=0.1,
        macd=1.5, macd_signal=1.0, macd_hist=0.5,
        bb_upper=110, bb_lower=90, bb_mid=100, atr=5.0,
        volume_delta=100, spread_pct=0.001, body_pct=0.5, gap_pct=0.0,
        volume_zscore=1.0, liquidity_proxy=10000,
        funding_rate=0.01, funding_extreme=False,
        raw_timestamp=datetime.now().isoformat(),
        current_risk_state="SAFE",
        current_drawdown_percent=0.0,
        current_open_positions=0,
        symbol="BTC/USDT",
        regime_confidence=0.8,
        regime_stable=True,
        momentum_shift_score=0.2,
        htf_trend_spread=0.02,
        htf_rsi=65.0,
        htf_atr=15.0
    )
    
    # Test LONG action
    action = Action(
        strategy=StrategyType.BREAKOUT,
        direction=ActionDirection.LONG,
        risk_level=RiskLevel.LOW,
        reasoning="Test"
    )
    
    try:
        conf = inf.predict_confidence(state, action)
        print(f"Predicted Confidence (LONG): {conf:.4f}")
    except Exception as e:
        print(f"CRITICAL: predict_confidence crashed: {e}")
        import traceback
        traceback.print_exc()
    
    # Test WAIT action
    wait_action = Action.wait("Test")
    wait_conf = inf.predict_confidence(state, wait_action)
    print(f"Predicted Confidence (WAIT): {wait_conf:.4f}")

if __name__ == "__main__":
    test()
