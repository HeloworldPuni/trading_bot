class ExecutionAlgo:
    @staticmethod
    def generate_twap_schedule(total_qty: float, duration_minutes: int):
        duration = max(1, int(duration_minutes))
        slice_qty = float(total_qty) / duration
        return [slice_qty] * duration
