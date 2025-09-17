"""
Given a list of request latencies and timestamps, calculate the rolling SLO (e.g., 95th percentile latency) over a sliding 1-hour window. 
(initial question can be for single service and follow up can be for multiple services)
"""
from collections import deque
from datetime import datetime, timedelta
import numpy as np

class RollingSLO:
    def __init__(self, window_minutes=60, percentile=95):
        self.window = timedelta(minutes=window_minutes)
        self.percentile = percentile
        self.data = deque()  # stores (timestamp, latency)

    def add_request(self, timestamp, latency):
        """Add a new request record and evict old ones."""
        self.data.append((timestamp, latency))

        # Remove data older than window
        while self.data and self.data[0][0] < timestamp - self.window:
            self.data.popleft()

    def get_slo(self):
        """Return rolling percentile latency (e.g., 95th)."""
        if not self.data:
            return None
        latencies = [lat for _, lat in self.data]
        return np.percentile(latencies, self.percentile)


# --- Example Usage ---
rolling_slo = RollingSLO(window_minutes=60, percentile=95)

now = datetime.now()
latencies = [100, 120, 200, 250, 300, 400, 500]
for i, latency in enumerate(latencies):
    rolling_slo.add_request(now + timedelta(minutes=i*10), latency)
    print(f"At t+{i*10}min: 95th percentile = {rolling_slo.get_slo():.2f} ms")

    


