
import json
import os
import uuid
import contextlib
import logging
from datetime import datetime, UTC
from typing import Dict, Any, List, Optional
from src.config import Config
from src.core.definitions import MarketState, Action

logger = logging.getLogger(__name__)

# File locking - Windows vs Unix
try:
    import msvcrt  # Windows
    WINDOWS = True
except ImportError:
    import fcntl  # Unix
    WINDOWS = False

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
        self.lockpath = self.filepath + ".lock"
        self._ensure_dir()

        self.stats = {
            "total": 0,
            "strategies": {},
            "regimes": {},
            "actions": {}
        }
        self.buffer_mode = False
        self.pending_updates = {} # decision_id -> Dict
        self.log_buffer = []      # List of new records
        self._load_stats()

    def enable_buffer_mode(self):
        self.buffer_mode = True
        self.pending_updates = {}
        self.log_buffer = []
        logger.info("ExperienceDB: Buffer Mode Enabled (Replay Optimized).")

    def _ensure_dir(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
    
    @contextlib.contextmanager
    def _file_lock(self, filepath: str, mode: str = 'a'):
        """
        Cross-platform file locking context manager.
        Ensures safe writes even in multi-process scenarios.
        """
        f = open(filepath, mode, encoding='utf-8')
        try:
            if WINDOWS:
                # Windows: lock the file
                msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                # Unix: use flock
                fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            yield f
        finally:
            if WINDOWS:
                try:
                    msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
                except:
                    pass
            else:
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)
            f.close()

    @contextlib.contextmanager
    def _global_lock(self):
        """
        Serialize access to the experience log using a dedicated lock file.
        This prevents append/replace races between log_decision and finalize/flush.
        """
        with self._file_lock(self.lockpath, 'a'):
            yield


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
            logger.warning(f"Stats Load Error: {e}")

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
            "timestamp": datetime.now(UTC).isoformat(),
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
        
        if self.buffer_mode:
            self.log_buffer.append(record)
        else:
            # Serialize access to avoid races with finalize/flush
            with self._global_lock():
                with open(self.filepath, "a", encoding="utf-8") as f:
                    f.write(json.dumps(record) + "\n")
            
        # Update Stats (in-memory)
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
            # If it's in the log_buffer, update it there
            for rec in self.log_buffer:
                if rec["id"] == decision_id:
                    rec["resolved"] = True
                    rec["reward"] = final_reward
                    rec["outcome"] = outcome_data
                    rec["resolution_time"] = datetime.now(UTC).isoformat()
                    return
            
            # Otherwise, add to pending_updates for existing records on disk
            self.pending_updates[decision_id] = {
                "outcome": outcome_data,
                "reward": final_reward,
                "resolution_time": datetime.now(UTC).isoformat()
            }
            return

        if not os.path.exists(self.filepath):
            return

        with self._global_lock():
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
                            record["resolution_time"] = datetime.now(UTC).isoformat()
                            updated = True
                        
                        outfile.write(json.dumps(record) + "\n")
                    except json.JSONDecodeError:
                        continue
            
            if updated:
                os.replace(temp_path, self.filepath)
            else:
                if os.path.exists(temp_path):
                    os.remove(temp_path)

    def flush_records(self):
        """
        Applies all pending updates and appends new buffered records.
        """
        if not self.pending_updates and not self.log_buffer:
            return

        with self._global_lock():
            # 1. Append new records (efficient 'a' mode)
            if self.log_buffer:
                with open(self.filepath, "a", encoding="utf-8") as f:
                    for rec in self.log_buffer:
                        f.write(json.dumps(rec) + "\n")
                logger.info(f"ExperienceDB: Flushed {len(self.log_buffer)} new records to disk.")
                self.log_buffer = []

            # 2. Update existing records if needed
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
                        
                        outfile.write(json.dumps(record) + "\n")
                    except json.JSONDecodeError:
                        continue
            
            if updated_count > 0:
                os.replace(temp_path, self.filepath)
                logger.info(f"ExperienceDB: Flushed {updated_count} updates to disk.")
            else:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                    
            self.pending_updates = {}

    def get_recent_records(self, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Returns the last N records, checking memory buffer first then disk.
        """
        records = []
        
        # 1. Take from log_buffer (most recent)
        if hasattr(self, "log_buffer") and self.log_buffer:
            # log_buffer is appended as we go; most recent are at the end
            # We want them in chronological order for the calling logic to reverse them correctly if needed
            records.extend(self.log_buffer[-limit:])
        
        # 2. If we need more, check disk
        if len(records) < limit and os.path.exists(self.filepath):
            remaining = limit - len(records)
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    # For small limits, reading from end of full file read is okay for backtests
                    lines = f.readlines()
                    disk_records = []
                    for line in lines[-remaining:]:
                        try:
                            disk_records.append(json.loads(line))
                        except:
                            continue
                    # Append disk records (older) before buffer records (newer)
                    records = disk_records + records
            except Exception as e:
                logger.warning(f"Failed to read recent records from disk: {e}")
        
        return records[-limit:]

    def count_records(self) -> int:
        if not os.path.exists(self.filepath):
            return 0
        return self.stats["total"]
