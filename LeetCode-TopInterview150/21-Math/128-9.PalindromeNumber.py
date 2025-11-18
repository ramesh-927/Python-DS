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
Follow up: Could you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True    # Single digit always Plaindrome
        
        reversed = 0
        num = x

        while num > 0:
            reversed = reversed * 10 + num % 10
            num //= 10

        return reversed == x

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))   # True
    print(sol.isPalindrome(-121))  # False
    print(sol.isPalindrome(10))    # False

# Time Complexity: O(log n) → only one pass through digits
# Space Complexity: O(1) → no extra space (doesn't use strings or lists)