
import json
import os
import uuid
import contextlib
import logging
import time
from datetime import datetime, UTC
from collections import deque
from typing import Dict, Any, List, Optional
from src.config import Config
from src.core.definitions import MarketState, Action

logger = logging.getLogger(__name__)


def get_resolution_log_path(base_log_path: str) -> str:
    """
    Sidecar log for append-only resolution updates.
    """
    return f"{base_log_path}.resolved.jsonl"


def load_resolution_updates(base_log_path: str) -> Dict[str, Dict[str, Any]]:
    """
    Load latest resolution update per decision id from sidecar.
    """
    sidecar = get_resolution_log_path(base_log_path)
    updates: Dict[str, Dict[str, Any]] = {}
    if not os.path.exists(sidecar):
        return updates

    try:
        with open(sidecar, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                decision_id = rec.get("id")
                if not decision_id:
                    continue
                updates[decision_id] = {
                    "resolved": True,
                    "reward": rec.get("reward"),
                    "outcome": rec.get("outcome"),
                    "resolution_time": rec.get("resolution_time"),
                }
    except Exception as e:
        logger.warning("Failed to load resolution sidecar %s: %s", sidecar, e)

    return updates

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
        default_filename = "experience_log.jsonl"
        configured_path = getattr(Config, "EXPERIENCE_LOG_FILE", "")
        base_filepath = configured_path if (filename == default_filename and configured_path) else filename

        if log_suffix:
            base_dir, base_name = os.path.split(base_filepath)
            name, ext = os.path.splitext(base_name)
            ext = ext or ".jsonl"
            base_name = f"{name}_{log_suffix}{ext}"
            base_filepath = os.path.join(base_dir, base_name) if base_dir else base_name

        if data_path:
            self.filepath = os.path.join(data_path, os.path.basename(base_filepath))
        else:
            # If caller passed a path with directories, honor it as-is.
            if os.path.isabs(base_filepath) or os.path.dirname(base_filepath):
                self.filepath = base_filepath
            else:
                self.filepath = os.path.join(Config.DATA_PATH, base_filepath)

        # Backward compatibility for historical default profile.
        legacy = os.path.join("data", default_filename)
        if (
            filename == default_filename
            and not log_suffix
            and not data_path
            and self.filepath != legacy
            and not os.path.exists(self.filepath)
            and Config.EXCHANGE_ID == "binance"
            and Config.QUOTE_CURRENCY == "USDT"
            and Config.TRADING_MODE == "paper"
            and os.path.exists(legacy)
        ):
            self.filepath = legacy

        self.lockpath = self.filepath + ".lock"
        self.resolution_path = get_resolution_log_path(self.filepath)
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
        directory = os.path.dirname(self.filepath)
        if directory:
            os.makedirs(directory, exist_ok=True)

    def _append_resolution_update(self, decision_id: str, outcome_data: Dict[str, Any], final_reward: float):
        update = {
            "id": decision_id,
            "resolved": True,
            "reward": final_reward,
            "outcome": outcome_data,
            "resolution_time": datetime.now(UTC).isoformat(),
            "record_type": "resolution_update",
        }
        with self._global_lock():
            with open(self.resolution_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(update) + "\n")

    @contextlib.contextmanager
    def _file_lock(self, filepath: str, mode: str = 'a'):
        """
        Cross-platform file locking context manager.
        Ensures safe writes even in multi-process scenarios.
        """
        lock_retries = 8
        backoff_sec = 0.08
        f = None
        acquired = False
        last_error = None
        for attempt in range(lock_retries):
            try:
                f = open(filepath, mode, encoding='utf-8')
                if WINDOWS:
                    # Use blocking lock on Windows to reduce transient PermissionError races.
                    msvcrt.locking(f.fileno(), msvcrt.LK_LOCK, 1)
                else:
                    # Unix: use flock
                    fcntl.flock(f.fileno(), fcntl.LOCK_EX)
                acquired = True
                break
            except (PermissionError, OSError) as exc:
                last_error = exc
                if f is not None:
                    try:
                        f.close()
                    except Exception:
                        pass
                    f = None
                if attempt >= lock_retries - 1:
                    break
                time.sleep(backoff_sec * (attempt + 1))
        if not acquired:
            raise last_error if last_error is not None else PermissionError(f"Unable to lock {filepath}")
        try:
            yield f
        finally:
            if WINDOWS:
                try:
                    msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
                except Exception:
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
        # Append-only resolution update (O(1)); avoids full-file rewrites on every close.
        self._append_resolution_update(decision_id, outcome_data, final_reward)

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
            if not self.pending_updates:
                return

            updates = list(self.pending_updates.items())
            with open(self.resolution_path, "a", encoding="utf-8") as f:
                for decision_id, update in updates:
                    payload = {
                        "id": decision_id,
                        "resolved": True,
                        "reward": update.get("reward"),
                        "outcome": update.get("outcome"),
                        "resolution_time": update.get("resolution_time"),
                        "record_type": "resolution_update",
                    }
                    f.write(json.dumps(payload) + "\n")
            logger.info(f"ExperienceDB: Flushed {len(updates)} updates to sidecar.")
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
                    # Stream tail into fixed-size deque to avoid loading whole file in memory.
                    lines = deque(f, maxlen=remaining)
                    disk_records = []
                    for line in lines:
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
