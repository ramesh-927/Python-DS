"""
Docstring for AppleInterview.04-Recurrsion.37-79.WordSearch
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example 1:
"A" "B" "C" "E"
"S" "F" "C" "S"
"A" "D" "E" "E"
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:
"A" "B" "C" "E"
"S" "F" "C" "S"
"A" "D" "E" "E"
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:
"A" "B" "C" "E"
"S" "F" "C" "S"
"A" "D" "E" "E"
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
    def exist(self, board, word):

        if not board or not board[0]:
            return False
    
        m, n = len(board), len(board[0])
    
        def dfs(i, j, idx):
            if idx == len(word):          # found whole word
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx]:
                return False
        
            # Mark cell as visited by changing its value temporarily
            temp = board[i][j]
            board[i][j] = '#'
        
            # Explore 4 directions
            found = (dfs(i+1, j, idx+1) or 
                    dfs(i-1, j, idx+1) or 
                    dfs(i, j+1, idx+1) or 
                    dfs(i, j-1, idx+1))
        
            # Backtrack: restore original value
            board[i][j] = temp
        
            return found
    
        # Try starting from every cell
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
    
        return False

if __name__== "__main__":
    sol = Solution()
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # Output : True
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) # Output : False
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # Output : True

#I used DFS with backtracking starting from every cell in the board. At each step, I temporarily mark 
# the cell as visited, explore all 4 directions for the next character, and backtrack by restoring the 
# cell if the path fails.

# Time Complexity: O(m × n × 4^L) → where L is word length
# Space Complexity: O(L) for recursion stack
