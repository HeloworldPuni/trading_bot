from src.exchange.hyperliquid_private import (
    HyperliquidPrivateClient,
    NonceThrottle,
    symbol_to_hyperliquid_coin,
)


def test_symbol_mapping_for_perp():
    assert symbol_to_hyperliquid_coin("BTC/USDC", market_type="swap") == "BTC"
    assert symbol_to_hyperliquid_coin("ETH/USDC:USDC", market_type="future") == "ETH"


def test_symbol_mapping_for_spot():
    assert symbol_to_hyperliquid_coin("HYPE/USDC", market_type="spot") == "HYPE/USDC"


def test_nonce_throttle_is_monotonic():
    throttle = NonceThrottle()
    n1 = throttle.reserve_slot()
    n2 = throttle.reserve_slot()
    n3 = throttle.reserve_slot()
    assert n1 < n2 < n3


def test_parse_exchange_response_resting():
    raw = {
        "status": "ok",
        "response": {
            "type": "order",
            "data": {"statuses": [{"resting": {"oid": 12345}}]},
        },
    }
    parsed = HyperliquidPrivateClient.parse_exchange_response(raw)
    assert parsed["ok"] is True
    assert parsed["order_status"] == "resting"
    assert parsed["oid"] == 12345


def test_parse_exchange_response_error():
    raw = {
        "status": "ok",
        "response": {
            "type": "order",
            "data": {"statuses": [{"error": "Order must have minimum value of $10."}]},
        },
    }
    parsed = HyperliquidPrivateClient.parse_exchange_response(raw)
    assert parsed["ok"] is False
    assert parsed["order_status"] == "error"
    assert "minimum value" in parsed["error"]


def test_tif_normalization():
    assert HyperliquidPrivateClient._normalize_tif("ioc") == "Ioc"
    assert HyperliquidPrivateClient._normalize_tif("GTC") == "Gtc"
