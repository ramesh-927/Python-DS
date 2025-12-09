"""
Docstring for AppleInterview.08-Others.56-7.ReverseInteger
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to 
go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
Example 2:
Input: x = -123
Output: -321
Example 3:
Input: x = 120
Output: 21
Constraints:
-231 <= x <= 231 - 1
"""
class Solution:
    def reverse(self, x):

        INT_MAX, INT_MIN = 2 ** 31 - 1, -2 ** 31
        rev, sign = 0, 1 if x >= 0 else -1
        x = abs(x)

        while x > 0:
            if rev > INT_MAX // 10:
                return 0
            rev = rev * 10 + x % 10
            x //= 10
        return sign * rev if sign * rev <= INT_MAX and sign * rev >= INT_MIN else 0

if __name__== "__main__":
    sol = Solution()
    print(sol.reverse(123))     # 321
    print(sol.reverse(-123))     # -321
    print(sol.reverse(120))      # 21
# Reverse Integer = Sign + 3 magic lines + Overflow police

# Best Time Complexity: O(log n), where n is the absolute value of the input. This is because we process each digit once, and the number of digits is log10(n). It's optimal—no faster way exists without skipping digits.
# Space Complexity: O(1), as we use fixed extra variables.

# I used the mathematical modulo method to extract and rebuild digits in reverse order while processing the number.This 
# ensures O(log n) time complexity with constant space, and I added step-by-step overflow checks 
# against 32-bit limits to return 0 if exceeded.