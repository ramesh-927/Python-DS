"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s 
such that every character in t (including duplicates) is included in the window. 
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
Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:   # ← Correct order: s first, t second
        if not s or not t:
            return ""
        
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        
        missing = len(t)
        left = 0
        result = ""

        for right, char in enumerate(s):
            if char in need:
                need[char] -= 1
                if need[char] >= 0:
                    missing -= 1
            
            while missing == 0:
                current = s[left: right + 1]

                if not result or len(current) < len(result):
                    result = current
                
                left_char = s[left]
                if left_char in need:
                    need[left_char] += 1
                    if need[left_char] > 0:
                        missing += 1
                left += 1
        
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))   # → "BANC"
    print(sol.minWindow("a", "aa"))                # → ""
    print(sol.minWindow("a", "a"))                 # → "a"
    print(sol.minWindow("ab", "b"))                # → "b"

    # Time Complexity: O(n) 
    # Space Complexity: O(1) (since max 52 unique chars)