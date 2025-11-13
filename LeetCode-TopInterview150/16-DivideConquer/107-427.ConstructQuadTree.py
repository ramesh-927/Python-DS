"""
Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.
Return the root of the Quad-Tree representing grid.
A Quad-Tree is a tree data structure in which each internal node has exactly four children. 
Besides, each node has two attributes:
val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. 
Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:
1. If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the 
value of the grid and set the four children to Null and stop.
2. If the current grid has different values, set isLeaf to False and set val to any value and divide the 
current grid into four sub-grids as shown in the photo.
3. Recurse for each of the children with the proper sub-grid.
If you want to know more about the Quad-Tree, you can refer to the wiki.
Quad-Tree format:
You don't need to read this section for solving the problem. This is only if you want to understand 
the output format here. The output represents the serialized format of a Quad-Tree using level order 
traversal, where null signifies a path terminator where no node exists below.
It is very similar to the serialization of the binary tree. The only difference is that the node is 
represented as a list [isLeaf, val].
If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value 
of isLeaf or val is False we represent it as 0.
If you want to know more about the Quad-Tree, you can refer to the wiki.
Example 1:
0  1
1  0
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.
Example 2:
1   1   1   1   0   0   0   0
1   1   1   1   0   0   0   0
1   1   1   1   1   1   1   1
1   1   1   1   1   1   1   1
1   1   1   1   0   0   0   0
1   1   1   1   0   0   0   0
1   1   1   1   0   0   0   0
1   1   1   1   0   0   0   0
Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:
Constraints:
n == grid.length == grid[i].length
n == 2x where 0 <= x <= 6
"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isleaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
class Solution:
    def construct(self, grid):
        def build(x1, y1, x2, y2):
            # Base case: if all values are the same
            total = sum(grid[i][j] for i in range(x1, x2) for j in range(y1, y2))
            if total == 0 or total == (x2 - x1) * (y2 - y1):
                return Node(total > 0, True, None, None, None, None)
            
            # Not all same → split into 4 quadrants
            mx, my = (x1 + x2) // 2, (y1 + y2) // 2
            return Node(
                True, False,
                build(x1, y1, mx, my),   # top-left
                build(x1, my, mx, y2),   # top-right
                build(mx, y1, x2, my),   # bottom-left
                build(mx, my, x2, y2)    # bottom-right
            )

        return build(0, 0, len(grid), len(grid))
# Time Complexity: O(n²)
# We visit each cell at most 4 times (once per level in the quadtree).
# Total nodes in quadtree ≤ 4n²/3 → still O(n²).

# Space Complexity: O(n²)
# Worst case: quadtree has O(n²) nodes (e.g., checkerboard pattern).