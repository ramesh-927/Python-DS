"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        for char in t:
            if char in char_count:
                char_count[char] -= 1
            else:
                return False
        return all(count == 0 for count in char_count.values())

sol = Solution()
s = "anagram"
t = "nagaram"
res = sol.isAnagram(s, t)

print(res)  # Output: True