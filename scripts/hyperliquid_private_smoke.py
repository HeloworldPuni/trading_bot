import argparse
import json
import logging
import os
import sys

sys.path.append(os.getcwd())

from src.config import Config
from src.exchange.hyperliquid_private import HyperliquidOrderRequest, HyperliquidPrivateClient

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("HyperliquidPrivateSmoke")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Hyperliquid private API smoke runner (connectivity + optional signed actions)"
    )
    parser.add_argument("--symbol", default=Config.SYMBOL, help="Symbol (e.g. BTC/USDC)")
    parser.add_argument("--side", default="BUY", help="BUY/SELL/LONG/SHORT")
    parser.add_argument("--size", type=float, default=0.001, help="Order size in coin units")
    parser.add_argument("--limit-price", type=float, default=None, help="Optional limit price")
    parser.add_argument("--tif", default="Ioc", help="Ioc/Gtc/Alo for limit orders")
    parser.add_argument("--reduce-only", action="store_true", help="Set reduce-only on limit orders")
    parser.add_argument("--cancel-oid", type=int, default=None, help="Cancel existing order id")
    parser.add_argument(
        "--place-order",
        action="store_true",
        help="Actually place one signed order (requires enable flag + credentials)",
    )
    parser.add_argument(
        "--confirm-live",
        action="store_true",
        help="Required when placing/canceling signed actions to prevent accidental execution.",
    )
    parser.add_argument("--testnet", action="store_true", help="Force testnet")
    parser.add_argument("--mainnet", action="store_true", help="Force mainnet")
    args = parser.parse_args()

    testnet = Config.HYPERLIQUID_TESTNET
    if args.testnet and args.mainnet:
        print("Choose only one of --testnet or --mainnet")
        return 2
    if args.testnet:
        testnet = True
    elif args.mainnet:
        testnet = False

    client = HyperliquidPrivateClient(testnet=testnet, auto_connect=False)
    if not client.is_configured():
        print("Missing credentials: set HYPERLIQUID_API_WALLET and HYPERLIQUID_PRIVATE_KEY in .env")
        return 2

    try:
        snapshot = client.connectivity_snapshot()
    except Exception as exc:
        print(f"Connectivity check failed: {exc}")
        return 1

    print(json.dumps(snapshot, indent=2))

    wants_signed_action = bool(args.place_order or args.cancel_oid is not None)
    if not wants_signed_action:
        return 0

    if not Config.HYPERLIQUID_ENABLE_PRIVATE_ORDERS:
        print("Blocked: HYPERLIQUID_ENABLE_PRIVATE_ORDERS=false")
        return 2
    if not args.confirm_live:
        print("Blocked: pass --confirm-live for signed actions.")
        return 2

    try:
        if args.cancel_oid is not None:
            response = client.cancel_order(symbol=args.symbol, oid=args.cancel_oid)
            print(json.dumps(response, indent=2))
            return 0

        if args.place_order:
            request = HyperliquidOrderRequest(
                symbol=args.symbol,
                side=args.side,
                size=args.size,
                limit_price=args.limit_price,
                tif=args.tif,
                reduce_only=bool(args.reduce_only),
            )
            response = client.place_order(request)
            print(json.dumps(response, indent=2))
            return 0
    except Exception as exc:
        print(f"Signed action failed: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
