"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
 Alphanumeric characters include letters and numbers.
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
    def is_palindrome(self, s):
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
    
sol = Solution()
s = "A man, a plan, a canal: Panama"
res = sol.is_palindrome(s)
print(res)

# Time Complexity: O(n), where n is the length of the string. We traverse the string once with the two pointers, and each character is processed at most once.
# Space Complexity: O(1), as we only use two pointers and no additional data structures.
