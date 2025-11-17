"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""
class Solution:
    def setZeroes(self, matrix):
        """
        Modifies matrix in-place.
        """
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        first_col_has_zero = False
        # 1) Use first row and first column as markers.
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
            for j in range(1, n):  # start j from 1 to avoid overwriting first col marker
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # 2) Use markers to set inner cells to zero (excluding first row & first column).
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # 3) Zero the first row if needed (matrix[0][0] is row-0 marker)
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        # 4) Zero the first column if needed (tracked separately)
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
if __name__ == "__main__":
    mat = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ]
    Solution().setZeroes(mat)
    print(mat)

# Time	O(m * n) — you scan the matrix a couple of times but only constant number of passes.
# Extra Space	O(1) — in-place markers; only a few boolean variables used