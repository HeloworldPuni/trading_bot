# 🤖 AI Trading Bot (Basecoin)

An adaptive cryptocurrency trading bot with ML-powered decision making, dynamic position sizing, and multi-asset support.

## 🏗️ Architecture

```
basecoin/
├── main.py                 # Entry point - run modes (live, replay, backtest)
├── src/
│   ├── config.py           # All configuration parameters
│   ├── core/
│   │   ├── definitions.py  # Enums (MarketRegime, Action, StrategyType)
│   │   ├── portfolio.py    # Position management, PnL tracking
│   │   ├── risk.py         # Risk validation
│   │   ├── gating.py       # Strategy gating by market regime
│   │   └── validation.py   # State validation
│   ├── engine/
│   │   └── system.py       # TradingEngine - main decision loop
│   ├── exchange/
│   │   └── connector.py    # Binance API wrapper (ccxt)
│   ├── data/
│   │   ├── feeder.py       # Live market data + indicators
│   │   └── replay_feeder.py # Historical data replay
│   ├── ml/
│   │   ├── inference.py    # PolicyInference - ML predictions
│   │   ├── pipeline.py     # Training pipeline
│   │   ├── trainer.py      # Model training
│   │   └── registry.py     # Model version management
│   ├── execution/
│   │   └── paper.py        # Paper trading executor
│   ├── database/
│   │   └── storage.py      # Experience logging (JSONL)
│   └── ui/
│       └── dashboard.py    # Rich terminal dashboard
└── scripts/
    ├── train_policy.py     # Train main model
    ├── train_ensemble.py   # Train regime-specific experts
    └── learning_scheduler.py # Automated retraining
```

## 🧠 ML Models

### Model Types

| Model | Path | Purpose |
|-------|------|---------|
| Main Policy | `models/policy_model_v1.pkl` | General trading decisions |
| Bull Expert | `models/policy_bull.pkl` | Bull market specialist |
| Bear Expert | `models/policy_bear.pkl` | Bear market specialist |
| Sideways Expert | `models/policy_sideways.pkl` | Range-bound specialist |

### Feature Vector (Input)

```python
features = {
    "market_regime": int,      # BULL_TREND, BEAR_TREND, SIDEWAYS_*
    "volatility_level": int,   # LOW, NORMAL, HIGH
    "trend_strength": int,     # WEAK, MODERATE, STRONG, VERY_STRONG
    "dist_to_high": float,     # % distance to recent high
    "dist_to_low": float,      # % distance to recent low
    "macd": float,            
    "macd_signal": float,
    "macd_hist": float,
    "bb_upper": float,         # Bollinger Bands
    "bb_lower": float,
    "bb_mid": float,
    "atr": float,              # Average True Range
    "volume_delta": float,     # Volume change %
    "spread_pct": float,       # (high-low)/close * 100
    "body_pct": float,         # |close-open|/close * 100
    "gap_pct": float,          # open-prev_close % gap
    "volume_zscore": float,    # volume z-score
    "liquidity_proxy": float,  # volume/ATR
    "htf_trend_spread": float, # Higher TF SMA spread
    "htf_rsi": float,          # Higher TF RSI
    "htf_atr": float,          # Higher TF ATR
    "trading_session": int,    # ASIA, LONDON, NY, OVERLAP
    "symbol": int,             # Encoded symbol
    "repeats": int,            # Consecutive same-action count
    "current_open_positions": int,
    "action_taken": int,       # Proposed strategy
    "regime_confidence": float,
    "regime_stable": int,
    "momentum_shift_score": float
}
```

### Output

- `predict_proba()` returns confidence [0.0 - 1.0]
- Confidence > `ML_CONFIDENCE_MIN` required to execute trade (configurable)
- Used for position sizing and leverage scaling

## 📊 Trading Logic Flow

```
1. Fetch Market Data (OHLCV + indicators)
         ↓
2. Detect Market Regime (BULL/BEAR/SIDEWAYS)
         ↓
3. Strategy Gating (which strategies allowed?)
         ↓
4. ML Confidence Prediction
         ↓
5. Smart Position Sizing (ATR + Confidence based)
         ↓
6. Execute Trade (if confidence > threshold)
         ↓
7. Monitor TP/SL → Close Position
         ↓
8. Log Experience → Future Training
```

## ⚙️ Key Configuration (src/config.py)

| Parameter | Value | Description |
|-----------|-------|-------------|
| `RISK_PROFILE` | balanced | `balanced` or `aggressive` default presets |
| `BASE_LEVERAGE` | 10 | Default leverage |
| `MAX_POSITION_PCT` | 0.10 | 10% of balance per trade |
| `MAX_POSITIONS_PER_SYMBOL` | 1 | Max concurrent positions per symbol |
| `MAX_CONCURRENT_POSITIONS` | 20 | Max total open positions |
| `TOP_COINS_COUNT` | 15 | Number of coins to scan |
| `SCAN_TIMEFRAME` | "15m" | Candle timeframe |
| `LTF_LOOKBACK` | 200 | Candles used for LTF features |
| `HTF_TIMEFRAME` | "1h" | Higher timeframe for features |
| `HTF_LOOKBACK` | 50 | Candles used for HTF features |
| `SCALP_TP_PCT` | 1.5% | Scalp take profit |
| `SWING_TP_PCT` | 6.0% | Swing take profit |
| `MIN_SIGNAL_SCORE` | 0.60 | Minimum rule-based signal score to allow trade |
| `ML_CONFIDENCE_MIN` | 0.65 | Minimum ML confidence to allow trade |
| `NEAR_LEVEL_PCT` | 1.0 | "Near high/low" proximity threshold (%) |
| `STRATEGIC_WAIT_PROB` | 0.10 | Random WAIT injection for data diversity (0 disables) |
| `EV_GATING` | true | Enable expected-value gating |
| `EV_THRESHOLD` | 0.0 | Minimum EV (percent) required to trade |
| `MAX_DAILY_LOSS_PCT` | 5.0 | Daily loss limit (% of equity) |
| `MAX_DRAWDOWN_PCT` | 15.0 | Max drawdown from peak equity |
| `VOL_TARGET_DAILY_PCT` | 2.0 | Volatility targeting (daily % vol) |
| `EXPOSURE_CAP_PCT` | 0.60 | Max gross exposure (% of equity) |
| `CORR_CLUSTER_CAP_PCT` | 0.40 | Max exposure per cluster |
| `STRATEGY_MIN_SAMPLES` | 20 | Minimum samples before weighting strategies |
| `STRATEGY_WEIGHTING_ENABLED` | true | Enable strategy performance weighting |
| `STRATEGY_FILTER_ENABLED` | true | Enable blocking underperforming strategies |
| `STRATEGY_FILTER_REGIME_AWARE` | true | Track performance per regime |
| `STRATEGY_FILTER_WINDOW` | 200 | Rolling trade window per strategy |
| `STRATEGY_FILTER_MIN_TRADES` | 30 | Minimum trades before blocking |
| `STRATEGY_FILTER_MIN_WIN_RATE` | 0.45 | Minimum win rate threshold |
| `STRATEGY_FILTER_MIN_AVG_PNL` | 0.0 | Minimum avg pnl% threshold |
| `ATR_TP_SL_ENABLED` | true | Enable ATR-based TP/SL |
| `ATR_TP_MULTIPLIER_SCALP` | 1.2 | ATR TP multiplier (scalp) |
| `ATR_SL_MULTIPLIER_SCALP` | 0.8 | ATR SL multiplier (scalp) |
| `ATR_TP_MULTIPLIER_SWING` | 2.5 | ATR TP multiplier (swing) |
| `ATR_SL_MULTIPLIER_SWING` | 1.2 | ATR SL multiplier (swing) |
| `CANARY_MODE` | false | Enable canary mode and auto-halt |
| `CANARY_TRADE_LIMIT` | 20 | Trades required before canary checks |
| `CANARY_MIN_WIN_RATE` | 0.45 | Canary minimum win rate |
| `CANARY_MAX_DD_PCT` | 5.0 | Canary max drawdown |
| `DRIFT_WINDOW` | 200 | Feature drift window |
| `DRIFT_ALERT_Z` | 3.0 | Drift z-score threshold |

## 🚀 Running

```bash
# Paper trading (default)
python main.py

# With specific mode
python main.py --mode paper

# Replay historical data
python main.py --mode replay --csv data/btc_data.csv
```

## 🧪 Backtesting & Walk-Forward

```bash
# Backtest with execution realism hooks
python scripts/backtest.py --csv data/BTC_TINY.csv --symbol BTC/USDT --slippage-bps 5 --latency 1

# Walk-forward evaluation (purge/embargo)
python scripts/walk_forward.py --data data/ml_dataset.csv --train-window 30000 --test-window 5000
```

## 📁 Data Files (Not in Git)

| File | Purpose |
|------|---------|
| `.env` | API keys (create from .env.example) |
| `data/experience_log.jsonl` | Decision logs for training |
| `data/portfolio_state.json` | Current positions/balance |
| `models/*.pkl` | Trained model binaries |
| `models/feature_maps.json` | Session/symbol encodings used by training + inference |

## 🔄 Retraining Models

```bash
# Train main policy
python scripts/train_policy.py

# Train regime experts
python scripts/train_ensemble.py
```
