
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
        # We define consistent mappings for categorical fields
        self.regime_map = {e.value: i for i, e in enumerate(MarketRegime)}
        self.vol_map = {e.value: i for i, e in enumerate(VolatilityLevel)}
        self.trend_map = {e.value: i for i, e in enumerate(TrendStrength)}
        self.strategy_map = {e.value: i for i, e in enumerate(StrategyType)}
        
        # Sessions and Symbols will be mapped dynamically on first pass to ensure all are caught
        self.session_map = {}
        self.symbol_map = {}

    def build_from_log(self, input_path: str, output_path: str):
        """
        Main entry point: Reads JSONL, transforms, and writes a SINGLE full CSV.
        """
        records = self._load_and_clean(input_path)
        if not records:
            return

        self._build_dynamic_maps(records)
        self._persist_feature_maps()

        transformed_rows = []
        for rec in records:
            row = self._transform_record(rec)
            if row:
                transformed_rows.append(row)

        self._write_csv(output_path, transformed_rows)
        logger.info(f"Full Dataset Built: {len(transformed_rows)} rows saved to {output_path}")
        return transformed_rows

    def build_splits(self, transformed_rows: List[List[Any]], data_dir: str):
        """
        Splits transformed rows into train/val/test based on time (70/15/15).
        """
        total = len(transformed_rows)
        if total < 10:
            logger.warning("Insufficient data for splitting.")
            return

        train_end = int(total * 0.70)
        val_end = train_end + int(total * 0.15)

        splits = {
            "train.csv": transformed_rows[:train_end],
            "validation.csv": transformed_rows[train_end:val_end],
            "test.csv": transformed_rows[val_end:]
        }

        for fname, rows in splits.items():
            fpath = os.path.join(data_dir, fname)
            self._write_csv(fpath, rows)
            logger.info(f"Split Created: {fname} with {len(rows)} rows.")

    def build_regime_splits(self, transformed_rows: List[List[Any]], data_dir: str):
        """
        Splits transformed rows by market regime into specialized datasets.
        """
        # Mapping back from regime index to filename suffix
        # regime_map = {e.value: i for i, e in enumerate(MarketRegime)}
        id_to_suffix = {
            self.regime_map.get(MarketRegime.BULL_TREND.value): "bull",
            self.regime_map.get(MarketRegime.BEAR_TREND.value): "bear",
            self.regime_map.get(MarketRegime.SIDEWAYS_LOW_VOL.value): "sideways"
        }

        regime_data = {suffix: [] for suffix in id_to_suffix.values()}

        for row in transformed_rows:
            regime_id = row[0] # regime is the first column
            suffix = id_to_suffix.get(regime_id)
            if suffix:
                regime_data[suffix].append(row)

        for suffix, rows in regime_data.items():
            if not rows:
                logger.warning(f"No data found for regime: {suffix}")
                continue

            # Further split each regime dataset into train/val
            total = len(rows)
            train_end = int(total * 0.80) # 80/20 split for specialized models

            train_path = os.path.join(data_dir, f"train_{suffix}.csv")
            val_path = os.path.join(data_dir, f"val_{suffix}.csv")

            self._write_csv(train_path, rows[:train_end])
            self._write_csv(val_path, rows[train_end:])
            logger.info(f"Regime Splits Created: {suffix} (Train: {train_end}, Val: {total-train_end})")

    def _write_csv(self, path: str, rows: List[List[Any]]):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            header = [
                "market_regime", "volatility_level", "trend_strength",
                "dist_to_high", "dist_to_low", "macd", "macd_signal", "macd_hist",
                "bb_upper", "bb_lower", "bb_mid", "atr", "volume_delta",
                "spread_pct", "body_pct", "gap_pct", "volume_zscore", "liquidity_proxy",
                "htf_trend_spread", "htf_rsi", "htf_atr",
                "trading_session", "symbol", "repeats", "current_open_positions",
                "action_taken", "regime_confidence", "regime_stable",
                "momentum_shift_score", "decision_quality"
            ]
            writer.writerow(header)
            writer.writerows(rows)

    def _load_and_clean(self, path: str) -> List[Dict[str, Any]]:
        """
        Only use resolved=True records, sorted chronologically.
        """
        valid_records = []
        if not os.path.exists(path):
            return []
            
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    rec = json.loads(line)
                    if rec.get("resolved") is True:
                        # Extract sortable key (raw_timestamp is ISO string from DataFeeder)
                        # Metadata timestamp is also ISO format.
                        sort_key = rec.get("market_state", {}).get("raw_timestamp") or rec.get("timestamp")
                        rec["_sort_key"] = sort_key
                        valid_records.append(rec)
                except:
                    continue
        
        # Sort by timestamp
        valid_records.sort(key=lambda x: x["_sort_key"])
        return valid_records

    def _build_dynamic_maps(self, records: List[Dict[str, Any]]):
        sessions = set()
        symbols = set()
        for rec in records:
            state = rec.get("market_state", {})
            sessions.add(state.get("trading_session", "OTHER"))
            symbols.add(state.get("symbol", "BTC/USDT"))
        
        self.session_map = {s: i for i, s in enumerate(sorted(list(sessions)))}
        self.symbol_map = {s: i for i, s in enumerate(sorted(list(symbols)))}
        logger.info(f"Encoded {len(self.session_map)} sessions and {len(self.symbol_map)} symbols.")

    def _persist_feature_maps(self):
        """Persist session/symbol mappings for inference consistency."""
        try:
            os.makedirs(os.path.dirname(self.FEATURE_MAPS_PATH), exist_ok=True)
            payload = {
                "version": "auto",
                "session_map": self.session_map,
                "symbol_map": self.symbol_map,
                "notes": "Auto-generated from training data to keep inference consistent."
            }
            with open(self.FEATURE_MAPS_PATH, "w", encoding="utf-8") as f:
                json.dump(payload, f, indent=4)
            logger.info(f"Feature maps saved to {self.FEATURE_MAPS_PATH}")
        except Exception as e:
            logger.warning(f"Failed to save feature maps: {e}")

    def _transform_record(self, rec: Dict[str, Any]) -> Optional[List[Any]]:
        """
        Flattens and encodes a single JSON record into a CSV row.
        """
        try:
            state = rec.get("market_state", {})
            action = rec.get("action_taken", {})
            
            # 1. Inputs (Encoded)
            regime = self.regime_map.get(state.get("market_regime"), -1)
            vol = self.vol_map.get(state.get("volatility_level"), -1)
            trend = self.trend_map.get(state.get("trend_strength"), -1)
            
            # Numerical
            dist_high = state.get("dist_to_high", state.get("distance_to_key_levels", 0.0))
            dist_low = state.get("dist_to_low", 0.0)
            
            # Phase 31 Indicators
            macd = state.get("macd", 0.0)
            macd_sig = state.get("macd_signal", 0.0)
            macd_hist = state.get("macd_hist", 0.0)
            bb_u = state.get("bb_upper", 0.0)
            bb_l = state.get("bb_lower", 0.0)
            bb_m = state.get("bb_mid", 0.0)
            atr = state.get("atr", 0.0)
            v_delta = state.get("volume_delta", 0.0)
            spread_pct = state.get("spread_pct", 0.0)
            body_pct = state.get("body_pct", 0.0)
            gap_pct = state.get("gap_pct", 0.0)
            volume_zscore = state.get("volume_zscore", 0.0)
            liquidity_proxy = state.get("liquidity_proxy", 0.0)
            htf_trend_spread = state.get("htf_trend_spread", 0.0)
            htf_rsi = state.get("htf_rsi", 50.0)
            htf_atr = state.get("htf_atr", 0.0)

            # Dynamic Encoded
            session = self.session_map.get(state.get("trading_session", "OTHER"), 0)
            symbol = self.symbol_map.get(state.get("symbol", "BTC/USDT"), 0)
            
            # Repeats (Retroactive calculation or direct extraction)
            repeats = rec.get("repetition_count", 0)
            # Note: For our recently generated data, repeats=0 is actually logged 
            # but we can trust the reward calculation already accounted for it.
            # In a real ML pipeline we might re-calc this from history, but here we extract.
            
            positions = state.get("current_open_positions", 0)
            
            # Action (Encoded Strategy)
            strat = self.strategy_map.get(action.get("strategy"), 0)

            # Phase C: Regime shift features
            regime_conf = state.get("regime_confidence", 0.0)
            regime_stable = 1 if state.get("regime_stable", False) else 0
            momentum_shift = state.get("momentum_shift_score", 0.0)
            
            # 2. Target Label (Y)
            # decision_quality = 1 if reward > 0 else 0
            reward = rec.get("reward", 0.0)
            quality = 1 if reward > 0 else 0
            
            return [
                regime, vol, trend,
                dist_high, dist_low, 
                macd, macd_sig, macd_hist,
                bb_u, bb_l, bb_m, atr, v_delta,
                spread_pct, body_pct, gap_pct, volume_zscore, liquidity_proxy,
                htf_trend_spread, htf_rsi, htf_atr,
                session, symbol, repeats, positions,
                strat, regime_conf, regime_stable, momentum_shift, quality
            ]
        except Exception as e:
            logger.warning(f"Transformation failed for record: {e}")
            return None
