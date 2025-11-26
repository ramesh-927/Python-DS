"""
Docstring for AppleInterview.01-ArraysandStrings.05-RomantoInteger
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for 
four is not IIII. Instead, the number four is written as IV. Because the one is before the five we 
subtract it making four. The same principle applies to the number nine, which is written as IX. T
here are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
class Solution:
    def romanToInteger(self, s):

        values = {"I": 1 ,"V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInteger("III"))         # Output: 3
    print(sol.romanToInteger("LVIII"))       # Output: 58
    print(sol.romanToInteger("MCMXCIV"))     # Output: 1994
    print(sol.romanToInteger("MMMDCCXLIX"))  # Output: 3749

# Time Complexity: O(n) – we visit each character once
# Space Complexity: O(1) – only a fixed dictionary

# I used a single pass from left to right with a hashmap of Roman values.
# The key insight is: if the current value is less than the next, subtract it (like IV = 5-1), 
# otherwise add — this naturally handles all subtractive cases in O(n) time.
