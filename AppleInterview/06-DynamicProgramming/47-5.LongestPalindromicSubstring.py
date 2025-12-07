"""
Docstring for AppleInterview.06-DynamicProgramming.47-5.LongestPalindromicSubstring
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
            return  ""
        
        start, max_len = 0, 1
        def expand(left, right):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1
            return right - left - 1
        
        for i in range(len(s)):
            len1 = expand(i, i)         # Odd length
            len2 = expand(i , i + 1)    # Even length

            if max(len1, len2) > max_len:
                max_len = max(len1, len2)
                start = i - (max_len - 1) // 2
        return s[start : start + max_len]
    
if __name__=="__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))      # bab
    print(sol.longestPalindrome("cbbd"))       # bb

# Time Complexity : O(n²): We loop n times, and each expansion can take up to O(n) in the worst case 
# (e.g., all characters same).
# Space Complexity : O(1), ignoring input.

# I used the "expand around centers" method, treating each character (for odd-length palindromes) 
# and each pair (for even-length) as a potential center. We expand outwards to find the longest 
# matching palindrome while tracking the maximum length and start position.