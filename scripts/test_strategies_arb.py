import sys
import os
import pandas as pd
sys.path.append(os.getcwd())

from src.strategies.arbitrage import FundingArbitrageStrategy

def main():
    print("Testing FundingArbitrageStrategy...")
    
    strat = FundingArbitrageStrategy(funding_threshold=0.05)
    
    # 1. High Positive Funding (0.1%) -> Short Perp
    row_high = pd.Series({'funding_rate': 0.10})
    signal_high = strat.generate_signal(row_high)
    
    print(f"Scenario 1 (High Funding 0.1%): Signal={signal_high.signal} Confidence={signal_high.confidence:.2f}")
    if signal_high.signal == -1:
        print("PASS: Shorted correctly.")
    else:
        print("FAIL: Did not short.")
        
    # 2. High Negative Funding (-0.08%) -> Long Perp
    row_low = pd.Series({'funding_rate': -0.08})
    signal_low = strat.generate_signal(row_low)
    
    print(f"Scenario 2 (Neg Funding -0.08%): Signal={signal_low.signal} Confidence={signal_low.confidence:.2f}")
    if signal_low.signal == 1:
        print("PASS: Longed correctly.")
    else:
        print("FAIL: Did not long.")
        
    # 3. Normal Funding (0.01%) -> No Signal
    row_normal = pd.Series({'funding_rate': 0.01})
    signal_normal = strat.generate_signal(row_normal)
    
    print(f"Scenario 3 (Normal Funding 0.01%): Signal={signal_normal.signal}")
    if signal_normal.signal == 0:
        print("PASS: Ignored normal funding.")
    else:
        print("FAIL: Traded on noise.")

if __name__ == "__main__":
    main()
