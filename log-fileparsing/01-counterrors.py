def count_keyword(log_file, keyword):

    keyword_lower = keyword.lower()
    count = 0
    try:
        with open(log_file, 'r') as file:
            for line_num, line in enumerate(file, 1):
                if keyword_lower in line.lower():
                    count += 1
        return count
    except FileNotFoundError:
        print(f"File '{log_file}' not Found!")
        return None


# Run for your local log file
count = count_keyword("web-server.log", "ERROR")
if count is not None:
    print(f"Occurrences of 'ERROR': {count}")
  

count1 = count_keyword("web-server.log", "WARNING")
if count1 is not None:
    print(f"Occurrences of 'WARNING': {count1}")
  