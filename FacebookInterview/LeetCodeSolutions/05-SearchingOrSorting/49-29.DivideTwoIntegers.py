"""
Docstring for FacebookInterview.LeetCodeSolutions.05-SearchingOrSorting.49-29.DivideTwoIntegers

Given two integers dividend and divisor, divide two integers without using multiplication, division, 
and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. For example, 
8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
Return the quotient after dividing dividend by divisor.
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed
 integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, 
 then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
-2**31 <= dividend, divisor <= 2**31 - 1
divisor != 0

"""
class Solution:
    def divideTwoInteger(self, dividend, divisor):

        if divisor  == 0:
            raise ValueError("Divided by Zero!")
        
        if dividend == -2**31 and divisor == -1:
            return 2**31 -1
        
        sign = 1 if (dividend ^ divisor) >= 0 else -1

        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                i <<= 1
            dividend -= temp
            quotient += i
        return sign * quotient

if __name__== "__main__":
    sol = Solution()
    print(sol.divideTwoInteger(10, 3))       #  3
    print(sol.divideTwoInteger(7, -3))       # -2

# Best algorithm for this kind of problem (division without operators): Bit manipulation with exponential 
# doubling (or binary search on the quotient, but doubling is simpler and common).

# Time complexity: O(log |dividend|), since each loop halves the effective size (32 steps max for 32-bit numbers). 
# Space Compleixty : O(1).

# I used bit manipulation with exponential doubling of the divisor via left shifts to subtract large 
# multiples efficiently, achieving O(log N) time by reducing the dividend logarithmically instead of 
# linearly. This avoids slow repeated subtraction and handles signs/overflow separately for correctness 
# in 32-bit constraints.