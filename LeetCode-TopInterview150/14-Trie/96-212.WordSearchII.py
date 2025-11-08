"""
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally 
or vertically neighboring. The same letter cell may not be used more than once in a word.
Example 1:
Input: board = [["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]] 
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
class Solution:
    def findWords(self, board, words):
        root = {}
        
        # Build Trie
        for w in words:
            node = root
            for c in w:
                node = node.setdefault(c, {})
            node['#'] = w  # word end marker
            
        res = []
        rows, cols = len(board), len(board[0])
        
        def dfs(i, j, node):
            c = board[i][j]
            if c not in node:
                return
            
            nxt = node[c]
            if "#" in nxt:
                res.append(nxt["#"])
                del nxt["#"]      # avoid duplicates
            
            board[i][j] = None  # mark visited
            
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                x, y = i + di, j + dj
                if 0 <= x < rows and 0 <= y < cols and board[x][y] is not None:
                    dfs(x, y, nxt)
            
            board[i][j] = c  # restore
            
            if not nxt:      # prune
                node.pop(c)
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)     
        return res
    
if __name__ == "__main__":
    board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
    words = ["oath","pea","eat","rain"]

    sol = Solution()
    print(sol.findWords(board, words))  # -> ["oath","eat"] (order may vary)
# | Item                      |       Complexity |                                                                            
# | ------------------------- | -----------------|
# | Time (build trie)         |           `O(S)` |                                                                                                       
# | Time (search worst-case)  | `O(m * n * 4^L)` | 
# | Space (trie)              |           `O(S)` |                                                                             
# | Space (recursion/visited) |           `O(L)` |
