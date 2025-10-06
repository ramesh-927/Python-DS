"""
Write a Python script to Count the occurances of the Error in log file
"""
def count_keyword(log_file, keyword):
    keyword_lower = keyword.lower()
    count = 0
    try:
        with open(log_file, 'r') as f:
            for line_num, line in enumerate(f, 1):
                if keyword_lower in line.lower():
                    count += 1
        return count
    except FileNotFoundError:
        print(f"file '{log_file}' dosn't Exist!")
        return None
    
count = count_keyword("web-server.log", "INFO")
if count is not None:
    print(f"Occurrences of 'ERROR': {count}")