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

class Solutions:
    def isPalindrome(self, s):
        s = ''.join(c.lower() for c in s if c.isalnum())
        
        # Set pointers after preprocessing
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    

sol = Solutions()
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

input1 = sol.isPalindrome(s1)
input2 = sol.isPalindrome(s2)
input3 = sol.isPalindrome(s3)

print(f"{s1} - First input: {input1}")  # True
print(f"{s2} - Second input: {input2}") # False
print(f"{s3} - Third input: {input3}")  # True


