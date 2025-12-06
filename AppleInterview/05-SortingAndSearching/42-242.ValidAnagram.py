"""
Docstring for AppleInterview.05-SortingAndSearching.42-242.ValidAnagram
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
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such 
a case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        
        # Step 1: Count characters in s
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Step 2: Decrement using characters in t
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] == 0:
                del count[char]  # Optional: keeps dict clean
        
        # Step 3: All counts must be zero
        return len(count) == 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram","nagaram"))     # Output : True
    print(sol.isAnagram("rat", "car"))            # Output : False

# I used a hash map to count character frequencies: increment counts while scanning the first string, 
# then decrement while scanning the second.
# If at any point we try to decrement a missing character or counts don't reach exactly zero at the end, 
# it's not an anagram — this is O(n) time and works for any character set.

# Time Complexity : O(n)
# Space Complexity : O(1)
# follow-up with Unicode → Hash map is the only fully correct and professional solution.
             