"""
Given a string num which represents an integer, return true if num is a strobogrammatic number.
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Example 1:
Input: num = "69"
Output: true
Example 2:
Input: num = "88"
Output: true
Example 3:
Input: num = "962"
Output: false 
Constraints:
1 <= num.length <= 50
num consists of only digits.
num does not contain any leading zeros except for zero itself.
"""
class Solutions:
    def isStrobogrammatic(self, num):

        mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        left, right = 0, len(num) - 1

        while left <= right:
            if num[left] not in mapping:
                return False
            if mapping[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True
    
if __name__ == "__main__":
    sol = Solutions()
    num = "69"
    result = sol.isStrobogrammatic(num)
    print(result)

