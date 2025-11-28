"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
 all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters 
 include letters and numbers.
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
        # Two pointers: left -> right, only consider alphanumeric & ignore case
        left, right = 0, len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():    # skip non-alphanumeric
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():  # compare ignoring case
                return False 
            
            left += 1
            right -= 1

        return True
    
if __name__== "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))    # prints : True
    print(sol.isPalindrome("race a car"))                        # prints : False
    print(sol.isPalindrome(" "))                                 # prints : True

# Time Complexity : O(n)
# Space Complexity : O(1) 
# "I used the two-pointer technique starting from both ends, skipping non-alphanumeric characters and 
# comparing characters ignoring case.It runs in O(n) time and O(1) extra space, which is optimal 
# for this problem."

