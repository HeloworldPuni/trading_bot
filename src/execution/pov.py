class POVOrder:
    def __init__(self, total_qty: float, participation_rate: float):
        self.total_qty = float(total_qty)
        self.participation_rate = float(participation_rate)
        self.market_volume = 0.0
        self.filled_qty = 0.0

    def update_market_volume(self, recent_market_volume: float) -> float:
        self.market_volume += max(0.0, float(recent_market_volume))
        target_cumulative = self.market_volume * self.participation_rate
        qty = target_cumulative - self.filled_qty
        qty = max(0.0, min(qty, self.total_qty - self.filled_qty))
        return float(qty)

    def fill(self, qty: float):
        self.filled_qty = min(self.total_qty, self.filled_qty + max(0.0, float(qty)))
