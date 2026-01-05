"""
Q1: 
How you would count ERROR vs WARNING entries in a large production log file. Please explain your 
approach and show how you would implement it.
Answer: Optimal Answer:
To avoid loading the whole file into memory, I would use a generator and process line by line.
Efficient: Doesnot load entire file
Scalable: Works for GB-sized logs

"""
from collections import Counter

def count_log_levels(log_file):
    count = Counter()
    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                count["ERROR"] += 1
            elif "WARNING" in line:
                count["WARNING"] += 1
            elif "DEBUG" in line:
                count["DEBUG"] += 1
    return count

result = count_log_levels("error-code.log")
print(result)