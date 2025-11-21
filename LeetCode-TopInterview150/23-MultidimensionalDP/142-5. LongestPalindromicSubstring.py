"""
Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        start = 0
        max_len = 1

        def expand(left, right):
            nonlocal start, max_len

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        return s[start: start + max_len]

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))   # prints "aba" or "bab"
    print(sol.longestPalindrome("cbbd"))  # prints "bb"


#  Time  Complexity     | O(n²) → For each character, expand can go up to n steps. 
#  Space  Complexity    | O(1) → Only pointers and string slices are used.         

# I expand around each character (and between each pair for even-length) to find all possible 
# palindromes and track the longest.

