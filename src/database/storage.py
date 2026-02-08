
import json
import os
import uuid
from datetime import datetime
from typing import Dict, Any, List, Optional
from src.config import Config
from src.core.definitions import MarketState, Action

class ExperienceDB:
    def __init__(self, filename: str = "experience_log.jsonl", log_suffix: Optional[str] = None, data_path: Optional[str] = None):
        """
        Initialize experience database.
        
        Args:
            filename: Name of the log file
            log_suffix: Optional suffix to append to filename
            data_path: Override for Config.DATA_PATH (useful for tests)
        """
        if log_suffix:
            name, ext = os.path.splitext(filename)
            filename = f"{name}_{log_suffix}{ext}"
        
        # Allow data_path override for test isolation
        base_path = data_path if data_path else Config.DATA_PATH
        self.filepath = os.path.join(base_path, filename)
        self._ensure_dir()
        self.stats = {
            "total": 0,
            "strategies": {},
            "regimes": {},
            "actions": {}
        }
        self.buffer_mode = False
        self.pending_updates = {} # decision_id -> Dict
        self._load_stats()

    def enable_buffer_mode(self):
        self.buffer_mode = True
        self.pending_updates = {}
        print("ExperienceDB: Buffer Mode Enabled (Replay Optimized).")

    def _ensure_dir(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

    def _load_stats(self):
        if not os.path.exists(self.filepath):
            return
            
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        record = json.loads(line)
                        self.stats["total"] += 1
                        
                        strat = record.get("action_taken", {}).get("strategy", "UNKNOWN")
                        self.stats["strategies"][strat] = self.stats["strategies"].get(strat, 0) + 1
                        
                        regime = record.get("market_state", {}).get("market_regime", "UNKNOWN")
                        self.stats["regimes"][regime] = self.stats["regimes"].get(regime, 0) + 1
                        
                        action = record.get("action_taken", {}).get("direction", "UNKNOWN")
                        self.stats["actions"][action] = self.stats["actions"].get(action, 0) + 1
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            print(f"Stats Load Error: {e}")

    def get_stats(self) -> Dict[str, Any]:
        return self.stats

    def log_decision(self, state: MarketState, action: Action, reward: float = 0.0, data_source: str = "live", market_period_id: str = None, repetition_count: int = 0, ml_confidence: Optional[float] = None, original_action: Optional[Dict] = None) -> str:
        """
        Appends a single decision record.
        Returns: decision_id (UUID)
        """
        decision_id = str(uuid.uuid4())
        record = {
            "id": decision_id,
            "timestamp": datetime.utcnow().isoformat(),
            "market_state": state.to_dict(),
            "action_taken": action.to_dict(),
            "reward": reward,
            "resolved": False,  # Pending outcome
            "outcome": None,
            "repetition_count": repetition_count,
            "metadata": {
                "version": "1.0",
                "mode": Config.TRADING_MODE,
                "data_source": data_source,
                "market_period_id": market_period_id,
                "ml_confidence": ml_confidence,
                "original_action": original_action
            }
        }
        
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")
            
        # Update Stats
        self.stats["total"] += 1
        
        s_name = action.strategy.value
        self.stats["strategies"][s_name] = self.stats["strategies"].get(s_name, 0) + 1
        
        r_name = state.market_regime.value
        self.stats["regimes"][r_name] = self.stats["regimes"].get(r_name, 0) + 1
        
        a_name = action.direction.value
        self.stats["actions"][a_name] = self.stats["actions"].get(a_name, 0) + 1
            
        return decision_id

    def finalize_record(self, decision_id: str, outcome_data: Dict[str, Any], final_reward: float):
        """
        Updates a specific record with outcome and final reward.
        """
        if self.buffer_mode:
            self.pending_updates[decision_id] = {
                "outcome": outcome_data,
                "reward": final_reward,
                "resolution_time": datetime.utcnow().isoformat()
            }
            return

        if not os.path.exists(self.filepath):
            return

        temp_path = self.filepath + ".tmp"
        updated = False
        
        with open(self.filepath, "r", encoding="utf-8") as infile, \
             open(temp_path, "w", encoding="utf-8") as outfile:
            
            for line in infile:
                try:
                    record = json.loads(line)
                    if record.get("id") == decision_id:
                        record["resolved"] = True
                        record["reward"] = final_reward
                        record["outcome"] = outcome_data
                        record["resolution_time"] = datetime.utcnow().isoformat()
                        updated = True
                    
                    outfile.write(json.dumps(record) + "\n")
                except json.JSONDecodeError:
                    continue # Skip corrupt lines
        
        # Atomic replace
        if updated:
            os.replace(temp_path, self.filepath)
        else:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def flush_records(self):
        """
        Applies all pending updates in a single file pass.
        """
        if not self.pending_updates or not os.path.exists(self.filepath):
            return

        temp_path = self.filepath + ".tmp"
        updated_count = 0
        
        with open(self.filepath, "r", encoding="utf-8") as infile, \
             open(temp_path, "w", encoding="utf-8") as outfile:
            
            for line in infile:
                try:
                    record = json.loads(line)
                    rec_id = record.get("id")
                    
                    if rec_id in self.pending_updates:
                        update = self.pending_updates[rec_id]
                        record["resolved"] = True
                        record["reward"] = update["reward"]
                        record["outcome"] = update["outcome"]
                        record["resolution_time"] = update["resolution_time"]
                        updated_count += 1
                        # Remove from pending to avoid double-processing (though unlikely with unique IDs)
                        # Actually better to keep for the loop and clear at end
                    
                    outfile.write(json.dumps(record) + "\n")
                except json.JSONDecodeError:
                    continue
        
        if updated_count > 0:
            os.replace(temp_path, self.filepath)
            print(f"ExperienceDB: Flushed {updated_count} updates to disk.")
        else:
            if os.path.exists(temp_path):
                os.remove(temp_path)
                
        self.pending_updates = {}

    def count_records(self) -> int:
        if not os.path.exists(self.filepath):
            return 0
        with open(self.filepath, "r", encoding="utf-8") as f:
            return sum(1 for _ in f)

    def get_recent_records(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get recent records efficiently without loading entire file.
        Uses reverse file reading to only process needed lines.
        """
        if not os.path.exists(self.filepath):
            return []
        
        records = []
        chunk_size = 8192  # Read 8KB chunks from end
        
        with open(self.filepath, "rb") as f:
            # Go to end
            f.seek(0, 2)
            file_size = f.tell()
            
            if file_size == 0:
                return []
            
            # Read backwards to find enough lines
            lines = []
            remaining = file_size
            leftover = b""
            
            while remaining > 0 and len(lines) <= limit:
                read_size = min(chunk_size, remaining)
                remaining -= read_size
                f.seek(remaining)
                chunk = f.read(read_size) + leftover
                
                # Split into lines
                chunk_lines = chunk.split(b"\n")
                
                # First part may be partial (save for next iteration)
                leftover = chunk_lines[0]
                
                # Add complete lines (reversed order)
                lines = chunk_lines[1:] + lines
            
            # Handle final leftover
            if leftover:
                lines = [leftover] + lines
            
            # Take last N non-empty lines
            recent_lines = [l for l in lines if l.strip()][-limit:]
            
            for line in recent_lines:
                try:
                    records.append(json.loads(line.decode("utf-8")))
                except (json.JSONDecodeError, UnicodeDecodeError):
                    continue
        
        return records
