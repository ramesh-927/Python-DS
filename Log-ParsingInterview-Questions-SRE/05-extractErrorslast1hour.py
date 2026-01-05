"""
Q3. Suppose logs contain timestamps. How would you extract only the errors in the last 1 hour?

"""
import re
from datetime import datetime, timedelta
class Solution:
    def recent_errors(self, file_path):
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
if __name__== "__main__":
    sol = Solution()
    for error in sol.recent_errors("error-code.log"):
        print(error)

