
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

class WhaleIngestor:
    """
    Phase 1 Retrofit: On-Chain Whale Alerting (Mock).
    """
    def fetch_large_transactions(self, threshold_usd: float = 1000000) -> List[Dict]:
        # Placeholder for real API (e.g., Whale Alert)
        return []
