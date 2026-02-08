# 🧠 Model Architecture Documentation

This document explains the ML models used in the trading bot for another agent or developer to understand.

## Overview

The bot uses an **ensemble of ML models** to predict trade quality:

```
                    ┌─────────────────┐
                    │  Market State   │
                    │   (Features)    │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ Regime Detector │
                    │(BULL/BEAR/SIDE) │
                    └────────┬────────┘
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
    ┌──────▼──────┐   ┌──────▼──────┐   ┌──────▼──────┐
    │ Bull Expert │   │ Bear Expert │   │Side Expert  │
    │   Model     │   │   Model     │   │   Model     │
    └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
           │                 │                 │
           └─────────────────┼─────────────────┘
                             │
                    ┌────────▼────────┐
                    │   Confidence    │
                    │   (0.0 - 1.0)   │
                    └─────────────────┘
```

## Model Details

### 1. Main Policy Model (`policy_model_v1.pkl`)

| Property | Value |
|----------|-------|
| **Algorithm** | XGBoost / LightGBM Classifier |
| **Output** | Binary (Good Trade = 1, Bad Trade = 0) |
| **Training Data** | Historical trades with outcomes |
| **Usage** | Fallback when regime expert unavailable |

### 2. Regime Expert Models

Each expert is trained on trades from specific market conditions:

| Model | Regime | Training Filter |
|-------|--------|-----------------|
| `policy_bull.pkl` | Bull markets | `market_regime = BULL_TREND` |
| `policy_bear.pkl` | Bear markets | `market_regime = BEAR_TREND` |
| `policy_sideways.pkl` | Range-bound | `market_regime = SIDEWAYS_*` |

## Feature Engineering

### Input Features (20 total)

```python
# Market Context (3)
market_regime: int        # Encoded: BULL=0, BEAR=1, SIDEWAYS_LOW=2, SIDEWAYS_HIGH=3
volatility_level: int     # Encoded: LOW=0, MEDIUM=1, HIGH=2
trend_strength: int       # Encoded: WEAK=0, MODERATE=1, STRONG=2, VERY_STRONG=3

# Price Position (2)
dist_to_high: float       # (current - 14d_high) / 14d_high * 100
dist_to_low: float        # (current - 14d_low) / 14d_low * 100

# Technical Indicators (7)
macd: float               # MACD line value
macd_signal: float        # Signal line value
macd_hist: float          # MACD histogram
bb_upper: float           # Bollinger upper band
bb_lower: float           # Bollinger lower band
bb_mid: float             # Bollinger middle band (SMA20)
atr: float                # 14-period ATR

# Volume (1)
volume_delta: float       # (current_vol - avg_vol) / avg_vol * 100

# Context (4)
trading_session: int      # ASIA=0, LONDON=1, NY=2, OTHER=3, OVERLAP=4
symbol: int               # Encoded symbol index
repeats: int              # Consecutive same-action count
action_taken: int         # Proposed strategy type

# Regime Stability (3)
regime_confidence: float  # Confidence in regime classification
regime_stable: int        # 1 if regime stable over lookback
momentum_shift_score: float  # Detected momentum changes
```

### Label (Target)

```python
# Binary classification
label = 1 if trade_pnl > 0 else 0  # "Good" trade = profitable
```

## Training Pipeline

```python
# Location: scripts/train_policy.py

1. Load experience logs (data/experience_log.jsonl)
2. Filter to FINALIZED records (trades with outcomes)
3. Extract features using same encoding as inference
4. Split train/test (80/20)
5. Train XGBoost with hyperparameters:
   - max_depth: 5
   - learning_rate: 0.1
   - n_estimators: 100
   - scale_pos_weight: auto (handle imbalance)
6. Save model with metadata to models/
```

## Inference Flow

```python
# Location: src/ml/inference.py

class PolicyInference:
    def predict_confidence(state, action, repeats):
        # 1. Select model based on regime
        if state.regime == BULL:
            model = ensemble["bull"]
        elif state.regime == BEAR:
            model = ensemble["bear"]
        else:
            model = ensemble["sideways"]
        
        # 2. Encode features
        features = encode_state(state, action, repeats)
        
        # 3. Predict
        proba = model.predict_proba(features)[0]
        confidence = proba[1]  # P(Good Trade)
        
        return confidence  # 0.0 to 1.0
```

## Confidence Thresholds

| Confidence | Action |
|------------|--------|
| < 0.50 | **Block trade** (ML veto) |
| 0.50 - 0.60 | Execute with 50% size |
| 0.60 - 0.70 | Execute with 75% size |
| > 0.70 | Execute with full size |

## Model Registry

Models are versioned in `models/registry.json`:

```json
{
  "active_version": "v1_ensemble",
  "models": {
    "v1_ensemble": {
      "type": "ensemble",
      "created": "2026-02-01",
      "experts": {
        "bull": {"path": "models/policy_bull.pkl"},
        "bear": {"path": "models/policy_bear.pkl"},
        "sideways": {"path": "models/policy_sideways.pkl"}
      }
    }
  }
}
```

## Retraining Schedule

The bot accumulates experience in `data/experience_log.jsonl`.

**Recommended retraining:**

- After 50-100 new trades
- When win rate drops significantly
- After major market regime changes

**Retrain command:**

```bash
python scripts/train_ensemble.py
```

## Key Files

| File | Purpose |
|------|---------|
| `src/ml/inference.py` | Load models, make predictions |
| `src/ml/pipeline.py` | Training pipeline |
| `src/ml/trainer.py` | Model training logic |
| `src/ml/dataset_builder.py` | Feature extraction from logs |
| `src/ml/registry.py` | Model version management |
| `scripts/train_policy.py` | CLI for training main model |
| `scripts/train_ensemble.py` | CLI for training experts |
