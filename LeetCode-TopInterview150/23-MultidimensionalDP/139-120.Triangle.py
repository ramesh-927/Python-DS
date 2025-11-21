"""
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, 
if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:
Input: triangle = [[-10]]
Output: -10
Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""
class Solution:
    def minTotal(self, triangle):

        if not triangle or not triangle[0]:
            return 0
        
        for i in range(len(triangle) -2, -1, -1):
            row = triangle[i]
            next_row = triangle[i + 1]
            for j in range(len(row)):
                row[j] += min(next_row[j], next_row[j + 1])
        return triangle[0][0]

if __name__=="__main__":
    sol = Solution()
    print(sol.minTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))  # Output : 11
    print(sol.minTotal([[-10]]))     # Output : -10

# Time Complexity   :    O(n²)We touch every number exactly once (total numbers ≈ n²/2)
# Space Complexity   :    (extra)O(n)Only one array of size = number of rows
# I’ll solve it with bottom-up DP using O(n) extra space.
#I start from the last row and move upward, at each step updating the minimum path cost to 
# reach the bottom from the current cell, so finally the top cell holds the answer.