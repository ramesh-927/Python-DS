"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:
Input: s = "aba"
Output: true
Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:
Input: s = "abc"
Output: false
Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""
class solutions(object):
    def validPalindrome(self, s):
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1
        return True




sol = solutions()
pal = "abca"
result = sol.validPalindrome(pal)
print(result)

# Time Complexity: O(n), where n is the string length.
# The main loop scans the string once, up to O(n/2) steps.
# On a mismatch, we call check twice, each taking up to O(n/2) steps.
# Total: O(n/2) + 2 * O(n/2) ≈ O(n)."""


# Space Complexity: O(1)