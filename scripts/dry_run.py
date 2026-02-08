
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
