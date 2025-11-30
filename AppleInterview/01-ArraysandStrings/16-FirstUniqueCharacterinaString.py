"""
Given a string s, find the first non-repeating character in it and return its index. If it does 
not exist, return -1.
Example 1:
Input: s = "leetcode"
Output: 0
Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.
Example 2:
Input: s = "loveleetcode"
Output: 2
Example 3:
Input: s = "aabb"
Output: -1
Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
"""
class Solution:
    def firstUniqChar(self, s):
        char_count = {}
        n = len(s)

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        return  -1
    
if __name__== "__main__":
    sol = Solution()
    print(sol.firstUniqChar("leetcode"))    # Output : 0
    print(sol.firstUniqChar("loveleetcode"))   # Output : 2
    print(sol.firstUniqChar("aabb"))          # Output : -1

# "I used a hash map to count character frequencies in one pass, then scanned the string again to 
# find the first character with a count of one. This gives O(n) time complexity and O(1) space for 
# lowercase letters."

# Time Complexity: O(n)
# First loop: O(n) to count characters.
# Second loop: O(n) to find the first unique character.
# Total: O(n), where n is the string length.

# Space Complexity: O(k)
# The dictionary stores at most k unique characters. Since the problem specifies lowercase letters, 
# k ≤ 26, which is effectively O(1). For general cases (e.g., Unicode characters), it’s O(k), 
# but still bounded by the input size.