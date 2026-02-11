
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

@dataclass
class RiskState:
    daily_pnl_pct: float = 0.0
    current_drawdown_pct: float = 0.0
    is_kill_switch_active: bool = False
    kill_reason: str = ""
    high_water_mark: float = 0.0

class RiskGuardian:
    """
    Phase 9: Institutional Risk Guardian.
    The "Hard Override" system that halts trading if global limits are breached.
    """
    def __init__(self, daily_stop_loss_pct: float = -0.03, max_drawdown_pct: float = -0.10):
        self.daily_stop_loss_pct = daily_stop_loss_pct
        self.max_drawdown_pct = max_drawdown_pct
        self.state = RiskState()
        self.starting_equity_day = 0.0
        
    def reset_daily(self, current_equity: float):
        self.starting_equity_day = current_equity
        self.state.daily_pnl_pct = 0.0
        if "Daily Stop" in self.state.kill_reason:
            logger.info("RiskGuardian: Resetting Daily Stop Kill Switch.")
            self.state.is_kill_switch_active = False
            self.state.kill_reason = ""
            
    def update_state(self, current_equity: float):
        if self.starting_equity_day == 0.0:
            self.starting_equity_day = current_equity
            self.state.high_water_mark = current_equity

        if current_equity > self.state.high_water_mark:
            self.state.high_water_mark = current_equity
            
        if self.state.high_water_mark > 0:
            dd = (current_equity - self.state.high_water_mark) / self.state.high_water_mark
            self.state.current_drawdown_pct = dd
        else:
            self.state.current_drawdown_pct = 0.0

        if self.starting_equity_day > 0:
            day_pnl = (current_equity - self.starting_equity_day) / self.starting_equity_day
            self.state.daily_pnl_pct = day_pnl
            
        self._check_triggers()

    def _check_triggers(self):
        if self.state.daily_pnl_pct <= self.daily_stop_loss_pct:
            if not self.state.is_kill_switch_active:
                logger.critical(f"RISK GUARDIAN: Daily Stop Hit! {self.state.daily_pnl_pct:.2%}")
                self.state.is_kill_switch_active = True
                self.state.kill_reason = f"Daily Stop Loss ({self.state.daily_pnl_pct:.2%})"

        if self.state.current_drawdown_pct <= self.max_drawdown_pct:
            if not self.state.is_kill_switch_active:
                logger.critical(f"RISK GUARDIAN: Max Drawdown Hit! {self.state.current_drawdown_pct:.2%}")
                self.state.is_kill_switch_active = True
                self.state.kill_reason = f"Max Drawdown ({self.state.current_drawdown_pct:.2%})"

    def check_system_health(self) -> bool:
        return not self.state.is_kill_switch_active
