"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid.
A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.
Example 1:
robot   empty   empty
empty   redDiamond  empty
empty   empty   star
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:
robot   redDiamond
empty   star
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * n
        dp[0] = 1      # one way to stand at start

        # If start or end is blocked
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1]:
            return 0
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0    # blocked → 0 ways
                elif j > 0:
                    dp[j] += dp[j - 1]   # add ways from left

        return dp[-1]

if __name__=="__main__":
    sol = Solution()
    print(Solution().uniquePathsWithObstacles([[0,0,0], [0,1,0], [0,0,0]]))  # prints 2
    print(Solution().uniquePathsWithObstacles([[0,1],[0,0]]))  # prints 1

# Time Complexity : 	O(m * n)
# Space	Complexity :    O(n) extra (where n is number of columns)

# We use 1D DP where dp[j] means ways to reach column j in the current row. 
# For each cell: if it's blocked, set dp[j]=0; otherwise add the ways from the left. 
# Finally dp[n-1] is the answer. O(m×n) time, O(n) space.
