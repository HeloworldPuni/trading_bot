
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Config:
    # API Keys
    EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY", "")
    EXCHANGE_SECRET = os.getenv("EXCHANGE_SECRET", "")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

    # Trading Config
    TRADING_MODE = os.getenv("TRADING_MODE", "paper")
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
    
    # Smart Leverage Config (Phase 35)
    # Leverage settings now respect TRADING_MODE for safety
    BASE_LEVERAGE = int(os.getenv("BASE_LEVERAGE", "10" if TRADING_MODE == "paper" else "2"))
    MAX_LEVERAGE = int(os.getenv("MAX_LEVERAGE", "10" if TRADING_MODE == "paper" else "5"))
    MIN_LEVERAGE = int(os.getenv("MIN_LEVERAGE", "5" if TRADING_MODE == "paper" else "1"))
    MAX_POSITION_PCT = float(os.getenv("MAX_POSITION_PCT", "0.10"))  # 10% of balance per position
    MAX_CONCURRENT_POSITIONS = int(os.getenv("MAX_CONCURRENT_POSITIONS", "20" if TRADING_MODE == "paper" else "5"))  # Conservative live defaults
    LEVERAGE_SCALING = os.getenv("LEVERAGE_SCALING", "true" if TRADING_MODE == "live" else "false").lower() == "true"
    
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
