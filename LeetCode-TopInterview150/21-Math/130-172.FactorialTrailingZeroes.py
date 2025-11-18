"""
Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:
Input: n = 0
Output: 0
Constraints:
0 <= n <= 104
Follow up: Could you write a solution that works in logarithmic time complexity?
"""
class Solution:
    def trailingZeroes(self, n):
        count = 0

        while n >= 5:
            n //= 5
            count += n
        return count
    
if __name__=="__main__":
    sol = Solution()
    print(sol.trailingZeroes(5))    # 1
    print(sol.trailingZeroes(26))   # 6
    print(sol.trailingZeroes(100))  # 24

# Time complexity	O(log_5 n) — number of loop iterations is how many powers of 5 fit in n.
# Space complexity	O(1) — constant extra space.