"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only. 
Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6. 
Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""
class Solution(object):
    def lengthOfLastWord(self, s):

        length = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] == ' ':
                if length > 0:
                    return length
                i -= 1
            else:
                    length += 1
                    i -= 1
        return length

sol = Solution()
s = "luffy is still joyboy"
res = sol.lengthOfLastWord(s)
print(res)

