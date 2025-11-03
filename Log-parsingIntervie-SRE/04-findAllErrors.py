"""
Q4. How would you parse a log file line by line in Python to find all error or warning messages?

Optimal Answer:
To avoid loading the whole file into memory, I would use a generator and process line by line.

"""
import re

def parse_log(log_file):

    pattern = re.compile(r"(ERROR)")

    with open(log_file, "r") as file:
        for line in file:
            if pattern.search(line):
                yield line.strip()

for log in parse_log("/Users/rameshgolla/Python-DS/Python-DS/log-fileparsing/error-code.log"):
    print(log)