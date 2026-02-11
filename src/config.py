
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


class Config:
    RISK_PROFILE = RISK_PROFILE
    # API Keys
    EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY", "")
    EXCHANGE_SECRET = os.getenv("EXCHANGE_SECRET", "")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

    # Trading Config
    TRADING_MODE = os.getenv("TRADING_MODE", "paper")
    STRICT_STARTUP = os.getenv("STRICT_STARTUP", "false").lower() == "true"
    EXCHANGE_ID = os.getenv("EXCHANGE_ID", "binance")
    SYMBOL = "BTC/USDT"
    
    # System Config
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    DATA_PATH = os.path.join(os.getcwd(), "data")
    
    # Portfolio Config (Phase 32)
    INITIAL_CAPITAL = 10000.0
    FEE_RATE = 0.0004 # 0.04% for Binance Futures
    
    # Phase 36: Aggressive Multi-Asset Config
    ACTIVE_SYMBOLS = []  # Dynamic - populated from Binance volume
    TOP_COINS_COUNT = 15  # Number of top volume coins to scan
    COIN_REFRESH_MINUTES = 15  # Refresh top coins every N minutes
    SCAN_TIMEFRAME = "15m"  # 15-minute candles for faster signals
    LTF_LOOKBACK = int(os.getenv("LTF_LOOKBACK", "200"))
    HTF_TIMEFRAME = os.getenv("HTF_TIMEFRAME", "1h")
    HTF_LOOKBACK = int(os.getenv("HTF_LOOKBACK", "50"))

    # Strategic WAIT injection (for data diversity). Set to 0.0 to disable.
    STRATEGIC_WAIT_PROB = float(os.getenv("STRATEGIC_WAIT_PROB", _profile_default("STRATEGIC_WAIT_PROB", "0.10")))
    
    # Smart Leverage Config (Phase 35)
    # Leverage settings now respect TRADING_MODE for safety
    BASE_LEVERAGE = int(os.getenv("BASE_LEVERAGE", _profile_default("BASE_LEVERAGE", "10" if TRADING_MODE == "paper" else "2")))
    MAX_LEVERAGE = int(os.getenv("MAX_LEVERAGE", _profile_default("MAX_LEVERAGE", "10" if TRADING_MODE == "paper" else "5")))
    MIN_LEVERAGE = int(os.getenv("MIN_LEVERAGE", _profile_default("MIN_LEVERAGE", "5" if TRADING_MODE == "paper" else "1")))
    MAX_POSITION_PCT = float(os.getenv("MAX_POSITION_PCT", _profile_default("MAX_POSITION_PCT", "0.10")))  # % of balance per position
    MAX_CONCURRENT_POSITIONS = int(os.getenv("MAX_CONCURRENT_POSITIONS", _profile_default("MAX_CONCURRENT_POSITIONS", "20" if TRADING_MODE == "paper" else "5")))  # Conservative live defaults
    LEVERAGE_SCALING = os.getenv("LEVERAGE_SCALING", "true" if TRADING_MODE == "live" else "false").lower() == "true"
    
    # Expected Value gating (probability * TP - (1-p) * SL)
    EV_GATING = os.getenv("EV_GATING", "true").lower() == "true"
    EV_THRESHOLD = float(os.getenv("EV_THRESHOLD", "0.0"))

    # Portfolio-level risk limits
    MAX_DAILY_LOSS_PCT = float(os.getenv("MAX_DAILY_LOSS_PCT", "5.0"))  # % of initial capital
    MAX_DRAWDOWN_PCT = float(os.getenv("MAX_DRAWDOWN_PCT", "15.0"))      # % from peak equity
    VOL_TARGET_DAILY_PCT = float(os.getenv("VOL_TARGET_DAILY_PCT", "2.0"))
    EXPOSURE_CAP_PCT = float(os.getenv("EXPOSURE_CAP_PCT", _profile_default("EXPOSURE_CAP_PCT", "0.60")))      # max gross exposure
    CORR_CLUSTER_CAP_PCT = float(os.getenv("CORR_CLUSTER_CAP_PCT", _profile_default("CORR_CLUSTER_CAP_PCT", "0.40")))
    STRATEGY_MIN_SAMPLES = int(os.getenv("STRATEGY_MIN_SAMPLES", "20"))
    STRATEGY_WEIGHTING_ENABLED = os.getenv("STRATEGY_WEIGHTING_ENABLED", "true").lower() == "true"
    STRATEGY_FILTER_ENABLED = os.getenv("STRATEGY_FILTER_ENABLED", "true").lower() == "true"
    STRATEGY_FILTER_REGIME_AWARE = os.getenv("STRATEGY_FILTER_REGIME_AWARE", "true").lower() == "true"
    STRATEGY_FILTER_WINDOW = int(os.getenv("STRATEGY_FILTER_WINDOW", "200"))
    STRATEGY_FILTER_MIN_TRADES = int(os.getenv("STRATEGY_FILTER_MIN_TRADES", _profile_default("STRATEGY_FILTER_MIN_TRADES", "30")))
    STRATEGY_FILTER_MIN_WIN_RATE = float(os.getenv("STRATEGY_FILTER_MIN_WIN_RATE", _profile_default("STRATEGY_FILTER_MIN_WIN_RATE", "0.45")))
    STRATEGY_FILTER_MIN_AVG_PNL = float(os.getenv("STRATEGY_FILTER_MIN_AVG_PNL", _profile_default("STRATEGY_FILTER_MIN_AVG_PNL", "0.0")))

    # Canary + rollback
    CANARY_MODE = os.getenv("CANARY_MODE", "false").lower() == "true"
    CANARY_TRADE_LIMIT = int(os.getenv("CANARY_TRADE_LIMIT", "20"))
    CANARY_MIN_WIN_RATE = float(os.getenv("CANARY_MIN_WIN_RATE", "0.45"))
    CANARY_MAX_DD_PCT = float(os.getenv("CANARY_MAX_DD_PCT", "5.0"))

    # Drift monitoring
    DRIFT_WINDOW = int(os.getenv("DRIFT_WINDOW", "200"))
    DRIFT_ALERT_Z = float(os.getenv("DRIFT_ALERT_Z", "3.0"))

    # Strategy signal thresholds
    MIN_SIGNAL_SCORE = float(os.getenv("MIN_SIGNAL_SCORE", _profile_default("MIN_SIGNAL_SCORE", "0.60")))
    ML_CONFIDENCE_MIN = float(os.getenv("ML_CONFIDENCE_MIN", _profile_default("ML_CONFIDENCE_MIN", "0.65")))
    RSI_OVERBOUGHT = float(os.getenv("RSI_OVERBOUGHT", "65"))
    RSI_OVERSOLD = float(os.getenv("RSI_OVERSOLD", "35"))
    TREND_SPREAD_MIN = float(os.getenv("TREND_SPREAD_MIN", "0.2"))
    HTF_TREND_SPREAD_MIN = float(os.getenv("HTF_TREND_SPREAD_MIN", "0.1"))
    MIN_VOLUME_ZSCORE = float(os.getenv("MIN_VOLUME_ZSCORE", "1.0"))
    MAX_SPREAD_PCT = float(os.getenv("MAX_SPREAD_PCT", "0.8"))
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

    @classmethod
    def validate(cls):
        """Ensure critical keys are present."""
        if not cls.EXCHANGE_API_KEY or not cls.EXCHANGE_SECRET:
            print("WARNING: Exchange keys are missing in .env")
