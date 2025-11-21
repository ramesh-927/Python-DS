"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example 1:
    1 →   3  →  1
    1 →   5  →  1
    4 →   2  →  1
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""
class Solution:
    def minPathsum(self, grid):
        m, n = len(grid), len(grid[0])

        # First column
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # First row   
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        ## Rest of the grid
        for i in range(1, m):
            for j in range(1 ,n):
                grid[i][j] += min(grid[i -1][j], grid[i][j - 1])
        return grid[-1][-1]
    
if __name__=="__main__":
    sol = Solution()
    print(sol.minPathsum([[1,3,1],[1,5,1],[4,2,1]]))  # prints 7
    print(sol.minPathsum([[1,2,3],[4,5,6]]))  # prints 12

# Approach,                  Time Complexity,     Space Complexity
# 2D DP (first version),       O(m × n),              O(m × n)
# In-place (best),             O(m × n),               O(1)

# I used bottom-up dynamic programming.
# We fill each cell with the minimum path sum to reach it by taking min(from above, 
# from left) + current value — can be done in-place for O(1) space.

