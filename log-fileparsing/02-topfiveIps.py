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

def top_5_ips(log_file):
    # Match any IPv4 address in the line (before :port if present)
    ip_pattern = re.compile(r'\b\d{1,3}(?:\.\d{1,3}){3}\b')
    counts = Counter()

    with open(log_file, 'r') as f:
        for line in f:
            match = ip_pattern.search(line)  # search anywhere in line
            if match:
                counts[match.group()] += 1

    return counts.most_common(5)

if __name__ == "__main__":
    log_path = "web-server.log"
    for ip, count in top_5_ips(log_path):
        print(f"{ip} → {count} requests")
