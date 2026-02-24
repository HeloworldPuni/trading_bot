
import time
import os
import argparse
import logging
import sys
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import List, Dict
from src.config import Config
from src.exchange import (
    HyperliquidPublicStream,
    HyperliquidRealtimeState,
    HyperliquidUserStream,
    create_exchange_connector,
    create_hyperliquid_private_client,
)
from src.data.feeder import DataFeeder
from src.engine.system import TradingEngine
from src.execution.paper import PaperExecutor
from src.execution.hyperliquid_live import HyperliquidLiveExecutor
from src.core.definitions import StrategyType, Action, ActionDirection
from src.core.trade_utils import calculate_tp_sl
from src.core.reward import RewardCalculator
from src.core.meta_learner import MetaLearner
from src.core.risk_controls import PortfolioRiskManager, compute_daily_vol, compute_gross_exposure, cluster_exposure
from src.core.allocator import StrategyPerformanceTracker, BanditAllocator
from src.agent.orchestrator import AgentOrchestrator
from src.agent.rollout_manager import AutoRolloutManager
from src.monitoring.drift import DriftMonitor
from src.monitoring.canary import CanaryMonitor
from src.monitoring.divergence import DivergenceMonitor
from src.marketdata import (
    CandleStore,
    MarketDataCache,
    build_market_input_snapshot,
    extract_ticker_last_price,
    is_safe_state_signature,
    market_state_from_payload,
    validate_market_input_snapshot,
)
from scripts.learning_scheduler import LearningScheduler
from scripts.startup_checks import run_startup_checks
# Phase 1: Safety Layer
from src.risk.guardian import RiskGuardian
from src.deployment.safety import SafetyLock
from src.data.quality import validate_ohlcv
# Phase 2: Observability
from src.monitoring.decision_audit import get_auditor
from src.monitoring.latency import LatencyMonitor
from src.monitoring.performance import PerformanceMonitor
# Phase 3: Data Pipeline
from src.data.ingestor import DataIngestor
# Phase 4: Risk Metrics & Canary
from src.risk.metrics import RiskMetrics
from src.deployment.canary import CanaryLauncher
# Phase 5: Spoofing Detection
from src.features.spoofing import SpoofingDetector


def _configure_console_encoding() -> None:
    """
    Prevent UnicodeEncodeError on Windows consoles.
    """
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


_configure_console_encoding()

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
    
    logger.debug(
        "Smart Size: base=$%.0f x vol=%.2f x conf=%.2f x lev=%sx = $%.0f",
        base_size,
        volatility_factor,
        confidence_factor,
        leverage,
        size_usd,
    )
    
    return size_usd


def _load_strategy_intelligence_state(perf_tracker: StrategyPerformanceTracker, bandit: BanditAllocator) -> None:
    path = Config.STRATEGY_INTELLIGENCE_FILE
    if not path or not os.path.exists(path):
        return
    try:
        with open(path, "r", encoding="utf-8") as f:
            state = json.load(f)
        perf_tracker.load_dict(state.get("performance_tracker", {}))
        bandit.load_dict(state.get("bandit_allocator", {}))
        logger.info("Loaded strategy intelligence state from %s", path)
    except Exception as e:
        logger.warning("Failed to load strategy intelligence state: %s", e)


def _save_strategy_intelligence_state(perf_tracker: StrategyPerformanceTracker, bandit: BanditAllocator) -> None:
    path = Config.STRATEGY_INTELLIGENCE_FILE
    if not path:
        return
    try:
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        payload = {
            "performance_tracker": perf_tracker.to_dict(),
            "bandit_allocator": bandit.to_dict(),
            "updated_at": datetime.now().isoformat(),
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
    except Exception as e:
        logger.warning("Failed to save strategy intelligence state: %s", e)

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
    logger.info(
        "Starting Adaptive Trading Assistant (Closed Loop V1) - %s MODE on %s...",
        Config.TRADING_MODE.upper(),
        Config.EXCHANGE_ID,
    )
    from src.core.portfolio import Portfolio
    from src.ui.dashboard import Dashboard
    from rich.live import Live
    from datetime import datetime, timedelta
    
    try:
        connector = create_exchange_connector()
        feeder = DataFeeder(connector)
        engine = TradingEngine()
        executor = PaperExecutor()
        hl_live_executor = None
        hl_realtime = None
        hl_user_stream = None
        hl_public_stream = None
        learning_scheduler = None
        agent_orchestrator = None
        auto_rollout = None
        portfolio = Portfolio()
        portfolio.backfill_open_position_strategies()
        dashboard = Dashboard()

        if Config.EXCHANGE_ID == "hyperliquid" and Config.HYPERLIQUID_PUBLIC_WS_ENABLED:
            try:
                hl_public_stream = HyperliquidPublicStream(
                    quote_currency=Config.QUOTE_CURRENCY,
                    testnet=Config.HYPERLIQUID_TESTNET,
                    stale_timeout_sec=Config.HYPERLIQUID_PUBLIC_WS_STALE_SEC,
                    queue_size=Config.HYPERLIQUID_PUBLIC_WS_QUEUE_SIZE,
                )
                hl_public_stream.start()
                logger.info("Hyperliquid public websocket stream enabled.")
            except Exception as e:
                hl_public_stream = None
                logger.warning(f"Hyperliquid public websocket unavailable, continuing with REST: {e}")

        if (
            Config.EXCHANGE_ID == "hyperliquid"
            and Config.TRADING_MODE == "live"
            and Config.HYPERLIQUID_ENABLE_PRIVATE_ORDERS
        ):
            hl_client = create_hyperliquid_private_client(auto_connect=False)
            snapshot = hl_client.connectivity_snapshot()
            if not snapshot.get("ok"):
                raise RuntimeError(f"Hyperliquid private connectivity failed: {snapshot}")
            hl_live_executor = HyperliquidLiveExecutor(hl_client)
            hl_realtime = HyperliquidRealtimeState()
            logger.info("Hyperliquid private execution enabled (signed orders active).")
            if Config.HYPERLIQUID_USER_WS_ENABLED:
                ws_user = snapshot.get("account_address") or Config.HYPERLIQUID_ACCOUNT_ADDRESS or Config.HYPERLIQUID_API_WALLET
                try:
                    hl_user_stream = HyperliquidUserStream(
                        user_address=ws_user,
                        testnet=Config.HYPERLIQUID_TESTNET,
                        stale_timeout_sec=Config.HYPERLIQUID_WS_STALE_SEC,
                    )
                    hl_user_stream.start()
                    logger.info("Hyperliquid user websocket stream enabled.")
                except Exception as e:
                    hl_user_stream = None
                    logger.warning(f"Hyperliquid websocket stream unavailable, continuing without ws: {e}")
            try:
                bootstrap_sizes = hl_live_executor.fetch_exchange_position_sizes()
                hl_realtime.seed_positions(bootstrap_sizes)
                logger.info("[HL] Reconciliation bootstrap loaded (%s coins).", len(bootstrap_sizes))
            except Exception as e:
                logger.warning(f"[HL] Initial position bootstrap failed, waiting for websocket fills: {e}")
        
        # Auto-Learning Systems (Now integrated into TradingEngine)
        meta_learner = engine.meta_learner
        risk_manager = PortfolioRiskManager(initial_equity=portfolio.equity)
        drift_monitor = DriftMonitor(window=Config.DRIFT_WINDOW, alert_z=Config.DRIFT_ALERT_Z)
        canary_monitor = CanaryMonitor(initial_equity=portfolio.equity)
        divergence_monitor = DivergenceMonitor()
        perf_tracker = StrategyPerformanceTracker(window=Config.STRATEGY_FILTER_WINDOW)
        bandit = BanditAllocator()
        _load_strategy_intelligence_state(perf_tracker, bandit)
        daily_returns: List[float] = []
        cluster_map = {}
        try:
            with open("data/cluster_map.json", "r", encoding="utf-8") as f:
                cluster_map = json.load(f)
        except Exception:
            cluster_map = {}
            logger.info("Cluster map unavailable. Using per-symbol fallback clusters.")

        # Set divergence baseline from recent backtest metrics if available
        try:
            if os.path.exists("reports/backtest_baseline.json"):
                with open("reports/backtest_baseline.json", "r", encoding="utf-8") as f:
                    divergence_monitor.set_baseline(json.load(f))
        except Exception:
            pass
        learning_scheduler = None
        if Config.LEARNING_ENABLED:
            learning_scheduler = LearningScheduler(
                interval_hours=Config.LEARNING_INTERVAL_HOURS,
                min_trades=Config.LEARNING_MIN_TRADES,
                data_log_path=Config.EXPERIENCE_LOG_FILE,
            )
            learning_scheduler.start_background()
            logger.info(
                "Auto-learning scheduler active (interval=%sh, min_trades=%s).",
                Config.LEARNING_INTERVAL_HOURS,
                Config.LEARNING_MIN_TRADES,
            )
        else:
            logger.info("Auto-learning scheduler disabled (LEARNING_ENABLED=false).")
        logger.info("Auto-learning systems initialized")

        if Config.AGENT_ORCHESTRATION_ENABLED:
            agent_orchestrator = AgentOrchestrator(
                log_path=Config.AGENT_LOG_FILE,
                min_confidence=Config.AGENT_MIN_CONFIDENCE,
                reduced_size_multiplier=Config.AGENT_REDUCED_SIZE_MULTIPLIER,
            )
            logger.info("Agent orchestration enabled (mode=%s).", Config.AGENT_MODE)
        else:
            logger.info("Agent orchestration disabled.")

        if Config.AUTO_ROLLOUT_ENABLED:
            auto_rollout = AutoRolloutManager(
                state_file=Config.AUTO_ROLLOUT_STATE_FILE,
                trigger_trades=Config.AUTO_ROLLOUT_TRIGGER_TRADES,
                window_trades=Config.AUTO_ROLLOUT_WINDOW_TRADES,
                max_stage_dd_pct=Config.AUTO_ROLLOUT_MAX_STAGE_DD_PCT,
            )
            logger.info("Auto-rollout enabled. Champion=%s", auto_rollout.snapshot().get("champion_version"))
        else:
            logger.info("Auto-rollout disabled.")

        # === Phase 1: Safety Layer ===
        risk_guardian = RiskGuardian(
            daily_stop_loss_pct=Config.RISK_DAILY_STOP_LOSS_PCT,
            max_drawdown_pct=Config.RISK_MAX_DRAWDOWN_PCT,
        )
        logger.info(
            "Risk Guardian active (daily_stop=%.1f%%, max_dd=%.1f%%)",
            Config.RISK_DAILY_STOP_LOSS_PCT * 100, Config.RISK_MAX_DRAWDOWN_PCT * 100,
        )
        safety_lock = None
        if Config.SAFETY_CHECK_ENABLED:
            try:
                safety_lock = SafetyLock(config_paths=[".env"])
                logger.info("Safety Lock active (config integrity monitoring).")
            except Exception as sl_err:
                logger.warning(f"Safety Lock init failed: {sl_err}")

        # === Phase 2: Observability ===
        decision_auditor = get_auditor()
        latency_monitor = LatencyMonitor()
        performance_monitor = PerformanceMonitor()
        logger.info("Observability layer active (decision audit, latency, performance).")

        # === Phase 3: Data Pipeline ===
        data_ingestor = None
        if Config.DATA_INGESTION_ENABLED:
            try:
                data_ingestor = DataIngestor(connector)
                logger.info("Data ingestor active — persisting OHLCV/trades/orderbook per cycle.")
            except Exception as di_err:
                logger.warning(f"Data ingestor init failed: {di_err}")

        # === Phase 5: Context Ingestors (scaffold) ===
        context_ingestors = []
        if Config.CONTEXT_INGESTION_ENABLED:
            try:
                from src.data.context.sentiment import SentimentIngestor
                from src.data.context.onchain import WhaleIngestor
                from src.data.context.macro import MacroIngestor
                context_ingestors = [SentimentIngestor(), WhaleIngestor(), MacroIngestor()]
                logger.info("Context ingestors active (sentiment, whale, macro).")
            except Exception as ci_err:
                logger.warning(f"Context ingestors init failed: {ci_err}")

        # === Phase 6: Shadow Executor ===
        shadow_executor = None
        if Config.SHADOW_MODE_ENABLED:
            try:
                from src.deployment.shadow import ShadowExecutor
                shadow_executor = ShadowExecutor(initial_capital=portfolio.balance)
                logger.info("Shadow executor active (paper trading alongside live).")
            except Exception as se_err:
                logger.warning(f"Shadow executor init failed: {se_err}")

        prev_orderbooks = {}  # For spoofing detection (Phase 5)

        
        # Sync MetaLearner with portfolio trade history (catch up on missed trades)
        if portfolio.trade_history:
            meta_learner.sync_from_history(portfolio.trade_history)
        
        # Phase 1: Dynamic coin selection - fetch top symbols by volume
        scan_limit = max(1, int(Config.TOP_COINS_COUNT))
        if Config.EXCHANGE_ID.lower() == "hyperliquid":
            rate_safe_limit = max(1, int(Config.HYPERLIQUID_RATE_SAFE_TOP_COINS))
            if scan_limit > rate_safe_limit:
                logger.info(
                    "Applying Hyperliquid rate-safe scan cap: %s -> %s symbols",
                    scan_limit,
                    rate_safe_limit,
                )
            scan_limit = min(scan_limit, rate_safe_limit)

        restored_symbols: List[str] = []
        if portfolio.active_positions:
            seen = set()
            for raw_sym, positions in portfolio.active_positions.items():
                if not positions:
                    continue
                norm = connector.normalize_symbol(raw_sym)
                if norm and norm not in seen:
                    seen.add(norm)
                    restored_symbols.append(norm)
            if restored_symbols:
                logger.info(
                    "Bootstrapping scan universe from %s restored position symbols.",
                    len(restored_symbols),
                )

        active_symbols = restored_symbols[:scan_limit]
        if len(active_symbols) < scan_limit and not restored_symbols:
            discovered = connector.fetch_top_symbols_by_volume(scan_limit)
            for sym in discovered:
                if sym not in active_symbols:
                    active_symbols.append(sym)
                if len(active_symbols) >= scan_limit:
                    break
        if not active_symbols:
            active_symbols = connector.fallback_symbols(limit=scan_limit)
        if not active_symbols:
            fallback_symbol = symbol or Config.SYMBOL
            logger.warning(
                "No symbols returned from volume scan/fallback. Using fallback symbol: %s",
                fallback_symbol,
            )
            active_symbols = [fallback_symbol]
        
        last_coin_refresh = datetime.now()  # Track when we last refreshed coins
        
        # Startup PnL refresh - fetch current prices for all restored positions
        if portfolio.active_positions:
            logger.info(
                "Refreshing PnL for %s restored positions...",
                len(portfolio.get_all_positions()),
            )
            refresh_started = time.time()
            refresh_budget_sec = 8.0
            updated_positions = 0
            cached_tickers = {}
            try:
                cached_tickers = connector.refresh_all_tickers() or {}
            except Exception:
                cached_tickers = {}
            for sym in list(portfolio.active_positions.keys()):
                try:
                    if time.time() - refresh_started > refresh_budget_sec:
                        logger.warning(
                            "Startup PnL refresh budget exceeded (%.1fs). Continuing with partial refresh.",
                            refresh_budget_sec,
                        )
                        break
                    norm_sym = connector.normalize_symbol(sym)
                    ticker = cached_tickers.get(sym) or cached_tickers.get(norm_sym) or {}
                    current_price = extract_ticker_last_price(ticker)
                    if current_price is None:
                        continue
                    portfolio.update_metrics(sym, current_price)
                    updated_positions += 1
                except Exception as e:
                    logger.warning(f"Could not refresh {sym}: {e}")
            logger.info(
                "PnL refresh complete (%s/%s positions updated).",
                updated_positions,
                len(portfolio.get_all_positions()),
            )
        
        logger.info(
            "Scanning %s coins: %s",
            len(active_symbols),
            ", ".join([s.split("/")[0] for s in active_symbols]),
        )
        # Validated Config
        logger.info(f"Loaded Config: RISK={Config.RISK_PROFILE} SCORE={Config.MIN_SIGNAL_SCORE} CONF={Config.ML_CONFIDENCE_MIN} WAIT={Config.STRATEGIC_WAIT_PROB} AUTO_ROLLOUT={Config.AUTO_ROLLOUT_ENABLED}")
        
        # Initialize components initialized.")
        logger.info("Components initialized.")
    except Exception as e:
        logger.critical(f"Init Failed: {e}")
        return

    latest_signal = None
    last_divergence_log_ts = 0.0
    last_data_ingestion_ts = 0.0
    last_exposure_log_ts = 0.0
    last_spoof_log_ts: Dict[str, float] = {}
    last_cluster_log_ts: Dict[str, float] = {}
    last_contract_log_ts: Dict[str, float] = {}
    contract_failure_streak: Dict[str, int] = {}
    contract_quarantine_until: Dict[str, float] = {}
    contract_quarantine_log_ts: Dict[str, float] = {}
    last_cache_health_log_ts = 0.0
    last_ws_status_log_ts = 0.0
    last_rate_guard_log_ts = 0.0
    refresh_cursor = 0
    scan_cursor = 0
    marketdata_cache = MarketDataCache()
    ws_candle_store = CandleStore(max_1m_bars=max(1000, int(Config.MARKETDATA_WS_CANDLE_MAX_1M_BARS)))
    exchange_position_sizes: Dict[str, float] = hl_realtime.snapshot_position_sizes() if hl_realtime else {}
    exchange_position_sizes_ok = (not bool(hl_live_executor)) or bool(hl_realtime and hl_realtime.position_state_ready)
    last_exchange_position_sync_ts = time.time() if exchange_position_sizes_ok else 0.0

    def _bootstrap_marketdata_cache_from_experience(symbols: List[str], max_lines: int = 8000) -> int:
        path = Config.EXPERIENCE_LOG_FILE
        if not path or not os.path.exists(path):
            return 0
        targets = {connector.normalize_symbol(s) for s in symbols if s}
        if not targets:
            return 0

        from collections import deque

        tail = deque(maxlen=max(1000, int(max_lines)))
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                tail.append(line)

        seeded = 0
        seen = set()
        for line in reversed(tail):
            if len(seen) >= len(targets):
                break
            try:
                rec = json.loads(line)
            except Exception:
                continue
            state_payload = rec.get("market_state")
            state = market_state_from_payload(state_payload)
            if not state:
                continue
            sym = connector.normalize_symbol(state.symbol)
            if sym not in targets or sym in seen:
                continue
            if is_safe_state_signature(state):
                continue
            ticker = None
            if getattr(state, "current_price", 0.0) and state.current_price > 0:
                ticker = {
                    "last": float(state.current_price),
                    "symbol": sym,
                    "_exchange_symbol": sym,
                    "_price_source": "portfolio_state",
                }
            marketdata_cache.upsert(sym, state=state, ticker=ticker, source="experience_bootstrap")
            seen.add(sym)
            seeded += 1
        return seeded

    try:
        seeded_symbols = _bootstrap_marketdata_cache_from_experience(active_symbols)
        if seeded_symbols > 0:
            logger.info(
                "Seeded market-data cache from experience log for %s symbols.",
                seeded_symbols,
            )
    except Exception as e:
        logger.warning(f"Market-data cache bootstrap skipped: {e}")
    
    try:
        with Live(dashboard.layout, refresh_per_second=1, screen=True) as live:
            # Render an explicit boot frame so the screen does not show bare Layout boxes.
            try:
                initial_summary = portfolio.get_summary()
                live.update(
                    dashboard.generate_renderable(
                        initial_summary,
                        portfolio.get_all_positions(),
                        portfolio.trade_history,
                        latest_signal={
                            "strategy": "WAIT",
                            "direction": "FLAT",
                            "confidence": 0.0,
                            "reasoning": "Bootstrapping first scan cycle",
                            "symbol": "--",
                        },
                        alerts=[],
                        meta_learner_summary=engine.meta_learner.get_summary(),
                    )
                )
            except Exception:
                pass
            while True:
                try:
                    # Dynamic coin refresh - catch volume spikes
                    if (datetime.now() - last_coin_refresh).total_seconds() > Config.COIN_REFRESH_MINUTES * 60:
                        new_symbols = connector.fetch_top_symbols_by_volume(scan_limit)
                        if new_symbols and new_symbols != active_symbols:
                            # Log new coins that appeared
                            new_coins = set(new_symbols) - set(active_symbols)
                            if new_coins:
                                logger.info(
                                    "Volume spike detected. New coins: %s",
                                    ", ".join([s.split("/")[0] for s in new_coins]),
                                )
                            active_symbols = new_symbols
                        last_coin_refresh = datetime.now()

                    rate_guard_profile = {}
                    try:
                        rate_guard_profile = getattr(connector, "get_rate_guard_profile", lambda: {})() or {}
                    except Exception:
                        rate_guard_profile = {}

                    # Position-first scanning:
                    # 1) Always scan symbols with open positions first (exit/risk critical path).
                    # 2) Then scan discovery symbols from top-volume list.
                    now_cycle_ts = time.time()
                    for q_sym, until_ts in list(contract_quarantine_until.items()):
                        if now_cycle_ts >= float(until_ts):
                            contract_quarantine_until.pop(q_sym, None)
                            contract_failure_streak.pop(q_sym, None)
                            contract_quarantine_log_ts.pop(q_sym, None)
                            logger.info("[DATA CONTRACT] Quarantine cleared for %s.", q_sym)

                    open_symbols: List[str] = []
                    for pos_sym, pos_items in portfolio.active_positions.items():
                        entries = pos_items if isinstance(pos_items, list) else [pos_items]
                        if any(entries):
                            open_symbols.append(connector.normalize_symbol(pos_sym))
                    # Preserve order while deduplicating
                    open_symbols = list(dict.fromkeys([s for s in open_symbols if s]))
                    open_symbol_set = set(open_symbols)

                    discovery_symbols: List[str] = []
                    for raw_sym in active_symbols:
                        norm_sym = connector.normalize_symbol(raw_sym)
                        if not norm_sym or norm_sym in open_symbol_set:
                            continue
                        until_ts = float(contract_quarantine_until.get(norm_sym, 0.0))
                        if until_ts > now_cycle_ts:
                            last_q_log_ts = contract_quarantine_log_ts.get(norm_sym, 0.0)
                            if now_cycle_ts - last_q_log_ts >= max(
                                30, Config.MARKETDATA_CONTRACT_LOG_COOLDOWN_SEC
                            ):
                                logger.info(
                                    "[DATA CONTRACT] %s skipped (quarantined %.0fs remaining).",
                                    norm_sym,
                                    until_ts - now_cycle_ts,
                                )
                                contract_quarantine_log_ts[norm_sym] = now_cycle_ts
                            continue
                        discovery_symbols.append(norm_sym)
                    discovery_symbols = list(dict.fromkeys(discovery_symbols))

                    scan_multiplier = float(rate_guard_profile.get("scan_symbol_multiplier", 1.0))
                    cycle_discovery = list(discovery_symbols)
                    if cycle_discovery and scan_multiplier < 1.0:
                        cycle_count = max(3, int(round(len(cycle_discovery) * scan_multiplier)))
                        cycle_count = min(len(cycle_discovery), cycle_count)
                        if cycle_count < len(cycle_discovery):
                            start_idx = scan_cursor % len(cycle_discovery)
                            rotated = cycle_discovery[start_idx:] + cycle_discovery[:start_idx]
                            cycle_discovery = rotated[:cycle_count]
                            scan_cursor = (start_idx + cycle_count) % len(discovery_symbols)

                    cycle_symbols = open_symbols + cycle_discovery

                    now_guard_ts = time.time()
                    if rate_guard_profile and (now_guard_ts - last_rate_guard_log_ts) >= 120:
                        logger.info(
                            "[RATE-GUARD] level=%s multiplier=%.2f scan=%s/%s refresh_cap=%s allow_batch_ticker=%s allow_orderbook=%s 429_window=%s",
                            rate_guard_profile.get("level"),
                            rate_guard_profile.get("multiplier", 1.0),
                            len(cycle_symbols),
                            len(active_symbols),
                            rate_guard_profile.get("max_refresh_symbols_per_cycle"),
                            rate_guard_profile.get("allow_batch_ticker"),
                            rate_guard_profile.get("allow_orderbook"),
                            rate_guard_profile.get("429_hits_window"),
                        )
                        last_rate_guard_log_ts = now_guard_ts

                    if hl_user_stream and hl_realtime:
                        ws_events = hl_user_stream.pop_events(max_items=200)
                        if ws_events:
                            ws_stats = hl_realtime.apply_events(ws_events)
                            exchange_position_sizes = hl_realtime.snapshot_position_sizes()
                            exchange_position_sizes_ok = hl_realtime.position_state_ready
                            if Config.HYPERLIQUID_WS_LOG_EVENTS:
                                logger.info(
                                    "[HL-WS] events=%s fills=%s/%s orders=%s",
                                    ws_stats.get("events", 0),
                                    ws_stats.get("fills_applied", 0),
                                    ws_stats.get("fills_seen", 0),
                                    ws_stats.get("order_updates_applied", 0),
                                )

                    if hl_live_executor and not hl_user_stream:
                        now_ts = time.time()
                        if now_ts - last_exchange_position_sync_ts >= 20.0:
                            try:
                                exchange_position_sizes = hl_live_executor.fetch_exchange_position_sizes()
                                if hl_realtime:
                                    hl_realtime.seed_positions(exchange_position_sizes)
                                exchange_position_sizes_ok = True
                                last_exchange_position_sync_ts = now_ts
                            except Exception as e:
                                logger.error(f"Hyperliquid position sync fetch failed: {e}")
                                exchange_position_sizes_ok = False
                    elif hl_live_executor and hl_user_stream and hl_realtime:
                        exchange_position_sizes = hl_realtime.snapshot_position_sizes()
                        exchange_position_sizes_ok = hl_realtime.position_state_ready
                        if (not exchange_position_sizes_ok) and (time.time() - last_exchange_position_sync_ts >= 60.0):
                            # Websocket-first flow: retry REST only until initial state is known.
                            try:
                                bootstrap_sizes = hl_live_executor.fetch_exchange_position_sizes()
                                hl_realtime.seed_positions(bootstrap_sizes)
                                exchange_position_sizes = hl_realtime.snapshot_position_sizes()
                                exchange_position_sizes_ok = hl_realtime.position_state_ready
                                last_exchange_position_sync_ts = time.time()
                                logger.info("[HL] Reconciliation bootstrap retry succeeded.")
                            except Exception as e:
                                logger.warning(f"[HL] Reconciliation bootstrap retry failed: {e}")
                    try:
                        cooldown_remaining = float(getattr(connector, "get_degraded_remaining", lambda: 0.0)())
                    except Exception:
                        cooldown_remaining = 0.0
                    if cooldown_remaining > 0.0:
                        wait_sec = min(3.0, cooldown_remaining)
                        logger.info(
                            "Exchange cooldown active (%.1fs). Waiting %.1fs before cycle prefetch.",
                            cooldown_remaining,
                            wait_sec,
                        )
                        time.sleep(wait_sec)
                    cycle_tickers: Dict[str, Dict] = {}
                    batch_tickers_ok = False
                    ws_tickers: Dict[str, Dict] = {}
                    active_norm_symbols = {connector.normalize_symbol(s) for s in cycle_symbols}
                    active_norm_symbols.update(
                        connector.normalize_symbol(s) for s in portfolio.active_positions.keys()
                    )
                    ws_updates_ingested = 0
                    if hl_public_stream and Config.MARKETDATA_WS_CANDLE_ENABLED:
                        try:
                            ws_updates = hl_public_stream.pop_price_updates(
                                max_items=max(100, int(Config.MARKETDATA_WS_DRAIN_MAX_UPDATES))
                            )
                            for upd in ws_updates:
                                u_sym = connector.normalize_symbol(str(upd.get("symbol") or ""))
                                if not u_sym or (active_norm_symbols and u_sym not in active_norm_symbols):
                                    continue
                                ws_candle_store.ingest_tick(
                                    u_sym,
                                    upd.get("price"),
                                    upd.get("ts"),
                                )
                                ws_updates_ingested += 1
                        except Exception:
                            pass
                    if hl_public_stream and hl_public_stream.is_healthy():
                        ws_tickers = hl_public_stream.snapshot_tickers(
                            max_age_sec=Config.HYPERLIQUID_PUBLIC_WS_STALE_SEC
                        )
                        if ws_tickers:
                            cycle_tickers.update(ws_tickers)
                            for ws_sym, ws_tk in ws_tickers.items():
                                marketdata_cache.upsert(ws_sym, ticker=ws_tk, source="hl_ws")

                    ws_coverage = 0.0
                    if cycle_symbols:
                        covered = 0
                        for sym in cycle_symbols:
                            norm = connector.normalize_symbol(sym)
                            if sym in cycle_tickers or norm in cycle_tickers:
                                covered += 1
                        ws_coverage = covered / max(1, len(cycle_symbols))

                    allow_batch_ticker = bool(rate_guard_profile.get("allow_batch_ticker", True))
                    use_rest_ticker_refresh = (
                        allow_batch_ticker
                        and ws_coverage < max(0.0, min(1.0, Config.MARKETDATA_WS_COVERAGE_MIN))
                    )
                    if use_rest_ticker_refresh:
                        try:
                            rest_tickers = connector.refresh_all_tickers() or {}
                            if rest_tickers:
                                cycle_tickers.update(rest_tickers)
                                batch_tickers_ok = True
                        except Exception:
                            pass
                    else:
                        batch_tickers_ok = bool(cycle_tickers)

                    ready_candle_symbols = 0
                    if Config.MARKETDATA_WS_CANDLE_ENABLED and active_norm_symbols:
                        ready_candle_symbols = ws_candle_store.symbols_with_min_bars(
                            list(active_norm_symbols),
                            Config.SCAN_TIMEFRAME,
                            max(50, int(Config.MARKETDATA_WS_CANDLE_MIN_BARS)),
                        )

                    now_ws_ts = time.time()
                    if hl_public_stream and (now_ws_ts - last_ws_status_log_ts) >= 120:
                        logger.info(
                            "[HL-PUBLIC-WS] healthy=%s tickers=%s coverage=%.0f%% rest_refresh=%s candles_ready=%s/%s ws_updates=%s",
                            hl_public_stream.is_healthy(),
                            len(ws_tickers),
                            ws_coverage * 100.0,
                            use_rest_ticker_refresh,
                            ready_candle_symbols,
                            len(active_norm_symbols),
                            ws_updates_ingested,
                        )
                        last_ws_status_log_ts = now_ws_ts

                    if auto_rollout:
                        rollout_event = auto_rollout.maybe_create_candidate(portfolio.trade_history)
                        if rollout_event:
                            logger.info(f"[AUTO-ROLLOUT] {rollout_event}")
                    
                    # === PHASE 1: Safety checks at cycle start ===
                    risk_guardian.update_state(portfolio.equity)
                    if not risk_guardian.check_system_health():
                        logger.critical(f"[RISK GUARDIAN] KILL SWITCH: {risk_guardian.state.kill_reason}")
                        if run_once: break
                        time.sleep(60)
                        continue
                    if safety_lock and not safety_lock.check_integrity():
                        logger.critical("[SAFETY LOCK] Config integrity breach detected!")

                    # ═══ PARALLEL DATA PREFETCH (all symbols at once) ═══
                    # Parallel prefetch with budgeted symbol refresh and local cache fallback.
                    refresh_budget = max(0, int(Config.MARKETDATA_REFRESH_SYMBOLS_PER_CYCLE))
                    refresh_cap = int(rate_guard_profile.get("max_refresh_symbols_per_cycle", refresh_budget))
                    if refresh_cap > 0:
                        refresh_budget = min(refresh_budget, refresh_cap)
                    open_symbol_set = set(open_symbols)
                    refresh_symbols = set(open_symbols)
                    allow_orderbook = bool(rate_guard_profile.get("allow_orderbook", True))
                    discovery_cycle_symbols = [s for s in cycle_symbols if s not in open_symbol_set]
                    if not open_symbols:
                        refresh_symbols = set(cycle_symbols)
                        if cycle_symbols and refresh_budget > 0 and refresh_budget < len(cycle_symbols):
                            start_idx = refresh_cursor % len(cycle_symbols)
                            chosen: List[str] = []
                            for i in range(refresh_budget):
                                chosen.append(cycle_symbols[(start_idx + i) % len(cycle_symbols)])
                            refresh_symbols = set(chosen)
                            refresh_cursor = (start_idx + refresh_budget) % len(cycle_symbols)
                    else:
                        # Always refresh open-position symbols; remaining budget goes to discovery symbols.
                        remaining_budget = max(0, refresh_budget - len(refresh_symbols))
                        if discovery_cycle_symbols and remaining_budget > 0:
                            if remaining_budget >= len(discovery_cycle_symbols):
                                refresh_symbols.update(discovery_cycle_symbols)
                            else:
                                start_idx = refresh_cursor % len(discovery_cycle_symbols)
                                chosen: List[str] = []
                                for i in range(remaining_budget):
                                    chosen.append(
                                        discovery_cycle_symbols[(start_idx + i) % len(discovery_cycle_symbols)]
                                    )
                                refresh_symbols.update(chosen)
                                refresh_cursor = (start_idx + remaining_budget) % len(discovery_cycle_symbols)

                    def _prefetch_symbol(sym):
                        """Fetch state + ticker + orderbook in parallel with cache fallback."""
                        try:
                            has_pos = portfolio.count_positions_for_symbol(sym)
                            norm_sym = connector.normalize_symbol(sym)
                            stale_state = (
                                marketdata_cache.get_state(sym, Config.MARKETDATA_STALE_STATE_MAX_SEC)
                                or marketdata_cache.get_state(norm_sym, Config.MARKETDATA_STALE_STATE_MAX_SEC)
                            )
                            stale_ticker = (
                                marketdata_cache.get_ticker(sym, Config.MARKETDATA_STALE_TICKER_MAX_SEC)
                                or marketdata_cache.get_ticker(norm_sym, Config.MARKETDATA_STALE_TICKER_MAX_SEC)
                                or {}
                            )
                            stale_orderbook = (
                                marketdata_cache.get_orderbook(sym, Config.MARKETDATA_STALE_TICKER_MAX_SEC)
                                or marketdata_cache.get_orderbook(norm_sym, Config.MARKETDATA_STALE_TICKER_MAX_SEC)
                                or {}
                            )
                            snap = marketdata_cache.get_snapshot(sym) or marketdata_cache.get_snapshot(norm_sym)
                            state_age_sec = None
                            if snap and snap.state_updated_at > 0:
                                state_age_sec = max(0.0, time.time() - snap.state_updated_at)

                            state_refresh_due = (
                                stale_state is None
                                or (
                                    sym in refresh_symbols
                                    and (
                                        state_age_sec is None
                                        or state_age_sec >= max(0, int(Config.MARKETDATA_STATE_REFRESH_MIN_SEC))
                                    )
                                )
                            )
                            ticker_missing = extract_ticker_last_price(stale_ticker) is None
                            if not state_refresh_due and not ticker_missing and stale_state is not None:
                                return sym, stale_state, stale_ticker, stale_orderbook, None

                            ws_ohlcv = None
                            if state_refresh_due and Config.MARKETDATA_WS_CANDLE_ENABLED:
                                ws_rows = ws_candle_store.get_recent_ohlcv(
                                    norm_sym,
                                    Config.SCAN_TIMEFRAME,
                                    limit=max(50, Config.LTF_LOOKBACK),
                                )
                                if len(ws_rows) >= max(50, int(Config.MARKETDATA_WS_CANDLE_MIN_BARS)):
                                    ws_ohlcv = ws_rows

                            st = stale_state
                            state_source = "live"
                            if state_refresh_due:
                                degraded_remaining = float(
                                    getattr(connector, "get_degraded_remaining", lambda: 0.0)()
                                )
                                if degraded_remaining > 0.0 and stale_state is not None and ws_ohlcv is None:
                                    st = stale_state
                                else:
                                    st = feeder.get_current_state(
                                        sym,
                                        open_positions=has_pos,
                                        ohlcv_override=ws_ohlcv,
                                    )
                                    if ws_ohlcv is not None:
                                        state_source = "ws_candle"
                                    if is_safe_state_signature(st) and stale_state is not None:
                                        st = stale_state

                            tk = (
                                cycle_tickers.get(sym)
                                or cycle_tickers.get(norm_sym)
                                or stale_ticker
                                or {}
                            )
                            if extract_ticker_last_price(tk) is None:
                                if batch_tickers_ok:
                                    tk = connector.get_market_structure(sym) or {}
                                elif st and st.current_price:
                                    tk = {"last": st.current_price, "_price_source": "ohlcv_fallback"}

                            ob = stale_orderbook
                            if (
                                allow_orderbook
                                and
                                Config.SPOOFING_DETECTION_ENABLED
                                and (has_pos > 0 or sym in prev_orderbooks)
                            ):
                                ob = connector.fetch_order_book(sym, depth=10) or stale_orderbook

                            if st and not is_safe_state_signature(st):
                                marketdata_cache.upsert(sym, state=st, source=state_source)
                            if extract_ticker_last_price(tk) is not None:
                                marketdata_cache.upsert(sym, ticker=tk, source="live")
                            if ob:
                                marketdata_cache.upsert(sym, orderbook=ob, source="live")
                            return sym, st, tk, ob, None
                        except Exception as exc:
                            stale_state = marketdata_cache.get_state(sym, Config.MARKETDATA_STALE_STATE_MAX_SEC)
                            stale_ticker = marketdata_cache.get_ticker(sym, Config.MARKETDATA_STALE_TICKER_MAX_SEC) or {}
                            stale_orderbook = marketdata_cache.get_orderbook(sym, Config.MARKETDATA_STALE_TICKER_MAX_SEC) or {}
                            if stale_state is not None:
                                return sym, stale_state, stale_ticker, stale_orderbook, None
                            return sym, None, {}, {}, exc

                    prefetched: Dict[str, tuple] = {}
                    prefetch_workers = (
                        Config.PREFETCH_WORKERS_HYPERLIQUID
                        if Config.EXCHANGE_ID.lower() == "hyperliquid"
                        else Config.PREFETCH_WORKERS_DEFAULT
                    )
                    with ThreadPoolExecutor(max_workers=max(1, int(prefetch_workers))) as pool:
                        futures = {pool.submit(_prefetch_symbol, s): s for s in cycle_symbols}
                        for fut in as_completed(futures):
                            sym, st, tk, ob, err = fut.result()
                            if err:
                                logger.warning(f"Prefetch failed for {sym}: {err}")
                            prefetched[sym] = (st, tk, ob)

                    now_cache_ts = time.time()
                    if now_cache_ts - last_cache_health_log_ts >= max(30, Config.MARKETDATA_CACHE_HEALTH_LOG_SEC):
                        cache_health = marketdata_cache.snapshot_health(now_ts=now_cache_ts)
                        logger.info(
                            "[MARKETDATA CACHE] symbols=%s state=%s ticker=%s max_state_age=%s max_ticker_age=%s refresh_budget=%s/%s",
                            cache_health.get("symbols"),
                            cache_health.get("with_state"),
                            cache_health.get("with_ticker"),
                            f"{cache_health.get('max_state_age_sec'):.1f}s" if cache_health.get("max_state_age_sec") is not None else "n/a",
                            f"{cache_health.get('max_ticker_age_sec'):.1f}s" if cache_health.get("max_ticker_age_sec") is not None else "n/a",
                            len(refresh_symbols),
                            len(cycle_symbols),
                        )
                        last_cache_health_log_ts = now_cache_ts

                    # Iterate over our dynamic squad (top 30 by volume)
                    for sym in cycle_symbols:
                        state, ticker, curr_book = prefetched.get(sym, (None, {}, {}))
                        if state is None:
                            continue

                        # Phase 2: Record tick arrival for latency tracking
                        latency_monitor.record_tick_arrival(sym)

                        current_price = extract_ticker_last_price(ticker)
                        if current_price is None and getattr(state, "current_price", None):
                            current_price = state.current_price
                            ticker = dict(ticker or {})
                            ticker["last"] = current_price
                            ticker["_price_source"] = "ohlcv_fallback"
                        if current_price is None:
                            logger.warning(f"Skipping {sym}: ticker last price unavailable.")
                            continue

                        norm_sym = connector.normalize_symbol(sym)

                        if Config.MARKETDATA_CONTRACT_ENFORCED:
                            market_snapshot = build_market_input_snapshot(
                                symbol=sym,
                                state=state,
                                ticker=ticker,
                                current_price=current_price,
                            )
                            snapshot_ok, snapshot_issues = validate_market_input_snapshot(
                                market_snapshot,
                                max_price_divergence_pct=Config.MARKETDATA_MAX_PRICE_DIVERGENCE_PCT,
                            )
                            if not snapshot_ok:
                                fail_count = int(contract_failure_streak.get(norm_sym, 0)) + 1
                                contract_failure_streak[norm_sym] = fail_count
                                now_ts = time.time()
                                last_ts = last_contract_log_ts.get(sym, 0.0)
                                if now_ts - last_ts >= max(1, Config.MARKETDATA_CONTRACT_LOG_COOLDOWN_SEC):
                                    logger.warning(
                                        "[DATA CONTRACT] Rejecting %s this cycle: %s",
                                        sym,
                                        "; ".join(snapshot_issues[:3]) if snapshot_issues else "unknown contract failure",
                                    )
                                    last_contract_log_ts[sym] = now_ts

                                if fail_count >= max(1, Config.DATA_QUALITY_STRIKE_LIMIT):
                                    if portfolio.count_positions_for_symbol(sym) <= 0:
                                        quarantine_sec = max(60, int(Config.DATA_QUALITY_QUARANTINE_SEC))
                                        contract_quarantine_until[norm_sym] = now_ts + quarantine_sec
                                        contract_failure_streak[norm_sym] = 0
                                        contract_quarantine_log_ts.pop(norm_sym, None)
                                        logger.warning(
                                            "[DATA CONTRACT] Quarantining %s for %ss after %s consecutive failures.",
                                            sym,
                                            quarantine_sec,
                                            fail_count,
                                        )
                                continue
                            contract_failure_streak.pop(norm_sym, None)
                        
                        # Drift monitoring (feature z-scores)
                        drift_alerts = drift_monitor.update(state.to_dict())
                        if drift_alerts:
                            logger.warning(f"DRIFT ALERT [{sym}]: " + "; ".join(drift_alerts[:3]))

                        # Phase 5: Spoofing Detection (orderbook anomalies)
                        try:
                            if Config.SPOOFING_DETECTION_ENABLED and curr_book and sym in prev_orderbooks:
                                spoof_events = SpoofingDetector.detect_events(
                                    prev_orderbooks[sym],
                                    curr_book,
                                    threshold_size=Config.SPOOFING_THRESHOLD_SIZE,
                                )
                                if len(spoof_events) >= max(1, Config.SPOOFING_MIN_EVENTS):
                                    now_ts = time.time()
                                    last_ts = last_spoof_log_ts.get(sym, 0.0)
                                    if now_ts - last_ts >= max(1, Config.SPOOFING_LOG_COOLDOWN_SEC):
                                        logger.warning(
                                            f"[SPOOFING] {sym}: {len(spoof_events)} large cancellations detected"
                                        )
                                        last_spoof_log_ts[sym] = now_ts
                                elif spoof_events:
                                    logger.debug(
                                        "[SPOOFING] %s: %s events below alert threshold (%s).",
                                        sym,
                                        len(spoof_events),
                                        Config.SPOOFING_MIN_EVENTS,
                                    )
                            if curr_book:
                                prev_orderbooks[sym] = curr_book
                        except Exception:
                            pass

                        # Auto-rollout runtime policy (champion/canary blend)
                        try:
                            if auto_rollout:
                                runtime_policy = auto_rollout.get_runtime_policy(
                                    active_mode=Config.AUTO_ROLLOUT_ACTIVE_MODE
                                )
                                engine.set_runtime_policy(runtime_policy)
                            else:
                                engine.set_runtime_policy({})

                            # 2. Decide
                            if Config.STRATEGY_FILTER_ENABLED or Config.STRATEGY_WEIGHTING_ENABLED:
                                strategy_weights = {}
                                blocked = set()
                                for strat in StrategyType:
                                    if strat == StrategyType.WAIT:
                                        continue
                                    key = f"{strat.name}|{state.market_regime.value}" if Config.STRATEGY_FILTER_REGIME_AWARE else strat.name
                                    if Config.STRATEGY_WEIGHTING_ENABLED:
                                        strategy_weights[strat] = perf_tracker.get_weight(
                                            key, min_samples=Config.STRATEGY_MIN_SAMPLES
                                        )
                                    if Config.STRATEGY_FILTER_ENABLED and perf_tracker.is_blocked(
                                        key,
                                        min_samples=Config.STRATEGY_FILTER_MIN_TRADES,
                                        min_win_rate=Config.STRATEGY_FILTER_MIN_WIN_RATE,
                                        min_avg_pnl=Config.STRATEGY_FILTER_MIN_AVG_PNL
                                    ):
                                        blocked.add(strat)
                                engine.set_strategy_overrides(strategy_weights=strategy_weights, blocked_strategies=blocked)
                            else:
                                engine.set_strategy_overrides()
                            
                            engine.update_cross_section_snapshot(sym, state)
                            engine.update_volatility_snapshot(sym, state)
                        except Exception as prep_error:
                            logger.error(f"[{sym}] Engine preparation failed: {prep_error}", exc_info=True)
                            continue
                        try:
                            action, decision_id, repeats = engine.run_analysis(state, data_source="live")
                        except Exception as e:
                            logger.error(f"[{sym}] FATAL: Engine analysis failed: {e}", exc_info=True)
                            continue

                        confidence = getattr(engine, 'last_confidence', 0.0)
                        agent_size_multiplier = 1.0

                        # Phase 2: Decision Audit Trail
                        try:
                            audit = decision_auditor.create_audit(decision_id, symbol=sym)
                            decision_auditor.log_market_context(
                                audit, state.market_regime.value, state.regime_confidence,
                                state.rsi, state.trend_spread, state.htf_trend_spread, state.volume_zscore,
                            )
                            decision_auditor.log_ml_result(audit, confidence, Config.MIN_SIGNAL_SCORE)
                            decision_auditor.log_final_action(audit, action.strategy.name, action.direction.name)
                            decision_auditor.save(audit)
                        except Exception:
                            pass
                        
                        agent_decision = None

                        if agent_orchestrator:
                            try:
                                current_positions = portfolio.get_all_positions()
                                agent_context = {
                                    "balance": portfolio.balance,
                                    "equity": portfolio.equity,
                                    "open_positions": len(current_positions),
                                    "max_positions": Config.MAX_CONCURRENT_POSITIONS,
                                    "gross_exposure": compute_gross_exposure(current_positions, portfolio.equity),
                                    "exposure_cap": Config.EXPOSURE_CAP_PCT,
                                }
                                agent_decision = agent_orchestrator.orchestrate(
                                    symbol=sym,
                                    state=state,
                                    proposed_action=action,
                                    model_confidence=confidence,
                                    context=agent_context,
                                )
                                if auto_rollout:
                                    risk_veto = bool((agent_decision.get("risk_veto") or {}).get("vetoed"))
                                    if risk_veto:
                                        veto_reason = str((agent_decision.get("risk_veto") or {}).get("reason") or "")
                                        rollout_event = auto_rollout.record_governance_signal(
                                            risk_veto=True,
                                            reason=veto_reason,
                                        )
                                        if rollout_event:
                                            logger.info(f"[AUTO-ROLLOUT] {rollout_event}")
                                if Config.AGENT_MODE == "active" and action.strategy != StrategyType.WAIT:
                                    final_action = agent_decision.get("final_action", "EXECUTE")
                                    if final_action in {"WAIT", "INSUFFICIENT_DATA"}:
                                        action = Action.wait(reason=f"Agent override: {final_action}")
                                    elif final_action == "EXECUTE_REDUCED":
                                        agent_size_multiplier = Config.AGENT_REDUCED_SIZE_MULTIPLIER
                            except Exception as e:
                                logger.warning(f"Agent orchestration error [{sym}]: {e}")

                        perf_key = action.strategy.name
                        
                        # Log coin scan result for visibility
                        if action.strategy == StrategyType.WAIT:
                            logger.info(
                                "[%s] SCAN: WAIT | Conf: %.2f | Regime: %s | Reason: %s...",
                                sym,
                                confidence,
                                state.market_regime.value,
                                action.reasoning[:50],
                            )
                        else:
                            logger.info(
                                "[%s] SCAN: %s %s | Conf: %.2f | Regime: %s",
                                sym,
                                action.strategy.name,
                                action.direction.name,
                                confidence,
                                state.market_regime.value,
                            )
                        
                        # Update Latest Signal for UI (shows the scan in progress)
                        latest_signal = {
                            "strategy": action.strategy.name,
                            "direction": action.direction.name,
                            "confidence": confidence,
                            "reasoning": action.reasoning,
                            "symbol": sym, # Trace which coin gave the signal
                            "agent_action": agent_decision.get("final_action") if agent_decision else None,
                        }
                        
                        # 3. Act & Track
                        if action.strategy != StrategyType.WAIT:
                            # Phase 1: Risk Guardian hard override
                            if not risk_guardian.check_system_health():
                                logger.warning(f"[RISK GUARDIAN] Trade blocked: {risk_guardian.state.kill_reason}")
                                continue
                            # Canary halt check
                            canary_reason = canary_monitor.check(portfolio.equity)
                            if canary_reason:
                                logger.warning(f"CANARY HALT: {canary_reason}")
                                if auto_rollout:
                                    rollout_event = auto_rollout.record_governance_signal(
                                        canary_failed=True,
                                        reason=canary_reason,
                                    )
                                    if rollout_event:
                                        logger.info(f"[AUTO-ROLLOUT] {rollout_event}")
                                continue
                            # Portfolio-level risk checks
                            halted, reason = risk_manager.check_limits(portfolio.equity, portfolio.initial_capital)
                            if halted:
                                logger.warning(f"RISK HALT: {reason}")
                                if auto_rollout:
                                    rollout_event = auto_rollout.record_governance_signal(
                                        risk_veto=True,
                                        reason=reason,
                                    )
                                    if rollout_event:
                                        logger.info(f"[AUTO-ROLLOUT] {rollout_event}")
                                continue

                            # Exposure checks
                            gross_exposure = compute_gross_exposure(portfolio.get_all_positions(), portfolio.equity)
                            if gross_exposure > Config.EXPOSURE_CAP_PCT:
                                now_ts = time.time()
                                if now_ts - last_exposure_log_ts >= max(1, Config.RISK_ALERT_COOLDOWN_SEC):
                                    logger.warning(f"Exposure cap reached: {gross_exposure:.2f} > {Config.EXPOSURE_CAP_PCT:.2f}")
                                    last_exposure_log_ts = now_ts
                                continue
                            cluster_exposure_pct = cluster_exposure(portfolio.get_all_positions(), portfolio.equity, cluster_map)
                            if cluster_exposure_pct:
                                worst_cluster = max(cluster_exposure_pct, key=cluster_exposure_pct.get)
                                if cluster_exposure_pct[worst_cluster] > Config.CORR_CLUSTER_CAP_PCT:
                                    now_ts = time.time()
                                    last_ts = last_cluster_log_ts.get(worst_cluster, 0.0)
                                    if now_ts - last_ts >= max(1, Config.RISK_ALERT_COOLDOWN_SEC):
                                        logger.warning(
                                            f"Cluster cap reached for {worst_cluster}: {cluster_exposure_pct[worst_cluster]:.2f} > {Config.CORR_CLUSTER_CAP_PCT:.2f}"
                                        )
                                        last_cluster_log_ts[worst_cluster] = now_ts
                                    continue

                            # Phase 2: Check cooldown and position limits
                            can_open, block_reason = portfolio.can_open_position(sym)
                            
                            if not can_open:
                                logger.warning(f"[BLOCKED] [{sym}] {block_reason}")
                            else:
                                strategy_admission_multiplier = 1.0
                                if (
                                    action.strategy == StrategyType.VOLATILITY_BREAKOUT
                                    and Config.VOL_BREAKOUT_ADMISSION_ENABLED
                                ):
                                    admission_key = (
                                        f"{action.strategy.name}|{state.market_regime.value}"
                                        if Config.STRATEGY_FILTER_REGIME_AWARE
                                        else action.strategy.name
                                    )
                                    stat_trades, stat_wr, stat_avg = perf_tracker.stats(admission_key)
                                    min_trades = Config.VOL_BREAKOUT_ADMISSION_MIN_TRADES
                                    if stat_trades < min_trades:
                                        strategy_admission_multiplier = Config.VOL_BREAKOUT_WARMUP_SIZE_MULTIPLIER
                                        if strategy_admission_multiplier <= 0:
                                            logger.info(
                                                "[%s] BLOCKED: VOLATILITY_BREAKOUT admission warmup disabled (trades=%s/%s).",
                                                sym,
                                                stat_trades,
                                                min_trades,
                                            )
                                            continue
                                        logger.info(
                                            "[%s] VOLATILITY_BREAKOUT warmup mode (trades=%s/%s, size x%.2f).",
                                            sym,
                                            stat_trades,
                                            min_trades,
                                            strategy_admission_multiplier,
                                        )
                                    elif (
                                        stat_wr < Config.VOL_BREAKOUT_ADMISSION_MIN_WIN_RATE
                                        or stat_avg < Config.VOL_BREAKOUT_ADMISSION_MIN_AVG_PNL
                                    ):
                                        logger.info(
                                            "[%s] BLOCKED: VOLATILITY_BREAKOUT admission fail (WR=%.2f, AVG=%.3f).",
                                            sym,
                                            stat_wr,
                                            stat_avg,
                                        )
                                        continue

                                # Phase 35: Smart Leverage Calculation
                                confidence = engine.last_confidence if hasattr(engine, 'last_confidence') else 0.5
                                leverage = calculate_smart_leverage(
                                    confidence=confidence,
                                    regime_stable=state.regime_stable,
                                    volatility=state.volatility_level.value
                                )

                                # Phase 5: Dynamic TP/SL based on trade mode
                                trade_mode, tp_price, sl_price, tp_pct, sl_pct = calculate_tp_sl(
                                    entry_price=current_price,
                                    direction=action.direction.name,
                                    atr=state.atr,
                                    regime=state.market_regime.value,
                                    trend_strength=state.trend_strength.value
                                )

                                # Smart Position Sizing: ATR + Confidence based
                                avg_atr = state.atr if state.atr > 0 else 1.0
                                size_usd = calculate_smart_position_size(
                                    balance=portfolio.balance,
                                    confidence=confidence,
                                    atr=state.atr,
                                    avg_atr=avg_atr,
                                    leverage=leverage
                                )
                                # Volatility targeting
                                if daily_returns:
                                    vol = compute_daily_vol(daily_returns) * 100
                                    size_usd *= risk_manager.volatility_scaler(vol)

                                # Strategy weighting (performance + bandit)
                                strat_key = f"{perf_key}|{state.market_regime.value}" if Config.STRATEGY_FILTER_REGIME_AWARE else perf_key
                                strat_weight = perf_tracker.get_weight(strat_key, min_samples=Config.STRATEGY_MIN_SAMPLES)
                                bandit_weight = bandit.weight(strat_key)
                                size_usd *= (strat_weight * bandit_weight)
                                size_usd *= agent_size_multiplier
                                size_usd *= strategy_admission_multiplier

                                # Phase 4: Kelly criterion sizing overlay
                                try:
                                    strat_name_k = action.strategy.name
                                    k_trades, k_wr, k_avg = perf_tracker.stats(strat_name_k)
                                    if k_trades >= 20:
                                        avg_loss = abs(k_avg) if k_avg < 0 else 1.0
                                        kelly_f = RiskMetrics.calculate_kelly(k_wr, abs(k_avg) if k_avg > 0 else 1.0, avg_loss)
                                        kelly_f = min(kelly_f, 0.25)  # Cap at 25% Kelly
                                        if kelly_f > 0:
                                            size_usd *= max(kelly_f, 0.1)
                                except Exception:
                                    pass
                                if agent_size_multiplier < 1.0:
                                    logger.info(
                                        f"[AGENT] Reduced execution sizing for {sym}: x{agent_size_multiplier:.2f}"
                                    )
                                size_qty = size_usd / max(current_price, 1e-9)

                                entry_ok = False
                                entry_price = current_price
                                exchange_order_id = None
                                exchange_order_status = None

                                if hl_live_executor:
                                    try:
                                        entry_resp = hl_live_executor.place_entry(
                                            symbol=sym,
                                            direction=action.direction,
                                            size_usd=size_usd,
                                            reference_price=current_price,
                                            decision_id=decision_id,
                                        )
                                        if entry_resp.get("ok") and entry_resp.get("order_status") != "error":
                                            entry_ok = True
                                            entry_price = float(entry_resp.get("fill_price") or current_price)
                                            exchange_order_id = entry_resp.get("oid")
                                            exchange_order_status = entry_resp.get("order_status")
                                            size_qty = float(entry_resp.get("requested_qty") or size_qty)
                                        else:
                                            logger.warning(f"[HL] Entry rejected for {sym}: {entry_resp.get('error') or entry_resp}")
                                    except Exception as e:
                                        logger.error(f"[HL] Entry order failed for {sym}: {e}")
                                else:
                                    entry_ok = executor.execute(action, sym, current_price, state.atr)

                                if entry_ok:
                                    opened = portfolio.open_position(
                                        sym,
                                        action.direction.name,
                                        entry_price,
                                        size_usd,
                                        tp_price,
                                        sl_price,
                                        decision_id,
                                        entry_regime=state.market_regime.value,
                                        entry_atr=state.atr,
                                        leverage=leverage,
                                        size_qty=size_qty,
                                        exchange_order_id=exchange_order_id,
                                        trade_mode=trade_mode,
                                        exchange_order_status=exchange_order_status,
                                        strategy=action.strategy.name,
                                    )
                                    if not opened and hl_live_executor:
                                        logger.error(f"[HL] Local open failed after live order for {sym}. Manual reconciliation required.")
                                    elif opened:
                                        # Phase 2: Latency measurement
                                        lat_ms = latency_monitor.record_execution_latency(sym)
                                        logger.info(
                                            f"[POSITION OPEN] [{trade_mode}] {sym} {action.direction.name} | Entry: {entry_price:.2f} | "
                                            f"Size: ${size_usd:.2f} ({leverage}x) | TP: {tp_price:.2f} ({tp_pct}%) | SL: {sl_price:.2f} ({sl_pct}%)"
                                            + (f" | Latency: {lat_ms:.0f}ms" if lat_ms > 0 else "")
                                        )
                                        # Phase 6: Shadow executor parallel paper trade
                                        if shadow_executor:
                                            try:
                                                shadow_executor.submit_order({
                                                    'symbol': sym, 'side': action.direction.name,
                                                    'amount': size_qty, 'price': entry_price,
                                                })
                                            except Exception:
                                                pass
                        # 4. Resolve & Learn (Specific to this symbol scan)
                        portfolio.update_metrics(sym, current_price)
                        
                        if sym in portfolio.active_positions:
                            positions = portfolio.active_positions[sym]
                            if not isinstance(positions, list):
                                positions = [positions]

                            to_close = []
                            forced_sync_flat = False

                            if hl_live_executor and exchange_position_sizes_ok:
                                try:
                                    coin = hl_live_executor.coin_for_symbol(sym, market_type=Config.EXCHANGE_MARKET_TYPE)
                                    exchange_szi = float(exchange_position_sizes.get(coin, 0.0))
                                    local_szi = 0.0
                                    pending_entry_ws_grace = False
                                    canceled_or_rejected = False
                                    cancel_reason = ""
                                    for pos in positions:
                                        if hl_realtime:
                                            ws_order = hl_realtime.get_order(pos.get("exchange_order_id"))
                                            if ws_order and ws_order.get("status"):
                                                pos["exchange_order_status"] = ws_order.get("status")

                                        status = str(pos.get("exchange_order_status") or "").strip().lower()
                                        if hl_realtime and hl_realtime.is_reject_or_cancel_status(status):
                                            canceled_or_rejected = True
                                            cancel_reason = status.upper()
                                        if hl_realtime and hl_realtime.is_pending_order_status(status):
                                            entry_age_sec = Config.HYPERLIQUID_ORDER_SYNC_GRACE_SEC + 1
                                            entry_time_raw = pos.get("entry_time")
                                            if entry_time_raw:
                                                try:
                                                    entry_dt = datetime.fromisoformat(str(entry_time_raw).replace("Z", "+00:00"))
                                                    if entry_dt.tzinfo:
                                                        entry_age_sec = (datetime.now(entry_dt.tzinfo) - entry_dt).total_seconds()
                                                    else:
                                                        entry_age_sec = (datetime.now() - entry_dt).total_seconds()
                                                except Exception:
                                                    pass
                                            if entry_age_sec < Config.HYPERLIQUID_ORDER_SYNC_GRACE_SEC:
                                                pending_entry_ws_grace = True

                                        qty = float(pos.get("size_qty") or 0.0)
                                        if qty <= 0:
                                            entry_px = float(pos.get("entry_price") or current_price)
                                            qty = float(pos.get("size_usd", 0.0)) / max(entry_px, 1e-9)
                                        if str(pos.get("direction", "")).upper() == "LONG":
                                            local_szi += abs(qty)
                                        else:
                                            local_szi -= abs(qty)

                                    if abs(local_szi) > 1e-9 and abs(exchange_szi) < 1e-9:
                                        if pending_entry_ws_grace:
                                            logger.debug(f"[HL] Sync: awaiting ws fill for pending {sym} order.")
                                        else:
                                            forced_sync_flat = True
                                            reason = f"EXCHANGE_ORDER_{cancel_reason}" if canceled_or_rejected and cancel_reason else "EXCHANGE_SYNC_FLAT"
                                            logger.warning(f"[HL] Sync: local {sym} position exists but exchange is flat. Closing local position(s).")
                                            for pos in positions:
                                                to_close.append((pos, current_price, reason, None))
                                    elif abs(local_szi) < 1e-9 and abs(exchange_szi) > 1e-9:
                                        logger.warning(f"[HL] Sync: exchange has {sym} size {exchange_szi:.6f} but local portfolio is flat.")
                                except Exception as e:
                                    logger.error(f"[HL] Position sync comparison failed for {sym}: {e}")

                            if not forced_sync_flat:
                                # Update trailing stops first
                                trail_closes = portfolio.update_trailing_stop(sym, current_price, state.atr)
                                for pos in trail_closes:
                                    exchange_exit_order_id = None
                                    final_exit_price = current_price
                                    final_reason = "TRAIL"
                                    if hl_live_executor:
                                        try:
                                            exit_resp = hl_live_executor.place_exit(pos, current_price=current_price, reason="TRAIL")
                                            if not exit_resp.get("ok") or exit_resp.get("order_status") == "error":
                                                logger.warning(f"[HL] Trail exit rejected for {sym}: {exit_resp.get('error') or exit_resp}")
                                                continue
                                            exchange_exit_order_id = exit_resp.get("oid")
                                            final_exit_price = float(exit_resp.get("fill_price") or current_price)
                                            final_reason = "TRAIL_LIVE"
                                        except Exception as e:
                                            logger.error(f"[HL] Trail exit order failed for {sym}: {e}")
                                            continue
                                    to_close.append((pos, final_exit_price, final_reason, exchange_exit_order_id))

                                for pos in positions:
                                    # Skip positions already marked for trail close
                                    if pos in trail_closes:
                                        continue
                                    # Skip positions in active trailing mode (don't check fixed TP)
                                    if pos.get("trail_active"):
                                        continue
                                    
                                    exit_price = None
                                    reason = None

                                    if pos['direction'] == "LONG":
                                        if current_price >= pos['tp']:
                                            # SWING trades: activate trailing instead of exiting at TP
                                            if pos.get("trade_mode") == Config.TRAILING_ACTIVATION_MODE and Config.TRAILING_STOP_ENABLED:
                                                # Trailing was already activated by update_trailing_stop above
                                                continue
                                            exit_price, reason = pos['tp'], "TP"
                                        elif current_price <= pos['sl']:
                                            exit_price, reason = pos['sl'], "SL"
                                    else:
                                        if current_price <= pos['tp']:
                                            if pos.get("trade_mode") == Config.TRAILING_ACTIVATION_MODE and Config.TRAILING_STOP_ENABLED:
                                                continue
                                            exit_price, reason = pos['tp'], "TP"
                                        elif current_price >= pos['sl']:
                                            exit_price, reason = pos['sl'], "SL"

                                    if exit_price:
                                        exchange_exit_order_id = None
                                        final_exit_price = exit_price
                                        final_reason = reason
                                        if hl_live_executor:
                                            try:
                                                exit_resp = hl_live_executor.place_exit(pos, current_price=current_price, reason=reason)
                                                if not exit_resp.get("ok") or exit_resp.get("order_status") == "error":
                                                    logger.warning(f"[HL] Exit rejected for {sym}: {exit_resp.get('error') or exit_resp}")
                                                    continue
                                                exchange_exit_order_id = exit_resp.get("oid")
                                                final_exit_price = float(exit_resp.get("fill_price") or current_price)
                                                final_reason = f"{reason}_LIVE"
                                            except Exception as e:
                                                logger.error(f"[HL] Exit order failed for {sym}: {e}")
                                                continue
                                        to_close.append((pos, final_exit_price, final_reason, exchange_exit_order_id))

                            for pos, exit_price, reason, exchange_exit_order_id in to_close:
                                closed_trade = portfolio.close_position(
                                    sym,
                                    exit_price,
                                    reason,
                                    exit_regime=state.market_regime.value,
                                    exit_atr=state.atr,
                                    decision_id=pos.get('decision_id'),
                                    exchange_exit_order_id=exchange_exit_order_id,
                                )
                                if not closed_trade:
                                    continue
                                logger.info(f"[POSITION CLOSED] {sym} | Exit: {exit_price:.2f} | Reason: {reason} | PnL: ${closed_trade['realized_pnl_usd']:.2f} ({closed_trade['realized_pnl_pct']:.2f}%)")
                                if closed_trade.get('loss_category'):
                                    logger.warning(f"LOSS TYPE: {closed_trade['loss_category']}")

                                pnl_pct = closed_trade.get('realized_pnl_pct', 0.0)
                                strat_name = closed_trade.get("strategy") or perf_key
                                entry_regime = closed_trade.get("entry_regime") or state.market_regime.value
                                perf_tracker.record(strat_name, pnl_pct)
                                if entry_regime:
                                    perf_tracker.record(f"{strat_name}|{entry_regime}", pnl_pct)
                                bandit_key = f"{strat_name}|{entry_regime}" if Config.STRATEGY_FILTER_REGIME_AWARE else strat_name
                                bandit.record(bandit_key, pnl_pct)
                                daily_returns.append(pnl_pct / 100.0)
                                canary_monitor.record_trade(pnl_pct)
                                # Phase 2: Performance Monitor
                                performance_monitor.update(pnl_pct)
                                engine.meta_learner.record_trade_result(
                                    won=pnl_pct > 0,
                                    loss_category=closed_trade.get("loss_category"),
                                    confidence=confidence,
                                    regime=state.market_regime.value,
                                    strategy=strat_name,
                                    entry_regime=closed_trade.get("entry_regime"),
                                    exit_reason=reason,
                                )
                                _save_strategy_intelligence_state(perf_tracker, bandit)
                                if auto_rollout:
                                    rollout_event = auto_rollout.record_trade_result(
                                        pnl_pct,
                                        portfolio.equity,
                                        active_mode=Config.AUTO_ROLLOUT_ACTIVE_MODE,
                                    )
                                    if rollout_event:
                                        logger.info(f"[AUTO-ROLLOUT] {rollout_event}")

                                if str(reason).startswith("TP"):
                                    final_reward = 1.0
                                elif str(reason).startswith("SL"):
                                    final_reward = -1.0
                                else:
                                    final_reward = 0.0

                                engine.db.finalize_record(
                                    decision_id=pos['decision_id'],
                                    outcome_data={
                                        "exit_price": exit_price,
                                        "reason": reason,
                                        "pnl_usd": closed_trade['realized_pnl_usd'],
                                        "loss_category": closed_trade.get('loss_category'),
                                        "entry_regime": closed_trade.get('entry_regime'),
                                        "exit_regime": closed_trade.get('exit_regime'),
                                        "exchange_exit_order_id": exchange_exit_order_id,
                                    },
                                    final_reward=final_reward,
                                )
                        # Periodically update dashboard even during the squad scan
                        summary = portfolio.get_summary()
                        # Optional divergence check
                        live_metrics = {
                            "win_rate": (sum(1 for t in portfolio.trade_history if t.get("realized_pnl_usd", 0) > 0) / max(1, len(portfolio.trade_history))) if portfolio.trade_history else 0.0,
                            "avg_pnl": (sum(t.get("realized_pnl_pct", 0.0) for t in portfolio.trade_history) / max(1, len(portfolio.trade_history))) if portfolio.trade_history else 0.0
                        }
                        div_msg = None
                        if len(portfolio.trade_history) >= max(1, Config.DIVERGENCE_MIN_TRADES):
                            div_msg = divergence_monitor.check(
                                live_metrics,
                                thresholds={
                                    "win_rate": Config.DIVERGENCE_WIN_RATE_TOL,
                                    "avg_pnl": Config.DIVERGENCE_AVG_PNL_TOL,
                                },
                            )
                        if div_msg and (time.time() - last_divergence_log_ts) >= max(1, Config.DIVERGENCE_ALERT_COOLDOWN_SEC):
                            logger.warning(f"DIVERGENCE: {div_msg}")
                            last_divergence_log_ts = time.time()
                        live.update(dashboard.generate_renderable(
                            summary, 
                            portfolio.get_all_positions(), 
                            portfolio.trade_history,
                            latest_signal,
                            alerts=drift_alerts,
                            meta_learner_summary=engine.meta_learner.get_summary()
                        ))
                    
                    # ═══ SAFETY NET: Check orphaned positions (symbols NOT in active scan) ═══
                    cycle_symbol_set = {connector.normalize_symbol(s) for s in cycle_symbols}
                    orphan_symbols = [
                        s
                        for s in portfolio.active_positions
                        if portfolio.active_positions[s] and connector.normalize_symbol(s) not in cycle_symbol_set
                    ]
                    for sym in orphan_symbols:
                        try:
                            norm_sym = connector.normalize_symbol(sym)
                            ticker = (
                                cycle_tickers.get(sym)
                                or cycle_tickers.get(norm_sym)
                                or {}
                            )
                            current_price = extract_ticker_last_price(ticker)
                            if current_price is None:
                                existing_positions = portfolio.active_positions.get(sym, [])
                                if not isinstance(existing_positions, list):
                                    existing_positions = [existing_positions]
                                for pos in existing_positions:
                                    pos_price = pos.get("current_price")
                                    if pos_price is not None:
                                        current_price = pos_price
                                        break
                            if current_price is None and batch_tickers_ok:
                                ticker = connector.get_market_structure(sym) or {}
                                current_price = extract_ticker_last_price(ticker)
                            if current_price is None:
                                continue

                            # Enforce market-data contract checks in orphan path too.
                            # This prevents orphan exits from using cross-source bad prices.
                            if Config.MARKETDATA_CONTRACT_ENFORCED:
                                orphan_state = (
                                    marketdata_cache.get_state(sym, Config.MARKETDATA_STALE_STATE_MAX_SEC)
                                    or marketdata_cache.get_state(norm_sym, Config.MARKETDATA_STALE_STATE_MAX_SEC)
                                )
                                if orphan_state is None:
                                    now_ts = time.time()
                                    last_ts = last_contract_log_ts.get(sym, 0.0)
                                    if now_ts - last_ts >= max(1, Config.MARKETDATA_CONTRACT_LOG_COOLDOWN_SEC):
                                        logger.warning(
                                            "[DATA CONTRACT] Rejecting orphan %s exit check: no validated state snapshot available.",
                                            sym,
                                        )
                                        last_contract_log_ts[sym] = now_ts
                                    continue

                                orphan_snapshot = build_market_input_snapshot(
                                    symbol=sym,
                                    state=orphan_state,
                                    ticker=ticker,
                                    current_price=current_price,
                                )
                                orphan_ok, orphan_issues = validate_market_input_snapshot(
                                    orphan_snapshot,
                                    max_price_divergence_pct=Config.MARKETDATA_MAX_PRICE_DIVERGENCE_PCT,
                                )
                                if not orphan_ok:
                                    now_ts = time.time()
                                    last_ts = last_contract_log_ts.get(sym, 0.0)
                                    if now_ts - last_ts >= max(1, Config.MARKETDATA_CONTRACT_LOG_COOLDOWN_SEC):
                                        logger.warning(
                                            "[DATA CONTRACT] Rejecting orphan %s exit check: %s",
                                            sym,
                                            "; ".join(orphan_issues[:3]) if orphan_issues else "unknown contract failure",
                                        )
                                        last_contract_log_ts[sym] = now_ts
                                    continue
                            portfolio.update_metrics(sym, current_price)
                            
                            positions = portfolio.active_positions[sym]
                            if not isinstance(positions, list):
                                positions = [positions]
                            
                            orphan_closes = []
                            
                            # Check trailing stops for orphan positions
                            trail_closes = portfolio.update_trailing_stop(sym, current_price, 0.0)  # ATR=0 is safe (no trail activation without ATR)
                            for pos in trail_closes:
                                orphan_closes.append((pos, current_price, "TRAIL_ORPHAN", None))
                            
                            for pos in positions:
                                if pos in trail_closes:
                                    continue
                                if pos.get("trail_active"):
                                    continue
                                exit_price = None
                                reason = None
                                if pos['direction'] == "LONG":
                                    if current_price >= pos['tp']:
                                        if pos.get("trade_mode") == Config.TRAILING_ACTIVATION_MODE and Config.TRAILING_STOP_ENABLED:
                                            continue
                                        exit_price, reason = pos['tp'], "TP_ORPHAN"
                                    elif current_price <= pos['sl']:
                                        exit_price, reason = pos['sl'], "SL_ORPHAN"
                                else:
                                    if current_price <= pos['tp']:
                                        if pos.get("trade_mode") == Config.TRAILING_ACTIVATION_MODE and Config.TRAILING_STOP_ENABLED:
                                            continue
                                        exit_price, reason = pos['tp'], "TP_ORPHAN"
                                    elif current_price >= pos['sl']:
                                        exit_price, reason = pos['sl'], "SL_ORPHAN"
                                
                                if exit_price:
                                    logger.warning(
                                        f"[ORPHAN EXIT] {sym} {pos['direction']} hit {reason} at {current_price} "
                                        f"(SL={pos['sl']}, TP={pos['tp']})"
                                    )
                                    # For paper orphan TP/SL exits, use the trigger level, not raw ticker.
                                    orphan_closes.append((pos, exit_price, reason, None))

                            closed_any = False
                            for pos, exit_price, reason, _ in orphan_closes:
                                exchange_exit_order_id = None
                                final_exit_price = exit_price
                                final_reason = reason
                                if hl_live_executor:
                                    try:
                                        exit_resp = hl_live_executor.place_exit(pos, current_price=current_price, reason=reason)
                                        if not exit_resp.get("ok") or exit_resp.get("order_status") == "error":
                                            logger.warning(f"[HL] Orphan exit rejected for {sym}: {exit_resp.get('error') or exit_resp}")
                                            continue
                                        exchange_exit_order_id = exit_resp.get("oid")
                                        final_exit_price = float(exit_resp.get("fill_price") or current_price)
                                        final_reason = f"{reason}_LIVE"
                                    except Exception as e:
                                        logger.error(f"[HL] Orphan exit order failed for {sym}: {e}")
                                        continue
                                closed_trade = portfolio.close_position(
                                    sym,
                                    final_exit_price,
                                    final_reason,
                                    exit_atr=0.0,
                                    exchange_exit_order_id=exchange_exit_order_id,
                                )
                                if closed_trade:
                                    closed_any = True
                                    won = closed_trade['realized_pnl_usd'] > 0
                                    orphan_strategy = closed_trade.get("strategy") or "UNKNOWN"
                                    engine.meta_learner.record_trade_result(
                                        won=won,
                                        loss_category=closed_trade.get('loss_category'),
                                        confidence=0.5,
                                        regime="UNKNOWN",
                                        strategy=orphan_strategy,
                                        entry_regime=closed_trade.get("entry_regime"),
                                        exit_reason=reason,
                                    )
                                    _save_strategy_intelligence_state(perf_tracker, bandit)
                                    if auto_rollout:
                                        pnl_pct = closed_trade.get("realized_pnl_pct", 0.0)
                                        rollout_event = auto_rollout.record_trade_result(
                                            pnl_pct,
                                            portfolio.equity,
                                            active_mode=Config.AUTO_ROLLOUT_ACTIVE_MODE,
                                        )
                            if orphan_closes and not closed_any:
                                logger.error(f"Failed to close orphan position for {sym} locally.")
                        except Exception as e:
                            logger.error(f"Orphan cleanup failed for {sym}: {e}")
                    # ═══ END SAFETY NET ═╕═


                    # === AGENT INTELLIGENCE LOOP ===
                    # Runs once per scan cycle: analyze trade history -> propose parameter
                    # adaptations -> create candidate policies for canary rollout.
                    if auto_rollout and portfolio.trade_history:
                        try:
                            event = auto_rollout.maybe_create_candidate(portfolio.trade_history)
                            if event:
                                logger.info(f"[AGENT-INTELLIGENCE] {event}")
                        except Exception as intel_err:
                            logger.warning(f"[AGENT-INTELLIGENCE] Error: {intel_err}")

                    # === Phase 3: Data Ingestor (persist market data) ===
                    if data_ingestor:
                        try:
                            now_ts = time.time()
                            if (now_ts - last_data_ingestion_ts) >= max(10, Config.DATA_INGESTION_INTERVAL_SEC):
                                ingestion_limit = max(1, int(Config.DATA_INGESTION_SYMBOL_LIMIT))
                                ingestion_symbols = cycle_symbols[:ingestion_limit]
                                data_ingestor.run_cycle(
                                    ingestion_symbols,
                                    timeframe=Config.SCAN_TIMEFRAME,
                                    ohlcv_limit=max(10, int(Config.DATA_INGESTION_OHLCV_LIMIT)),
                                    trade_limit=max(0, int(Config.DATA_INGESTION_TRADE_LIMIT)),
                                )
                                last_data_ingestion_ts = now_ts
                        except Exception as di_err:
                            logger.warning(f"[DATA INGESTOR] {di_err}")

                    # === Phase 5: Context Ingestors ===
                    for ing in context_ingestors:
                        try:
                            ing.run_cycle()
                        except Exception:
                            pass

                    # === Phase 2: Log rolling Sharpe ===
                    try:
                        rolling_sharpe = performance_monitor.get_sharpe_ratio()
                        if rolling_sharpe != 0.0:
                            logger.info(f"[PERFORMANCE] Rolling Sharpe: {rolling_sharpe:.2f} | Avg Latency: {latency_monitor.get_average_latency():.0f}ms")
                        # Phase 4: Canary Launcher capital staging
                        if Config.CANARY_LAUNCHER_ENABLED and hasattr(risk_guardian, 'state'):
                            if not hasattr(portfolio, '_canary_launcher'):
                                portfolio._canary_launcher = CanaryLauncher()
                                logger.info("Canary Launcher initialized (stage=PROBE).")
                            dd = (portfolio.equity - portfolio.initial_capital) / portfolio.initial_capital if portfolio.initial_capital > 0 else 0.0
                            promo = portfolio._canary_launcher.evaluate_promotion(rolling_sharpe, abs(dd))
                            if promo not in ("WAITING_TIME", "MAX_STAGE"):
                                logger.info(f"[CANARY] Promotion status: {promo}")
                    except Exception:
                        pass

                    if run_once: break
                    time.sleep(20) # 20-second scan cycle (rate-limit safe for 30 coins)

                except Exception as e:
                    logger.error(f"Cycle Error: {e}")
                    if run_once:
                        break
                    time.sleep(10)
    finally:
        if learning_scheduler:
            try:
                learning_scheduler.stop()
            except Exception:
                pass
        if hl_user_stream:
            try:
                hl_user_stream.stop()
            except Exception:
                pass
        if hl_public_stream:
            try:
                hl_public_stream.stop()
            except Exception:
                pass

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
    parser.add_argument("--skip-checks", action="store_true", help="Skip startup validation checks")
    
    args = parser.parse_args()
    
    # Run startup checks (config validation, model staleness, audit setup)
    if not args.skip_checks:
        if not run_startup_checks():
            logger.critical("Startup checks failed. Exiting. Use --skip-checks only for controlled debugging.")
            sys.exit(1)

    
    if args.replay:
        run_replay_mode(
            args.replay, 
            period_id=args.period_id, 
            symbol=args.symbol, 
            no_throttle=args.no_throttle,
            log_suffix=args.log_suffix
        )
    else:
        try:
            run_live_mode(args.symbol, run_once=args.once)
        except KeyboardInterrupt:
            print("\nBot stopped by user (Ctrl+C). Exiting gracefully.")
            sys.exit(0)

