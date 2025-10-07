"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string. 

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa". 

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""
class Solution:
    def countSubstrings(self, s):
        n = len(s)
        count = 0
        def expand(l, r):
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        return count

# count_substrings("aaa") -> 6 (a, a, a, aa, aa, aaa)

        

sol = Solution()
s = "aaa"
res = sol.countSubstrings(s)
print(f"Total Count of substring {s} is: ", res)

# Time: O(n^2). Space: O(1).