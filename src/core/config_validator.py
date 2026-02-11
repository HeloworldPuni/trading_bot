"""
Configuration Validator - Solution #1
Validates config for risky combinations at startup.
"""
from typing import List


def validate_config() -> List[str]:
    """
    Comprehensive config validation. Returns list of warnings/errors.
    Call at startup to catch misconfigurations early.
    """
    from src.config import Config
    
    issues = []
    
    # API Keys
    if not Config.EXCHANGE_API_KEY or not Config.EXCHANGE_SECRET:
        issues.append("⚠️ WARNING: Exchange keys are missing in .env")
    
    # Risky leverage/position combinations for LIVE mode
    if Config.TRADING_MODE == "live":
        if Config.MAX_LEVERAGE > 5:
            issues.append(f"🔴 DANGER: MAX_LEVERAGE={Config.MAX_LEVERAGE} is high for live trading!")
        if Config.MAX_CONCURRENT_POSITIONS > 10:
            issues.append(f"🔴 DANGER: MAX_CONCURRENT_POSITIONS={Config.MAX_CONCURRENT_POSITIONS} may overexpose")
        if Config.MAX_POSITION_PCT > 0.15:
            issues.append(f"⚠️ HIGH RISK: MAX_POSITION_PCT={Config.MAX_POSITION_PCT*100:.0f}% per position")

    # Aggressive profile warnings
    if getattr(Config, "RISK_PROFILE", "balanced") == "aggressive":
        issues.append("⚠️ RISK_PROFILE=aggressive: expect high drawdowns and possible account loss")
        if Config.MAX_LEVERAGE >= 10:
            issues.append("🔴 DANGER: 10x leverage enabled under aggressive profile")
    
    # ATR TP/SL sanity checks
    if Config.ATR_TP_SL_ENABLED:
        if Config.ATR_TP_MULTIPLIER_SCALP < Config.ATR_SL_MULTIPLIER_SCALP:
            issues.append("⚠️ SCALP: TP multiplier < SL multiplier (negative R:R)")
        if Config.ATR_TP_MULTIPLIER_SWING < Config.ATR_SL_MULTIPLIER_SWING:
            issues.append("⚠️ SWING: TP multiplier < SL multiplier (negative R:R)")
    
    # Strategy filter sanity
    if Config.STRATEGY_FILTER_ENABLED:
        if Config.STRATEGY_FILTER_MIN_WIN_RATE > 0.6:
            issues.append(f"⚠️ STRATEGY_FILTER_MIN_WIN_RATE={Config.STRATEGY_FILTER_MIN_WIN_RATE} may block all strategies")
    
    # Canary sanity
    if Config.CANARY_MODE:
        if Config.CANARY_TRADE_LIMIT < 10:
            issues.append(f"⚠️ CANARY_TRADE_LIMIT={Config.CANARY_TRADE_LIMIT} too small for statistical significance")
    
    # EV gating with high threshold
    if Config.EV_GATING and Config.EV_THRESHOLD > 0.5:
        issues.append(f"⚠️ EV_THRESHOLD={Config.EV_THRESHOLD} may block most trades")
    
    # ML Ensemble health check
    try:
        from src.ml.registry import ModelRegistry
        import os
        registry = ModelRegistry()
        active_ver = registry.data.get("active_version")
        if active_ver:
            model_info = registry.data["models"].get(active_ver)
            if model_info and model_info.get("type") == "ensemble":
                experts = model_info.get("experts", {})
                for regime, info in experts.items():
                    path = info.get("path")
                    if not os.path.isabs(path):
                        root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
                        path = os.path.join(root, path)
                    if not os.path.exists(path):
                        issues.append(f"🔴 CRITICAL: Ensemble Expert '{regime}' model file missing: {path}")
    except Exception as e:
        issues.append(f"⚠️ Registry Check failed: {e}")

    # HTF lookback needs enough LTF data
    if Config.HTF_TIMEFRAME == "1h" and Config.LTF_LOOKBACK < 200:
        issues.append("⚠️ LTF_LOOKBACK < 200 may not have enough candles to resample to 1h HTF")
    
    # Print all issues
    for issue in issues:
        print(issue)
    
    if not issues:
        print("✅ Config validation passed - no risky combinations detected")
    
    return issues


if __name__ == "__main__":
    validate_config()
