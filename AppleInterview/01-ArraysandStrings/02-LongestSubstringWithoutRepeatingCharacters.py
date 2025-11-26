"""
Given a string s, find the length of the longest substring without duplicate characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOflongestSubString(self, s):

        char_set = {}     # Dictionary to store last position of each character
        max_length = 0    # Track longest substring length
        left = 0

        for right, char in enumerate(s):     # Move right side of window
            if char in char_set and char_set[char] >= left:
                left = char_set[char] + 1   # Move left to just after last occurrence
            char_set[char] = right
            max_length = max(max_length, right - left + 1)     # Update max length
        return max_length
    
if __name__ =="__main__":
    sol = Solution()
    print(sol.lengthOflongestSubString("abcabcbb"))   # prints 3
    print(sol.lengthOflongestSubString("bbbbb"))      # prints 1
    print(sol.lengthOflongestSubString("pwwkew"))     # prints 3

# Time Complexity: O(n), where n is the length of the string. We only scan the string once, and each 
# character is processed in constant time.
# Space Complexity: O(min(m, n)), where m is the size of the character set (e.g., 26 for lowercase 
# letters) and n is the string length. The dictionary stores at most m or n characters.

# I used the sliding window technique with a hash map to track the last position of each character, 
# achieving O(n) time complexity. The window expands until a repeat is found, then shrinks by moving 
# the left pointer past the last occurrence of the repeated character.