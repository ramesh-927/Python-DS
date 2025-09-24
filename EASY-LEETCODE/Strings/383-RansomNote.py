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

class Solutions:
    def canConstruct(self, ransomNote, magazine):

        count_ransomNote = Counter(ransomNote)
        count_magazine = Counter(magazine)

        for char, count in count_ransomNote.items():
            if count_magazine[char] < count:
                return False
        return True
    
if __name__ == "__main__":

    sol = Solutions()
    ransomNote = "aa"
    magazine = "ab"
    res = sol.canConstruct(ransomNote, magazine)
    print(res)



# Time Complexity : O(n+m), where n = len(ransomNote) and m = len(magazine).

# Checking counts: O(k), where k = number of unique letters in ransomNote (≤ 26 for lowercase letters).
# O(n+m) → linear and optimal.

# Space Complexity : O(1) for counters since max 26 lowercase letters → constant space.