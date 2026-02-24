"""
Configuration validator for startup safety checks.
"""

from typing import List


def validate_config() -> List[str]:
    """
    Validate config values and print issues.
    Returns a list of human-readable warnings/errors.
    """
    from src.config import Config

    issues: List[str] = []

    # API keys
    if not Config.EXCHANGE_API_KEY or not Config.EXCHANGE_SECRET:
        issues.append("[WARNING] Exchange keys are missing in .env")

    # Venue/profile sanity
    if Config.EXCHANGE_ID == "hyperliquid" and Config.QUOTE_CURRENCY != "USDC":
        issues.append(
            f"[WARNING] EXCHANGE_ID=hyperliquid usually uses QUOTE_CURRENCY=USDC (current: {Config.QUOTE_CURRENCY})"
        )
    if "/" in Config.SYMBOL:
        try:
            _, quote = Config.SYMBOL.split("/", 1)
            if quote.upper() != Config.QUOTE_CURRENCY:
                issues.append(
                    f"[WARNING] SYMBOL quote ({quote.upper()}) does not match QUOTE_CURRENCY ({Config.QUOTE_CURRENCY})"
                )
        except Exception:
            issues.append(f"[WARNING] SYMBOL format looks invalid: {Config.SYMBOL}")

    if Config.EXCHANGE_ID == "hyperliquid":
        if Config.TRADING_MODE == "live" and not Config.HYPERLIQUID_ENABLE_PRIVATE_ORDERS:
            issues.append(
                "[WARNING] TRADING_MODE=live with Hyperliquid but HYPERLIQUID_ENABLE_PRIVATE_ORDERS=false (orders disabled)."
            )
        if Config.HYPERLIQUID_ENABLE_PRIVATE_ORDERS:
            if not Config.HYPERLIQUID_API_WALLET or not Config.HYPERLIQUID_PRIVATE_KEY:
                issues.append(
                    "[CRITICAL] Hyperliquid private orders enabled but HYPERLIQUID_API_WALLET/HYPERLIQUID_PRIVATE_KEY is missing."
                )
            else:
                try:
                    import hyperliquid  # noqa: F401
                except Exception:
                    issues.append(
                        "[CRITICAL] Hyperliquid private orders enabled but `hyperliquid-python-sdk` is not installed."
                    )
            if Config.HYPERLIQUID_ORDER_SLIPPAGE <= 0 or Config.HYPERLIQUID_ORDER_SLIPPAGE > 0.1:
                issues.append(
                    f"[WARNING] HYPERLIQUID_ORDER_SLIPPAGE={Config.HYPERLIQUID_ORDER_SLIPPAGE} looks unsafe. Typical range: 0.001-0.05."
                )
        if Config.HYPERLIQUID_USER_WS_ENABLED and Config.HYPERLIQUID_WS_STALE_SEC < 30:
            issues.append(
                f"[WARNING] HYPERLIQUID_WS_STALE_SEC={Config.HYPERLIQUID_WS_STALE_SEC} is too low and may cause reconnect thrash."
            )
        if Config.HYPERLIQUID_ORDER_SYNC_GRACE_SEC < 15:
            issues.append(
                f"[WARNING] HYPERLIQUID_ORDER_SYNC_GRACE_SEC={Config.HYPERLIQUID_ORDER_SYNC_GRACE_SEC} may be too low for websocket fill confirmation."
            )

    # Live trading risk profile checks
    if Config.TRADING_MODE == "live":
        if Config.MAX_LEVERAGE > 5:
            issues.append(f"[WARNING] MAX_LEVERAGE={Config.MAX_LEVERAGE} is high for live trading")
        if Config.MAX_CONCURRENT_POSITIONS > 10:
            issues.append(f"[DANGER] MAX_CONCURRENT_POSITIONS={Config.MAX_CONCURRENT_POSITIONS} may overexpose")
        if Config.MAX_POSITION_PCT > 0.15:
            issues.append(f"[HIGH RISK] MAX_POSITION_PCT={Config.MAX_POSITION_PCT * 100:.0f}% per position")

    # Aggressive mode
    if getattr(Config, "RISK_PROFILE", "balanced") == "aggressive":
        issues.append("[WARNING] RISK_PROFILE=aggressive: expect higher drawdowns and possible account loss")
        if Config.MAX_LEVERAGE >= 10:
            issues.append("[WARNING] 10x leverage enabled under aggressive profile")

    # ATR TP/SL sanity
    if Config.ATR_TP_SL_ENABLED:
        if Config.ATR_TP_MULTIPLIER_SCALP < Config.ATR_SL_MULTIPLIER_SCALP:
            issues.append("[WARNING] SCALP TP multiplier < SL multiplier (negative R:R)")
        if Config.ATR_TP_MULTIPLIER_SWING < Config.ATR_SL_MULTIPLIER_SWING:
            issues.append("[WARNING] SWING TP multiplier < SL multiplier (negative R:R)")

    # Strategy filter sanity
    if Config.STRATEGY_FILTER_ENABLED and Config.STRATEGY_FILTER_MIN_WIN_RATE > 0.6:
        issues.append(
            f"[WARNING] STRATEGY_FILTER_MIN_WIN_RATE={Config.STRATEGY_FILTER_MIN_WIN_RATE} may block all strategies"
        )
    if Config.CROSS_SECTIONAL_MOMENTUM_ENABLED:
        if Config.CROSS_SECTIONAL_MIN_UNIVERSE < 4:
            issues.append(
                f"[WARNING] CROSS_SECTIONAL_MIN_UNIVERSE={Config.CROSS_SECTIONAL_MIN_UNIVERSE} is too low for relative ranking"
            )
        if not (0.05 <= Config.CROSS_SECTIONAL_TOP_PCT <= 0.50):
            issues.append(
                f"[WARNING] CROSS_SECTIONAL_TOP_PCT={Config.CROSS_SECTIONAL_TOP_PCT} should be in [0.05, 0.50]"
            )
        if not (0.05 <= Config.CROSS_SECTIONAL_BOTTOM_PCT <= 0.50):
            issues.append(
                f"[WARNING] CROSS_SECTIONAL_BOTTOM_PCT={Config.CROSS_SECTIONAL_BOTTOM_PCT} should be in [0.05, 0.50]"
            )
        if Config.CROSS_SECTIONAL_MIN_ABS_SPREAD < 0:
            issues.append(
                f"[WARNING] CROSS_SECTIONAL_MIN_ABS_SPREAD={Config.CROSS_SECTIONAL_MIN_ABS_SPREAD} should be non-negative"
            )
    if Config.VOLATILITY_BREAKOUT_ENABLED:
        if Config.VOL_BREAKOUT_BBW_SQUEEZE_MAX <= 0:
            issues.append(
                f"[WARNING] VOL_BREAKOUT_BBW_SQUEEZE_MAX={Config.VOL_BREAKOUT_BBW_SQUEEZE_MAX} should be positive"
            )
        if Config.VOL_BREAKOUT_EXPANSION_RATIO_MIN <= 1.0:
            issues.append(
                f"[WARNING] VOL_BREAKOUT_EXPANSION_RATIO_MIN={Config.VOL_BREAKOUT_EXPANSION_RATIO_MIN} should be > 1.0"
            )
        if Config.VOL_BREAKOUT_BASELINE_WINDOW < 5:
            issues.append(
                f"[WARNING] VOL_BREAKOUT_BASELINE_WINDOW={Config.VOL_BREAKOUT_BASELINE_WINDOW} is too small"
            )
        if Config.VOL_BREAKOUT_MIN_VOLUME_ZSCORE < 0:
            issues.append(
                f"[WARNING] VOL_BREAKOUT_MIN_VOLUME_ZSCORE={Config.VOL_BREAKOUT_MIN_VOLUME_ZSCORE} should be non-negative"
            )
        if Config.VOL_BREAKOUT_MIN_ATR_PCT < 0:
            issues.append(
                f"[WARNING] VOL_BREAKOUT_MIN_ATR_PCT={Config.VOL_BREAKOUT_MIN_ATR_PCT} should be non-negative"
            )
        if Config.VOL_BREAKOUT_ADMISSION_ENABLED:
            if Config.VOL_BREAKOUT_ADMISSION_MIN_TRADES < 10:
                issues.append(
                    f"[WARNING] VOL_BREAKOUT_ADMISSION_MIN_TRADES={Config.VOL_BREAKOUT_ADMISSION_MIN_TRADES} may overfit"
                )
            if not (0.0 <= Config.VOL_BREAKOUT_ADMISSION_MIN_WIN_RATE <= 1.0):
                issues.append(
                    f"[WARNING] VOL_BREAKOUT_ADMISSION_MIN_WIN_RATE={Config.VOL_BREAKOUT_ADMISSION_MIN_WIN_RATE} should be in [0,1]"
                )
            if not (0.0 <= Config.VOL_BREAKOUT_WARMUP_SIZE_MULTIPLIER <= 1.0):
                issues.append(
                    f"[WARNING] VOL_BREAKOUT_WARMUP_SIZE_MULTIPLIER={Config.VOL_BREAKOUT_WARMUP_SIZE_MULTIPLIER} should be in [0,1]"
                )

    # Canary sanity
    if Config.CANARY_MODE and Config.CANARY_TRADE_LIMIT < 10:
        issues.append(
            f"[WARNING] CANARY_TRADE_LIMIT={Config.CANARY_TRADE_LIMIT} is too small for statistical significance"
        )

    # EV gating sanity
    if Config.EV_GATING and Config.EV_THRESHOLD > 0.5:
        issues.append(f"[WARNING] EV_THRESHOLD={Config.EV_THRESHOLD} may block most trades")

    # Adaptive policy sanity
    if Config.ADAPTIVE_POLICY_ENABLED:
        if Config.ADAPTIVE_POLICY_MIN_SAMPLES < 5:
            issues.append(
                f"[WARNING] ADAPTIVE_POLICY_MIN_SAMPLES={Config.ADAPTIVE_POLICY_MIN_SAMPLES} may overfit to noise"
            )
        if not (0.2 <= Config.ADAPTIVE_POLICY_MIN_DOMINANCE <= 0.9):
            issues.append(
                f"[WARNING] ADAPTIVE_POLICY_MIN_DOMINANCE={Config.ADAPTIVE_POLICY_MIN_DOMINANCE} is outside typical range (0.2-0.9)"
            )
        if not (0.0 <= Config.ADAPTIVE_POLICY_MAX_SCORE_PENALTY <= 0.6):
            issues.append(
                f"[WARNING] ADAPTIVE_POLICY_MAX_SCORE_PENALTY={Config.ADAPTIVE_POLICY_MAX_SCORE_PENALTY} looks unsafe"
            )
        if not (0.0 <= Config.ADAPTIVE_POLICY_MAX_THRESHOLD_BONUS <= 0.2):
            issues.append(
                f"[WARNING] ADAPTIVE_POLICY_MAX_THRESHOLD_BONUS={Config.ADAPTIVE_POLICY_MAX_THRESHOLD_BONUS} looks unsafe"
            )
        if Config.ADAPTIVE_POLICY_MIN_SIZE_MULTIPLIER <= 0 or Config.ADAPTIVE_POLICY_MIN_SIZE_MULTIPLIER > 1:
            issues.append(
                f"[WARNING] ADAPTIVE_POLICY_MIN_SIZE_MULTIPLIER={Config.ADAPTIVE_POLICY_MIN_SIZE_MULTIPLIER} should be in (0,1]"
            )

    if Config.LEARNING_ENABLED:
        if Config.LEARNING_INTERVAL_HOURS < 1:
            issues.append(
                f"[WARNING] LEARNING_INTERVAL_HOURS={Config.LEARNING_INTERVAL_HOURS} may cause retrain thrash"
            )
        if Config.LEARNING_MIN_TRADES < 10:
            issues.append(
                f"[WARNING] LEARNING_MIN_TRADES={Config.LEARNING_MIN_TRADES} may retrain on weak sample sizes"
            )

    # Agent orchestration sanity
    if Config.AGENT_ORCHESTRATION_ENABLED:
        if Config.AGENT_MODE not in {"shadow", "active"}:
            issues.append(f"[WARNING] AGENT_MODE={Config.AGENT_MODE} is invalid (expected shadow|active)")
        if not (0.0 <= Config.AGENT_MIN_CONFIDENCE <= 1.0):
            issues.append(f"[WARNING] AGENT_MIN_CONFIDENCE={Config.AGENT_MIN_CONFIDENCE} should be between 0 and 1")
        if not (0.1 <= Config.AGENT_REDUCED_SIZE_MULTIPLIER <= 1.0):
            issues.append(
                f"[WARNING] AGENT_REDUCED_SIZE_MULTIPLIER={Config.AGENT_REDUCED_SIZE_MULTIPLIER} should be in [0.1, 1.0]"
            )

    if Config.AUTO_ROLLOUT_ENABLED:
        if Config.AUTO_ROLLOUT_TRIGGER_TRADES < 10:
            issues.append(
                f"[WARNING] AUTO_ROLLOUT_TRIGGER_TRADES={Config.AUTO_ROLLOUT_TRIGGER_TRADES} may trigger unstable candidate churn"
            )
        if Config.AUTO_ROLLOUT_WINDOW_TRADES < 20:
            issues.append(
                f"[WARNING] AUTO_ROLLOUT_WINDOW_TRADES={Config.AUTO_ROLLOUT_WINDOW_TRADES} is likely too small for baseline metrics"
            )
        stage_fracs = [
            Config.AUTO_ROLLOUT_STAGE_FRACTION_PROBE,
            Config.AUTO_ROLLOUT_STAGE_FRACTION_SCALE,
            Config.AUTO_ROLLOUT_STAGE_FRACTION_FULL,
        ]
        if any(f <= 0 or f > 1.0 for f in stage_fracs):
            issues.append("[WARNING] AUTO_ROLLOUT_STAGE_FRACTION_* values must be in (0, 1].")
        if stage_fracs != sorted(stage_fracs):
            issues.append("[WARNING] AUTO_ROLLOUT stage fractions should be non-decreasing (probe <= scale <= full).")
        if Config.AUTO_ROLLOUT_MAX_STAGE_DD_PCT <= 0:
            issues.append("[WARNING] AUTO_ROLLOUT_MAX_STAGE_DD_PCT should be positive.")
        if Config.AUTO_ROLLOUT_MAX_RISK_VETO_STREAK < 1:
            issues.append("[WARNING] AUTO_ROLLOUT_MAX_RISK_VETO_STREAK should be >= 1.")
        if Config.AUTO_ROLLOUT_POLICY_COOLDOWN_TRADES < 0:
            issues.append("[WARNING] AUTO_ROLLOUT_POLICY_COOLDOWN_TRADES should be >= 0.")
        if Config.AUTO_ROLLOUT_MAX_REJECT_MEMORY < 10:
            issues.append("[WARNING] AUTO_ROLLOUT_MAX_REJECT_MEMORY is very low and may lose useful memory.")

    # Ensemble artifact health check
    try:
        import os
        from src.ml.registry import ModelRegistry

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
                        issues.append(f"[CRITICAL] Ensemble expert '{regime}' model file missing: {path}")
    except Exception as e:
        issues.append(f"[WARNING] Registry check failed: {e}")

    # HTF resampling sanity
    if Config.HTF_TIMEFRAME == "1h" and Config.LTF_LOOKBACK < 200:
        issues.append("[WARNING] LTF_LOOKBACK < 200 may be insufficient for 1h HTF resampling")
    if Config.TOP_COINS_COUNT < 1:
        issues.append("[WARNING] TOP_COINS_COUNT should be >= 1")
    if Config.EXCHANGE_ID.lower() == "hyperliquid" and Config.HYPERLIQUID_RATE_SAFE_TOP_COINS < 1:
        issues.append("[WARNING] HYPERLIQUID_RATE_SAFE_TOP_COINS should be >= 1")
    if Config.PREFETCH_WORKERS_DEFAULT < 1:
        issues.append("[WARNING] PREFETCH_WORKERS_DEFAULT should be >= 1")
    if Config.PREFETCH_WORKERS_HYPERLIQUID < 1:
        issues.append("[WARNING] PREFETCH_WORKERS_HYPERLIQUID should be >= 1")
    if Config.DATA_QUALITY_STRIKE_LIMIT < 1:
        issues.append("[WARNING] DATA_QUALITY_STRIKE_LIMIT should be >= 1")
    if Config.DATA_QUALITY_QUARANTINE_SEC < 60:
        issues.append("[WARNING] DATA_QUALITY_QUARANTINE_SEC should be >= 60 seconds")
    if Config.MARKETDATA_MAX_PRICE_DIVERGENCE_PCT <= 0:
        issues.append("[WARNING] MARKETDATA_MAX_PRICE_DIVERGENCE_PCT should be > 0")
    if Config.MARKETDATA_CONTRACT_LOG_COOLDOWN_SEC < 1:
        issues.append("[WARNING] MARKETDATA_CONTRACT_LOG_COOLDOWN_SEC should be >= 1")
    if Config.MARKETDATA_STALE_STATE_MAX_SEC < 30:
        issues.append("[WARNING] MARKETDATA_STALE_STATE_MAX_SEC should be >= 30")
    if Config.MARKETDATA_STALE_TICKER_MAX_SEC < 10:
        issues.append("[WARNING] MARKETDATA_STALE_TICKER_MAX_SEC should be >= 10")
    if Config.MARKETDATA_STATE_REFRESH_MIN_SEC < 10:
        issues.append("[WARNING] MARKETDATA_STATE_REFRESH_MIN_SEC should be >= 10")
    if Config.MARKETDATA_REFRESH_SYMBOLS_PER_CYCLE < 0:
        issues.append("[WARNING] MARKETDATA_REFRESH_SYMBOLS_PER_CYCLE should be >= 0")
    if Config.MARKETDATA_WS_COVERAGE_MIN < 0 or Config.MARKETDATA_WS_COVERAGE_MIN > 1:
        issues.append("[WARNING] MARKETDATA_WS_COVERAGE_MIN should be between 0 and 1")
    if Config.MARKETDATA_CACHE_HEALTH_LOG_SEC < 30:
        issues.append("[WARNING] MARKETDATA_CACHE_HEALTH_LOG_SEC should be >= 30")
    if Config.MARKETDATA_WS_CANDLE_MIN_BARS < 50:
        issues.append("[WARNING] MARKETDATA_WS_CANDLE_MIN_BARS should be >= 50")
    if Config.MARKETDATA_WS_CANDLE_MAX_1M_BARS < 1000:
        issues.append("[WARNING] MARKETDATA_WS_CANDLE_MAX_1M_BARS should be >= 1000")
    if Config.MARKETDATA_WS_DRAIN_MAX_UPDATES < 100:
        issues.append("[WARNING] MARKETDATA_WS_DRAIN_MAX_UPDATES should be >= 100")
    if Config.RATE_GUARD_WINDOW_SEC < 30:
        issues.append("[WARNING] RATE_GUARD_WINDOW_SEC should be >= 30")
    if Config.RATE_GUARD_429_ESCALATE_HITS < 1:
        issues.append("[WARNING] RATE_GUARD_429_ESCALATE_HITS should be >= 1")
    if Config.RATE_GUARD_SUCCESS_RECOVERY < 10:
        issues.append("[WARNING] RATE_GUARD_SUCCESS_RECOVERY should be >= 10")
    if Config.RATE_GUARD_MAX_LEVEL < 0:
        issues.append("[WARNING] RATE_GUARD_MAX_LEVEL should be >= 0")
    if Config.RATE_GUARD_BUDGET_OHLCV_PER_MIN < 1:
        issues.append("[WARNING] RATE_GUARD_BUDGET_OHLCV_PER_MIN should be >= 1")
    if Config.RATE_GUARD_BUDGET_ORDERBOOK_PER_MIN < 0:
        issues.append("[WARNING] RATE_GUARD_BUDGET_ORDERBOOK_PER_MIN should be >= 0")
    if Config.RATE_GUARD_BUDGET_TICKER_SNAPSHOT_PER_MIN < 1:
        issues.append("[WARNING] RATE_GUARD_BUDGET_TICKER_SNAPSHOT_PER_MIN should be >= 1")
    if Config.RATE_GUARD_BUDGET_BATCH_TICKERS_PER_MIN < 0:
        issues.append("[WARNING] RATE_GUARD_BUDGET_BATCH_TICKERS_PER_MIN should be >= 0")
    if Config.RATE_GUARD_BUDGET_FUNDING_PER_MIN < 0:
        issues.append("[WARNING] RATE_GUARD_BUDGET_FUNDING_PER_MIN should be >= 0")
    if Config.RATE_GUARD_BUDGET_TOP_SYMBOLS_PER_MIN < 0:
        issues.append("[WARNING] RATE_GUARD_BUDGET_TOP_SYMBOLS_PER_MIN should be >= 0")
    if Config.HYPERLIQUID_PUBLIC_WS_QUEUE_SIZE < 1000:
        issues.append("[WARNING] HYPERLIQUID_PUBLIC_WS_QUEUE_SIZE should be >= 1000")
    if Config.HYPERLIQUID_PUBLIC_WS_STALE_SEC < 5:
        issues.append("[WARNING] HYPERLIQUID_PUBLIC_WS_STALE_SEC should be >= 5")
    if Config.MARKETDATA_WS_CANDLE_ENABLED and not Config.HYPERLIQUID_PUBLIC_WS_ENABLED:
        issues.append("[WARNING] MARKETDATA_WS_CANDLE_ENABLED=true but HYPERLIQUID_PUBLIC_WS_ENABLED=false")
    if Config.DATA_INGESTION_SYMBOL_LIMIT < 1:
        issues.append("[WARNING] DATA_INGESTION_SYMBOL_LIMIT should be >= 1")
    if Config.DATA_INGESTION_OHLCV_LIMIT < 10:
        issues.append("[WARNING] DATA_INGESTION_OHLCV_LIMIT should be >= 10")
    if Config.DATA_INGESTION_TRADE_LIMIT < 0:
        issues.append("[WARNING] DATA_INGESTION_TRADE_LIMIT should be >= 0")
    if Config.DIVERGENCE_MIN_TRADES < 5:
        issues.append("[WARNING] DIVERGENCE_MIN_TRADES is very low and may create noise")
    if Config.DIVERGENCE_ALERT_COOLDOWN_SEC < 30:
        issues.append("[WARNING] DIVERGENCE_ALERT_COOLDOWN_SEC should be >= 30 seconds")
    if Config.DATA_INGESTION_ENABLED and Config.DATA_INGESTION_INTERVAL_SEC < 30:
        issues.append("[WARNING] DATA_INGESTION_INTERVAL_SEC < 30 may cause API pressure")
    if Config.RISK_ALERT_COOLDOWN_SEC < 5:
        issues.append("[WARNING] RISK_ALERT_COOLDOWN_SEC should be >= 5 seconds")
    if Config.SPOOFING_DETECTION_ENABLED:
        if Config.SPOOFING_THRESHOLD_SIZE <= 0:
            issues.append("[WARNING] SPOOFING_THRESHOLD_SIZE should be positive")
        if Config.SPOOFING_MIN_EVENTS < 1:
            issues.append("[WARNING] SPOOFING_MIN_EVENTS should be >= 1")
        if Config.SPOOFING_LOG_COOLDOWN_SEC < 10:
            issues.append("[WARNING] SPOOFING_LOG_COOLDOWN_SEC should be >= 10 seconds")

    for issue in issues:
        print(issue)

    if not issues:
        print("[OK] Config validation passed - no risky combinations detected")

    return issues


if __name__ == "__main__":
    validate_config()
