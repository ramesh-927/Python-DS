"""
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
 
Seen this question in a real interview before?
1/5
"""
class Solution:
    def spiralMatrix(self, matrix):
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bottom:
            # Traverse Top row
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            for i in range(top, bottom + 1):    # Traverse right column
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top -1, -1):
                    res. append(matrix[i][left])
                left += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    res = sol.spiralMatrix(matrix)
    print(res)
    
# TimeComplexity: 	O(m × n)	Each element visited once
# SpaceComplexity : O(1)	Output list only (no extra data structures)