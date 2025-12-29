"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.10-76.MinimumWindowSubstring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such 
that every character in t (including duplicates) is included in the window. If there is no such substring, 
return the empty string "".
The testcases will be generated such that the answer is unique.
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
from collections import Counter
class Solution:
    def minwindow(self, s, t):

        if not s or not t:
            return ""
        
        need = Counter(t)
        missing = len(t)
        start = left = 0
        end = float('inf')  # Use large number instead of 0

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                if end == 0 or right - left + 1 < end - start:
                    start, end = left, right + 1
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return  s[start:end] if end != float('inf') else ""

if __name__ =="__main__":
    sol = Solution()
    print(sol.minwindow("ADOBECODEBANC", "ABC"))        # BANC
    print(sol.minwindow("a", "a"))                      # a
    print(sol.minwindow("a", "aa"))                      # ""

# Sliding Window with Frequency Counting .This is the standard and expected solution in interviews.
# I used a sliding window with a single frequency map that allows negative counts for extras. I track the 
# remaining characters needed with a 'missing' counter, expand the right pointer to satisfy requirements, 
# and shrink from the left when valid to minimize the window — achieving O(n) time with very minimal code

# Time Complexity : 	O(n)
# Space Complexity : 	O(k) (characters in t)
