"""
Docstring for FacebookInterview.LeetCodeSolutions.05-SearchingOrSorting.52-50.Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""
class Solution:
    def myPow(self, x, n):

        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result
    
if __name__== "__main__":
    sol = Solution()
    print(sol.myPow(2.00000, 10))         # Outputs: 1024.0
    print(sol.myPow(2.00000, -2))         # Outputs: 0.25
    print(sol.myPow(2.10000, 3))          # Outputs: 9.261000000000001

# I used exponentiation by squaring (binary exponentiation) to compute x^n in O(log n) time by repeatedly 
# squaring the base and halving the exponent, handling negative n by taking the reciprocal. This avoids 
# the O(n) brute force loop, making it efficient for large exponents.

# This runs in O(log n) time—super fast, as log(2 billion) is just about 30 steps. Space is O(1), constant.

# It's the best because it minimizes multiplications using math properties (binary decomposition), 
# handles huge n efficiently, and works for both positive/negative exponents without recursion 
# (to avoid stack overflow).

