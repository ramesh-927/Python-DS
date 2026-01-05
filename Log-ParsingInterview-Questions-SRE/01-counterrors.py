"""
Write a Python function that takes a log file path and a keyword as input, counts the number of lines 
in the file that contain the keyword (case-insensitive), and handles the case where the file does not 
exist. Then, demonstrate how to call the function to count occurrences of the keyword "INFO" in a file 
named "web-server.log" and print the result, ensuring to handle any potential errors appropriately.
Write a Python script to Count the occurances of the Error in log file
"""
class Solution:
    def count_keyword_in_log(self, log_file, keyword):
        """
        Counts how many lines in a log file contain the given keyword (case-insensitive).
    
        Args:
            log_file (str): Path to the log file
            keyword (str): Keyword to search for
    
        Returns:
        int: Number of lines containing the keyword, or None if file not found
        """
        count = 0
        try:
            with open(log_file, 'r', encoding='utf-8') as file:
                for line in file:
                    if keyword.lower() in line.lower():
                        count += 1
            return count
    
        except FileNotFoundError:
            print(f"Error: File '{log_file}' does not exist!")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None


# --- Main part: Count occurrences of "ERROR" in the log file ---

sol = Solution()
log_file = "web-server.log"
keyword = "ERROR"
result = sol.count_keyword_in_log(log_file, keyword)
if result is not None:
    print(f"Occurrences of '{keyword}': {result}")
else:
    print("Counting failed due to file error.")