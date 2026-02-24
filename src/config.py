
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

RISK_PROFILE = os.getenv("RISK_PROFILE", "balanced").lower()

AGGRESSIVE_DEFAULTS = {
    "BASE_LEVERAGE": "10",
    "MAX_LEVERAGE": "10",
    "MIN_LEVERAGE": "5",
    "MAX_POSITION_PCT": "0.12",
    "MAX_CONCURRENT_POSITIONS": "8",
    "EXPOSURE_CAP_PCT": "0.85",
    "CORR_CLUSTER_CAP_PCT": "0.55",
    "ML_CONFIDENCE_MIN": "0.58",
    "MIN_SIGNAL_SCORE": "0.55",
    "STRATEGY_FILTER_MIN_TRADES": "20",
    "STRATEGY_FILTER_MIN_WIN_RATE": "0.43",
    "STRATEGY_FILTER_MIN_AVG_PNL": "-0.02",
    "STRATEGIC_WAIT_PROB": "0.03",
    "ATR_TP_MULTIPLIER_SCALP": "1.4",
    "ATR_SL_MULTIPLIER_SCALP": "0.9",
    "ATR_TP_MULTIPLIER_SWING": "3.0",
    "ATR_SL_MULTIPLIER_SWING": "1.5",
}


def _profile_default(key: str, default: str) -> str:
    if RISK_PROFILE == "aggressive":
        return AGGRESSIVE_DEFAULTS.get(key, default)
    return default


def _drawdown_pct_env(default_pct: float = 15.0) -> float:
    """
    Supports both:
    - MAX_DRAWDOWN_PCT (percent, e.g. 10.0)
    - MAX_DRAWDOWN_PERCENT legacy alias (ratio or percent, e.g. 0.05 or 5)
    """
    raw_pct = os.getenv("MAX_DRAWDOWN_PCT")
    if raw_pct not in (None, ""):
        try:
            return float(raw_pct)
        except Exception:
            return float(default_pct)

    raw_legacy = os.getenv("MAX_DRAWDOWN_PERCENT")
    if raw_legacy in (None, ""):
        return float(default_pct)
    try:
        val = float(raw_legacy)
        return (val * 100.0) if val <= 1.0 else val
    except Exception:
        return float(default_pct)


class Config:
    RISK_PROFILE = RISK_PROFILE
    # API Keys
    EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY", "")
    EXCHANGE_SECRET = os.getenv("EXCHANGE_SECRET", "")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
    FRED_API_KEY = os.getenv("FRED_API_KEY", "")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")

    # Trading Config
    TRADING_MODE = os.getenv("TRADING_MODE", "paper")
    STRICT_STARTUP = os.getenv("STRICT_STARTUP", "false").lower() == "true"
    EXCHANGE_ID = os.getenv("EXCHANGE_ID", "binance").strip().lower()
    EXCHANGE_MARKET_TYPE = os.getenv(
        "EXCHANGE_MARKET_TYPE",
        "swap" if EXCHANGE_ID == "hyperliquid" else "future",
    ).strip().lower()
    QUOTE_CURRENCY = os.getenv(
        "QUOTE_CURRENCY",
        "USDC" if EXCHANGE_ID == "hyperliquid" else "USDT",
    ).strip().upper()
    SYMBOL = os.getenv("SYMBOL", f"BTC/{QUOTE_CURRENCY}")
    PORTFOLIO_STATE_FILE = os.getenv(
        "PORTFOLIO_STATE_FILE",
        os.path.join("data", f"portfolio_state_{EXCHANGE_ID}_{QUOTE_CURRENCY}_{TRADING_MODE}.json"),
    )
    EXPERIENCE_LOG_FILE = os.getenv(
        "EXPERIENCE_LOG_FILE",
        os.path.join("data", f"experience_log_{EXCHANGE_ID}_{QUOTE_CURRENCY}_{TRADING_MODE}.jsonl"),
    )
    STRATEGY_INTELLIGENCE_FILE = os.getenv(
        "STRATEGY_INTELLIGENCE_FILE",
        os.path.join("data", f"strategy_intelligence_{EXCHANGE_ID}_{QUOTE_CURRENCY}_{TRADING_MODE}.json"),
    )
    AGENT_ORCHESTRATION_ENABLED = os.getenv("AGENT_ORCHESTRATION_ENABLED", "true").lower() == "true"
    AGENT_MODE = os.getenv("AGENT_MODE", "shadow").strip().lower()  # shadow | active
    AGENT_MIN_CONFIDENCE = float(os.getenv("AGENT_MIN_CONFIDENCE", "0.55"))
    AGENT_REDUCED_SIZE_MULTIPLIER = float(os.getenv("AGENT_REDUCED_SIZE_MULTIPLIER", "0.60"))
    AGENT_LOG_FILE = os.getenv(
        "AGENT_LOG_FILE",
        os.path.join("data", f"agent_decisions_{EXCHANGE_ID}_{QUOTE_CURRENCY}_{TRADING_MODE}.jsonl"),
    )
    AUTO_ROLLOUT_ENABLED = os.getenv("AUTO_ROLLOUT_ENABLED", "false").lower() == "true"
    AUTO_ROLLOUT_ACTIVE_MODE = os.getenv(
        "AUTO_ROLLOUT_ACTIVE_MODE",
        "true" if AGENT_MODE == "active" else "false",
    ).lower() == "true"
    AUTO_ROLLOUT_STATE_FILE = os.getenv(
        "AUTO_ROLLOUT_STATE_FILE",
        os.path.join("data", f"auto_rollout_state_{EXCHANGE_ID}_{QUOTE_CURRENCY}_{TRADING_MODE}.json"),
    )
    AUTO_ROLLOUT_TRIGGER_TRADES = int(os.getenv("AUTO_ROLLOUT_TRIGGER_TRADES", "40"))
    AUTO_ROLLOUT_WINDOW_TRADES = int(os.getenv("AUTO_ROLLOUT_WINDOW_TRADES", "60"))
    AUTO_ROLLOUT_STAGE_FRACTION_PROBE = float(os.getenv("AUTO_ROLLOUT_STAGE_FRACTION_PROBE", "0.25"))
    AUTO_ROLLOUT_STAGE_FRACTION_SCALE = float(os.getenv("AUTO_ROLLOUT_STAGE_FRACTION_SCALE", "0.60"))
    AUTO_ROLLOUT_STAGE_FRACTION_FULL = float(os.getenv("AUTO_ROLLOUT_STAGE_FRACTION_FULL", "1.00"))
    AUTO_ROLLOUT_STAGE_TRADES_PROBE = int(os.getenv("AUTO_ROLLOUT_STAGE_TRADES_PROBE", "8"))
    AUTO_ROLLOUT_STAGE_TRADES_SCALE = int(os.getenv("AUTO_ROLLOUT_STAGE_TRADES_SCALE", "16"))
    AUTO_ROLLOUT_STAGE_TRADES_FULL = int(os.getenv("AUTO_ROLLOUT_STAGE_TRADES_FULL", "24"))
    AUTO_ROLLOUT_MAX_STAGE_DD_PCT = float(os.getenv("AUTO_ROLLOUT_MAX_STAGE_DD_PCT", "4.0"))
    AUTO_ROLLOUT_MIN_WIN_RATE_DELTA = float(os.getenv("AUTO_ROLLOUT_MIN_WIN_RATE_DELTA", "-0.02"))
    AUTO_ROLLOUT_MIN_SHARPE_DELTA = float(os.getenv("AUTO_ROLLOUT_MIN_SHARPE_DELTA", "-0.10"))
    AUTO_ROLLOUT_MAX_DD_INCREASE = float(os.getenv("AUTO_ROLLOUT_MAX_DD_INCREASE", "1.0"))
    AUTO_ROLLOUT_MAX_RISK_VETO_STREAK = int(os.getenv("AUTO_ROLLOUT_MAX_RISK_VETO_STREAK", "3"))
    AUTO_ROLLOUT_POLICY_COOLDOWN_TRADES = int(os.getenv("AUTO_ROLLOUT_POLICY_COOLDOWN_TRADES", "60"))
    AUTO_ROLLOUT_MAX_REJECT_MEMORY = int(os.getenv("AUTO_ROLLOUT_MAX_REJECT_MEMORY", "120"))
    LEARNING_ENABLED = os.getenv("LEARNING_ENABLED", "true").lower() == "true"
    LEARNING_INTERVAL_HOURS = int(os.getenv("LEARNING_INTERVAL_HOURS", "24"))
    LEARNING_MIN_TRADES = int(os.getenv("LEARNING_MIN_TRADES", "50"))
    HYPERLIQUID_TESTNET = os.getenv("HYPERLIQUID_TESTNET", "true").lower() == "true"
    HYPERLIQUID_API_WALLET = os.getenv("HYPERLIQUID_API_WALLET", "")
    HYPERLIQUID_PRIVATE_KEY = os.getenv("HYPERLIQUID_PRIVATE_KEY", "")
    HYPERLIQUID_ACCOUNT_ADDRESS = os.getenv("HYPERLIQUID_ACCOUNT_ADDRESS", "")
    HYPERLIQUID_VAULT_ADDRESS = os.getenv("HYPERLIQUID_VAULT_ADDRESS", "")
    HYPERLIQUID_ENABLE_PRIVATE_ORDERS = os.getenv("HYPERLIQUID_ENABLE_PRIVATE_ORDERS", "false").lower() == "true"
    HYPERLIQUID_ORDER_SLIPPAGE = float(os.getenv("HYPERLIQUID_ORDER_SLIPPAGE", "0.01"))
    HYPERLIQUID_USER_WS_ENABLED = os.getenv("HYPERLIQUID_USER_WS_ENABLED", "true").lower() == "true"
    HYPERLIQUID_WS_STALE_SEC = int(os.getenv("HYPERLIQUID_WS_STALE_SEC", "120"))
    HYPERLIQUID_WS_LOG_EVENTS = os.getenv("HYPERLIQUID_WS_LOG_EVENTS", "false").lower() == "true"
    HYPERLIQUID_ORDER_SYNC_GRACE_SEC = int(os.getenv("HYPERLIQUID_ORDER_SYNC_GRACE_SEC", "90"))
    HYPERLIQUID_PUBLIC_WS_ENABLED = os.getenv("HYPERLIQUID_PUBLIC_WS_ENABLED", "true").lower() == "true"
    HYPERLIQUID_PUBLIC_WS_STALE_SEC = int(os.getenv("HYPERLIQUID_PUBLIC_WS_STALE_SEC", "30"))
    HYPERLIQUID_PUBLIC_WS_QUEUE_SIZE = int(os.getenv("HYPERLIQUID_PUBLIC_WS_QUEUE_SIZE", "12000"))
    
    # System Config
    LOG_LEVEL = "DEBUG"
    DATA_PATH = os.path.join(os.getcwd(), "data")
    
    # Portfolio Config (Phase 32)
    INITIAL_CAPITAL = 10000.0
    FEE_RATE = float(os.getenv("FEE_RATE", "0.0004"))
    
    # Phase 36: Aggressive Multi-Asset Config
    ACTIVE_SYMBOLS = []  # Dynamic - populated from exchange volume ranking
    TOP_COINS_COUNT = 30  # Number of top volume coins to scan
    HYPERLIQUID_RATE_SAFE_TOP_COINS = int(os.getenv("HYPERLIQUID_RATE_SAFE_TOP_COINS", "15"))
    COIN_REFRESH_MINUTES = 15  # Refresh top coins every N minutes
    PREFETCH_WORKERS_DEFAULT = int(os.getenv("PREFETCH_WORKERS_DEFAULT", "4"))
    PREFETCH_WORKERS_HYPERLIQUID = int(os.getenv("PREFETCH_WORKERS_HYPERLIQUID", "2"))
    SCAN_TIMEFRAME = os.getenv("SCAN_TIMEFRAME", os.getenv("TIMEFRAME_LTF", "15m"))  # 15-minute candles for faster signals
    LTF_LOOKBACK = int(os.getenv("LTF_LOOKBACK", "200"))
    HTF_TIMEFRAME = os.getenv("HTF_TIMEFRAME", os.getenv("TIMEFRAME_HTF", "1h"))
    HTF_LOOKBACK = int(os.getenv("HTF_LOOKBACK", "50"))
    DATA_QUALITY_STRIKE_LIMIT = int(os.getenv("DATA_QUALITY_STRIKE_LIMIT", "3"))
    DATA_QUALITY_QUARANTINE_SEC = int(os.getenv("DATA_QUALITY_QUARANTINE_SEC", "1800"))
    DATA_QUALITY_WARN_COOLDOWN_SEC = int(os.getenv("DATA_QUALITY_WARN_COOLDOWN_SEC", "300"))
    MARKETDATA_CONTRACT_ENFORCED = os.getenv("MARKETDATA_CONTRACT_ENFORCED", "true").lower() == "true"
    MARKETDATA_MAX_PRICE_DIVERGENCE_PCT = float(os.getenv("MARKETDATA_MAX_PRICE_DIVERGENCE_PCT", "5.0"))
    MARKETDATA_CONTRACT_LOG_COOLDOWN_SEC = int(os.getenv("MARKETDATA_CONTRACT_LOG_COOLDOWN_SEC", "120"))
    MARKETDATA_STALE_STATE_MAX_SEC = int(os.getenv("MARKETDATA_STALE_STATE_MAX_SEC", "300"))
    MARKETDATA_STALE_TICKER_MAX_SEC = int(os.getenv("MARKETDATA_STALE_TICKER_MAX_SEC", "120"))
    MARKETDATA_STATE_REFRESH_MIN_SEC = int(os.getenv("MARKETDATA_STATE_REFRESH_MIN_SEC", "90"))
    MARKETDATA_REFRESH_SYMBOLS_PER_CYCLE = int(
        os.getenv(
            "MARKETDATA_REFRESH_SYMBOLS_PER_CYCLE",
            "6" if EXCHANGE_ID == "hyperliquid" else "0",
        )
    )
    MARKETDATA_WS_COVERAGE_MIN = float(os.getenv("MARKETDATA_WS_COVERAGE_MIN", "0.60"))
    MARKETDATA_CACHE_HEALTH_LOG_SEC = int(os.getenv("MARKETDATA_CACHE_HEALTH_LOG_SEC", "300"))
    MARKETDATA_WS_CANDLE_ENABLED = os.getenv(
        "MARKETDATA_WS_CANDLE_ENABLED",
        "true" if EXCHANGE_ID == "hyperliquid" else "false",
    ).lower() == "true"
    MARKETDATA_WS_CANDLE_MIN_BARS = int(os.getenv("MARKETDATA_WS_CANDLE_MIN_BARS", "50"))
    MARKETDATA_WS_CANDLE_MAX_1M_BARS = int(os.getenv("MARKETDATA_WS_CANDLE_MAX_1M_BARS", "5000"))
    MARKETDATA_WS_DRAIN_MAX_UPDATES = int(os.getenv("MARKETDATA_WS_DRAIN_MAX_UPDATES", "4000"))
    RATE_GUARD_ENABLED = os.getenv("RATE_GUARD_ENABLED", "true").lower() == "true"
    RATE_GUARD_WINDOW_SEC = int(os.getenv("RATE_GUARD_WINDOW_SEC", "60"))
    RATE_GUARD_429_ESCALATE_HITS = int(os.getenv("RATE_GUARD_429_ESCALATE_HITS", "6"))
    RATE_GUARD_SUCCESS_RECOVERY = int(os.getenv("RATE_GUARD_SUCCESS_RECOVERY", "120"))
    RATE_GUARD_MAX_LEVEL = int(os.getenv("RATE_GUARD_MAX_LEVEL", "3"))
    RATE_GUARD_BUDGET_OHLCV_PER_MIN = int(os.getenv("RATE_GUARD_BUDGET_OHLCV_PER_MIN", "20"))
    RATE_GUARD_BUDGET_ORDERBOOK_PER_MIN = int(os.getenv("RATE_GUARD_BUDGET_ORDERBOOK_PER_MIN", "6"))
    RATE_GUARD_BUDGET_TICKER_SNAPSHOT_PER_MIN = int(os.getenv("RATE_GUARD_BUDGET_TICKER_SNAPSHOT_PER_MIN", "30"))
    RATE_GUARD_BUDGET_BATCH_TICKERS_PER_MIN = int(os.getenv("RATE_GUARD_BUDGET_BATCH_TICKERS_PER_MIN", "4"))
    RATE_GUARD_BUDGET_FUNDING_PER_MIN = int(os.getenv("RATE_GUARD_BUDGET_FUNDING_PER_MIN", "20"))
    RATE_GUARD_BUDGET_TOP_SYMBOLS_PER_MIN = int(os.getenv("RATE_GUARD_BUDGET_TOP_SYMBOLS_PER_MIN", "4"))
    DATA_INGESTION_SYMBOL_LIMIT = int(os.getenv("DATA_INGESTION_SYMBOL_LIMIT", "8"))
    DATA_INGESTION_OHLCV_LIMIT = int(os.getenv("DATA_INGESTION_OHLCV_LIMIT", "120"))
    DATA_INGESTION_TRADE_LIMIT = int(os.getenv("DATA_INGESTION_TRADE_LIMIT", "100"))

    # Strategic WAIT injection (for data diversity). Set to 0.0 to disable.
    STRATEGIC_WAIT_PROB = float(os.getenv("STRATEGIC_WAIT_PROB", _profile_default("STRATEGIC_WAIT_PROB", "0.10")))
    
    # Smart Leverage Config (Phase 35)
    # Leverage settings now respect TRADING_MODE for safety
    BASE_LEVERAGE = int(os.getenv("BASE_LEVERAGE", _profile_default("BASE_LEVERAGE", "10" if TRADING_MODE == "paper" else "2")))
    MAX_LEVERAGE = int(os.getenv("MAX_LEVERAGE", _profile_default("MAX_LEVERAGE", "10" if TRADING_MODE == "paper" else "5")))
    MIN_LEVERAGE = int(os.getenv("MIN_LEVERAGE", _profile_default("MIN_LEVERAGE", "5" if TRADING_MODE == "paper" else "1")))
    RISK_PER_TRADE = float(os.getenv("RISK_PER_TRADE", "0.01"))
    MAX_POSITION_PCT = float(
        os.getenv(
            "MAX_POSITION_PCT",
            _profile_default(
                "MAX_POSITION_PCT",
                os.getenv("RISK_PER_TRADE", "0.20" if TRADING_MODE == "paper" else "0.05"),
            ),
        )
    )  # % of balance per position
    MAX_CONCURRENT_POSITIONS = int(os.getenv("MAX_CONCURRENT_POSITIONS", _profile_default("MAX_CONCURRENT_POSITIONS", "20" if TRADING_MODE == "paper" else "5")))  # Conservative live defaults
    LEVERAGE_SCALING = os.getenv("LEVERAGE_SCALING", "true" if TRADING_MODE == "live" else "false").lower() == "true"
    
    # Expected Value gating (probability * TP - (1-p) * SL)
    EV_GATING = os.getenv("EV_GATING", "true").lower() == "true"
    EV_THRESHOLD = float(os.getenv("EV_THRESHOLD", "0.0"))

    # Portfolio-level risk limits
    MAX_DAILY_LOSS_PCT = float(os.getenv("MAX_DAILY_LOSS_PCT", "5.0"))  # % of initial capital
    MAX_DRAWDOWN_PCT = _drawdown_pct_env(15.0)      # % from peak equity
    VOL_TARGET_DAILY_PCT = float(os.getenv("VOL_TARGET_DAILY_PCT", "2.0"))
    EXPOSURE_CAP_PCT = float(os.getenv("EXPOSURE_CAP_PCT", _profile_default("EXPOSURE_CAP_PCT", "10.0")))      # max gross exposure (1000%)
    CORR_CLUSTER_CAP_PCT = float(os.getenv("CORR_CLUSTER_CAP_PCT", _profile_default("CORR_CLUSTER_CAP_PCT", "4.0")))
    RISK_ALERT_COOLDOWN_SEC = int(os.getenv("RISK_ALERT_COOLDOWN_SEC", "120"))
    STRATEGY_MIN_SAMPLES = int(os.getenv("STRATEGY_MIN_SAMPLES", "20"))
    STRATEGY_WEIGHTING_ENABLED = os.getenv("STRATEGY_WEIGHTING_ENABLED", "true").lower() == "true"
    STRATEGY_FILTER_ENABLED = os.getenv("STRATEGY_FILTER_ENABLED", "true").lower() == "true"
    STRATEGY_FILTER_REGIME_AWARE = os.getenv("STRATEGY_FILTER_REGIME_AWARE", "true").lower() == "true"
    STRATEGY_FILTER_WINDOW = int(os.getenv("STRATEGY_FILTER_WINDOW", "200"))
    STRATEGY_FILTER_MIN_TRADES = int(os.getenv("STRATEGY_FILTER_MIN_TRADES", _profile_default("STRATEGY_FILTER_MIN_TRADES", "30")))
    STRATEGY_FILTER_MIN_WIN_RATE = float(os.getenv("STRATEGY_FILTER_MIN_WIN_RATE", _profile_default("STRATEGY_FILTER_MIN_WIN_RATE", "0.45")))
    STRATEGY_FILTER_MIN_AVG_PNL = float(os.getenv("STRATEGY_FILTER_MIN_AVG_PNL", _profile_default("STRATEGY_FILTER_MIN_AVG_PNL", "0.0")))

    # Loss-category adaptive policy (MetaLearner -> execution controls)
    ADAPTIVE_POLICY_ENABLED = os.getenv("ADAPTIVE_POLICY_ENABLED", "true").lower() == "true"
    ADAPTIVE_POLICY_MIN_SAMPLES = int(os.getenv("ADAPTIVE_POLICY_MIN_SAMPLES", "12"))
    ADAPTIVE_POLICY_MIN_DOMINANCE = float(os.getenv("ADAPTIVE_POLICY_MIN_DOMINANCE", "0.45"))
    ADAPTIVE_POLICY_MAX_SCORE_PENALTY = float(os.getenv("ADAPTIVE_POLICY_MAX_SCORE_PENALTY", "0.30"))
    ADAPTIVE_POLICY_MAX_THRESHOLD_BONUS = float(os.getenv("ADAPTIVE_POLICY_MAX_THRESHOLD_BONUS", "0.10"))
    ADAPTIVE_POLICY_MIN_SIZE_MULTIPLIER = float(os.getenv("ADAPTIVE_POLICY_MIN_SIZE_MULTIPLIER", "0.70"))
    ADAPTIVE_POLICY_MAX_SIZE_MULTIPLIER = float(os.getenv("ADAPTIVE_POLICY_MAX_SIZE_MULTIPLIER", "1.15"))
    ADAPTIVE_POLICY_RECOVERY_WIN_RATE = float(os.getenv("ADAPTIVE_POLICY_RECOVERY_WIN_RATE", "0.58"))

    # Canary + rollback
    CANARY_MODE = os.getenv("CANARY_MODE", "false").lower() == "true"
    CANARY_TRADE_LIMIT = int(os.getenv("CANARY_TRADE_LIMIT", "20"))
    CANARY_MIN_WIN_RATE = float(os.getenv("CANARY_MIN_WIN_RATE", "0.45"))
    CANARY_MAX_DD_PCT = float(os.getenv("CANARY_MAX_DD_PCT", "5.0"))

    # Drift monitoring
    DRIFT_WINDOW = int(os.getenv("DRIFT_WINDOW", "200"))
    DRIFT_ALERT_Z = float(os.getenv("DRIFT_ALERT_Z", "3.0"))
    DIVERGENCE_MIN_TRADES = int(os.getenv("DIVERGENCE_MIN_TRADES", "30"))
    DIVERGENCE_ALERT_COOLDOWN_SEC = int(os.getenv("DIVERGENCE_ALERT_COOLDOWN_SEC", "300"))
    DIVERGENCE_WIN_RATE_TOL = float(os.getenv("DIVERGENCE_WIN_RATE_TOL", "0.15"))
    DIVERGENCE_AVG_PNL_TOL = float(os.getenv("DIVERGENCE_AVG_PNL_TOL", "0.50"))

    # Spoofing detector tuning
    SPOOFING_DETECTION_ENABLED = os.getenv("SPOOFING_DETECTION_ENABLED", "true").lower() == "true"
    SPOOFING_THRESHOLD_SIZE = float(os.getenv("SPOOFING_THRESHOLD_SIZE", "25.0"))
    SPOOFING_MIN_EVENTS = int(os.getenv("SPOOFING_MIN_EVENTS", "8"))
    SPOOFING_LOG_COOLDOWN_SEC = int(os.getenv("SPOOFING_LOG_COOLDOWN_SEC", "120"))

    # Strategy signal thresholds
    MIN_SIGNAL_SCORE = float(os.getenv("MIN_SIGNAL_SCORE", _profile_default("MIN_SIGNAL_SCORE", "0.60")))
    ML_CONFIDENCE_MIN = float(os.getenv("ML_CONFIDENCE_MIN", _profile_default("ML_CONFIDENCE_MIN", "0.65")))
    CROSS_SECTIONAL_MOMENTUM_ENABLED = os.getenv("CROSS_SECTIONAL_MOMENTUM_ENABLED", "true").lower() == "true"
    CROSS_SECTIONAL_MIN_UNIVERSE = int(os.getenv("CROSS_SECTIONAL_MIN_UNIVERSE", "8"))
    CROSS_SECTIONAL_TOP_PCT = float(os.getenv("CROSS_SECTIONAL_TOP_PCT", "0.20"))
    CROSS_SECTIONAL_BOTTOM_PCT = float(os.getenv("CROSS_SECTIONAL_BOTTOM_PCT", "0.20"))
    CROSS_SECTIONAL_MIN_ABS_SPREAD = float(os.getenv("CROSS_SECTIONAL_MIN_ABS_SPREAD", "0.35"))
    VOLATILITY_BREAKOUT_ENABLED = os.getenv("VOLATILITY_BREAKOUT_ENABLED", "true").lower() == "true"
    VOL_BREAKOUT_BBW_SQUEEZE_MAX = float(os.getenv("VOL_BREAKOUT_BBW_SQUEEZE_MAX", "2.00"))
    VOL_BREAKOUT_EXPANSION_RATIO_MIN = float(os.getenv("VOL_BREAKOUT_EXPANSION_RATIO_MIN", "1.25"))
    VOL_BREAKOUT_BASELINE_WINDOW = int(os.getenv("VOL_BREAKOUT_BASELINE_WINDOW", "24"))
    VOL_BREAKOUT_MIN_VOLUME_ZSCORE = float(os.getenv("VOL_BREAKOUT_MIN_VOLUME_ZSCORE", "1.10"))
    VOL_BREAKOUT_MIN_ATR_PCT = float(os.getenv("VOL_BREAKOUT_MIN_ATR_PCT", "0.20"))
    VOL_BREAKOUT_ADMISSION_ENABLED = os.getenv("VOL_BREAKOUT_ADMISSION_ENABLED", "true").lower() == "true"
    VOL_BREAKOUT_ADMISSION_MIN_TRADES = int(os.getenv("VOL_BREAKOUT_ADMISSION_MIN_TRADES", "80"))
    VOL_BREAKOUT_ADMISSION_MIN_WIN_RATE = float(os.getenv("VOL_BREAKOUT_ADMISSION_MIN_WIN_RATE", "0.45"))
    VOL_BREAKOUT_ADMISSION_MIN_AVG_PNL = float(os.getenv("VOL_BREAKOUT_ADMISSION_MIN_AVG_PNL", "0.02"))
    VOL_BREAKOUT_WARMUP_SIZE_MULTIPLIER = float(os.getenv("VOL_BREAKOUT_WARMUP_SIZE_MULTIPLIER", "0.35"))
    RSI_OVERBOUGHT = float(os.getenv("RSI_OVERBOUGHT", "65"))
    RSI_OVERSOLD = float(os.getenv("RSI_OVERSOLD", "35"))
    TREND_SPREAD_MIN = float(os.getenv("TREND_SPREAD_MIN", "0.2"))
    HTF_TREND_SPREAD_MIN = float(os.getenv("HTF_TREND_SPREAD_MIN", "0.1"))
    MIN_VOLUME_ZSCORE = float(os.getenv("MIN_VOLUME_ZSCORE", "1.0"))
    MAX_SPREAD_PCT = float(os.getenv("MAX_SPREAD_PCT", "5.0"))
    MAX_GAP_PCT = float(os.getenv("MAX_GAP_PCT", "1.0"))
    MAX_BODY_PCT = float(os.getenv("MAX_BODY_PCT", "2.0"))
    NEAR_LEVEL_PCT = float(os.getenv("NEAR_LEVEL_PCT", "1.0"))
    FUNDING_ARB_THRESHOLD = float(os.getenv("FUNDING_ARB_THRESHOLD", "0.08"))  # funding rate % threshold
    MM_MAX_SPREAD_PCT = float(os.getenv("MM_MAX_SPREAD_PCT", "0.12"))          # spread cap for market making
    MM_MAX_BODY_PCT = float(os.getenv("MM_MAX_BODY_PCT", "0.80"))              # body cap for market making

    # ATR-based TP/SL (adaptive to volatility)
    ATR_TP_SL_ENABLED = os.getenv("ATR_TP_SL_ENABLED", "true").lower() == "true"
    ATR_TP_MULTIPLIER_SCALP = float(os.getenv("ATR_TP_MULTIPLIER_SCALP", _profile_default("ATR_TP_MULTIPLIER_SCALP", "1.2")))
    ATR_SL_MULTIPLIER_SCALP = float(os.getenv("ATR_SL_MULTIPLIER_SCALP", _profile_default("ATR_SL_MULTIPLIER_SCALP", "0.8")))
    ATR_TP_MULTIPLIER_SWING = float(os.getenv("ATR_TP_MULTIPLIER_SWING", _profile_default("ATR_TP_MULTIPLIER_SWING", "2.5")))
    ATR_SL_MULTIPLIER_SWING = float(os.getenv("ATR_SL_MULTIPLIER_SWING", _profile_default("ATR_SL_MULTIPLIER_SWING", "1.2")))
    
    # Phase 2: Single Position Per Symbol (cooldown protects capital)
    MAX_POSITIONS_PER_SYMBOL = 1   # 1 position per coin (prevents margin overwrite bug)
    ENTRY_COOLDOWN_MINUTES = int(os.getenv("ENTRY_COOLDOWN_MINUTES", "30"))
    
    # Phase 5: Scalp vs Swing Mode
    SCALP_TP_PCT = 1.5    # Take profit for scalp trades
    SCALP_SL_PCT = 1.0    # Stop loss for scalp trades
    SWING_TP_PCT = 6.0    # Take profit for swing trades  
    SWING_SL_PCT = 2.0    # Stop loss for swing trades

    # Trailing Stop Config (lets winners run on SWING trades)
    TRAILING_STOP_ENABLED = os.getenv("TRAILING_STOP_ENABLED", "true").lower() == "true"
    TRAILING_ACTIVATION_MODE = os.getenv("TRAILING_ACTIVATION_MODE", "SWING")  # Only trail on SWING trades
    TRAILING_ATR_MULTIPLIER = float(os.getenv("TRAILING_ATR_MULTIPLIER", "2.0"))  # Trail distance = N × ATR

    # --- Risk Guardian (Kill Switch) ---
    RISK_DAILY_STOP_LOSS_PCT = float(os.getenv("RISK_DAILY_STOP_LOSS_PCT", "-0.03"))
    RISK_MAX_DRAWDOWN_PCT = float(os.getenv("RISK_MAX_DRAWDOWN_PCT", "-0.10"))
    SAFETY_CHECK_ENABLED = os.getenv("SAFETY_CHECK_ENABLED", "true").lower() == "true"

    # --- Feature Integration Flags ---
    DATA_INGESTION_ENABLED = os.getenv("DATA_INGESTION_ENABLED", "false").lower() == "true"
    DATA_INGESTION_INTERVAL_SEC = int(os.getenv("DATA_INGESTION_INTERVAL_SEC", "300"))
    CONTEXT_INGESTION_ENABLED = os.getenv("CONTEXT_INGESTION_ENABLED", "false").lower() == "true"
    CANARY_LAUNCHER_ENABLED = os.getenv("CANARY_LAUNCHER_ENABLED", "false").lower() == "true"
    SHADOW_MODE_ENABLED = os.getenv("SHADOW_MODE_ENABLED", "false").lower() == "true"

    @classmethod
    def validate(cls):
        """Ensure critical keys are present."""
        if not cls.EXCHANGE_API_KEY or not cls.EXCHANGE_SECRET:
            print("WARNING: Exchange keys are missing in .env")
