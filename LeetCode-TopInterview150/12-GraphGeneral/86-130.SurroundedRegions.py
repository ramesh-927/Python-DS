"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything. 
Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation:
X X X X
X O O X
X X O X
X O X X
   =>
X X X X
X X X X
X X X X
X O X X

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.
Example 2:
Input: board = [["X"]]
Output: [["X"]]
Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""
from collections import deque

class Solution:
    def solve(self, board):
        # in-place modification; returns None
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])
        q = deque()

        # Add border 'O's (first/last column for every row)
        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == 'O':
                    board[r][c] = 'S'
                    q.append((r, c))

        # Add border 'O's (first/last row for every column)
        for c in range(cols):
            for r in (0, rows - 1):
                if board[r][c] == 'O':
                    board[r][c] = 'S'
                    q.append((r, c))

        # BFS from all border 'O's and mark connected 'O's as 'S'
        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    board[nr][nc] = 'S'
                    q.append((nr, nc))

        # Flip the remaining 'O' -> 'X' and 'S' -> 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'


board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]

Solution().solve(board)

for row in board:
    print(row)

# board becomes:
#[["X","X","X","X"], ["X","X","X","X"], ["X","X","X","X"], ["X","O","X","X"]]

#  Time  Complexity : `O(m * n)`                                                                                                 |
#  Space (extra) | `O(m * n)` worst-case for the queue (but typically less). 
# In-place marks use constant extra besides queue. 


                



