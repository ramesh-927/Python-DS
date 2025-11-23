"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and 
return its area.
Example 1:
Input:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:
Input:
0 1 
1 0 
Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:
Input: matrix = [["0"]]
Output: 0
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""
class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        max_sqlen = 0

        for i in range(rows):
            prev = 0
            for j in range(cols):
                temp = dp[j + 1]     # save current dp[j+1] before overwrite
                if matrix[i][j] == '1':
                    dp[j + 1] = min(dp[j], dp[j + 1], prev) + 1
                    max_sqlen = max(max_sqlen, dp[j + 1])
                else:
                    dp[j + 1] = 0
                prev = temp
        return max_sqlen ** 2
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    # Output: 4
    print(sol.maximalSquare([["0","1"],["1","0"]]))   # Output: 1

# We use 1D DP where dp[j] means the largest square ending at column j in the current row.
# To compute it, we need the min of left, top, and top-left (diagonal).
# We maintain a 'prev' variable to store the diagonal value safely.
# This reduces space from O(mn) to O(n)."