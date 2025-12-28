"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.07-43.MultiplyStrings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and 
num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""
class Solution:
    def multiply(self, num1, num2):

        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) +len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, - 1):
                mul = int(num1[i]) * int(num2[j])
                pos1, pos2 = i + j, i + j + 1
                total = mul + res[pos2]
                res[pos2] = total % 10
                res[pos1] += total // 10
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        return "".join(map(str, res[i:]))
    
if __name__== "__main__":
    sol = Solution()
    print(sol.multiply("123", "456"))

# For multiplying two large numbers given as strings (or arrays of digits), the best standard algorithm 
# is this "grade-school multiplication" with an accumulation array. It's O(m * n) and practical. 
# For even larger scales (e.g., millions of digits), you'd use faster methods like Karatsuba 
# (O(n^1.58)) or FFT-based (O(n log n)), but they're overkill here—more complex, higher constants, 
# and not needed for LeetCode constraints (up to 200 digits). Stick to the simple one for interviews: 
# it's easy to code, debug, and explain.

# Time complexity: O(m * n)
# Space complexity: O(m + n)
