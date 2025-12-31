"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.12-125.ValidPalindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include 
letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
class Solution:
    def isPalindrome(self, s):

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

if __name__== "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))        # True
    print(sol.isPalindrome("race a car"))                            # False
    print(sol.isPalindrome(" "))                                     # True

# Time Complexity: O(n) – we might check every character once in the worst case.
# Space Complexity: O(1) – no extra space beyond a few variables.

# Best Algorithm for This Kind of Problem: The two-pointer technique is the go-to for palindrome checks, 
# especially when you need to ignore certain characters or handle edge cases efficiently. It's simple, runs 
# in linear time, and avoids unnecessary work.

# I used the two-pointer method, starting one at each end of the string and moving inward while skipping 
# non-alphanumeric characters. We compare characters case-insensitively, returning false on mismatch or 
# true if they all align.