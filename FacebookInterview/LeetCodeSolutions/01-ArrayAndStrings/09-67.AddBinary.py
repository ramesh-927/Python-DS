"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.09-67.AddBinary

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
class solution:
    def addBinary(self, a, b):

        i , j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            result.append(str(total % 2))
            carry = total // 2

        return "".join(reversed(result))

if __name__ == "__main__":
    sol = solution()
    print(sol.addBinary("11", "1"))            # 100
    print(sol.addBinary("1010", "1011"))       # 10101

# Two Pointer + Carry (Binary Addition)

# I used a two-pointer approach starting from the end of both binary strings while maintaining a carry. 
# This simulates manual binary addition and runs in linear time with optimal space usage.


#  Time Complexity :    **O(n)**   
#  Space  Complexity :  **O(n)**   



