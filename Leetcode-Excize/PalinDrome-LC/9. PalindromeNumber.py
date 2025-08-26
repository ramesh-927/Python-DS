"""
Given an integer x, return true if x is a palindrome, and false otherwise. 
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Constraints:
-231 <= x <= 231 - 1
"""
class Solution:
    def is_palindrome(self, x):
        if x < 0:
            return False
        original = x
        reversed = 0

        while x > 0:
            digit = x % 10
            reversed = reversed * 10 + digit
            x = x // 10
        return original == reversed

res = Solution()
result = res.is_palindrome(-123)
print(result)

# Time Complexity: O(log x), where x is the input number. The number of digits in x is proportional to log x, and we process each digit once.
# Space Complexity: O(1), as we only use a constant amount of extra space (variables for reversed_num and digit).