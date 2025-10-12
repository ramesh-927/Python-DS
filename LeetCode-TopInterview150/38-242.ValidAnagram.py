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
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case
"""
class Solution:
    def validAnagram(self, s, t):

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


if __name__ == "__main__":
    sol = Solution()
    tests = [
    ("anagram", "nagaram"),    # True
    ("rat", "car"),   # False
    ]
    for a, b in tests:
        res = sol.validAnagram(a, b)
        print(f"{a} -> {b} : {res}")

# Time	O(n) — traverse both strings once
# Space	O(1) if only lowercase English letters (26), else O(k) for unique chars

