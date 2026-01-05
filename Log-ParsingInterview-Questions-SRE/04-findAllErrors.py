"""
Q4. How would you parse a log file line by line in Python to find all error or warning messages?

Optimal Answer:
To avoid loading the whole file into memory, I would use a generator and process line by line.

"""
import re
class Solution:
    def parse_log(self, log_file):
        
        pattern = re.compile(r"(ERROR)")
        with open(log_file, "r") as file:
            for line in file:
                if pattern.search(line):
                    yield line.strip()
if __name__== "__main__":
    sol = Solution()
    for log in sol.parse_log("error-code.log"):
        print(log)