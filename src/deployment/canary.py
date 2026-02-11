
import logging
import time
from typing import Dict

logger = logging.getLogger(__name__)

class CanaryLauncher:
    """
    Phase 11 Retrofit: Automated Canary Deployment.
    Manages capital scaling from 1% -> 10% -> 100%.
    """
    STAGES = {
        0: {"name": "PROBE", "capital_pct": 0.01, "duration_h": 24, "min_sharpe": 0.5},
        1: {"name": "SCALE", "capital_pct": 0.10, "duration_h": 48, "min_sharpe": 1.0},
        2: {"name": "FULL", "capital_pct": 1.00, "duration_h": 0, "min_sharpe": 1.5}
    }

    def __init__(self):
        self.current_stage_idx = 0
        self.stage_start_time = time.time()
        self.is_halted = False
        logger.info("CanaryLauncher initialized at Stage 0 (PROBE)")

    def get_current_capital_allocation(self, total_equity: float) -> float:
        if self.is_halted:
            return 0.0
        
        stage = self.STAGES[self.current_stage_idx]
        return total_equity * stage['capital_pct']

    def evaluate_promotion(self, live_sharpe: float, current_drawdown: float) -> str:
        """
        Checks if we can promote to next stage.
        """
        if self.is_halted:
            return "HALTED"
            
        stage = self.STAGES[self.current_stage_idx]
        
        # 1. Check Safety
        if current_drawdown > 0.05: # > 5% drawdown during canary
            self._halt_deployment(f"Excessive Drawdown: {current_drawdown:.1%}")
            return "HALTED"

        # 2. Check Duration
        elapsed_hours = (time.time() - self.stage_start_time) / 3600
        if elapsed_hours < stage['duration_h'] and stage['duration_h'] > 0:
            return "WAITING_TIME"

        # 3. Check Performance
        if live_sharpe < stage['min_sharpe']:
            logger.warning(f"Sharpe {live_sharpe:.2f} below threshold {stage['min_sharpe']}")
            return "WAITING_PERFORMANCE"

        # Promote
        if self.current_stage_idx < 2:
            self.current_stage_idx += 1
            self.stage_start_time = time.time()
            new_stage = self.STAGES[self.current_stage_idx]
            logger.info(f"🚀 PROMOTED to Stage {self.current_stage_idx} ({new_stage['name']})")
            return "PROMOTED"
        
        return "MAX_STAGE"

    def _halt_deployment(self, reason: str):
        self.is_halted = True
        logger.critical(f"🛑 CANARY DEPLOYMENT HALTED: {reason}")
