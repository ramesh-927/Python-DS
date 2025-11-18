"""
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
    
        # Handle negative exponents
        if n < 0:
            x = 1 / x
            n = -n
    
        result = 1
        current_product = x
    
        while n > 0:
            # If n is odd, multiply result by current_product
            if n % 2 == 1:
                result *= current_product
        
            # Square the base and halve the exponent
            current_product *= current_product
            n //= 2
    
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.0, 10))
    print(sol.myPow(2.10000, 3))
    print(sol.myPow(2.00000, -2))

# Time Complexity: O(log n) — Optimal!
# Space Complexity: O(1) — Uses only a few variables

