"""
Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. 
You may assume that multiplication is always possible.
Example 1:
A = [[1,0,0],
     [-1,0,3]]
B = [[7,0,0],
     [0,0,0],
     [0,0,1]]
OUTPUT = [[7,0,0],
        [-7,0,3]]
Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output: [[7,0,0],[-7,0,3]]
Example 2:
Input: mat1 = [[0]], mat2 = [[0]]
Output: [[0]]
Constraints:
m == mat1.length
k == mat1[i].length == mat2.length
n == mat2[i].length
1 <= m, n, k <= 100
-100 <= mat1[i][j], mat2[i][j] <= 100
"""
from typing import List

class Solution:
    def multiply(self, mat1, mat2):
        if not mat1 or not mat1[0] or not mat2 or not mat2[0]:
            return []
        
        m, n, p = len(mat1), len(mat1[0]), len(mat2[0])
        
        # Step 1: Initialize result matrix with zeros
        result = [[0] * p for _ in range(m)]
        
        # Step 2: Build sparse representation of mat2 (only non-zero entries)
        mat2_sparse = [[] for _ in range(n)]
        for j in range(n):
            for k in range(p):
                if mat2[j][k] != 0:
                    mat2_sparse[j].append((k, mat2[j][k]))  # (column_index, value)
        
        # Step 3: Multiply using only non-zero elements
        for i in range(m):
            for j in range(n):
                if mat1[i][j] != 0:  # Skip if zero — this is the key optimization!
                    for col, val in mat2_sparse[j]:
                        result[i][col] += mat1[i][j] * val
        
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply([[1,0,0],[-1,0,3]], [[7,0,0],[0,0,0],[0,0,1]]))
    # Output : [[7, 0, 0], [-7, 0, 3]]
    print(sol.multiply([[0]], [[0]]))    # Output : [[0]]

# "Since the matrices are sparse, I avoid the naive triple loop by pre-processing matrix mat2 to store 
# only its non-zero elements per row.
# Then, for every non-zero value in mat1, I only multiply it with the non-zero values from the 
# corresponding row in mat2 — this skips all zero multiplications and runs much faster."

# Time Complexity:
# Naive: O(m × n × p) → too slow for large sparse matrices
# This solution: O(m × n + non_zeros_in_A × avg_non_zeros_per_row_in_B)