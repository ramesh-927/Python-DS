"""
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
1   2   3
4   5   6
7   8   9
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
1   2   3   4
5   6   7   8
9   10  11  12
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

"""
class Solution:
    def spiralMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return []
    
        result = []
        while matrix:
            # 1. Take the first row
            result += matrix.pop(0)
        
            # 2. Take the right column (only if still rows left)
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
        
            # 3. Take the bottom row (if still rows)
            if matrix:
                result += matrix.pop()[::-1]
        
            # 4. Take the left column upwards (if still rows and columns)
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
    
        return result

if __name__=="__main__":
    sol = Solution()
    print(sol.spiralMatrix([[1,2,3],[4,5,6],[7,8,9]])) 
                                # prints  [1,2,3,6,9,8,7,4,5]
    print(sol.spiralMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
                                # prints  [1,2,3,4,8,12,11,10,9,5,6,7]

# Time Complexity: O(m × n) — visits each cell exactly once
# Space Complexity: O(1) — excluding the output array

# I simulate the spiral by repeatedly removing and appending the outer layers: first row, then right 
# column, then bottom row reversed, then left column upwards — using pop() to shrink the matrix naturally.
    

