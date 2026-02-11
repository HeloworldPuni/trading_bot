import numpy as np
import pandas as pd


class RiskManager:
    def cap_positions(self, weights: dict[str, float]) -> dict[str, float]:
        if self.kill_switch_active:
            return {k: 0.0 for k in weights}
        
        capped = {k: float(np.clip(v, -self.max_position_size, self.max_position_size)) for k, v in weights.items()}
        total_lev = sum(abs(v) for v in capped.values())
        if total_lev <= self.max_leverage or total_lev == 0:
            return capped
        scale = self.max_leverage / total_lev
        return {k: v * scale for k, v in capped.items()}

    # --- Persistence & Kill Switch ---
    def __init__(self, max_leverage: float = 2.0, max_position_size: float = 0.5, target_volatility: float = 0.4, state_file: str = "data/risk_state.json"):
        self.max_leverage = float(max_leverage)
        self.max_position_size = float(max_position_size)
        self.target_volatility = float(target_volatility)
        self.state_file = state_file
        self.kill_switch_active = False
        self._load_state()

    def trip_kill_switch(self, reason: str):
        self.kill_switch_active = True
        self._save_state({"kill_switch": True, "reason": reason})

    def reset_kill_switch(self):
        self.kill_switch_active = False
        self._save_state({"kill_switch": False, "reason": "manual_reset"})

    def _save_state(self, data: dict):
        import json
        try:
            with open(self.state_file, "w") as f:
                json.dump(data, f)
        except Exception:
            pass

    def _load_state(self):
        import json
        import os
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r") as f:
                    data = json.load(f)
                    self.kill_switch_active = data.get("kill_switch", False)
            except Exception:
                pass
