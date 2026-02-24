import sys
import os
import logging
import pandas as pd

sys.path.append(os.getcwd())

from src.features.store import FeatureStore
from src.strategies.trend import TrendFollowingStrategy
from src.strategies.mean_reversion import MeanReversionStrategy
from src.strategies.arbitrage import FundingArbitrageStrategy
from src.models.dataset import StrategyDataset
from src.models.engine import StrategyModel

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def train_strategy_model(strategy, store):
    logging.info(f"\n=== Training Model for {strategy.name} ===")
    
    # 1. Prepare Data
    ds = StrategyDataset(store)
    X, y = ds.prepare_dataset(strategy)
    
    if X.empty or y.empty:
        logging.warning(f"Skipping {strategy.name} due to empty dataset (no signals or labels).")
        return
        
    logging.info(f"Dataset Shape: X={X.shape}, y={y.shape}")
    logging.info(f"Target Distribution:\n{y.value_counts(normalize=True)}")
    
    if len(y.unique()) < 2:
        logging.warning(f"Target has only 1 class: {y.unique()}. Cannot train classifier.")
        return

    # 2. Train Model
    model = StrategyModel(name=strategy.name)
    model.train(X, y)
    
    # 3. Save
    model.save()
    logging.info(f"Model for {strategy.name} saved.")

def main():
    symbol = "BTC/USDT"
    store = FeatureStore(symbol)
    
    # Define Strategies to Train
    strategies = [
        TrendFollowingStrategy(adx_threshold=10),
        MeanReversionStrategy(rsi_buy=40, rsi_sell=60), # Looser RSI
        # FundingArbitrageStrategy() 
    ]
    
    for strat in strategies:
        try:
            train_strategy_model(strat, store)
        except Exception as e:
            logging.error(f"Failed to train {strat.name}: {e}")

if __name__ == "__main__":
    main()
