"""
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
Example 1:
[
  [1, 3, 5, 7],
  [10,11,16,20],
  [23,30,34,60]
]
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:
[
  [1, 3, 5, 7],
  [10,11,16,20],
  [23,30,34,60]
]
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
class Solution:
    def searchMatrix(self, matrix, target):
        
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left = 0 
        right = m * n  - 1

        while left <= right:
            mid = (left + right) // 2
            row  = mid // n
            col = mid % n
            val = matrix[row][col]

            if val == target:
                return True
            if val < target:
                left = left + 1
            else:
                right = right - 1
        return left

if __name__ == "__main__":
    matrix  = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print("Input: matrix =", matrix, ", target =", target)
    print("Output:", Solution().searchMatrix(matrix, target))

# | Approach      | Time            | Space    |
# | ------------- | --------------- | -------- |
# | Binary Search | **O(log(m·n))** | **O(1)** |

# Use binary search. At each mid, determine which half is sorted and whether target lies in it. Shrink search space accordingly.