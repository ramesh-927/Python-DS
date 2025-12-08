"""
Docstring for AppleInterview.06-DynamicProgramming.48-10.RegularExpressionMatching
Given an input string s and a pattern p, implement regular expression matching with support 
for '.' and '*' where:

1. '.' Matches any single character.
2. '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character 
to match.
"""
from functools import lru_cache

class Solution:
    def isMatch(self, s, p):

        @lru_cache
        def dp(i, j):   # i = position in s, j = position in p
            # If I finished the pattern...
            if j == len(p):
                return i == len(s)   # success only if I also finished the text!

            # Can current letters match?
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # If the NEXT thing is a star (*)
            if j+1 < len(p) and p[j+1] == '*':
                # I have TWO superpowers!
                return (dp(i, j+2)                  # Option 1: ignore "x*" completely (use 0 times)
                        or
                        (first_match and dp(i+1, j)) # Option 2: use one more letter, stay on "*"
                        )
            else:
                # Normal case: must match one letter and move both fingers
                return first_match and dp(i+1, j+1)
            
        return dp(0, 0)

if __name__== "__main__":
    sol = Solution()
    print(sol.isMatch("aa", "a*"))     # True
    print(sol.isMatch("aa", "a*"))     # True
    print(sol.isMatch("ab", ".*"))     # True
        
#I used recursion with memoization (@lru_cache) to try matching the string and pattern step by step.
# When I see 'x*', I have two choices: skip it entirely or use it to match one more character — and 
# Python remembers results to avoid repetition.

#  Time Complexity   :  O(m * n) where m = len(s), n = len(p)                   
#  Space Complexity  :  O(m * n) for memoization + recursion stack (worst-case) 





"""
from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dp(i, j):
            if j == len(p):
                return i == len(s)            
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')            
            if j + 1 < len(p) and p[j + 1] == '*':
                return dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                return first_match and dp(i + 1, j + 1)       
        return dp(0, 0)
"""