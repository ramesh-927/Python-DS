"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.
Example 1:
_  Q  _  _                 _  _  Q  _
_  _  _  Q                 Q  _  _  _
Q  _  _  _      =>         _  _  _  Q
_  _  Q  _                 _  Q  _  _

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:
Input: n = 1
Output: 1
"""
class Solution:
    def totalNQueens(self, n):
        def backtrack(row, cols, daig1, daig2):
            if row == n:
                return 1    # Found a valid way
            count = 0
            for c in range(n):
                if c in cols or (row - c) in daig1 or (row + c) in daig2:
                    continue     # Not safe
                # Place queen
                cols.add(c)
                daig1.add(row - c)
                daig2.add(row + c)

                # Go to next row
                count += backtrack(row + 1, cols, daig1, daig2)

                # Remove queen (backtrack)
                cols.remove(c)
                daig1.remove(row - c)
                daig2.remove(row + c)
            return count
        return backtrack(0, set(), set(), set())
    
if __name__ == "__main__":
    sol = Solution()
    n = 4
    for n in [1, 4, 5, 8]:
        out = sol.totalNQueens(n)
        print(f"Placing {n}-queens on a {n}×{n} board → {out} ways")

    # Time: O(N!), which is optimal since we must explore all configurations.
    # Space: O(N) for recursion and sets."
