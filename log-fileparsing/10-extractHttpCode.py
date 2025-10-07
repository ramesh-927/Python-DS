"""
Write a Optimal python script to find the number of http response code along with timestamp 
and also provide number of hits for each response.
"""
from collections import defaultdict
import re

def parseHttp_time_log(log_file_path):

    response_data = defaultdict(lambda: {"count":0, "timestamps": []})    # Dictionary to store counts and timestamps
    pattern = re.compile(r"\[(.*?)\].*\"\s(\d{3})\s")

    with open(log_file_path, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                timestamp, code = match.groups()
                response_data[code]["count"] += 1
                response_data[code]["timestamps"].append(timestamp)
    # Print the summary
    for code, data in sorted(response_data.items()):
        print(f"HTTP {code} - Hits: {data['count']}")
        print("Timestamps:", data['timestamps'])
        print()


# Example usage
if __name__ == "__main__":
    log_file = "/Users/rameshgolla/Python-DS/Python-DS/log-fileparsing/NGINX-10-06.log"
    parseHttp_time_log(log_file)