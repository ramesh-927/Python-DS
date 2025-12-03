"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down. You may not move 
diagonally or move outside the boundary (i.e., wrap-around is not allowed).
Example 1:
    [9, 9,  4],
    [6, 6,  8],
    [2, 1,  1]
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:
Input: matrix = [[1]]
Output: 1
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        cache = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if cache[i][j]:               # already computed → use cached value
                return cache[i][j]
            
            length = 1
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + x, j + y
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    length = max(length, 1 + dfs(ni, nj))
            
            cache[i][j] = length          # remember the answer
            return length

        # Try starting from every cell and take the maximum
        return max(dfs(i, j) for i in range(m) for j in range(n))


# Test
matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
print(Solution().longestIncreasingPath(matrix))  # Output: 4  # prints 4

# I use DFS with a cache: for each cell, I remember the longest uphill path starting from it, so 
# I never compute the same cell twice

# Time Complexity: O(m * n) – Each cell is visited once.
# Space Complexity: O(m * n) – For the memo grid (and recursion stack in worst case).



