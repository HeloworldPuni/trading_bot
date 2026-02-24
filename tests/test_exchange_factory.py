import ccxt

from src.exchange import create_exchange_connector


class _FakeExchange:
    def __init__(self, params):
        self.params = params
        self.markets = {}

    def load_markets(self):
        self.markets = {
            "BTC/USDC:USDC": {},
            "ETH/USDC:USDC": {},
            "SOL/USDC:USDC": {},
        }
        return self.markets

    def fetch_tickers(self):
        return {
            "BTC/USDC": {"quoteVolume": 1000.0},
            "BTC/USDC:USDC": {"quoteVolume": 2000.0},
            "ETH/USDC:USDC": {"quoteVolume": 1500.0},
            "USDC/USDC:USDC": {"quoteVolume": 99999.0},
            "DOGE/USDT": {"quoteVolume": 9999.0},
        }

    def fetch_ticker(self, symbol):
        return {"symbol": symbol, "last": 1.0}

    def fetch_ohlcv(self, symbol, timeframe, limit=100):
        return [[0, 1, 1, 1, 1, 1] for _ in range(limit)]

    def fetch_balance(self):
        return {"total": {}}

    def fetch_funding_rate(self, symbol):
        return {"fundingRate": 0.0001}


def test_factory_returns_hyperliquid_connector(monkeypatch):
    monkeypatch.setenv("QUOTE_CURRENCY", "USDC")
    monkeypatch.setenv("EXCHANGE_MARKET_TYPE", "swap")
    monkeypatch.setattr(ccxt, "hyperliquid", _FakeExchange, raising=False)

    connector = create_exchange_connector(exchange_id="hyperliquid")
    assert connector.exchange_id == "hyperliquid"
    assert connector.quote_currency == "USDC"
    assert connector.market_type == "swap"


def test_symbol_translation_for_settlement_suffix(monkeypatch):
    monkeypatch.setenv("QUOTE_CURRENCY", "USDC")
    monkeypatch.setenv("EXCHANGE_MARKET_TYPE", "swap")
    monkeypatch.setattr(ccxt, "hyperliquid", _FakeExchange, raising=False)

    connector = create_exchange_connector(exchange_id="hyperliquid")
    assert connector.to_exchange_symbol("BTC/USDC") == "BTC/USDC:USDC"
    assert connector.normalize_symbol("BTC/USDC:USDC") == "BTC/USDC"


def test_top_volume_scan_returns_normalized_symbols(monkeypatch):
    monkeypatch.setenv("QUOTE_CURRENCY", "USDC")
    monkeypatch.setenv("EXCHANGE_MARKET_TYPE", "swap")
    monkeypatch.setattr(ccxt, "hyperliquid", _FakeExchange, raising=False)

    connector = create_exchange_connector(exchange_id="hyperliquid")
    top = connector.fetch_top_symbols_by_volume(limit=2)
    assert top == ["BTC/USDC", "ETH/USDC"]
