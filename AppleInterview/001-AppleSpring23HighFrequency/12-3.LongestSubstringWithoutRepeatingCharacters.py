"""
Docstring for AppleInterview.001-AppleSpring23HighFrequency.12-3.LongestSubstringWithoutRepeatingCharacters
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
    def lenghtOfLongestSubString(self, s):

        char_idx = {}
        max_len = 0
        left = 0

        for right in range(len(s)):

            if s[right] in char_idx and char_idx[s[right]] >= left:
                left = char_idx[s[right]] + 1
            char_idx[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lenghtOfLongestSubString("abcabcbb"))      # Prints : 3
    print(sol.lenghtOfLongestSubString("bbbbb"))         # Prints : 1
    print(sol.lenghtOfLongestSubString("pwwkew"))        # Prints :
