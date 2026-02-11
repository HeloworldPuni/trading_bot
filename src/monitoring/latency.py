
import time
import logging
from typing import List

logger = logging.getLogger(__name__)

class LatencyMonitor:
    """
    Phase 10 Retrofit: Latency Monitoring.
    Tracks tick-to-trade and API response times.
    """
    def __init__(self, window_size: int = 100):
        self.tick_timestamps = {}
        self.latencies: List[float] = []
        self.window_size = window_size

    def record_tick_arrival(self, symbol: str):
        self.tick_timestamps[symbol] = time.time()

    def record_execution_latency(self, symbol: str) -> float:
        """
        Call this immediately after Order Submit.
        Returns latency in milliseconds.
        """
        arrival = self.tick_timestamps.get(symbol)
        if not arrival:
            return 0.0
            
        now = time.time()
        latency_ms = (now - arrival) * 1000.0
        self.latencies.append(latency_ms)
        
        if len(self.latencies) > self.window_size:
            self.latencies.pop(0)
            
        return latency_ms

    def get_average_latency(self) -> float:
        if not self.latencies:
            return 0.0
        return sum(self.latencies) / len(self.latencies)
