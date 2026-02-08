
import ccxt
import logging
from typing import Dict, Any, List, Optional
from src.config import Config

logger = logging.getLogger(__name__)

class BinanceConnector:
    def __init__(self):
        self.exchange = None
        self._connect()

    def _connect(self):
        """Initializes the CCXT exchange instance."""
        try:
            exchange_class = getattr(ccxt, Config.EXCHANGE_ID)
            self.exchange = exchange_class({
                'apiKey': Config.EXCHANGE_API_KEY,
                'secret': Config.EXCHANGE_SECRET,
                'enableRateLimit': True,
                'options': {'defaultType': 'future'} # Default to Futures if applicable
            })
            # Test connection (optional, can be skipped for speed)
            # self.exchange.load_markets() 
            logger.info(f"Connected to {Config.EXCHANGE_ID}")
        except Exception as e:
            logger.error(f"Failed to connect to exchange: {e}")
            raise

    def fetch_ohlcv(self, symbol: str, timeframe: str, limit: int = 100) -> List[List]:
        """Fetches OHLCV data."""
        try:
            return self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        except Exception as e:
            logger.error(f"Error fetching candles for {symbol}: {e}")
            return []

    def fetch_balance(self) -> Dict[str, Any]:
        """Fetches account balance (for live trading)."""
        try:
            return self.exchange.fetch_balance()
        except Exception as e:
            logger.error(f"Error fetching balance: {e}")
            return {}
            
    def get_market_structure(self, symbol: str):
        """Fetches ticker/orderbook to help determine volatility/trends."""
        try:
             ticker = self.exchange.fetch_ticker(symbol)
             return ticker
        except Exception as e:
            logger.error(f"Error fetching ticker for {symbol}: {e}")
            return None

    def fetch_funding_rate(self, symbol: str) -> float:
        """
        Fetches the current funding rate for a futures symbol.
        Returns 0.0 if not available (spot markets).
        Extreme funding rates (>0.1% or <-0.1%) can indicate reversals.
        """
        try:
            # Try to fetch funding rate (works for futures)
            funding = self.exchange.fetch_funding_rate(symbol)
            if funding and 'fundingRate' in funding:
                rate = float(funding['fundingRate']) * 100  # Convert to percentage
                logger.debug(f"Funding rate for {symbol}: {rate:.4f}%")
                return rate
            return 0.0
        except Exception as e:
            # Likely spot market or unsupported exchange
            logger.debug(f"Could not fetch funding rate for {symbol}: {e}")
            return 0.0

    def fetch_top_symbols_by_volume(self, limit: int = 15) -> List[str]:
        """
        Phase 1: Dynamically fetch top coins by 24h volume.
        Filters for USDT pairs and excludes stablecoins.
        """
        try:
            # Ensure markets are loaded
            if not self.exchange.markets:
                self.exchange.load_markets()
            
            # Fetch all tickers
            tickers = self.exchange.fetch_tickers()
            
            # Filter and sort
            excluded = ['USDC', 'BUSD', 'DAI', 'TUSD', 'USDP', 'FDUSD', 'USDT']
            usdt_pairs = []
            
            for symbol, ticker in tickers.items():
                # Handle Binance Futures format: BTC/USDT:USDT -> BTC/USDT
                # Match both spot (BTC/USDT) and futures (BTC/USDT:USDT)
                if '/USDT' not in symbol:
                    continue
                
                # Normalize symbol: remove :USDT suffix for futures
                normalized = symbol.split(':')[0] if ':' in symbol else symbol
                    
                # Get base currency (e.g., BTC from BTC/USDT)
                base = normalized.split('/')[0]
                
                # Exclude stablecoins
                if base in excluded:
                    continue
                
                # Must have volume data
                volume = ticker.get('quoteVolume', 0) or 0
                if volume > 0:
                    usdt_pairs.append((normalized, volume))
            
            # Remove duplicates (same base appears in spot and futures)
            seen = set()
            unique_pairs = []
            for symbol, volume in usdt_pairs:
                if symbol not in seen:
                    seen.add(symbol)
                    unique_pairs.append((symbol, volume))
            
            # Sort by volume (descending) and take top N
            unique_pairs.sort(key=lambda x: x[1], reverse=True)
            top_symbols = [pair[0] for pair in unique_pairs[:limit]]
            
            logger.info(f"📊 Top {limit} coins by volume: {', '.join([s.split('/')[0] for s in top_symbols])}")
            return top_symbols
            
        except Exception as e:
            logger.error(f"Error fetching top symbols: {e}")
            # Fallback to default list
            return ["BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT", "DOGE/USDT"]
