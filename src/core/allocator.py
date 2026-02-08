import math
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
