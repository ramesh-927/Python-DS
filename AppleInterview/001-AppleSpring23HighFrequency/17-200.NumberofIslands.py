"""
Docstring for AppleInterview.001-AppleSpring23HighFrequency.17-200.NumberofIslands
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
    def numIslands(self, grid):

        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands  = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'                  # mark visited (sink it)
            dfs(r-1, c)                       # up
            dfs(r+1, c)                       # down
            dfs(r, c-1)                       # left
            dfs(r, c+1)                       # right
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands

if __name__== "__main__":

    sol = Solution()
    print(sol.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]))           # Prints : 3
    print(sol.numIslands( [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]))          # Prints : 1

# When I see a '1', I count +1 island and DFS-sink the entire island so I never see it again.

# This is a classic "connected components" problem in a graph, where each '1' is a node, and connections 
# are to neighboring '1's (up, down, left, right). The best algorithms are graph traversals like 
# Depth-First Search (DFS) or Breadth-First Search (BFS), as they efficiently explore and mark groups 
# without revisiting cells.

# Time Complexity: O(m * n), where m is rows and n is columns—we visit each cell at most once.
# Space Complexity: O(m * n) in the worst case (if the grid is all '1's, the recursion stack could 
# grow deep), but we optimize by modifying the grid in place (no extra visited array).

# I used Depth-First Search (DFS) to traverse the grid and count connected components of '1's. We 
# iterate over each cell; if it's '1', increment the island count and recursively "sink" (mark as '0') 
# all adjacent '1's to avoid recounting