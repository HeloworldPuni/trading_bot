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
    "volatility_level": int,   # LOW, MEDIUM, HIGH
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
    "trading_session": int,    # ASIA, LONDON, NY, OVERLAP
    "symbol": int,             # Encoded symbol
    "repeats": int,            # Consecutive same-action count
    "action_taken": int,       # Proposed strategy
    "regime_confidence": float,
    "regime_stable": int,
    "momentum_shift_score": float
}
```

### Output

- `predict_proba()` returns confidence [0.0 - 1.0]
- Confidence > 0.5 required to execute trade
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
| `BASE_LEVERAGE` | 10 | Default leverage |
| `MAX_POSITION_PCT` | 0.10 | 10% of balance per trade |
| `TOP_COINS_COUNT` | 15 | Number of coins to scan |
| `SCAN_TIMEFRAME` | "15m" | Candle timeframe |
| `SCALP_TP_PCT` | 1.5% | Scalp take profit |
| `SWING_TP_PCT` | 6.0% | Swing take profit |

## 🚀 Running

```bash
# Paper trading (default)
python main.py

# With specific mode
python main.py --mode paper

# Replay historical data
python main.py --mode replay --csv data/btc_data.csv
```

## 📁 Data Files (Not in Git)

| File | Purpose |
|------|---------|
| `.env` | API keys (create from .env.example) |
| `data/experience_log.jsonl` | Decision logs for training |
| `data/portfolio_state.json` | Current positions/balance |
| `models/*.pkl` | Trained model binaries |

## 🔄 Retraining Models

```bash
# Train main policy
python scripts/train_policy.py

# Train regime experts
python scripts/train_ensemble.py
```
