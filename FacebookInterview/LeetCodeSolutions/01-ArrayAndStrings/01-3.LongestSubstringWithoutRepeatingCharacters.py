"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.01-3.LongestSubstringWithoutRepeatingCharacters

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
    def longestSubstring(self, s):
        max_len = 0
        left = 0
        char_set = {}

        for right, char in enumerate(s):
            if char in char_set and char_set[char] >= left:
                left = char_set[char] + 1
            char_set[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubstring("abcabcbb"))        # Prints : 3
    print(sol.longestSubstring("bbbbb"))           # Prints : 1
    print(sol.longestSubstring("pwwkew"))          # Prints : 3

# For the optimal way, we use a "sliding window" technique. Think of it like a window frame sliding 
# along a wall (the string). The window starts small and grows by moving the right side forward, 
# adding new letters. If we see a repeat, we slide the left side forward to shrink the window until 
# no repeats. We keep track of the biggest window size seen.

# I used a sliding window approach with a hashmap to track the last seen indices of characters.This 
# achieves O(n) time complexity by scanning the string once and efficiently handling duplicates by 
# adjusting the window start.

# Time Complexity:     O(n)
# Space Complexity :   O(min(n, 26)) for English letters, but up to O(n) for unique chars.


