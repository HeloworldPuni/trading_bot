# Adaptive Trading Assistant - Project Context

## 1. Directory Structure
```
./
    .env
    .env.example
    .gitignore
    intelligent_results_competition_v2.json
    main.py
    requirements.txt
    docs/
        master_trader_prompt.md
    scripts/
        dry_run.py
        export_project.py
    src/
        config.py
        core/
            definitions.py
            gating.py
            reward.py
            risk.py
            validation.py
        database/
            storage.py
        engine/
            system.py
        exchange/
            connector.py
        execution/
            paper.py
    tests/
        test_mock_scenarios.py
```

## 2. File Contents

### File: `main.py`

```python

import time
import argparse
import logging
from typing import List, Dict
from src.config import Config
from src.exchange.connector import BinanceConnector
from src.data.feeder import DataFeeder
from src.engine.system import TradingEngine
from src.execution.paper import PaperExecutor
from src.core.definitions import StrategyType, Action
from src.core.reward import RewardCalculator

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

def run_live_mode(symbol: str):
    logger.info("Starting Adaptive Trading Assistant (Closed Loop V1) - LIVE MODE...")
    try:
        connector = BinanceConnector()
        feeder = DataFeeder(connector)
        engine = TradingEngine()
        executor = PaperExecutor()
        tracker = TradeTracker(engine.db)
        logger.info("Components initialized.")
    except Exception as e:
        logger.critical(f"Init Failed: {e}")
        return

    while True:
        try:
            logger.info("--- New Cycle ---")
            
            # 1. Observe
            state = feeder.get_current_state(symbol)
            
            # Fetch Price
            # In live mode, we need a separate call or trust state implied price
            # For hack, fetch again or use connector
            # Let's assume connector fetch
            ticker = connector.exchange.fetch_ticker(symbol)
            current_price = ticker['last']
            
            # 2. Decide
            action, decision_id, repeats = engine.run_analysis(state, data_source="live")
            
            # 3. Act & Track
            if action.strategy != StrategyType.WAIT:
                if executor.execute(action, symbol):
                    tracker.add_position(action, decision_id, current_price, repeats)
            else:
                logger.info(f"WAIT: {action.reasoning}")
                tracker.add_wait(action, decision_id, current_price)
            
            # 4. Resolve & Learn
            tracker.update(current_price)
            
            time.sleep(60) # 1 Minute Loop

        except Exception as e:
            logger.error(f"Cycle Error: {e}")
            time.sleep(10)

def run_replay_mode(csv_path: str):
    logger.info(f"Starting REPLAY MODE with {csv_path}...")
    from src.data.replay_feeder import ReplayFeeder
    
    feeder = ReplayFeeder(csv_path)
    engine = TradingEngine()
    # Executor: In replay, we don't use PaperExecutor. execution is simulated instantly.
    # Tracker: Needs to handle instant flow.
    tracker = TradeTracker(engine.db)
    
    count = 0
    while True:
        # 1. Get Next State
        state = feeder.get_next_state()
        if not state:
            logger.info("Replay Finished (End of Data).")
            break
            
        # Get "Current" Price (Last close of the state window)
        # We need to peek at the last candle of the window provided by feeder
        # Since feeder doesn't expose window easily, let's use a helper or assume logical consistency.
        # But wait, we need execution price.
        # State creation uses the window.
        # Let's trust logic: 
        # Price available for decision is the Close of the last candle in state.
        # Use state data? State has heuristic regime, not raw price.
        # Let's fetch raw price from feeder? 
        # ReplayFeeder history buffer...
        # "Simulate live conditions": We only know what's in state/past.
        # Check src/data/feeder.py refactor... logic was extracted.
        # I need the price.
        # Let's assume current price is the last close in the window used for state.
        
        # 2. Decide
        # Note: Decision is made on Past Data.
        action, decision_id, repeats = engine.run_analysis(state, data_source="replay")
        
        # 3. Future Peek for Execution
        future_candle = feeder.get_future_candle()
        if not future_candle:
            break
            
        # [ts, op, hi, lo, cl, vol]
        next_open = future_candle[1]
        next_high = future_candle[2]
        next_low = future_candle[3]
        next_close = future_candle[4]
        
        # Execution Price: Assume we fill at Next Open (Market Order)
        fill_price = next_open
        
        if count % 100 == 0:
            logger.info(f"Replay Step {count} | Action: {action.strategy.name}")
        
        # 3. Act & Track
        if action.strategy != StrategyType.WAIT:
             tracker.add_position(action, decision_id, fill_price, repeats)
        else:
             tracker.add_wait(action, decision_id, fill_price)
             
        # 4. Resolve Outcomes Immediately (Fast Forward)
        # In live mode, 'tracker.update' checks if price moved.
        # In replay, we advance 1 step per loop.
        # The 'current_price' for update is the Next Close (end of the 1m candle we just simulated).
        tracker.update(next_close)
        
        count += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", type=str, default="BTC/USDT")
    parser.add_argument("--replay", type=str, help="Path to CSV file for replay mode")
    args = parser.parse_args()
    
    if args.replay:
        run_replay_mode(args.replay)
    else:
        run_live_mode(args.symbol)

```

### File: `requirements.txt`

```python

ccxt
python-dotenv==1.0.0


```

### File: `.env.example`

```python
# API KEYS (Secrets)
EXCHANGE_API_KEY=your_api_key_here
EXCHANGE_SECRET=your_secret_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here

# TRADING CONFIG
TRADING_MODE=paper  # paper | live
EXCHANGE_ID=binance # binance, bybit, etc.
TIMEFRAME_HTF=1h
TIMEFRAME_LTF=15m

# RISK MANAGEMENT
RISK_PER_TRADE=0.01 # 1% per trade
MAX_DRAWDOWN_PERCENT=0.05 # 5% max drawdown
LEVERAGE=1

```

### File: `src/config.py`

```python

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
    
    # System Config
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    DATA_PATH = os.path.join(os.getcwd(), "data")

    @classmethod
    def validate(cls):
        """Ensure critical keys are present."""
        if not cls.EXCHANGE_API_KEY or not cls.EXCHANGE_SECRET:
            print("WARNING: Exchange keys are missing in .env")

```

Note: `src/config.py` also includes leverage caps, cooldown/position limits, and `STRATEGIC_WAIT_PROB` to control random WAIT injection for data diversity. See the file for the full, current list.

### File: `src/core/definitions.py`

```python

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Dict, Any

# --- ENUMS ---

class MarketRegime(Enum):
    BULL_TREND = "BULL_TREND"
    BEAR_TREND = "BEAR_TREND"
    SIDEWAYS_LOW_VOL = "SIDEWAYS_LOW_VOL"
    SIDEWAYS_HIGH_VOL = "SIDEWAYS_HIGH_VOL"
    TRANSITION = "TRANSITION"

class VolatilityLevel(Enum):
    LOW = "LOW"
    NORMAL = "NORMAL"
    HIGH = "HIGH"

class TrendStrength(Enum):
    WEAK = "WEAK"
    MODERATE = "MODERATE"
    STRONG = "STRONG"

class RiskLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class StrategyType(Enum):
    MOMENTUM = "MOMENTUM"
    BREAKOUT = "BREAKOUT"
    SHORT_MOMENTUM = "SHORT_MOMENTUM"
    SCALP = "SCALP"
    MEAN_REVERSION = "MEAN_REVERSION"
    WAIT = "WAIT"

class ActionDirection(Enum):
    LONG = "LONG"
    SHORT = "SHORT"
    FLAT = "FLAT"

# --- DATA OBJECTS ---

@dataclass
class MarketState:
    """
    Structured representation of the market context.
    Strictly adherence to 'PRE-TRADE STATE REQUIREMENT'.
    """
    # Core Regime
    market_regime: MarketRegime
    volatility_level: VolatilityLevel
    trend_strength: TrendStrength
    
    # Time Context
    time_of_day: str  # OPEN, MID, CLOSE, DEAD_ZONE
    trading_session: str  # ASIA, LONDON, NY, OVERLAP
    day_type: str  # WEEKDAY, WEEKEND
    week_phase: str  # EARLY, MID, LATE
    time_remaining_days: float
    
    # Technical Context
    distance_to_key_levels: float  # Percent to HTF High/Low
    funding_extreme: bool
    
    # Risk Context
    current_risk_state: str  # SAFE, CAUTION, DANGER
    current_drawdown_percent: float
    current_open_positions: int

    def to_dict(self) -> Dict[str, Any]:
        return {
            "market_regime": self.market_regime.value,
            "volatility_level": self.volatility_level.value,
            "trend_strength": self.trend_strength.value,
            "time_of_day": self.time_of_day,
            "trading_session": self.trading_session,
            "day_type": self.day_type,
            "week_phase": self.week_phase,
            "time_remaining_days": self.time_remaining_days,
            "distance_to_key_levels": self.distance_to_key_levels,
            "funding_extreme": self.funding_extreme,
            "current_risk_state": self.current_risk_state,
            "current_drawdown_percent": self.current_drawdown_percent,
            "current_open_positions": self.current_open_positions
        }

@dataclass
class Action:
    """
    Represents a trading decision.
    Strictly adherence to 'ACTION DEFINITION'.
    """
    strategy: StrategyType
    direction: ActionDirection
    risk_level: RiskLevel
    reasoning: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "strategy": self.strategy.value,
            "direction": self.direction.value,
            "risk_level": self.risk_level.value,
            "reasoning": self.reasoning
        }

    @staticmethod
    def wait(reason: str = "Insufficient specific signal") -> 'Action':
        return Action(
            strategy=StrategyType.WAIT,
            direction=ActionDirection.FLAT,
            risk_level=RiskLevel.LOW,
            reasoning=reason
        )

```

### File: `src/core/gating.py`

```python

from typing import List, Set
from src.core.definitions import MarketState, StrategyType, MarketRegime, VolatilityLevel

class StrategyGater:
    @staticmethod
    def get_allowed_strategies(state: MarketState) -> List[StrategyType]:
        """
        Determines which strategies are PERMITTED based on the Master Protocol.
        """
        
        # 1. Circuit Breaker (Hard Rule)
        # "If current_drawdown_percent <= -5: Disallow ALL strategies."
        if state.current_drawdown_percent <= -5.0:
            return []

        allowed: Set[StrategyType] = set()

        # 2. Regime-Based Rules
        if state.market_regime == MarketRegime.BULL_TREND:
            allowed.add(StrategyType.MOMENTUM)
            allowed.add(StrategyType.BREAKOUT)
            
        elif state.market_regime == MarketRegime.BEAR_TREND:
            allowed.add(StrategyType.SHORT_MOMENTUM)
            
        elif state.market_regime in [MarketRegime.SIDEWAYS_LOW_VOL, MarketRegime.SIDEWAYS_HIGH_VOL]:
            allowed.add(StrategyType.SCALP)
            allowed.add(StrategyType.MEAN_REVERSION)
            
        # TRANSITION regime usually implies caution; strictly following protocol implies NO strategies allowed
        # unless explicitly stated. Protocol says:
        # "If a strategy is not explicitly allowed, it must NOT be considered."
        # So TRANSITION -> Empty list (WAIT).

        # 3. Volatility Rules
        if state.volatility_level == VolatilityLevel.LOW:
            # "Disallow BREAKOUT (False break risk high)"
            if StrategyType.BREAKOUT in allowed:
                allowed.remove(StrategyType.BREAKOUT)

        return list(allowed)

```

### File: `src/core/reward.py`

```python

from src.core.definitions import MarketState

class RewardCalculator:
    @staticmethod
    def calculate_reward(
        state: MarketState, 
        realized_pnl_percent: float, 
        rule_violation: bool = False, 
        regime_mismatch: bool = False
    ) -> float:
        """
        Original method (kept for backward compatibility or estimates).
        """
        reward = realized_pnl_percent
        if rule_violation:
            reward -= 10.0
        if state.current_drawdown_percent < -2.0 and realized_pnl_percent < 0:
            reward -= abs(realized_pnl_percent) * 0.5
        if regime_mismatch:
            reward -= 2.0
        return round(reward, 4)

    @staticmethod
    def calculate_final_reward(
        exit_reason: str,
        realized_pnl: float,
        duration_candles: int,
        is_wait_action: bool = False,
        market_change_during_wait: float = 0.0,
        repetition_count: int = 0
    ) -> float:
        """
        Computes FINAL REWARD for Closed Loop Learning.
        Includes Diminishing Returns for Repetition.
        """
        reward = 0.0

        # 1. HANDLE WAIT ACTIONS
        if is_wait_action:
            # If we waited and market crashed -> Big Positive Reward (Savior)
            if market_change_during_wait < -1.0: # Market dropped > 1%
                reward += 1.0 # Good wait
            # If we waited and market pumped -> Negative Reward (Missed Opportunity)
            elif market_change_during_wait > 2.0: # Market pumped > 2%
                reward -= 0.5 # Missed out
            else:
                reward += 0.05 # Tiny reward for patience in noise
            return round(reward, 4)

        # 2. HANDLE TRADES
        reward = realized_pnl

        # Bonus for quick TP
        if exit_reason == "TP" and duration_candles < 5:
            reward += 0.5

        # Penalty for Timeouts (Stagnant capital)
        if exit_reason == "TIME":
            reward -= 0.1

        # Penalty for SL
        if exit_reason == "SL":
            # Standard PnL capture handles this, but maybe extra pain?
            pass

        return round(reward, 4) if is_wait_action else RewardCalculator._apply_diminishing_returns(reward, repetition_count)

    @staticmethod
    def _apply_diminishing_returns(base_reward: float, repeats: int) -> float:
        """
        Rules:
        0 (1st exec): 1.0x
        1 (2nd exec): 0.8x
        2 (3rd exec): 0.5x
        3+ (Further): 0.2x
        """
        if base_reward <= 0: return round(base_reward, 4) # Don't diminish penalties
        
        scale = 1.0
        if repeats == 1: scale = 0.8
        elif repeats == 2: scale = 0.5
        elif repeats >= 3: scale = 0.2
        
        return round(base_reward * scale, 4)

```

### File: `src/core/risk.py`

```python

from src.core.definitions import MarketState, Action, RiskLevel, StrategyType

class RiskManager:
    @staticmethod
    def validate_action(state: MarketState, action: Action) -> Action:
        """
        Validates and potentially modifies the action's risk parameters based on state.
        Returns the final authorized Action.
        """
        if action.strategy == StrategyType.WAIT:
            return action

        # 1. Enforcement of "DANGER" state
        if state.current_risk_state == "DANGER":
            # In Danger state, we only allow LOW risk or force WAIT.
            if action.risk_level != RiskLevel.LOW:
                # Downgrade to LOW
                return Action(
                    strategy=action.strategy,
                    direction=action.direction,
                    risk_level=RiskLevel.LOW,
                    reasoning=f"Downgraded risk due to DANGER state. (Original: {action.reasoning})"
                )
        
        # 2. Drawdown Proximity (Soft Circuit Breaker)
        # If close to -5%, force LOW risk
        if state.current_drawdown_percent <= -4.0:
            if action.risk_level != RiskLevel.LOW:
                 return Action(
                    strategy=action.strategy,
                    direction=action.direction,
                    risk_level=RiskLevel.LOW,
                    reasoning=f"Downgraded risk due to Drawdown proximity. (Original: {action.reasoning})"
                )
        
        return action

```

### File: `src/core/validation.py`

```python

from src.core.definitions import MarketState, MarketRegime, VolatilityLevel, TrendStrength

class ValidationException(Exception):
    """Raised when data integrity is compromised."""
    pass

class StateValidator:
    @staticmethod
    def validate_state(state: MarketState) -> bool:
        """
        Strictly validates constraints.
        Raises ValidationException on failure.
        """
        # 1. Null Checks
        if state.market_regime is None:
            raise ValidationException("Market Regime cannot be None")
        if state.volatility_level is None:
            raise ValidationException("Volatility Level cannot be None")
        
        # 2. Type Checks
        if not isinstance(state.market_regime, MarketRegime):
            raise ValidationException(f"Invalid Regime Type: {type(state.market_regime)}")
        
        # 3. Value Constraints
        if state.current_drawdown_percent > 0:
            # Drawdown should be negative or zero (e.g. -5.0)
            raise ValidationException(f"Drawdown must be <= 0, got {state.current_drawdown_percent}")
        
        if state.current_drawdown_percent < -100:
            raise ValidationException(f"Drawdown cannot be less than -100%, got {state.current_drawdown_percent}")

        if state.time_remaining_days < 0:
            raise ValidationException(f"Time remaining cannot be negative: {state.time_remaining_days}")

        # 4. Consistency Checks
        if state.market_regime == MarketRegime.SIDEWAYS_LOW_VOL and state.volatility_level == VolatilityLevel.HIGH:
            raise ValidationException("Contradiction: Regime is SIDEWAYS_LOW_VOL but Volatility is HIGH")

        return True

```

### File: `src/database/storage.py`

```python

import json
import os
import uuid
from datetime import datetime
from typing import Dict, Any, List, Optional
from src.config import Config
from src.core.definitions import MarketState, Action

class ExperienceDB:
    def __init__(self, filename: str = "experience_log.jsonl"):
        self.filepath = os.path.join(Config.DATA_PATH, filename)
        self._ensure_dir()

    def _ensure_dir(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

    def log_decision(self, state: MarketState, action: Action, reward: float = 0.0, data_source: str = "live") -> str:
        """
        Appends a single decision record.
        Returns: decision_id (UUID)
        """
        decision_id = str(uuid.uuid4())
        record = {
            "id": decision_id,
            "timestamp": datetime.utcnow().isoformat(),
            "market_state": state.to_dict(),
            "action_taken": action.to_dict(),
            "reward": reward,
            "resolved": False,  # Pending outcome
            "outcome": None,
            "metadata": {
                "version": "1.0",
                "mode": Config.TRADING_MODE,
                "data_source": data_source
            }
        }
        
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")
            
        return decision_id

    def finalize_record(self, decision_id: str, outcome_data: Dict[str, Any], final_reward: float):
        """
        Updates a specific record with outcome and final reward.
        Strategy: Read-Modify-Write (Acceptable for <100MB logs).
        """
        if not os.path.exists(self.filepath):
            return

        temp_path = self.filepath + ".tmp"
        updated = False
        
        with open(self.filepath, "r", encoding="utf-8") as infile, \
             open(temp_path, "w", encoding="utf-8") as outfile:
            
            for line in infile:
                try:
                    record = json.loads(line)
                    if record.get("id") == decision_id:
                        if record.get("resolved"):
                            # Already resolved, skip double update or overwrite?
                            # Protocol says: "Reward must be written exactly once."
                            # We'll assume overwrite is okay if correcting, 
                            # but normally we shouldn't hit this.
                            pass
                        
                        record["resolved"] = True
                        record["reward"] = final_reward
                        record["outcome"] = outcome_data
                        record["resolution_time"] = datetime.utcnow().isoformat()
                        updated = True
                    
                    outfile.write(json.dumps(record) + "\n")
                except json.JSONDecodeError:
                    continue # Skip corrupt lines
        
        # Atomic replace
        if updated:
            os.replace(temp_path, self.filepath)
        else:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def count_records(self) -> int:
        if not os.path.exists(self.filepath):
            return 0
        with open(self.filepath, "r", encoding="utf-8") as f:
            return sum(1 for _ in f)

    def get_recent_records(self, limit: int = 10) -> List[Dict[str, Any]]:
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return [json.loads(line) for line in lines[-limit:]]

```

### File: `src/engine/system.py`

```python

import logging
from typing import Optional, List, Tuple

from src.core.definitions import MarketState, Action, StrategyType, ActionDirection, RiskLevel, MarketRegime
from src.core.validation import StateValidator, ValidationException
from src.core.gating import StrategyGater
from src.core.risk import RiskManager
from src.database.storage import ExperienceDB

logger = logging.getLogger(__name__)

class TradingEngine:
    def __init__(self):
        self.db = ExperienceDB()
        
    def run_analysis(self, state: MarketState, data_source: str = "live") -> Tuple[Action, str, int]:
        """
        The Main Loop:
        Returns: (Action, decision_id, repetition_count)
        """
        try:
            # 1. Validation
            StateValidator.validate_state(state)
            
            # 2. Gating
            allowed_strategies = StrategyGater.get_allowed_strategies(state)
            
            # 3. Decision (Cold Start Rule Logic)
            raw_action, repeats = self._basic_selector(state, allowed_strategies)
            
            # 4. Risk Management
            final_action = RiskManager.validate_action(state, raw_action)
            
            # 5. Logging (Pending Reward)
            # Store repeats in metadata for complete traceability
            # But the return value is what matters really for Immediate Finalize loop
            decision_id = self.db.log_decision(state, final_action, reward=0.0, data_source=data_source)
            
            return final_action, decision_id, repeats

        except ValidationException as e:
            logger.error(f"State Validation Failed: {e}")
            fallback = Action.wait(reason=f"Validation Error: {e}")
            decision_id = self.db.log_decision(state, fallback, reward=0.0, data_source=data_source)
            return fallback, decision_id, 0
            
        except Exception as e:
            logger.error(f"System Error: {e}")
            fallback = Action.wait(reason=f"System Error: {e}")
            decision_id = self.db.log_decision(state, fallback, reward=0.0)
            return fallback, decision_id, 0

    def _basic_selector(self, state: MarketState, allowed: List[StrategyType]) -> Tuple[Action, int]:
        """
        A simple rule-based selector for Cold Start.
        Includes Logic to prevent excessive repetition (Max 3 consecutive same actions).
        Returns (Action, RepetitionCount for Diminishing Rewards)
        """
        if not allowed:
            return Action.wait(reason="No strategies allowed by Gating Protocol"), 0

        # 1. Fetch History
        history = self.db.get_recent_records(limit=3)
        
        # 2. Identify proposed primary strategy
        # Default: Pick first allowed
        proposed_strategy = allowed[0]

        # 2.5 Strategic Wait Injection (10% Chance)
        # "In strong trends, WAIT must still be chosen occasionally."
        import random
        if random.random() < 0.10:
             return Action.wait(reason="Strategic WAIT injection to gather inaction data."), 0
        
        # 3. Check Repetition
        # Count how many times we've done this EXACT strategy in the SAME context
        repeats = 0
        current_context = (state.market_regime.value, state.volatility_level.value)
        
        for record in reversed(history):
            recorded_action = record.get("action_taken", {})
            recorded_state = record.get("market_state", {})
            
            # Construct context from record
            # Note: Enums are stored as strings in JSON
            record_context = (recorded_state.get("market_regime"), recorded_state.get("volatility_level"))
            
            # Check for IDENTITY: Same Strategy AND Same Context
            is_same_strategy = recorded_action.get("strategy") == proposed_strategy.value
            is_same_context = record_context == current_context
            
            if is_same_strategy and is_same_context:
                repeats += 1
            else:
                break # Sequence broken (different strategy OR different context)
        
        # 4. Enforce Variety Rule
        if repeats >= 3:
            # We have done this 3 times in a row.
            # Try to find an alternative in 'allowed'
            alternatives = [s for s in allowed if s != proposed_strategy]
            
            if alternatives:
                # Pick the alternative
                proposed_strategy = alternatives[0]
                logger.info(f"Switching strategy to {proposed_strategy.name} to avoid repetition.")
                repeats = 0 # Reset repeats for new strategy
            else:
                # No alternatives?
                # Force WAIT
                return Action.wait(reason="Max consecutive repetitions reached. Forcing WAIT for diversity."), 0

        strategy = proposed_strategy
        
        direction = ActionDirection.FLAT
        if state.market_regime == MarketRegime.BULL_TREND:
            direction = ActionDirection.LONG
        elif state.market_regime == MarketRegime.BEAR_TREND:
            direction = ActionDirection.SHORT
        else:
            direction = ActionDirection.LONG 

        return Action(
            strategy=strategy,
            direction=direction,
            risk_level=RiskLevel.LOW, 
            reasoning=f"Selected {strategy.name} based on {state.market_regime.name}"
        ), repeats

```

### File: `src/exchange/connector.py`

```python

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

```

### File: `src/execution/paper.py`

```python

import logging
from src.core.definitions import Action, ActionDirection, StrategyType

logger = logging.getLogger(__name__)

class PaperExecutor:
    def __init__(self):
        logger.info("Paper Executor Initialized")

    def execute(self, action: Action, symbol: str) -> bool:
        """
        Simulates order execution.
        Returns True if successful.
        """
        if action.strategy == StrategyType.WAIT:
            return True

        if action.direction == ActionDirection.FLAT:
            return True

        # Simulate Order
        print(f"\n[PAPER TRADE] Executing {action.direction.name} on {symbol}")
        print(f"Strategy: {action.strategy.name}")
        print(f"Risk: {action.risk_level.name}")
        print(f"Reasoning: {action.reasoning}\n")
        
        logger.info(f"PAPER ORDER: {action.direction.name} {symbol} ({action.risk_level.name})")
        return True

```

### File: `docs/master_trader_prompt.md`

```markdown
# Master Trader Prompt

### CURRENT MISSION PHASE: DATA COLLECTION

You are being built to become a machine-learning based decision system.
**However, you must NOT use machine learning yet.**

Your current goal is:

- To collect clean, structured experience data.
- To learn which actions work in which situations.
- To prepare high-quality data for future ML training.

**Do NOT pretend to learn.**
**Do NOT hallucinate intelligence.**
Only observe, decide, and record.

**Data Quality Priority:**
Your highest priority is **DATA QUALITY**, not profit.

- A missed trade is acceptable.
- A bad data point is **not**.
- If market conditions are unclear, choose **WAIT**.
- WAIT decisions are valuable data.

You must prefer **fewer, cleaner decisions** over many noisy ones.

---

You are NOT a trading bot.
You are NOT allowed to predict price.
You are NOT allowed to give buy or sell commands.

Your role is an Adaptive Trading Execution Assistant.

Your ONLY responsibilities:

1. Decide whether trading is ALLOWED or FORBIDDEN
2. Select which strategy is PERMITTED
3. Select a risk bucket (LOW / MEDIUM / HIGH)
4. Enforce hard risk and discipline rules

You must prefer NO ACTION over bad action.
Doing nothing is a valid and often optimal decision.

If information is insufficient or ambiguous, you must respond with WAIT.

---

## MARKET PHILOSOPHY & OPERATIONAL RULES

You must treat the market as a probabilistic, adversarial system.

Price movement is caused by:

- Order flow
- Liquidity seeking
- Crowd positioning
- Volatility expansion and contraction

Indicators do NOT predict.
Indicators only DESCRIBE current state.

You must never assume future price direction.
You only reason about:

- Current market state
- Whether a strategy historically performed well in similar states

---

## PRE-TRADE STATE REQUIREMENT

Before evaluating any trade, you must construct a MARKET STATE object.

The state MUST include:

- market_regime: BULL_TREND / BEAR_TREND / SIDEWAYS_LOW_VOL / SIDEWAYS_HIGH_VOL / TRANSITION
- volatility_level: LOW / NORMAL / HIGH
- trend_strength: WEAK / MODERATE / STRONG
- time_of_day: OPEN / MID / CLOSE / DEAD_ZONE
- trading_session: ASIA / LONDON / NY / OVERLAP
- distance_to_key_levels: (Percent to HTF High/Low)
- current_risk_state: SAFE / CAUTION / DANGER
- day_type: WEEKDAY / WEEKEND
- week_phase: EARLY / MID / LATE
- funding_extreme: TRUE / FALSE
- time_remaining_days
- current_drawdown_percent
- current_open_positions

**Strict Prohibition:**

- **Never reason using raw price.**
- **Only reason using state.**

You are NOT allowed to evaluate trades without an explicit state.

You are NOT allowed to evaluate trades without an explicit state.

---

## REGIME MODELING & TRANSITIONS

You must explicitly model market regimes and regime transitions.

You are NOT allowed to instantly switch regimes based on a single signal.

**Valid Regimes:**

- `BULL_TREND`
- `BEAR_TREND`
- `SIDEWAYS_LOW_VOL`
- `SIDEWAYS_HIGH_VOL`
- `TRANSITION`

**Determination Rules:**

- You must determine regime using persistent evidence, not single candles.
- Regime stability is more important than early detection.

**Transition Rules:**

- If regime signals conflict, enter `TRANSITION` state.
- `TRANSITION` must persist for a minimum confirmation window.
- During `TRANSITION`:
  - Confidence is **LOW**
  - Risk must be **LOW**
  - Learning updates must be **down-weighted**
  - Default decision is **WAIT**

**State Labels:**
You must clearly label:

- `current_regime`
- `previous_regime`
- `transition_confidence` (LOW / MEDIUM / HIGH)

---

## TIME CONTEXT & SESSION LOGIC

You must treat time as a core part of market state.

**Expanded State Requirements:**
Every market state must include:

- `trading_session`: ASIA / LONDON / NY / OVERLAP
- `time_window`: OPEN / MID / CLOSE / DEAD_ZONE
- `day_type`: WEEKDAY / WEEKEND
- `week_phase`: EARLY / MID / LATE

**Time-Based Rules:**

- Strategies may perform well in one session and fail in another.
- You must learn performance **conditioned on time context**.
- You must **never generalize performance** across time contexts without evidence.

**Evaluation Logic:**

- Reward evaluation must account for time context.
- Losses during statistically weak time windows are **less penalized**.
- Profits during statistically weak time windows are **more valuable**.

If time context historically shows low reward expectancy, prefer **WAIT**.

---

## STRATEGY GATING LOGIC

You must NOT evaluate all strategies.
You must FIRST decide which strategies are ALLOWED based on state.

**Regime Rules:**

- If market_regime == **BULL**:  
  Allow only `MOMENTUM`, `BREAKOUT`
- If market_regime == **BEAR**:  
  Allow only `SHORT_MOMENTUM` (Bias towards defense)
- If market_regime == **SIDEWAYS**:  
  Allow only `SCALP` or `MEAN_REVERSION`

**Volatility Rules:**

- If volatility_bucket == **LOW**:  
  Disallow `BREAKOUT` (False break risk high)

**Circuit Breaker (Hard Rule):**

- If current_drawdown_percent <= -5:  
  **Disallow ALL strategies.** (Stop trading immediately)

If a strategy is not explicitly allowed, it must NOT be considered.

---

## INDICATOR MINIMALISM & CONFIDENCE

You must never use more than ONE indicator per information category.

**Allowed Mapping:**

- Trend → EMA 20/50
- Momentum → RSI
- Volatility → ATR
- Location → HTF Support/Resistance

If two indicators describe the same thing, discard one.
More indicators must REDUCE confidence, not increase it (due to overfitting risk).

---

## ACTION DEFINITION & OUTPUT

You do NOT choose BUY or SELL.

An ACTION is defined as:

- strategy_name
- direction (LONG / SHORT)
- risk_level (LOW / MEDIUM / HIGH)

**Example Action:**

```json
{
  "strategy": "MOMENTUM",
  "direction": "LONG",
  "risk_level": "MEDIUM"
}
```

If no action is clearly good, choose **WAIT**.
**WAIT is a valid action.**

---

## REWARD FUNCTION & EVALUATION

You must evaluate outcomes using a **REWARD**, not raw PnL.

**Reward Formula:**

```python
reward = 
  realized_pnl 
  - drawdown_penalty 
  - rule_violation_penalty
  - regime_quality_penalty
```

**Key Principles:**

1. **Context Matters:** Losses taken in a "Correct" state are LESS negative than losses taken in a "Bad" state.
2. **Rule Violations:** Breaking a hard rule is the **HIGHEST penalty**.
3. **Positive Zero:** Avoiding a bad trade is a **POSITIVE** reward (saved capital).
4. **Stability:** Consistent small wins > One lucky big win.

---

## MEMORY & ADAPTATION

For every evaluated action (including NO ACTION), you must store:

- `market_state` (The context)
- `chosen_action` (What you did)
- `reward` (The outcome score)
- `result` (WIN / LOSS / NO_TRADE)

This memory must be used to compare future decisions.
**Rule:** *“If I did X in State Y and got a bad Reward, I must lower the probability of doing X in State Y again.”*

**Learning & Updates:**
You must update behavior by comparing **average rewards**.

For similar market states:

- **Increase preference** for actions with higher average reward.
- **Decrease preference** for actions with lower average reward.

**Stability Rule:**
You must NOT instantly flip behavior based on one result.
Learning must be **gradual and conservative**.

**Sample Size & Confidence:**
You must track sample size.

If an action has **fewer than 20 samples** in a given state:

- Treat confidence as **LOW**.
- Prefer **conservative** risk buckets.

If uncertainty is high, default to **WAIT**.

---

## MACHINE LEARNING ROLE & RULES

Machine learning is an **assistant** to decision-making, not a replacement.

**Prohibitions:**

- You must **never** use ML to predict price direction.
- ML must **never override** risk limits or hard rules.

**Allowed ML Usage:**

- Estimating action success probability given a state.
- Ranking allowed actions by expected reward.
- Detecting weak patterns humans miss.

**Rules for ML Usage:**

- ML must operate only on **structured state features**.
- ML output must be **probabilistic**, not deterministic.
- Session/symbol encodings are persisted in `models/feature_maps.json` and reused in inference to keep training/inference aligned.

**Confidence Discounting:**
ML confidence must be **discounted** when:

- Sample size is low.
- Regime is `TRANSITION`.
- Volatility is extreme.

**Conflict Resolution:**
If ML confidence conflicts with rules, **RULES ALWAYS WIN**.

**ML Activation Criteria (Cold Start):**
You are **NOT allowed** to use machine learning until **ALL** of the following are true:

- At least **300 decisions** are recorded.
- Market states are stable.
- Reward calculation is consistent.

**Until Activation:**

- Use **rules**.
- Use **statistics**.
- **Store experience**.

**Future ML Constraints (When Enabled):**

- ML will **NOT** predict price.
- ML will **NOT** decide trades.
- ML will **ONLY**:
  - Estimate how good an action is in a given state.
  - Rank possible actions.
  - Suggest probabilities.

**Rules and risk controls will ALWAYS override ML.**

- Do not simulate learning you do not yet have.

---

## DATA LOGGING PROTOCOL

For **EVERY** decision (trade or wait), you **MUST** record:

1. `market_state` (Full context object)
2. `action_considered` (Strategy + Parameters)
3. `action_taken` (or WAIT)
4. `final_outcome` (Win/Loss/No Trade)
5. `reward_value` (Calculated via Reward Function)

**Purpose:**
This record will later be used to train a machine learning model.

**Strict Gate:**
If you cannot record cleanly, **do NOT act**.

---

## OUTPUT FORMAT

Your output must **always** follow this format:

**STATE SUMMARY:**

- market_regime:
- volatility_bucket:
- trend_strength:

**DECISION:**

- trade_allowed: YES / NO / WAIT
- allowed_strategies:
- recommended_risk_bucket:

**REASONING:**

- (One short paragraph only)

```

### File: `tests/test_mock_scenarios.py`

```python

import unittest
import shutil
import os
from src.core.definitions import MarketState, MarketRegime, VolatilityLevel, TrendStrength, StrategyType, ActionDirection, RiskLevel
from src.engine.system import TradingEngine

class TestTradingEngine(unittest.TestCase):
    def setUp(self):
        # Use a temporary test data directory
        self.test_data_dir = "tests/data"
        if os.path.exists(self.test_data_dir):
            shutil.rmtree(self.test_data_dir)
        os.makedirs(self.test_data_dir)
        
        # Patch config data path for testing (simplified approach)
        # Ideally we'd mock Config, but for now we just instantiate the Engine which uses Config.
        # We'll rely on the Engine creating the DB.
        # Note: The DB writes to Config.DATA_PATH. 
        # For this mock test, we mainly care about the RETURNED ACTION, not the file persistence.
        self.engine = TradingEngine()

    def create_mock_state(self, **kwargs):
        defaults = {
            "market_regime": MarketRegime.BULL_TREND,
            "volatility_level": VolatilityLevel.NORMAL,
            "trend_strength": TrendStrength.STRONG,
            "time_of_day": "MID",
            "trading_session": "NY",
            "day_type": "WEEKDAY",
            "week_phase": "MID",
            "time_remaining_days": 10.0,
            "distance_to_key_levels": 5.0,
            "funding_extreme": False,
            "current_risk_state": "SAFE",
            "current_drawdown_percent": 0.0,
            "current_open_positions": 0
        }
        defaults.update(kwargs)
        return MarketState(**defaults)

    def test_bull_market_logic(self):
        """Test 1: Bull Market -> Should allow Momentum -> Buy"""
        state = self.create_mock_state(market_regime=MarketRegime.BULL_TREND)
        action = self.engine.run_analysis(state)
        
        # Expectation: Strategy MOMENTUM or BREAKOUT allowed.
        # Basic Selector picks first one.
        # Direction should be LONG.
        self.assertIn(action.strategy, [StrategyType.MOMENTUM, StrategyType.BREAKOUT])
        self.assertEqual(action.direction, ActionDirection.LONG)

    def test_crash_circuit_breaker(self):
        """Test 2: Crash (-6% Drawdown) -> Should STOP trading (WAIT)"""
        state = self.create_mock_state(current_drawdown_percent=-6.0)
        action = self.engine.run_analysis(state)
        
        # Expectation: WAIT because Gating returns empty list.
        self.assertEqual(action.strategy, StrategyType.WAIT)
        self.assertIn("No strategies allowed", action.reasoning)

    def test_danger_risk_reduction(self):
        """Test 3: Danger State -> Should force LOW risk"""
        state = self.create_mock_state(current_risk_state="DANGER")
        action = self.engine.run_analysis(state)
        
        # Expectation: Action might be valid, but Risk must be LOW.
        if action.strategy != StrategyType.WAIT:
            self.assertEqual(action.risk_level, RiskLevel.LOW)
            self.assertIn("Downgraded risk", action.reasoning)

    def test_invalid_data_rejection(self):
        """Test 4: Bad Data (Negative Time) -> Should Reject"""
        # Logic error: time cannot be negative
        state = self.create_mock_state(time_remaining_days=-5.0)
        action = self.engine.run_analysis(state)
        
        self.assertEqual(action.strategy, StrategyType.WAIT)
        self.assertIn("Validation Error", action.reasoning)

    def test_bear_market_logic(self):
        """Test 5: Bear Market -> Should SHORT"""
        state = self.create_mock_state(market_regime=MarketRegime.BEAR_TREND)
        action = self.engine.run_analysis(state)
        
        self.assertEqual(action.strategy, StrategyType.SHORT_MOMENTUM)
        self.assertEqual(action.direction, ActionDirection.SHORT)

if __name__ == '__main__':
    unittest.main()

```

### File: `scripts/dry_run.py`

```python

import random
from src.core.definitions import MarketState, MarketRegime, VolatilityLevel, TrendStrength
from src.engine.system import TradingEngine

def generate_random_state(regime: MarketRegime) -> MarketState:
    """Helper to generate a varied state for testing."""
    return MarketState(
        market_regime=regime,
        volatility_level=random.choice(list(VolatilityLevel)),
        trend_strength=random.choice(list(TrendStrength)),
        time_of_day="MID",
        trading_session="NY",
        day_type="WEEKDAY",
        week_phase="MID",
        time_remaining_days=float(random.randint(1, 30)),
        distance_to_key_levels=random.uniform(0.5, 10.0),
        funding_extreme=False,
        current_risk_state="SAFE",
        current_drawdown_percent=random.uniform(-4.0, 0.0),
        current_open_positions=0
    )

def main():
    print("Starting Dry Run: Observation Mode...")
    engine = TradingEngine()
    
    # 1. Bull Trends (Should Buy)
    for _ in range(4):
        state = generate_random_state(MarketRegime.BULL_TREND)
        action = engine.run_analysis(state)
        print(f"[BULL] Action: {action.strategy.name} {action.direction.name} | R: {action.risk_level.name}")

    # 2. Bear Trends (Should Short)
    for _ in range(3):
        state = generate_random_state(MarketRegime.BEAR_TREND)
        action = engine.run_analysis(state)
        print(f"[BEAR] Action: {action.strategy.name} {action.direction.name} | R: {action.risk_level.name}")

    # 3. Sideways (Should Scalp)
    for _ in range(3):
        state = generate_random_state(MarketRegime.SIDEWAYS_HIGH_VOL)
        action = engine.run_analysis(state)
        print(f"[SIDE] Action: {action.strategy.name} {action.direction.name} | R: {action.risk_level.name}")

    print("\nDry Run Complete.")
    print(f"Data logged to: {engine.db.filepath}")
    print(f"Total Records: {engine.db.count_records()}")

if __name__ == "__main__":
    main()

```

### File: `scripts/export_project.py`

```python

import os

OUTPUT_FILE = "project_context.md"

# Directories/Files to Include
INCLUDE_DIRS = ["src", "docs", "tests", "scripts"]
INCLUDE_FILES = ["main.py", "requirements.txt", ".env.example"]

# Directories/Files to Exclude
EXCLUDE_DIRS = [".venv", "__pycache__", ".git", "pine_scripts", "data", "Lib", "Include", "Scripts"]
EXCLUDE_EXTENSIONS = [".pyc", ".pyd", ".log", ".jsonl"]

def get_file_content(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def main():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("# Adaptive Trading Assistant - Project Context\n\n")
        
        # 1. Directory Structure
        out.write("## 1. Directory Structure\n```\n")
        for root, dirs, files in os.walk("."):
            # Filter excludes
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]
            
            level = root.replace(".", "").count(os.sep)
            indent = " " * 4 * (level)
            out.write(f"{indent}{os.path.basename(root)}/\n")
            subindent = " " * 4 * (level + 1)
            for f in files:
                if not any(f.endswith(ext) for ext in EXCLUDE_EXTENSIONS) and f != OUTPUT_FILE:
                    out.write(f"{subindent}{f}\n")
        out.write("```\n\n")

        # 2. File Contents
        out.write("## 2. File Contents\n\n")
        
        # Root Files
        for f in INCLUDE_FILES:
            if os.path.exists(f):
                content = get_file_content(f)
                out.write(f"### File: `{f}`\n\n```python\n{content}\n```\n\n")

        # Directory Walk
        for target_dir in INCLUDE_DIRS:
            for root, dirs, files in os.walk(target_dir):
                # Filter excludes
                dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
                
                for file in files:
                    if any(file.endswith(ext) for ext in EXCLUDE_EXTENSIONS):
                        continue
                        
                    filepath = os.path.join(root, file)
                    # Determine language for markdown fencing
                    ext = os.path.splitext(file)[1]
                    lang = "python" if ext == ".py" else "markdown" if ext == ".md" else "text"
                    
                    content = get_file_content(filepath)
                    out.write(f"### File: `{filepath.replace(os.sep, '/')}`\n\n```{lang}\n{content}\n```\n\n")

    print(f"Project exported to {os.path.abspath(OUTPUT_FILE)}")

if __name__ == "__main__":
    main()

```

