
import sys
import os
import time
import logging
from datetime import datetime
import warnings

# Suppress XGBoost/Pickle compatibility warnings (benign)
warnings.filterwarnings("ignore", category=UserWarning, message=".*XGBoost.*")


# Add project root to path
sys.path.append(os.getcwd())

from src.exchange import create_exchange_connector
from src.data.feeder import LiveFeeder
from src.engine.system import TradingEngine
from src.deployment.shadow import ShadowExecutor
from src.core.definitions import StrategyType, ActionDirection
from src.config import Config

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("shadow_run.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("ShadowRunner")

def main():
    print(f"\n{'='*60}")
    print(f"   INSTITUTIONAL SHADOW TRADER v2 (Full Pipeline) - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    print("Initializing System Stack...")
    
    # 1. Infrastructure Layer
    connector = create_exchange_connector()
    feeder = LiveFeeder(connector)
    print("  [OK] Data Layer (Feeder + Connector)")
    
    # 2. Decision Engine (The Brain)
    # This loads ML models, Risk Policies, and Strategy Logic
    engine = TradingEngine(log_suffix="_shadow")
    print("  [OK] Decision Engine (ML + Strategies + Risk)")
    
    # 3. Execution Layer (Virtual)
    shadow = ShadowExecutor(initial_capital=10000.0)
    print(f"  [OK] Execution Layer (Shadow Cap: ${shadow.balance})")
    
    # Define Universe
    pairs = Config.ACTIVE_SYMBOLS or connector.fetch_top_symbols_by_volume(5)
    if not pairs:
        pairs = connector.fallback_symbols(limit=5)
    print(f"\nScanning Universe: {pairs}")
    print("Press Ctrl+C to Stop.\n")
    
    try:
        while True:
            for symbol in pairs:
                try:
                    # A. Market State Construction (Phase 1-4)
                    # Fetches OHLCV, calculates Features, Regimes, Clusters
                    state = feeder.get_current_state(symbol, open_positions=0)
                    
                    if state.current_risk_state == "DANGER":
                        logger.warning(f"Skipping {symbol}: Data Quality / Risk Danger")
                        continue

                    # B. Decision Analysis (Phase 5-10)
                    # Run Strategies -> Filter by ML Confidence -> Validate by Risk -> Audit
                    action, decision_id, repeats = engine.run_analysis(state, data_source="shadow")
                    
                    # C. Execution Logic (Phase 11)
                    # C. Execution Logic (Phase 11)
                    if action.strategy != StrategyType.WAIT:
                        # Check if we already have a position in this symbol
                        current_pos = shadow.inventory.get(symbol)
                        existing_qty = current_pos.size if current_pos else 0.0
                        
                        # Prevent duplicate entries (Spam Protection)
                        # Only allow trade if:
                        # 1. No position exists
                        # 2. OR Signal is opposite to current position (Close/Flip)
                        is_same_direction = (existing_qty > 0 and action.direction == ActionDirection.LONG) or \
                                          (existing_qty < 0 and action.direction == ActionDirection.SHORT)
                        
                        if is_same_direction:
                            logger.info(f"  [SKIP] {symbol}: Already {action.direction.value} ({existing_qty:.4f}). Pyramiding disabled in Shadow.")
                            continue

                        logger.info(f"SIGNAL: {symbol} {action.direction.value} | Strat: {action.strategy.name} | Conf: {engine.last_confidence:.2f}")
                        
                        # Calculate Position Size (Simplified for Shadow)
                        # Use Adjusted Risk % from Action (e.g. 1.0 = 1% of capital)
                        risk_pct = action.adjusted_risk if action.adjusted_risk > 0 else 1.0
                        allocation = shadow.balance * (risk_pct / 100.0)
                        
                        # Re-fetch price for execution accuracy
                        ticker = connector.get_market_structure(symbol)
                        exec_price = float(ticker.get('last', 0.0)) if ticker else 0.0
                        
                        if exec_price > 0:
                            qty = allocation / exec_price
                            
                            # If flipping, add existing size to close it first (Netting)
                            if (existing_qty > 0 and action.direction == ActionDirection.SHORT) or \
                               (existing_qty < 0 and action.direction == ActionDirection.LONG):
                                qty += abs(existing_qty)
                            
                            order = {
                                "symbol": symbol,
                                "side": action.direction.value, # LONG/SHORT -> BUY/SELL mapping needed?
                                "type": "MARKET",
                                "amount": qty,
                                "price": exec_price
                            }
                            
                            # Map Direction to Side
                            if action.direction == ActionDirection.LONG:
                                order['side'] = 'BUY'
                            elif action.direction == ActionDirection.SHORT:
                                order['side'] = 'SELL'
                            else:
                                continue # Flat

                            # Execute
                            status = shadow.submit_order(order)
                            logger.info(f"  -> Order {status}: {order['side']} {qty:.4f} {symbol}")
                            
                    else:
                        # Log heartbeat for WAIT actions (verbose only if interesting)
                        if engine.last_confidence > 0.6: # Interesting but blocked?
                             logger.info(f"  [WAIT] {symbol}: High Conf ({engine.last_confidence:.2f}) but Wait. Reason: {action.reasoning}")
                
                except Exception as e:
                    logger.error(f"Error processing {symbol}: {e}")
                    # continue

            # Dashboard Update
            if time.time() % 10 < 2:
                # Extract simple price map from full tickers
                tickers = connector.refresh_all_tickers() or {}
                prices = {s: float(t.get('last') or 0.0) for s, t in tickers.items() if t.get('last')}
                print(f"  [SCAN] Equity: ${shadow.get_equity(prices):.2f} | Active Positions: {len(shadow.inventory)}")

            # Rate Limit Protection
            time.sleep(2.0) 

    except KeyboardInterrupt:
        print("\nStopping Shadow Mode...")
        tickers = connector.refresh_all_tickers() or {}
        prices = {s: float(t.get('last') or 0.0) for s, t in tickers.items() if t.get('last')}
        print(f"Final Equity: ${shadow.get_equity(prices):.2f}")
        
if __name__ == "__main__":
    main()
