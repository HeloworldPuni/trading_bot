import sys
import os
import pandas as pd
import numpy as np
import logging

sys.path.append(os.getcwd())

from src.config import Config
from src.features.store import FeatureStore
from src.features.microstructure import MicrostructureFeatures
from src.features.context import ContextFeatures
from src.features.relative import RelativeFeatures
from src.features.volatility import VolatilityEstimator
from src.features.labeler import TripleBarrierLabeler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    symbol = "BTC/USDT"
    logging.info(f"Generating Dataset for {symbol}...")
    
    store = FeatureStore(symbol)
    
    # 1. Load Raw Data
    trades = store.load_trades()
    ob = store.load_orderbook()
    
    if trades.empty:
        logging.error("No trades found.")
        return

    # 2. Resample (5-min bars for ML)
    # Note: Phase 3 Labeler used 1-min for high freq, but for Strategy Filtering 
    # we standardizing on 5-min execution for now.
    bars = store.resample_trades(trades, rule='5min')
    logging.info(f"Resampled to {len(bars)} 5-min bars.")
    
    # 3. Features (Phase 2)
    logging.info("Calculating Features...")
    
    # Microstructure (OFI, Spread)
    # Note: Microstructure usually needs high-res data. 
    # For now we use the aggregated bars as inputs or simpler logic.
    # Assuming MicrostructureFeatures works on bars or we skip specific tick-level ones.
    # Actually, MicrostructureFeatures might expect tick data.
    # Let's use simple logic here or what was available.
    
    # Recalculating aggregated features on 5-min bars
    df_feat = bars.copy()
    
    # Context (Vol, Funding)
    # Dummy Funding for now if not in bars
    if 'funding_rate' not in df_feat.columns:
        df_feat['funding_rate'] = 0.0001
        
    df_feat['vol_expansion'] = ContextFeatures.calc_volatility_expansion(df_feat['close'], short_span=10, long_span=50)
    
    # Funding Divergence (Corr between Funding and Price Trend)
    df_feat['funding_divergence'] = ContextFeatures.calc_funding_divergence(
        df_feat['funding_rate'], 
        df_feat['close'] # Pass raw price, method handles trend? No, checks corr.
    )
    
    # Microstructure (Spread, OFI)
    # If we have orderbook data loaded
    if not ob.empty:
        # Ensure DatetimeIndex for resampling
        if 'timestamp' in ob.columns:
            ob = ob.set_index('timestamp')
            
        # Resample OB to match bars?
        # Or just calculate spread on OB and then resample/reindex
        logging.info("Calculating Microstructure Features...")
        spread_df = MicrostructureFeatures.calc_spread(ob)
        # Resample spread to 5min (mean)
        spread_resampled = spread_df.resample('5min').mean()
        
        # Join to df_feat (align index)
        # Note: resample creates bins, might need reindex
        df_feat['spread_rel'] = spread_resampled['spread_rel']
        
        # OFI (Change in Order Flow)
        # OFI on raw OB then resample sum?
        # OFI is cumulative volume. Sum is appropriate.
        ofi = MicrostructureFeatures.calc_ofi(ob)
        ofi_resampled = ofi.resample('5min').sum()
        df_feat['ofi'] = ofi_resampled
    else:
        df_feat['spread_rel'] = 0.0
        df_feat['ofi'] = 0.0
    
    # Relative (need ETH, but we skip for single-asset test)
    
    # Add Technicals (EMA, RSI, BB) - Strategy Inputs
    close = df_feat['close']
    df_feat['ema_20'] = close.ewm(span=20).mean()
    df_feat['ema_50'] = close.ewm(span=50).mean()
    df_feat['adx'] = 30.0 # Placeholder
    
    # Save Features
    feat_path = os.path.join(Config.DATA_PATH, "features", f"{symbol.replace('/', '_')}_features.parquet")
    if not os.path.exists(os.path.dirname(feat_path)):
        os.makedirs(os.path.dirname(feat_path))
        
    df_feat.to_parquet(feat_path)
    logging.info(f"Saved features to {feat_path}")
    
    # 4. Labels (Phase 3)
    logging.info("Calculating Labels...")
    vol = VolatilityEstimator.get_daily_vol(close, span=50)
    
    t_events = close.index
    vertical_barriers = t_events + pd.Timedelta(minutes=60) # 1 hour horizon
    
    labels = TripleBarrierLabeler.get_events(
        close_prices=close,
        t_events=t_events,
        pt_sl=[1.0, 1.0], # Symmetric 1x Vol
        target=vol,
        min_ret=0.0005,
        vertical_barrier_times=pd.Series(vertical_barriers, index=t_events)
    )
    
    # Calculate Returns for the labels
    # labels has index t0, column t1
    # We need to fetch price at t1 and t0
    
    # Filter out where t1 is NaT (shouldn't happen with vertical barriers but check)
    labels = labels.dropna(subset=['t1'])
    
    t0_prices = close.loc[labels.index]
    # t1 might not be in close.index if it falls between bars or is future
    # We use asof or reindex. 
    # Since t1 comes from vertical barrier (future time), it might match a bar exactly or not.
    # Vertical barrier was created with +1h.
    # We use searchsorted or map.
    
    # Simplest: use map if aligned, else use get_indexer
    # close is indexed by timestamp.
    # We need price at labels['t1']
    
    t1_prices = close.asof(labels['t1']) # Last available price at t1
    
    # Return = (P_t1 / P_t0) - 1
    # Align t1_prices to labels index
    t1_prices.index = labels.index
    
    labels['ret'] = (t1_prices / t0_prices) - 1
    
    label_path = os.path.join(Config.DATA_PATH, "features", f"{symbol.replace('/', '_')}_labels.parquet")
    labels.to_parquet(label_path)
    logging.info(f"Saved labels to {label_path}")
    logging.info(f"Label Stats:\n{labels['label'].value_counts()}")

if __name__ == "__main__":
    main()
