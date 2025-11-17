"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine):
        
        ransomNote_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char, count in ransomNote_count.items():
            if magazine_count[char] < count:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    ransomNote = "aa"
    magazine = "aab"
    res = sol.canConstruct(ransomNote, magazine)
    print(res)


# Time	O(m + n)	Counting letters in both strings
# Space	O(1)	Only 26 lowercase letters (constant space)