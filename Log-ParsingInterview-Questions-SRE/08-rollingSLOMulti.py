
"""
Log-Parsing Interview Question – SRE 08: Rolling SLO (Multi-Service)

Problem:
You receive a continuous stream of request latency events.
Each event contains:
- service_id
- timestamp
- latency (ms)

Requirements:
1. Compute a rolling 95th percentile latency SLO for EACH service
2. Use a sliding 1-hour time window
3. Support hundreds or thousands of services
4. Avoid recomputing percentiles from scratch for every request

High-Level Approach:
- Maintain a per-service sliding window using a deque
- Evict requests older than 1 hour on ingestion
- Compute percentile only from the active window
- Use a dictionary to isolate state per service

Scalability Notes (Interview Discussion):
- Per-service isolation prevents cross-service contention
- Deque enables O(1) insertions and evictions
- In real production systems, percentiles would be computed using
  histograms or streaming approximations (HDRHistogram / t-digest)
  instead of raw arrays

This solution demonstrates:
- Sliding window computation
- Per-service state management
- Trade-offs between simplicity and production scalability
"""
from collections import deque
from datetime import datetime, timedelta
import numpy as np


class RollingSLO:
    def __init__(self, window_minutes=60, percentile=95):
        if window_minutes <= 0:
            raise ValueError("window_minutes must be positive")
        if not 0 <= percentile <= 100:
            raise ValueError("percentile must be between 0 and 100")

        self.window = timedelta(minutes=window_minutes)
        self.percentile = percentile
        self.requests = deque()  # Use requests consistently

    def add_request(self, timestamp, latency):
        self.requests.append((timestamp, latency))

        # Remove old requests outside the window
        while self.requests and self.requests[0][0] < timestamp - self.window:
            self.requests.popleft()

    def calculate_slo(self):
        if not self.requests:
            return None
        latencies = [lat for _, lat in self.requests]
        return np.percentile(latencies, self.percentile)


class MultiServiceSLO:
    def __init__(self, window_minutes=60, percentile=95):
        self.services = {}
        self.window_minutes = window_minutes
        self.percentile = percentile

    def add_request(self, service_id, timestamp, value):
        if service_id not in self.services:
            self.services[service_id] = RollingSLO(
                window_minutes=self.window_minutes,
                percentile=self.percentile,
            )
        self.services[service_id].add_request(timestamp, value)

    def calculate_slo(self, service_id):
        if service_id in self.services:
            return self.services[service_id].calculate_slo()
        return None


# ---------- Example Usage ----------
if __name__ == "__main__":
    multi_slo = MultiServiceSLO(window_minutes=60, percentile=95)

    now = datetime.now()
    multi_slo.add_request("service-A", now, 200)
    multi_slo.add_request("service-A", now + timedelta(seconds=10), 180)
    multi_slo.add_request("service-B", now, 300)

    print("Service-A SLO:", multi_slo.calculate_slo("service-A"))
    print("Service-B SLO:", multi_slo.calculate_slo("service-B"))

# | Component       | Complexity                     |
# | --------------- | ------------------------------ |
# | Add request     | O(1)                           |
# | Evict old data  | O(1) amortized                 |
# | Percentile calc | O(n) per service               |
# | Memory          | O(active requests per service) |
