import math
from collections import deque
from typing import Dict, Deque, Tuple, List


class DriftMonitor:
    """
    Simple feature drift tracker using rolling z-scores.
    """
    def __init__(self, window: int = 200, alert_z: float = 3.0):
        self.window = window
        self.alert_z = alert_z
        self.values: Dict[str, Deque[float]] = {}

    def update(self, features: Dict[str, float]) -> List[str]:
        alerts: List[str] = []
        for k, v in features.items():
            if v is None or isinstance(v, bool):
                continue
            try:
                v = float(v)
            except (TypeError, ValueError):
                continue
            if k not in self.values:
                self.values[k] = deque(maxlen=self.window)
            q = self.values[k]
            q.append(v)
            if len(q) >= max(10, self.window // 2):
                mean = sum(q) / len(q)
                var = sum((x - mean) ** 2 for x in q) / len(q)
                std = math.sqrt(var) if var > 0 else 0.0
                if std > 0:
                    z = (v - mean) / std
                    if abs(z) >= self.alert_z:
                        alerts.append(f"{k}: z={z:.2f}")
        return alerts
