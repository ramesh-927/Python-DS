"""
Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.
Example 1:
Input: s = "code"
Output: false
Example 2:
Input: s = "aab"
Output: true
Example 3:
Input: s = "carerac"
Output: true
Constraints:
1 <= s.length <= 5000
s consists of only lowercase English letters.
"""
from collections import Counter
class Solution:
    def canPermutePalindrome(self, s):

        freq = Counter(s)
        odd_count  = 0

        for count in freq.values():
            if count % 2 == 1:
                odd_count += 1
                if odd_count > 1:
                    return False
        return True
    
if __name__ =="__main__":
    sol = Solution()
    s = "carerac"
    res = sol.canPermutePalindrome(s)
    print(res)

# Time & Space Complexity
# Time: O(n) → count characters once, where n = len(s)
# Space: O(1) → at most 26 lowercase English letters.