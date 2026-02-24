import math
import json
import os
from collections import defaultdict, deque
from typing import Dict, List, Tuple


class StrategyPerformanceTracker:
    def __init__(self, window: int = 200):
        self.window = window
        self.history = defaultdict(lambda: deque(maxlen=window))

    def record(self, key: str, pnl_pct: float):
        self.history[key].append(float(pnl_pct))

    def _stats(self, key: str) -> Tuple[int, float, float]:
        trades = list(self.history.get(key, []))
        total = len(trades)
        if total == 0:
            return 0, 0.0, 0.0
        wins = sum(1 for p in trades if p > 0)
        win_rate = wins / total
        avg_pnl = sum(trades) / total
        return total, win_rate, avg_pnl

    def stats(self, key: str) -> Tuple[int, float, float]:
        """Public stats accessor used by strategy admission gates."""
        return self._stats(key)

    def get_weight(self, key: str, min_samples: int = 20) -> float:
        total, win_rate, avg_pnl = self._stats(key)
        if total < min_samples:
            return 1.0
        weight = max(0.5, min(1.5, win_rate / 0.5))
        if avg_pnl < 0:
            weight *= 0.8
        return max(0.25, min(1.75, weight))

    def is_blocked(self, key: str, min_samples: int, min_win_rate: float, min_avg_pnl: float) -> bool:
        total, win_rate, avg_pnl = self._stats(key)
        if total < min_samples:
            return False
        return win_rate < min_win_rate or avg_pnl < min_avg_pnl

    def get_weights(self, min_samples: int = 20) -> Dict[str, float]:
        return {k: self.get_weight(k, min_samples=min_samples) for k in self.history.keys()}

    def to_dict(self) -> Dict[str, object]:
        return {
            "window": int(self.window),
            "history": {k: list(v) for k, v in self.history.items()},
        }

    def load_dict(self, data: Dict[str, object]) -> None:
        if not isinstance(data, dict):
            return
        self.window = int(data.get("window", self.window))
        self.history = defaultdict(lambda: deque(maxlen=self.window))
        raw_history = data.get("history", {})
        if isinstance(raw_history, dict):
            for key, values in raw_history.items():
                dq = deque(maxlen=self.window)
                if isinstance(values, list):
                    for val in values:
                        try:
                            dq.append(float(val))
                        except Exception:
                            continue
                self.history[str(key)] = dq

    def save(self, path: str) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)

    def load(self, path: str) -> bool:
        if not os.path.exists(path):
            return False
        with open(path, "r", encoding="utf-8") as f:
            self.load_dict(json.load(f))
        return True


class BanditAllocator:
    """
    Simple UCB1 allocator to weight strategies/regimes by performance.
    """
    def __init__(self):
        self.counts = defaultdict(int)
        self.values = defaultdict(float)
        self.total = 0

    def record(self, key: str, reward: float):
        self.total += 1
        self.counts[key] += 1
        n = self.counts[key]
        self.values[key] += (reward - self.values[key]) / n

    def weight(self, key: str) -> float:
        if self.counts[key] == 0:
            return 1.5
        exploration = math.sqrt(2 * math.log(max(1, self.total)) / self.counts[key])
        return max(0.5, min(1.5, self.values[key] + exploration))

    def get_weights(self, keys: List[str]) -> Dict[str, float]:
        return {k: self.weight(k) for k in keys}

    def to_dict(self) -> Dict[str, object]:
        return {
            "counts": dict(self.counts),
            "values": dict(self.values),
            "total": int(self.total),
        }

    def load_dict(self, data: Dict[str, object]) -> None:
        if not isinstance(data, dict):
            return
        raw_counts = data.get("counts", {})
        raw_values = data.get("values", {})
        self.counts = defaultdict(int)
        self.values = defaultdict(float)
        if isinstance(raw_counts, dict):
            for key, value in raw_counts.items():
                try:
                    self.counts[str(key)] = int(value)
                except Exception:
                    continue
        if isinstance(raw_values, dict):
            for key, value in raw_values.items():
                try:
                    self.values[str(key)] = float(value)
                except Exception:
                    continue
        self.total = int(data.get("total", sum(self.counts.values())))

    def save(self, path: str) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)

    def load(self, path: str) -> bool:
        if not os.path.exists(path):
            return False
        with open(path, "r", encoding="utf-8") as f:
            self.load_dict(json.load(f))
        return True
