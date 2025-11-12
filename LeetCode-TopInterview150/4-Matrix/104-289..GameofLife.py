"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular 
automaton devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (
represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors 
(horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. 
In this process, births and deaths occur simultaneously.
Given the current state of the board, update the board to reflect its next state.
Note that you do not need to return anything.
Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
Follow up:
Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot 
update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, 
which would cause problems when the active area encroaches upon the border of the array 
(i.e., live cells reach the border). How would you address these problems?
"""
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        # make a copy of the original board
        original = [row[:] for row in board]
        
        # update each cell using the copy
        for i in range(rows):
            for j in range(cols):
                live = self.count_neighbors(i, j, original, rows, cols)
                
                if original[i][j] == 1:  # was alive
                    if live < 2 or live > 3:
                        board[i][j] = 0  # dies
                    # else stays alive (do nothing)
                else:  # was dead
                    if live == 3:
                        board[i][j] = 1  # becomes alive
        
    def count_neighbors(self, i: int, j: int, board: List[List[int]], rows: int, cols: int) -> int:
        count = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] == 1:
                    count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    sol.gameOfLife(board)          # modifies 'board' in-place
    print(board)                   # print the updated board

# Time: O(m × n) → every cell checked once
# Space: O(1) → done in-place, no extra copy

