"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:
1. Whitespace: Ignore any leading whitespace (" ").
2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered 
or the end of the string is reached. If no digits were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the 
integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and 
integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
Example 1:
Input: s = "42"
Output: 42
Explanation:
The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:
Input: s = " -042"
Output: -42
Explanation:
Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:
Input: s = "1337c0d3"
Output: 1337
Explanation:
Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:
Input: s = "0-1"
Output: 0
Explanation:
Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
Example 5:
Input: s = "words and 987"
Output: 0
Explanation:
Reading stops at the first non-digit character 'w'.
Constraints:
0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()          # Remove leading/trailing whitespace
        if not s:
            return 0
        
        sign = 1
        i = 0
        # Determine sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1    
        num = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])                      # Fixed: int(s[i]), not int([s[i]])
            
            # Check for overflow BEFORE updating num
            if num > (2147483647 - digit) // 10:
                return 2147483647 if sign == 1 else -2147483648
            
            num = num * 10 + digit
            i += 1
            
        return sign * num


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("42"))          # 42
    print(sol.myAtoi("   -042"))     # -42
    print(sol.myAtoi("1337c0d3"))    # 1337
    print(sol.myAtoi("0-1"))         # 0
    print(sol.myAtoi("words and 987"))  # 0
    print(sol.myAtoi("4193 with words"))   # 4193
    print(sol.myAtoi("+42"))         # 42
    print(sol.myAtoi("   +0"))       # 0

# If I multiply my current number by 10 and add this new digit, will it become too big?"
# The biggest allowed number for positive is 2147483647

# Time Complexity :  O(n)
# Space Complexity : O(1)