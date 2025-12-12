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
    print(sol.lenghtOfLongestSubString("pwwkew"))        # Prints : 3

# Time Complexity: O(n) – we loop through the string once.
# Space Complexity: O(min(n, m)) where m is the character set size (e.g., 26 for lowercase letters, 256 for ASCII).

# I used a sliding window with two pointers (left and right) and a dictionary to track the last index 
# of each character. When a repeat is found, I move the left pointer to just after the previous 
# occurrence, updating the max length along the way – achieving O(n) time.

# 4-Word Magic Phrase SLIDING WIDNOW ALGO (Never Forget This!) “Expand → Check → Shrink → Update”

# When I see ‘longest/minimum subarray/substring with constraint’, I immediately think Sliding Window 
# → Expand right, shrink left when invalid, update answer after every valid window.
# Pesudo Code : for right in range(len(arr)):
    # 1. Expand – add arr[right]
    # window.add(arr[right])           # or count[arr[right]] += 1

    # 2. Check + 3. Shrink – while window is bad
    # while window_is_invalid():       # e.g. duplicate exists, sum > k, etc.
    #     window.remove(arr[left])     # or count[arr[left]] -= 1
    #    left += 1

    # 4. Update – now the window is valid → grab the result
    # answer = max(answer, right - left + 1)   # or min, or count, etc.

    #Step,Word,What You Actually Do,One-Line Memory Trick
# 1,Expand,Move the right pointer → add s[right] into the window,“Always grow first – make the window bigger”
# 2,Check,"While the window is invalid (e.g., has duplicate, sum > target, etc.) → go to step 3",“Is it broken? Yes → fix it”
# 3,Shrink,Move the left pointer → remove s[left] from the window (repeat until valid again),“Throw out the bad stuff from the left”
# 4,Update,"After every valid window → update the answer (max length, min length, count, etc.)",“Take a photo of the best window so far”