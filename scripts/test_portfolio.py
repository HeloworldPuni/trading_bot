import sys
import os
import pandas as pd
import numpy as np
import logging

sys.path.append(os.getcwd())

from src.portfolio.allocator import PortfolioAllocator
from src.portfolio.risk import RiskManager
from src.strategies.base import StrategySignal

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def main():
    print("=== Testing Portfolio Allocation Engine (Phase 7) ===")
    
    # Setup
    risk_man = RiskManager(max_leverage=2.0, max_position_size=0.5, target_volatility=0.40)
    allocator = PortfolioAllocator(risk_man)
    
    print("\n[Scenario 1] High Confidence, Low Volatility")
    # Signals
    signals = {
        'Trend': StrategySignal(1, 0.8),    # Strong Long
        'MeanRev': StrategySignal(-1, 0.6)  # Moderate Short
    }
    
    # Market Data (Low Vol: 1% daily)
    prices = pd.Series(np.cumprod(1 + np.random.normal(0, 0.01, 100))) 
    hist_prices = {'BTC/USDT': prices}
    current_prices = {'BTC/USDT': prices.iloc[-1]}
    
    # Run Allocator
    weights = allocator.allocate(signals, current_prices, hist_prices)
    print("Weights:", weights)
    
    # Validate Scen 1
    total_lev = sum(abs(w) for w in weights.values())
    print(f"Total Leverage: {total_lev:.2f}")
    
    if total_lev <= risk_man.max_leverage + 0.1:
        print(f"PASS: Leverage <= {risk_man.max_leverage}")
    else:
        print(f"FAIL: Leverage {total_lev:.2f} > {risk_man.max_leverage}")
        
    for k, w in weights.items():
        if abs(w) > risk_man.max_position_size + 0.01:
            print(f"FAIL: {k} Size {w:.2f} > Limit {risk_man.max_position_size}")
        else:
            print(f"PASS: {k} Size {w:.2f} <= Limit")

    trend_base = abs(weights['Trend']) # Capture for comparison

    print("\n[Scenario 2] High Volatility (Crash Mode)")
    # Market Data (High Vol: 5% daily -> ~100% annual)
    prices_crash = pd.Series(np.cumprod(1 + np.random.normal(0, 0.05, 100)))
    hist_prices_crash = {'BTC/USDT': prices_crash}
    
    weights_crash = allocator.allocate(signals, current_prices, hist_prices_crash)
    print("Weights (Crash):", weights_crash)
    
    # Validate Scen 2
    trend_crash = abs(weights_crash['Trend'])
    
    print(f"Base Trend Size: {trend_base:.4f}")
    print(f"Crash Trend Size: {trend_crash:.4f}")
    
    if trend_crash < trend_base:
         print(f"PASS: Volatility Targeting Active ({trend_crash:.4f} < {trend_base:.4f}).")
    else:
         print(f"FAIL: High Vol did not reduce size. {trend_crash} >= {trend_base}")

if __name__ == "__main__":
    main()
