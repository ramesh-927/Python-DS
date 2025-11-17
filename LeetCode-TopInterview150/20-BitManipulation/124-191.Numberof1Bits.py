"""
Given a positive integer n, write a function that returns the number of set bits in its binary representation 
(also known as the Hamming weight).
Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.
Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.
Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
Constraints:
1 <= n <= 231 - 1
Follow up: If this function is called many times, how would you optimize it?
"""
class Solution:
    def hammingWeight(self, n):
        count = 0
        while n:
            n &= n - 1   # Removes the lowest set bit (rightmost 1)
            count += 1
        return count
    
if __name__ == "__main__":
    sol = Solution()
    n = 2147483645
    out = sol.hammingWeight(n)
    print(out)

# Use the n &= n-1 version in interviews — it shows you know bit tricks and optimal algorithms!
# Time: O(number of bits) = O(32) → O(1) since fixed size
# Space: O(1) — a few integer variables only.
