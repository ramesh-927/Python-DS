"""
Write a Optimal python script to find the number of http response code along with timestamp 
and also provide number of hits for each response.
--
You are given a large HTTP access log where each entry contains a timestamp and an HTTP response status 
code.
Design and implement an optimal Python solution to:
Parse the log stream efficiently (assume it may not fit in memory).
Count the total number of occurrences of each HTTP response status code.
Track the number of hits per status code over time (using the timestamp).
Ensure the solution is performant and scalable for production-scale logs.
Follow-up discussion points:
How would your solution change if logs arrive as a real-time stream?
How would you aggregate counts per minute or per hour?
How would you optimize for very high cardinality timestamps?
"""
from collections import defaultdict
from datetime import datetime
import re

# Log timestamp example: [10/Oct/2025:13:55:36 +0000]
TIME_FORMAT = "%d/%b/%Y:%H:%M:%S %z"
pattern = re.compile(r"\[(.*?)\].*\"\s(\d{3})\s")

def parse_http_logs(log_file_path):
    """
    Parse HTTP logs efficiently:
    - Count total hits per status code
    - Aggregate hits per minute per status code
    """

    total_counts = defaultdict(int)
    per_minute_counts = defaultdict(lambda: defaultdict(int))

    with open(log_file_path, "r") as file:
        for line in file:
            match = pattern.search(line)
            if not match:
                continue

            raw_time, status = match.groups()
            ts = datetime.strptime(raw_time, TIME_FORMAT)
            minute_bucket = ts.strftime("%Y-%m-%d %H:%M")

            total_counts[status] += 1
            per_minute_counts[minute_bucket][status] += 1

    # Print total counts
    print("=== Total HTTP Status Counts ===")
    for status, count in sorted(total_counts.items()):
        print(f"HTTP {status} - Hits: {count}")

    print("\n=== Hits per Minute per Status ===")
    for minute, counts in sorted(per_minute_counts.items()):
        counts_str = ", ".join(f"{status}: {count}" for status, count in sorted(counts.items()))
        print(f"{minute} -> {counts_str}")


# Example usage
if __name__ == "__main__":
    log_file = "NGINX-10-06.log"  # replace with your log file path
    parse_http_logs(log_file)

