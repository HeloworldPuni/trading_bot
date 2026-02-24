from typing import Optional

from src.config import Config

from .ccxt_connector import BinanceConnector, CCXTConnector, HyperliquidConnector


def create_exchange_connector(exchange_id: Optional[str] = None) -> CCXTConnector:
    """
    Create an exchange connector based on configured venue.
    """
    venue = (exchange_id or Config.EXCHANGE_ID or "binance").strip().lower()

    if venue == "hyperliquid":
        return HyperliquidConnector()
    if venue == "binance":
        return BinanceConnector()

    return CCXTConnector(
        exchange_id=venue,
        quote_currency=Config.QUOTE_CURRENCY,
        market_type=Config.EXCHANGE_MARKET_TYPE,
        settlement_currency=Config.QUOTE_CURRENCY,
    )
