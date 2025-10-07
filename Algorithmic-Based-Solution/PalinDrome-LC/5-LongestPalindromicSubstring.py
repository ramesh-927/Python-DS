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
s consist of only digits and English letters
"""
class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        start, end = 0, 0
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = expand(i, i )  # Odd length
            l2, r2 = expand(i, i + 1)  # Even lenght

            if r1 - l1 > end - start:
                start, end = l1, r1 
            if r2  - l2  > end - start:
                start, end = l2, r2
        return s[start:end + 1]


sol = Solution()
s = "babad"
res = sol.longestPalindrome(s)
print(f"Lomgest palindrome {s}", res)

# Time: O(n^2) worst-case.
# Space: O(1).

