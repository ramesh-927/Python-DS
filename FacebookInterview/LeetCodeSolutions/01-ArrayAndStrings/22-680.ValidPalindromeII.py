"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.22-680.ValidPalindromeII

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
class Solution:
    def validPalindrome(self, s):
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return is_pal(left + 1, right) or is_pal(left, right - 1)
            left += 1
            right -= 1
        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.validPalindrome("aba"))       # True
    print(sol.validPalindrome("abca"))      # True
    print(sol.validPalindrome("abc"))       # False

# Time complexity: O(n) – Best possible for this problem, as we must read the string at least once.
# Why minimal code? It uses a nested helper function for clarity, avoids unnecessary variables, and handles 
# the base case (already a palindrome) naturally.

# For palindrome validation with modifications (like allowing k deletions), the two-pointer approach is 
# best. It efficiently finds mismatches and branches minimally. For k>1, it generalizes to dynamic programming 
# or greedy with recursion, but for k=1 (this problem), the simple dual-check on mismatch is optimal.

# I used a two-pointer technique starting from both ends of the string to detect mismatches efficiently. 
# When a mismatch occurs, I check if skipping either the left or right character makes the remaining 
# substring a palindrome, ensuring O(n) time with at most one deletion.