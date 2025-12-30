"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.19-340-LongestSubstringwithAtMostKDistinctCharacters
Given a string s and an integer k, return the length of the longest substring of s that contains 
at most k distinct characters.
Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50
"""
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):

        if k == 0:
            return 0
        char_count = defaultdict(int)
        max_len = left = 0

        for right in range(len(s)):
            char_count[s[right]] += 1

            while len(char_count) > k:
                char_count[s[left]] -= 1

                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstringKDistinct("eceba", 2))        #  3
    print(sol.lengthOfLongestSubstringKDistinct("aa", 1))           #  2

# For problems like "longest/maximum substring/subarray with constraint X" (e.g., at most k distinct 
# items, sum <= target), the sliding window with two pointers is the go-to algorithm. It keeps 
# a dynamic "window" that expands and contracts efficiently, often achieving O(n) time. Pair it 
# with a frequency map (like a dictionary or Counter) to track the constraint (here, distinct 
# count).

# This is O(n) time (n is string length) and O(min(n, 26)) space if assuming lowercase letters, 
# or O(k) in general. It's optimal because we scan the string once with two pointers moving 
# forward only.

# I used a sliding window with two pointers (left and right) and a frequency dictionary to track 
# characters in the current window. We expand the right pointer, shrink from left if distinct 
# characters exceed k, and update the max length—achieving O(n) time.

        