import os

from src.config import Config
from src.core.portfolio import PORTFOLIO_STATE_FILE, Portfolio


def test_portfolio_uses_scoped_state_file_by_default():
    original_exchange = Config.EXCHANGE_ID
    original_quote = Config.QUOTE_CURRENCY
    original_mode = Config.TRADING_MODE
    original_state_file = getattr(Config, "PORTFOLIO_STATE_FILE", None)

    try:
        Config.EXCHANGE_ID = "hyperliquid"
        Config.QUOTE_CURRENCY = "USDC"
        Config.TRADING_MODE = "paper"
        Config.PORTFOLIO_STATE_FILE = os.path.join(
            "data",
            f"portfolio_state_{Config.EXCHANGE_ID}_{Config.QUOTE_CURRENCY}_{Config.TRADING_MODE}.json",
        )
        p = Portfolio(initial_balance=1000.0, load_state=False)
        assert p.state_file.endswith("portfolio_state_hyperliquid_USDC_paper.json")
    finally:
        Config.EXCHANGE_ID = original_exchange
        Config.QUOTE_CURRENCY = original_quote
        Config.TRADING_MODE = original_mode
        Config.PORTFOLIO_STATE_FILE = original_state_file


def test_legacy_binance_file_is_still_compatible():
    original_exchange = Config.EXCHANGE_ID
    original_quote = Config.QUOTE_CURRENCY
    original_mode = Config.TRADING_MODE
    original_state_file = getattr(Config, "PORTFOLIO_STATE_FILE", None)

    try:
        Config.EXCHANGE_ID = "binance"
        Config.QUOTE_CURRENCY = "USDT"
        Config.TRADING_MODE = "paper"
        Config.PORTFOLIO_STATE_FILE = PORTFOLIO_STATE_FILE
        p = Portfolio(initial_balance=1000.0, load_state=False)
        assert p.state_file == PORTFOLIO_STATE_FILE
    finally:
        Config.EXCHANGE_ID = original_exchange
        Config.QUOTE_CURRENCY = original_quote
        Config.TRADING_MODE = original_mode
        Config.PORTFOLIO_STATE_FILE = original_state_file
