"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example 1:
A B C E
S F C S
A D E E
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:
A B C E
S F C S
A D E E
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:
A B C E
S F C S
A D E E
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
class Solution:
    def exists(self, board, word):
        if not board or not board[0]:
            return False
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]):
                return False
            temp = board[r][c]
            board[r][c] = "#"
            found = (dfs(r + 1, c, idx + 1) or
                     dfs(r - 1, c, idx + 1) or
                     dfs(r, c + 1, idx + 1) or 
                     dfs(r, c - 1, idx + 1))
            board[r][c] = temp
            return found
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
    
if __name__ == "__main__":
    sol = Solution()
    board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
    print(sol.exists(board, "ABCCED"))  # True
    print(sol.exists(board, "SEE"))     # True
    print(sol.exists(board, "ABCB"))    # False
