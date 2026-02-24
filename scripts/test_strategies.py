import sys
import os
import pandas as pd
import numpy as np
sys.path.append(os.getcwd())

from src.features.store import FeatureStore
from src.features.regime import RegimeDetector
from src.strategies.trend import TrendFollowingStrategy
from src.strategies.mean_reversion import MeanReversionStrategy

def calculate_indicators(df: pd.DataFrame):
    """Augment DataFrame with necessary indicators."""
    close = df['close']
    
    # EMAs for Trend
    df['ema_20'] = close.ewm(span=20).mean()
    df['ema_50'] = close.ewm(span=50).mean()
    
    # ADX for Trend
    # (Simplified for test script, usually use TA-Lib or the RegimeDetector logic)
    # Re-using passing 'adx' if available or calculating simplified version
    
    # Bollinger for MeanReversion
    sma = close.rolling(20).mean()
    std = close.rolling(20).std()
    df['bb_upper'] = sma + (2 * std)
    df['bb_lower'] = sma - (2 * std)
    
    # RSI for MeanReversion
    delta = close.diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ema_up = up.ewm(com=13, adjust=False).mean()
    ema_down = down.ewm(com=13, adjust=False).mean()
    rs = ema_up / ema_down
    df['rsi'] = 100 - (100 / (1 + rs))
    
    # ATR for Risk
    tr1 = df['high'] - df['low']
    tr2 = (df['high'] - close.shift(1)).abs()
    tr3 = (df['low'] - close.shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    df['atr'] = tr.rolling(14).mean()
    
    # ADX (Quick implementation)
    # Using the RegimeDetector private logic or standard lib would be better
    # We will assume ADX comes from RegimeDetector or calc it here
    df['adx'] = 30 # Mock ADX for testing entry logic mostly
    
    return df

def main():
    symbol = "BTC/USDT"
    print(f"Testing Strategy Library for {symbol}...\n")
    
    store = FeatureStore(symbol)
    trades = store.load_trades()
    if trades.empty:
        print("Data missing.")
        return

    # 1. Prepare Data
    bars = store.resample_trades(trades, rule='5min')
    bars = calculate_indicators(bars)
    
    # 2. Prepare Context (Regime)
    regime_df = pd.DataFrame(index=bars.index)
    regime_df['vol_regime'] = RegimeDetector.get_volatility_regime(bars['close'])
    regime_df['trend_regime'] = RegimeDetector.get_trend_regime(bars['high'], bars['low'], bars['close'])
    
    # 3. Initialize Strategies
    trend_strat = TrendFollowingStrategy()
    mean_strat = MeanReversionStrategy()
    
    print("Running Strategies...")
    
    trend_signals = []
    mean_signals = []
    
    for i in range(50, len(bars)):
        row = bars.iloc[i]
        ctx = regime_df.iloc[i]
        
        # Trend
        ts = trend_strat.generate_signal(row, ctx)
        if ts.signal != 0:
            trend_signals.append((bars.index[i], ts))
            
        # Mean Reversion
        ms = mean_strat.generate_signal(row, ctx)
        if ms.signal != 0:
            mean_signals.append((bars.index[i], ms))
            
    print(f"\nTrend Signals: {len(trend_signals)}")
    if trend_signals:
        print(f"Sample: {trend_signals[0]}")
        
    print(f"\nMean Reversion Signals: {len(mean_signals)}")
    if mean_signals:
        print(f"Sample: {mean_signals[0]}")
        
    # Validation: Ensure Trend Strategy didn't trade in Range Regime
    trend_violations = 0
    for ts in trend_signals:
        idx = ts[0]
        if regime_df.loc[idx, 'trend_regime'] == 0 and regime_df.loc[idx, 'vol_regime'] != 1:
            trend_violations += 1
            
    print(f"\nRegime Violations (Trend Strategy): {trend_violations}")

if __name__ == "__main__":
    main()
