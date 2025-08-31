"""
Q3. Suppose logs contain timestamps. How would you extract only the errors in the last 1 hour?

"""
import re
from datetime import datetime, timedelta

def recent_errors(file_path):
    time_pattern = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")  # e.g. 2025-08-30 10:15:32
    hour_ago = datetime.now() - timedelta(hours=1)

    with open(file_path, "r") as f:
        for line in f:
            match = time_pattern.search(line)
            if match and "ERROR" in line:
                timestamp = datetime.strptime(match.group(), "%Y-%m-%d %H:%M:%S")
                if timestamp >= hour_ago:
                    yield line.strip()

# Example
for error in recent_errors("/Users/rameshgolla/Python-DS/Python-DS/log-fileparsing/error-code.log"):
    print(error)

