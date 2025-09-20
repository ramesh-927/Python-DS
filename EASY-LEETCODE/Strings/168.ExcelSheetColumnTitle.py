"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
Example 1:
Input: columnNumber = 1
Output: "A"
Example 2:
Input: columnNumber = 28
Output: "AB"
Example 3:
Input: columnNumber = 701
Output: "ZY" 
Constraints:
1 <= columnNumber <= 231 - 1
"""
class Solutions:
    def convertToTitle(self, columnNumber):

        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            result = chr(ord('A') + columnNumber % 26) + result
            columnNumber //= 26
        return result

sol = Solutions()
columnNumber = 701
res = sol.convertToTitle(columnNumber)
print(res)

# Time Complexity: O(log n), as the number of iterations is proportional to the number of digits in base-26, which is log₂₆(n).
# Space Complexity: O(1) auxiliary space, as we only use a string to store the result, which is required for the output.
