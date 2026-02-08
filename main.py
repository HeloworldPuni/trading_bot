
import time
import argparse
import logging
from typing import List, Dict
from src.config import Config
from src.exchange.connector import BinanceConnector
from src.data.feeder import DataFeeder
from src.engine.system import TradingEngine
from src.execution.paper import PaperExecutor
from src.core.definitions import StrategyType, Action, ActionDirection
from src.core.reward import RewardCalculator
from src.core.meta_learner import MetaLearner
from scripts.learning_scheduler import LearningScheduler

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("adaptive_trader.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("Main")


def calculate_smart_leverage(confidence: float, regime_stable: bool, volatility: str) -> int:
    """
    Phase 35: Calculate leverage based on confidence and market conditions.
    
    Returns leverage multiplier (1x to 10x).
    """
    if not Config.LEVERAGE_SCALING:
        return Config.BASE_LEVERAGE
    
    # Start with base leverage
    leverage = Config.BASE_LEVERAGE
    
    # Scale by confidence (0.5 = base, 0.8+ = max, <0.5 = min)
    if confidence >= 0.80:
        leverage = Config.MAX_LEVERAGE
    elif confidence >= 0.70:
        leverage = min(Config.BASE_LEVERAGE + 3, Config.MAX_LEVERAGE)
    elif confidence >= 0.60:
        leverage = Config.BASE_LEVERAGE
    elif confidence >= 0.50:
        leverage = max(Config.BASE_LEVERAGE - 1, Config.MIN_LEVERAGE)
    else:
        leverage = Config.MIN_LEVERAGE
    
    # Reduce leverage in unstable regimes
    if not regime_stable:
        leverage = max(leverage - 2, Config.MIN_LEVERAGE)
    
    # Reduce leverage in high volatility
    if volatility == "HIGH":
        leverage = max(leverage - 2, Config.MIN_LEVERAGE)
    
    return int(leverage)


def get_trade_mode(regime: str, trend_strength: str) -> tuple:
    """
    Phase 5: Determine trade mode (SCALP vs SWING) based on market conditions.
    Returns (mode, tp_pct, sl_pct)
    """
    # Strong trends = SWING for bigger targets
    if trend_strength in ["STRONG", "VERY_STRONG"]:
        if "BULL" in regime or "BEAR" in regime:
            return "SWING", Config.SWING_TP_PCT, Config.SWING_SL_PCT
    
    # Everything else = SCALP for quick profits
    return "SCALP", Config.SCALP_TP_PCT, Config.SCALP_SL_PCT


def calculate_smart_position_size(balance: float, confidence: float, atr: float, 
                                   avg_atr: float, leverage: int) -> float:
    """
    Hybrid ATR + Confidence Position Sizing.
    
    - Smaller positions when market is volatile (high ATR)
    - Bigger positions when ML is confident
    - Self-adjusting to market conditions
    
    Returns: Position size in USD
    """
    base_size = balance * Config.MAX_POSITION_PCT  # 10% of balance
    
    # Volatility Factor: Scale DOWN in volatile markets (0.5 to 1.5)
    # High ATR = smaller position, Low ATR = larger position
    if avg_atr > 0 and atr > 0:
        volatility_ratio = atr / avg_atr
        # Clamp between 0.5 and 2.0, then invert (high vol = low factor)
        volatility_factor = 1.0 / max(0.5, min(2.0, volatility_ratio))
        volatility_factor = max(0.5, min(1.5, volatility_factor))
    else:
        volatility_factor = 1.0
    
    # Confidence Factor: Scale UP with ML confidence (0.5 to 1.5)
    # Maps confidence 0.0-1.0 to factor 0.5-1.5
    confidence_factor = 0.5 + confidence
    confidence_factor = max(0.5, min(1.5, confidence_factor))
    
    # Calculate final size
    size_usd = base_size * volatility_factor * confidence_factor * leverage
    
    # Cap at 30% of balance (margin protection)
    size_usd = min(size_usd, balance * 0.3)
    
    # Minimum position size of $10
    size_usd = max(size_usd, 10.0)
    
    logger.debug(f"Smart Size: base=${base_size:.0f} × vol={volatility_factor:.2f} × conf={confidence_factor:.2f} × lev={leverage}x = ${size_usd:.0f}")
    
    return size_usd

class TradeTracker:
    def __init__(self, db):
        self.db = db
        self.open_positions: List[Dict] = []
        self.pending_waits: List[Dict] = []

    def add_position(self, action: Action, decision_id: str, entry_price: float, repeats: int):
        self.open_positions.append({
            "id": decision_id,
            "action": action,
            "entry_price": entry_price,
            "entry_time": time.time(),
            "duration": 0,
            "repeats": repeats
        })

    def add_wait(self, action: Action, decision_id: str, current_price: float):
        self.pending_waits.append({
            "id": decision_id,
            "price_at_wait": current_price,
            "time": time.time(),
            "repeats": 0 # Waits don't diminish same way or usually 0
        })

    def update(self, current_price: float):
        # 1. Resolve WAITS (Simple: Resolve after 1 tick/minute for now)
        for wait in self.pending_waits[:]:
            # outcomes: did market drop? if so, good wait.
            change = ((current_price - wait["price_at_wait"]) / wait["price_at_wait"]) * 100
            
            reward = RewardCalculator.calculate_final_reward(
                exit_reason="WAIT_RESOLVED",
                realized_pnl=0.0,
                duration_candles=1,
                is_wait_action=True,
                market_change_during_wait=change,
                repetition_count=wait["repeats"]
            )
            
            self.db.finalize_record(
                decision_id=wait["id"],
                outcome_data={"reason": "WAIT_RESOLVED", "price_change": change},
                final_reward=reward
            )
            self.pending_waits.remove(wait)

        # 2. Resolve TRADES (Mock TP/SL for Paper Mode)
        for pos in self.open_positions[:]:
            pos["duration"] += 1
            # Mock Result (Replace with real logic in V2)
            # For now, just close immediately to test loop
            
            pnl = 0.5 # Fake profit
            exit_reason = "TP"
            
            reward = RewardCalculator.calculate_final_reward(
                exit_reason=exit_reason,
                realized_pnl=pnl,
                duration_candles=pos["duration"],
                repetition_count=pos["repeats"]
            )
            
            self.db.finalize_record(
                decision_id=pos["id"],
                outcome_data={
                    "exit_price": current_price,
                    "pnl": pnl,
                    "reason": exit_reason
                },
                final_reward=reward
            )
            logger.info(f"Trade Finalized (ID: {pos['id']}): Reward = {reward}")
            self.open_positions.remove(pos)

def run_live_mode(symbol: str, run_once: bool = False):
    logger.info("Starting Adaptive Trading Assistant (Closed Loop V1) - LIVE MODE...")
    from src.core.portfolio import Portfolio
    from src.ui.dashboard import Dashboard
    from rich.live import Live
    from datetime import datetime, timedelta
    
    try:
        connector = BinanceConnector()
        feeder = DataFeeder(connector)
        engine = TradingEngine()
        executor = PaperExecutor()
        portfolio = Portfolio()
        dashboard = Dashboard()
        
        # Auto-Learning Systems
        meta_learner = MetaLearner()
        learning_scheduler = LearningScheduler(interval_hours=24, min_trades=50)
        learning_scheduler.start_background()  # Start background retraining
        logger.info("🧠 Auto-learning systems initialized")
        
        # Phase 1: Dynamic coin selection - fetch top 15 by volume
        active_symbols = connector.fetch_top_symbols_by_volume(Config.TOP_COINS_COUNT)
        if not active_symbols:
            active_symbols = ["BTC/USDT", "ETH/USDT", "SOL/USDT"]  # Fallback
        
        last_coin_refresh = datetime.now()  # Track when we last refreshed coins
        
        # Startup PnL refresh - fetch current prices for all restored positions
        if portfolio.active_positions:
            logger.info(f"💰 Refreshing PnL for {len(portfolio.active_positions)} restored positions...")
            for sym in list(portfolio.active_positions.keys()):
                try:
                    ticker = connector.exchange.fetch_ticker(sym)
                    current_price = ticker['last']
                    portfolio.update_metrics(sym, current_price)
                except Exception as e:
                    logger.warning(f"Could not refresh {sym}: {e}")
            logger.info("✅ PnL refresh complete")
        
        logger.info(f"📊 Scanning {len(active_symbols)} coins: {', '.join([s.split('/')[0] for s in active_symbols])}")
        logger.info("Components initialized.")
    except Exception as e:
        logger.critical(f"Init Failed: {e}")
        return

    latest_signal = None
    
    with Live(dashboard.layout, refresh_per_second=1, screen=True) as live:
        while True:
            try:
                # Dynamic coin refresh - catch volume spikes
                if (datetime.now() - last_coin_refresh).total_seconds() > Config.COIN_REFRESH_MINUTES * 60:
                    new_symbols = connector.fetch_top_symbols_by_volume(Config.TOP_COINS_COUNT)
                    if new_symbols and new_symbols != active_symbols:
                        # Log new coins that appeared
                        new_coins = set(new_symbols) - set(active_symbols)
                        if new_coins:
                            logger.info(f"🆕 Volume spike detected! New coins: {', '.join([s.split('/')[0] for s in new_coins])}")
                        active_symbols = new_symbols
                    last_coin_refresh = datetime.now()
                
                # Iterate over our dynamic squad (top 15 by volume)
                for sym in active_symbols:
                    # 1. Observe (with Position Awareness - Phase 34)
                    has_position = 1 if sym in portfolio.active_positions else 0
                    state = feeder.get_current_state(sym, open_positions=has_position)
                    
                    # Fetch Price
                    ticker = connector.exchange.fetch_ticker(sym)
                    current_price = ticker['last']
                    
                    # 2. Decide
                    action, decision_id, repeats = engine.run_analysis(state, data_source="live")
                    confidence = getattr(engine, 'last_confidence', 0.0)
                    
                    # Log coin scan result for visibility
                    if action.strategy == StrategyType.WAIT:
                        logger.info(f"🔍 [{sym}] SCAN: WAIT | Conf: {confidence:.2f} | Regime: {state.market_regime.value} | Reason: {action.reasoning[:50]}...")
                    else:
                        logger.info(f"🎯 [{sym}] SCAN: {action.strategy.name} {action.direction.name} | Conf: {confidence:.2f} | Regime: {state.market_regime.value}")
                    
                    # Update Latest Signal for UI (shows the scan in progress)
                    latest_signal = {
                        "strategy": action.strategy.name,
                        "direction": action.direction.name,
                        "confidence": confidence,
                        "reasoning": action.reasoning,
                        "symbol": sym # Trace which coin gave the signal
                    }
                    
                    # 3. Act & Track
                    if action.strategy != StrategyType.WAIT:
                        # Phase 2: Check cooldown and position limits
                        can_open, block_reason = portfolio.can_open_position(sym)
                        
                        if not can_open:
                            logger.debug(f"⏸️ [{sym}] Blocked: {block_reason}")
                        elif executor.execute(action, sym, current_price, state.atr):
                            # Phase 35: Smart Leverage Calculation
                            confidence = engine.last_confidence if hasattr(engine, 'last_confidence') else 0.5
                            leverage = calculate_smart_leverage(
                                confidence=confidence,
                                regime_stable=state.regime_stable,
                                volatility=state.volatility_level.value
                            )
                            
                            # Phase 5: Dynamic TP/SL based on trade mode
                            trade_mode, tp_pct, sl_pct = get_trade_mode(
                                state.market_regime.value, 
                                state.trend_strength.value
                            )
                            
                            # Calculate TP/SL from current price
                            if action.direction.name == "LONG":
                                tp_price = current_price * (1 + tp_pct / 100)
                                sl_price = current_price * (1 - sl_pct / 100)
                            else:
                                tp_price = current_price * (1 - tp_pct / 100)
                                sl_price = current_price * (1 + sl_pct / 100)
                            
                            # Smart Position Sizing: ATR + Confidence based
                            # Get average ATR for this symbol (use current as fallback)
                            avg_atr = state.atr if state.atr > 0 else 1.0
                            size_usd = calculate_smart_position_size(
                                balance=portfolio.balance,
                                confidence=confidence,
                                atr=state.atr,
                                avg_atr=avg_atr,
                                leverage=leverage
                            )
                                    
                            if portfolio.open_position(sym, action.direction.name, current_price, size_usd, tp_price, sl_price, decision_id,
                                                        entry_regime=state.market_regime.value, entry_atr=state.atr, leverage=leverage):
                                logger.info(f"🚀 [{trade_mode}] {sym} {action.direction.name} | Entry: {current_price:.2f} | Size: ${size_usd:.2f} ({leverage}x) | TP: {tp_price:.2f} ({tp_pct}%) | SL: {sl_price:.2f} ({sl_pct}%)")

                    # 4. Resolve & Learn (Specific to this symbol scan)
                    portfolio.update_metrics(sym, current_price)
                    
                    if sym in portfolio.active_positions:
                        pos = portfolio.active_positions[sym]
                        exit_price = None
                        reason = None
                        
                        if pos['direction'] == "LONG":
                            if current_price >= pos['tp']:
                                exit_price, reason = pos['tp'], "TP"
                            elif current_price <= pos['sl']:
                                exit_price, reason = pos['sl'], "SL"
                        else:
                            if current_price <= pos['tp']:
                                exit_price, reason = pos['tp'], "TP"
                            elif current_price >= pos['sl']:
                                exit_price, reason = pos['sl'], "SL"
                        
                        if exit_price:
                            closed_trade = portfolio.close_position(sym, exit_price, reason,
                                                                     exit_regime=state.market_regime.value, exit_atr=state.atr)
                            logger.info(f"🎯 [POSITION CLOSED] {sym} | Exit: {exit_price:.2f} | Reason: {reason} | PnL: ${closed_trade['realized_pnl_usd']:.2f} ({closed_trade['realized_pnl_pct']:.2f}%)")
                            # Log loss category if present
                            if closed_trade.get('loss_category'):
                                logger.warning(f"📊 LOSS TYPE: {closed_trade['loss_category']}")
                            
                            # MetaLearner: Record trade result for adaptive thresholds
                            pnl_pct = closed_trade.get('realized_pnl_pct', 0.0)
                            meta_learner.record_trade_result(
                                won=pnl_pct > 0,
                                pnl_percent=pnl_pct,
                                context={
                                    "symbol": sym,
                                    "regime": state.market_regime.value,
                                    "exit_reason": reason,
                                    "confidence": confidence
                                }
                            )
                            
                            engine.db.finalize_record(
                                decision_id=pos['decision_id'],
                                outcome_data={
                                    "exit_price": exit_price, 
                                    "reason": reason, 
                                    "pnl_usd": closed_trade['realized_pnl_usd'],
                                    "loss_category": closed_trade.get('loss_category'),
                                    "entry_regime": closed_trade.get('entry_regime'),
                                    "exit_regime": closed_trade.get('exit_regime'),
                                },
                                final_reward=1.0 if reason == "TP" else -1.0
                            )


                    # Periodically update dashboard even during the squad scan
                    summary = portfolio.get_summary()
                    live.update(dashboard.generate_renderable(
                        summary, 
                        list(portfolio.active_positions.values()), 
                        portfolio.trade_history,
                        latest_signal
                    ))
                
                if run_once: break
                time.sleep(60) # 1 Minute Cycle for the entire squad

            except Exception as e:
                logger.error(f"Cycle Error: {e}")
                if run_once: break
                time.sleep(10)

            except Exception as e:
                logger.error(f"Cycle Error: {e}")
                if run_once: break
                time.sleep(10)

def run_replay_mode(csv_path: str, period_id: str = None, symbol: str = "BTC/USDT", no_throttle: bool = False, log_suffix: str = None):
    logger.info(f"Starting REPLAY MODE with {csv_path} (Period ID: {period_id}, Symbol: {symbol})...")
    from src.data.replay_feeder import ReplayFeeder
    from src.core.balancer import BalanceSupervisor
    
    feeder = ReplayFeeder(csv_path, symbol=symbol)
    engine = TradingEngine(log_suffix=log_suffix)
    engine.db.enable_buffer_mode()
    # Executor: In replay, we don't use PaperExecutor. execution is simulated instantly.
    # Tracker: Needs to handle instant flow.
    tracker = TradeTracker(engine.db)
    
    count = 0
    # HOLDING_HORIZON is now variable (Phase 15)
    active_trade = None # {entry_price, direction, exit_step, decision_id, repeats}
    
    while True:
        # --- PHASE 12: EXPERIENCE BALANCING ---
        # Check Stats before proceeding (or after? Requirements say "after logging" usually, but here checking globally)
        # Check if we should throttle
        if not no_throttle:
            stats = engine.db.get_stats()
            throttle, reason = BalanceSupervisor.check(stats)
            if throttle:
                 logger.warning(f"BALANCER: Throttling Replay! {reason}")
                 time.sleep(2.0)
             
        # 1. Get Next State (Past Data Only)
        # Advances feeder index by 1.
        state = feeder.get_next_state()
        if not state:
            break
        
        # Current logical step is `count`
        # Current "Price" at this state is the Close of the last candle provided in state.
        current_candle = feeder.get_latest_candle()
        if not current_candle: 
            break
        current_price = current_candle[4]
            
        # 2. Manage Active Trade (Check Exit)
        if active_trade:
            if count >= active_trade['exit_step']:
                # Resolve Trade
                exit_price = current_price
                entry_price = active_trade['entry_price']
                repeats = active_trade['repeats']
                decision_id = active_trade['decision_id']
                direction = active_trade['direction']
                
                pnl = 0.0
                if entry_price > 0:
                    if direction == ActionDirection.LONG:
                        pnl = (exit_price - entry_price) / entry_price * 100
                    elif direction == ActionDirection.SHORT:
                        pnl = (entry_price - exit_price) / entry_price * 100
                else:
                    logger.warning(f"Skipping PnL calculation for trade {decision_id} due to zero entry_price.")
                    
                duration = count - active_trade['start_step']
                
                from src.core.reward import RewardCalculator
                reward = RewardCalculator.calculate_final_reward(
                   exit_reason="TIME_EXIT",
                   realized_pnl=pnl,
                   duration_candles=duration,
                   repetition_count=repeats
                )
                
                engine.db.finalize_record(
                   decision_id=decision_id,
                   outcome_data={
                       "entry_price": entry_price,
                       "exit_price": exit_price,
                       "pnl": pnl,
                       "holding_period": duration,
                       "reason": "TIME_EXIT"
                   },
                   final_reward=reward
                )
                
                # Close Position
                active_trade = None
                if tracker.open_positions:
                    tracker.open_positions.pop()
                    
            else:
                # Trade still active.
                # Inject knowledge into State so Engine knows we are exposed
                state.current_open_positions = 1
                
        # 3. Decide (Tagged as 'replay')
        # Engine sees the modified state
        action, decision_id, repeats = engine.run_analysis(state, data_source="replay", market_period_id=period_id)
        
        if action.strategy != StrategyType.WAIT:
            # Check Gating: If we have active trade, ignore new signals (or assumed filtered by Engine)
            # But if Engine says BUY despite us setting positions=1 (maybe Risk allows it?), 
            # we adhere to user rule: "No additional trades in same direction".
            # For simplicity in this phase, we enforce 1 active trade max.
            if active_trade is None:
                # Execution: Fill at Next Open (T+1)
                entry_candle = feeder.get_future_candle(offset=0)
                if entry_candle:
                    # entry_price = entry_candle[1] # Open
                    
                    # PHASE 14: Realistic Entry Simulation
                    # entry_price = Open * (1 ± small random slippage)
                    import random
                    slippage_pct = random.uniform(0.0002, 0.0005) # 0.02% to 0.05%
                    jitter_direction = random.choice([-1, 1]) # Unbiased
                    entry_price_raw = entry_candle[1]
                    entry_price = entry_price_raw * (1 + (jitter_direction * slippage_pct))
                    
                    # Schedule Exit
                    # If we enter at T+1 (Step count+1 implicitly?). 
                    # Actually, `count` tracks the State Index T.
                    # We enter at Open of T+1.
                    # We hold for N candles from entry.
                    # Exit at Close of T+N.
                    # PHASE 15: Variable Holding Horizon
                    holding_horizon = random.randint(3, 8)
                    
                    active_trade = {
                        'entry_price': entry_price,
                        'direction': action.direction,
                        'exit_step': count + holding_horizon,
                        'start_step': count,
                        'decision_id': decision_id,
                        'repeats': repeats
                    }
                    
                    logger.info(f"Replay Trade OPEN: {action.direction} @ {entry_price:.2f} (Slip: {jitter_direction*slippage_pct*100:.4f}%, Horizon: {holding_horizon})")
                    tracker.add_position(action, decision_id, entry_price, repeats)
        
        else:
             # WAIT
             tracker.add_wait(action, decision_id, current_price)
             tracker.update(current_price)
        
        if count % 100 == 0:
            status = "OPEN" if active_trade else "FLAT"
            logger.info(f"Replay Step {count} | Action: {action.strategy.name} | Status: {status}")
            
        count += 1
            
    # Flush pending updates to disk
    engine.db.flush_records()
    logger.info("Replay Finished (End of Data).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Adaptive Trading Assistant")
    parser.add_argument("--symbol", type=str, default=Config.SYMBOL, help="Trading Pair (e.g., BTC/USDT)")
    parser.add_argument("--once", action="store_true", help="Run a single analysis cycle and exit")
    parser.add_argument("--replay", type=str, default=None, help="Path to CSV file for Replay Mode")
    parser.add_argument("--period-id", type=str, default=None, help="Market Period ID for Replay Mode (e.g. BTC_2021_BULL)")
    parser.add_argument("--no-throttle", action="store_true", help="Bypass distribution balancing for high-speed replay")
    parser.add_argument("--log-suffix", type=str, default=None, help="Suffix for log file (e.g. btc, eth)")
    
    args = parser.parse_args()
    
    if args.replay:
        run_replay_mode(
            args.replay, 
            period_id=args.period_id, 
            symbol=args.symbol, 
            no_throttle=args.no_throttle,
            log_suffix=args.log_suffix
        )
    else:
        run_live_mode(args.symbol, run_once=args.once)
