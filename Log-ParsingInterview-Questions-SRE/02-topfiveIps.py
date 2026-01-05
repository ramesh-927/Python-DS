# Interview question: Top IPs from a log file
"""
Write a Python script to extract all IP addresses from a log file.
Count the occurrences of each IP and print the top 5 most frequent.
Make sure it works efficiently for large files.
Regex-focused
Given a line from a log, write a regex to extract the IP address.
How would you modify it to ignore ports?
"""

import re
from collections import Counter
class Solution:
    def top_5_ips(self, log_file):
        # Regex to match IPv4 address (ignores ports like :8080)
        ip_regex = re.compile(r'\b\d{1,3}(?:\.\d{1,3}){3}\b')

        ip_count = Counter()

        # Read file line by line (memory-efficient for large files)
        with open(log_file, "r") as file:
            for line in file:
                ip = ip_regex.search(line)
                if ip:
                    ip_count[ip.group()] += 1

        return ip_count.most_common(5)


if __name__ == "__main__":
    log_file = "web-server.log"
    for ip, count in Solution().top_5_ips(log_file):
        print(f"{ip} → {count} requests")

# Regex explanation:
    # \b              → word boundary (ensures we don't match inside larger numbers)
    # (\d{1,3}\.){3}  → three groups of 1-3 digits followed by a dot
    # \d{1,3}         → final group of 1-3 digits
    # (?=:\d+$|$)     → positive lookahead: either followed by :port or end of line
    # This safely ignores ports like :8080 but still matches IPs without ports


# I used regex to extract IPv4 addresses and Counter to track occurrences.The solution is memory-efficient 
# because it processes the log file line by line.