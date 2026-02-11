
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
    ARBITRAGE = "ARBITRAGE"
    MARKET_MAKING = "MARKET_MAKING"
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
    distance_to_key_levels: float  # Legacy, will keep for now
    current_price: float = 0.0
    rsi: float = 50.0
    trend_spread: float = 0.0      # SMA20 - SMA50 %
    dist_to_high: float = 0.0      # % to 50h High
    dist_to_low: float = 0.0       # % to 50h Low
    
    # Advanced Indicators (Phase 31)
    macd: float = 0.0
    macd_signal: float = 0.0
    macd_hist: float = 0.0
    bb_upper: float = 0.0
    bb_lower: float = 0.0
    bb_mid: float = 0.0
    atr: float = 0.0
    volume_delta: float = 0.0      # Net buying pressure (if available)
    
    # Execution-Aware Features
    spread_pct: float = 0.0         # (high - low) / close * 100
    body_pct: float = 0.0           # |close - open| / close * 100
    gap_pct: float = 0.0            # (open - prev_close) / prev_close * 100
    volume_zscore: float = 0.0      # Z-score of volume over window
    liquidity_proxy: float = 0.0    # Volume / ATR proxy

    # Metadata
    funding_rate: float = 0.0         # Current funding rate % (extreme = potential reversal)
    funding_extreme: bool = False     # True if |funding_rate| > 0.1%
    raw_timestamp: Optional[str] = None
    
    # Risk Context
    current_risk_state: str = "SAFE"
    current_drawdown_percent: float = 0.0
    current_open_positions: int = 0
    symbol: str = "BTC/USDT" 
    
    # Phase C: Anticipatory Regime Detection
    regime_confidence: float = 1.0      # 0-1 score of regime stability
    regime_stable: bool = True          # False if momentum shows potential shift
    momentum_shift_score: float = 0.0   # -1 to 1: negative = bearish momentum, positive = bullish
    
    # Higher Timeframe (HTF) Features
    htf_trend_spread: float = 0.0
    htf_rsi: float = 50.0
    htf_atr: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "symbol": self.symbol,
            "market_regime": self.market_regime.value,
            "volatility_level": self.volatility_level.value,
            "trend_strength": self.trend_strength.value,
            "time_of_day": self.time_of_day,
            "trading_session": self.trading_session,
            "day_type": self.day_type,
            "week_phase": self.week_phase,
            "time_remaining_days": self.time_remaining_days,
            "distance_to_key_levels": self.distance_to_key_levels,
            "current_price": self.current_price,
            "rsi": self.rsi,
            "trend_spread": self.trend_spread,
            "dist_to_high": self.dist_to_high,
            "dist_to_low": self.dist_to_low,
            "macd": self.macd,
            "macd_signal": self.macd_signal,
            "macd_hist": self.macd_hist,
            "bb_upper": self.bb_upper,
            "bb_lower": self.bb_lower,
            "bb_mid": self.bb_mid,
            "atr": self.atr,
            "volume_delta": self.volume_delta,
            "spread_pct": self.spread_pct,
            "body_pct": self.body_pct,
            "gap_pct": self.gap_pct,
            "volume_zscore": self.volume_zscore,
            "liquidity_proxy": self.liquidity_proxy,
            "funding_rate": self.funding_rate,  # Added for inference parity
            "funding_extreme": self.funding_extreme,
            "raw_timestamp": self.raw_timestamp,
            "current_risk_state": self.current_risk_state,
            "current_drawdown_percent": self.current_drawdown_percent,
            "current_open_positions": self.current_open_positions,
            "regime_confidence": self.regime_confidence,  # Added for inference parity
            "regime_stable": self.regime_stable,  # Added for inference parity
            "momentum_shift_score": self.momentum_shift_score,  # Added for inference parity
            "htf_trend_spread": self.htf_trend_spread,
            "htf_rsi": self.htf_rsi,
            "htf_atr": self.htf_atr,
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
    base_risk: float = 0.0 # Percentage risk (e.g., 1.0 for 1%)
    adjusted_risk: float = 0.0
    risk_multiplier: float = 1.0
    target_weight: float = 0.0
    tp: float = 0.0
    sl: float = 0.0
    reasoning: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "strategy": self.strategy.value,
            "direction": self.direction.value,
            "risk_level": self.risk_level.value,
            "base_risk": self.base_risk,
            "adjusted_risk": self.adjusted_risk,
            "risk_multiplier": self.risk_multiplier,
            "target_weight": self.target_weight,
            "tp": self.tp,
            "sl": self.sl,
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
