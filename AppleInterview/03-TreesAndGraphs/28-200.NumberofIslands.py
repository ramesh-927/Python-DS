"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the 
number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
class Solution:
    def numIsLands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                return
            
            grid[i][j] = '#' 
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    tests = [([
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ], 3), (
            [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ], 1), ]
    
    for i, (grid, expected) in enumerate(tests, 1):
        # copy grid if you want to reuse original test values later
        import copy
        gcopy = copy.deepcopy(grid)
        out = sol.numIsLands(gcopy)
        print(f"Test #{i}: output={out} expected={expected}")

# Time Complexity: O(M × N) — optimal
# Space Complexity: O(M × N) (due to recursion stack in worst case)

# I used DFS to traverse each island. Whenever I find a '1', I explore and mark the entire connected 
# land using recursion, then increment the island count. This ensures each island is counted exactly 
# once in O(M×N) time.

