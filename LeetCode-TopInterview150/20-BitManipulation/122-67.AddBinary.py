"""
Given two binary strings a and b, return their sum as a binary string.
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
class Solution:
    def addBinary(self, a, b):
        result = []
        carry = 0
        i , j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry
            result.append(str(total % 2))
            carry = total // 2
            i -= 1
            j -= 1
        return ''.join(reversed(result))

if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("11", "1"))
    print(sol.addBinary("1010", "1011"))

# | Resource | Cost                                   |
# | -------- | -------------------------------------- |
# | Time     | O(n) where n = max(len(a), len(b))     |
# | Space    | O(n) for the output (plus O(1) extras) |
