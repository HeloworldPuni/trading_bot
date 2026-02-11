
import json
import csv
import os
import logging
from typing import List, Dict, Any, Optional
from src.core.definitions import MarketRegime, VolatilityLevel, TrendStrength, StrategyType

logger = logging.getLogger(__name__)

class DatasetBuilder:
    FEATURE_MAPS_PATH = os.path.join("models", "feature_maps.json")

    def __init__(self):
        self.regime_map = {e.value: i for i, e in enumerate(MarketRegime)}
        self.vol_map = {e.value: i for i, e in enumerate(VolatilityLevel)}
        self.trend_map = {e.value: i for i, e in enumerate(TrendStrength)}
        self.strategy_map = {e.value: i for i, e in enumerate(StrategyType)}
        self.session_map = {}
        self.symbol_map = {}

    def build_from_log(self, input_path: str, output_path: str):
        """Streaming Pass 1 & 2: Build full CSV without loading log into memory."""
        logger.info("Scanning log for metadata...")
        self._scan_for_metadata(input_path)
        self._persist_feature_maps()

        logger.info("Transforming records to CSV...")
        count = 0
        with open(input_path, "r", encoding="utf-8") as f_in, \
             open(output_path, "w", newline="", encoding="utf-8") as f_out:
            
            writer = csv.writer(f_out)
            writer.writerow(self._get_header())
            
            for line in f_in:
                try:
                    rec = json.loads(line)
                    if rec.get("resolved") is True:
                        row = self._transform_record(rec)
                        if row:
                            writer.writerow(row)
                            count += 1
                except:
                    continue
                    
        logger.info(f"Full Dataset Built: {count} rows saved to {output_path}")
        return count

    def build_splits(self, total_count: int, master_csv: str, data_dir: str):
        """Streaming Pass 3: Split the master CSV into train/val/test."""
        train_end = int(total_count * 0.70)
        val_end = train_end + int(total_count * 0.15)

        logger.info(f"Splitting {total_count} rows (70/15/15)...")
        
        with open(master_csv, "r", encoding="utf-8") as f_in, \
             open(os.path.join(data_dir, "train.csv"), "w", newline="", encoding="utf-8") as f_train, \
             open(os.path.join(data_dir, "validation.csv"), "w", newline="", encoding="utf-8") as f_val, \
             open(os.path.join(data_dir, "test.csv"), "w", newline="", encoding="utf-8") as f_test:
            
            header = f_in.readline()
            f_train.write(header)
            f_val.write(header)
            f_test.write(header)
            
            for i, line in enumerate(f_in):
                if i < train_end:
                    f_train.write(line)
                elif i < val_end:
                    f_val.write(line)
                else:
                    f_test.write(line)
        logger.info("Time-based splits created.")

    def build_regime_splits(self, master_csv: str, data_dir: str):
        """Streaming Pass 4: Split by market regime."""
        id_to_suffix = {
            self.regime_map.get(MarketRegime.BULL_TREND.value): "bull",
            self.regime_map.get(MarketRegime.BEAR_TREND.value): "bear",
            self.regime_map.get(MarketRegime.SIDEWAYS_LOW_VOL.value): "sideways"
        }
        
        handles = {}
        header = ""
        
        logger.info("Building regime-specific splits (streaming)...")
        
        with open(master_csv, "r", encoding="utf-8") as f_in:
            header = f_in.readline()
            
            # Create files on demand to save descriptors
            for line in f_in:
                parts = line.split(",")
                if not parts: continue
                regime_id = int(parts[0])
                suffix = id_to_suffix.get(regime_id)
                if suffix:
                    if suffix not in handles:
                        path = os.path.join(data_dir, f"ml_ready_{suffix}.csv")
                        h = open(path, "w", newline="", encoding="utf-8")
                        h.write(header)
                        handles[suffix] = h
                    handles[suffix].write(line)
        
        for h in handles.values():
            h.close()
            
        # Optional: Secondary split each regime file into train/val (not strictly needed if main splits exist, but ensemble scripts use them)
        for suffix in handles.keys():
            self._split_regime_file(os.path.join(data_dir, f"ml_ready_{suffix}.csv"), data_dir, suffix)

    def _split_regime_file(self, path: str, data_dir: str, suffix: str):
        """Sub-split a regime file into 80/20 train/val."""
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines() # Regime files are small enough (<20% of total)
        
        if len(lines) < 10: return
        
        header = lines[0]
        data = lines[1:]
        split_idx = int(len(data) * 0.8)
        
        with open(os.path.join(data_dir, f"train_{suffix}.csv"), "w", encoding="utf-8") as f1:
            f1.write(header)
            f1.writelines(data[:split_idx])
            
        with open(os.path.join(data_dir, f"val_{suffix}.csv"), "w", encoding="utf-8") as f2:
            f2.write(header)
            f2.writelines(data[split_idx:])

    def _get_header(self):
        return [
            "market_regime", "volatility_level", "trend_strength",
            "dist_to_high", "dist_to_low", "macd", "macd_signal", "macd_hist",
            "bb_upper", "bb_lower", "bb_mid", "atr", "volume_delta",
            "spread_pct", "body_pct", "gap_pct", "volume_zscore", "liquidity_proxy",
            "htf_trend_spread", "htf_rsi", "htf_atr",
            "trading_session", "symbol", "repeats", "current_open_positions",
            "action_taken", "regime_confidence", "regime_stable",
            "momentum_shift_score", "decision_quality"
        ]

    def _scan_for_metadata(self, path: str):
        sessions = set()
        symbols = set()
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    rec = json.loads(line)
                    state = rec.get("market_state", {})
                    s = state.get("trading_session")
                    if s: sessions.add(s)
                    sy = state.get("symbol")
                    if sy: symbols.add(sy)
                except: continue
        self.session_map = {s: i for i, s in enumerate(sorted(list(sessions)))}
        self.symbol_map = {s: i for i, s in enumerate(sorted(list(symbols)))}

    def _persist_feature_maps(self):
        os.makedirs(os.path.dirname(self.FEATURE_MAPS_PATH), exist_ok=True)
        payload = {
            "version": "v4",
            "session_map": self.session_map,
            "symbol_map": self.symbol_map,
            "notes": "v4 brain: Stricter fee-aware labeling + Streaming I/O."
        }
        with open(self.FEATURE_MAPS_PATH, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=4)

    def _transform_record(self, rec: Dict[str, Any]) -> Optional[List[Any]]:
        try:
            state = rec.get("market_state", {})
            action = rec.get("action_taken", {})
            
            # Phase 35: EXCLUDE WAIT ACTIONS FROM TRAINING DATA
            # The ML model is a gater for TRADES, not a whole-policy model.
            # Training on WAIT actions (which are 90% of data) creates massive 0.99 bias.
            strat_name = action.get("strategy")
            if strat_name == "WAIT":
                return None
            
            # Inputs
            regime = self.regime_map.get(state.get("market_regime"), -1)
            vol = self.vol_map.get(state.get("volatility_level"), -1)
            trend = self.trend_map.get(state.get("trend_strength"), -1)
            dist_high = state.get("dist_to_high", state.get("distance_to_key_levels", 0.0))
            dist_low = state.get("dist_to_low", 0.0)
            
            # Target Label (v4: Net Profit > 0.2% only)
            reward = rec.get("reward", 0.0)
            outcome = rec.get("outcome") or {}
            exit_reason = outcome.get("reason", "UNKNOWN")
            is_tp = exit_reason == "TP"
            
            # Remove the +0.5 bonus to find true profit
            # Stricter 0.2% threshold to ensure we cover fees and noise
            net_pnl = (reward - 0.5) if is_tp else reward
            quality = 1 if net_pnl > 0.002 else 0
            
            return [
                regime, vol, trend, dist_high, dist_low,
                state.get("macd", 0.0), state.get("macd_signal", 0.0), state.get("macd_hist", 0.0),
                state.get("bb_upper", 0.0), state.get("bb_lower", 0.0), state.get("bb_mid", 0.0),
                state.get("atr", 0.0), state.get("volume_delta", 0.0),
                state.get("spread_pct", 0.0), state.get("body_pct", 0.0), state.get("gap_pct", 0.0),
                state.get("volume_zscore", 0.0), state.get("liquidity_proxy", 0.0),
                state.get("htf_trend_spread", 0.0), state.get("htf_rsi", 50.0), state.get("htf_atr", 0.0),
                self.session_map.get(state.get("trading_session", "OTHER"), 0),
                self.symbol_map.get(state.get("symbol", "BTC/USDT"), 0),
                rec.get("repetition_count", 0),
                state.get("current_open_positions", 0),
                self.strategy_map.get(action.get("strategy"), 0),
                state.get("regime_confidence", 0.0),
                1 if state.get("regime_stable", False) else 0,
                state.get("momentum_shift_score", 0.0),
                quality
            ]
        except: return None
