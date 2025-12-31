"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.15-161.OneEditDistance

Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.
A string s is said to be one distance apart from a string t if you can:
Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
Example 1:
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:
Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
Constraints:
0 <= s.length, t.length <= 104
s and t consist of lowercase letters, uppercase letters, and digits.
"""
# Best Algorithm to Choose :     Two Pointers + Greedy comparison
class Solution:
    def isOneEditDistance(self, s, t):
        
        m, n = len(s), len(t)

        if abs(m - n) > 1:
            return False
        
        i = j = edits = 0

        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                edits += 1

                if edits > 1:
                    return False
                if m > n:
                    i += 1
                elif m < n:
                    j += 1
                else:
                    i += 1
                    j += 1
        if i < m or j <  n:
            edits += 1
        
        return edits == 1

if __name__ =="__main__":
    sol = Solution()
    print(sol.isOneEditDistance("ab", "acb"))     # True
    print(sol.isOneEditDistance("",  ""))         # False

# Time  Complexity :  O(N)
# Space Complexity :  O(1) 

# I used a two-pointer greedy approach to compare both strings character by character. I allow 
# only one mismatch and adjust pointers based on insert, delete, or replace scenarios

