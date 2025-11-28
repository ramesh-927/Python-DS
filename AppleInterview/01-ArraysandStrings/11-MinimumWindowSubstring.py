"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring 
of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
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
"""
from collections import Counter
class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        
        need = Counter(t)                  # Characters we want
        have = {}                          # Characters in the current window
        need_count  = len(need)            # How many unique chars are required.
        have_count = 0                     # have many currently we satisfy
        res = ""
        left = 0

        for right, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1

            if ch in need and have[ch] == need[ch]:
                have_count += 1
            
            # shrink from left while window is valid
            while have_count == need_count:
                window = s[left: right + 1]
                if res == "" or len(window) < len(res):
                    res = window
                
                left_char = s[left]
                have[left_char]  -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    have_count -= 1
                left += 1

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))     # prints BANC
    print(sol.minWindow("a", "a"))           # prints a
    print(sol.minWindow("a", "aa"))          # prints  ""

# "I used a sliding-window (two-pointer) technique with frequency maps: expand the right pointer 
# until all required characters from t are included, then contract the left pointer to minimize the 
# window. This yields an optimal O(n) time solution where n = |s|."

# Time Complexity: O(n) where n = len(s)
# Space Complexity: O(1) (at most 52 keys: 26 lowercase + 26 uppercase)