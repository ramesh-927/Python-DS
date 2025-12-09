"""
You are given the root of a binary tree.
A ZigZag path for a binary tree is defined as follow:
1. Choose any node in the binary tree and a direction (right or left).
2. If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
3. Change the direction from right to left or from left to right.
4. Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
Return the longest ZigZag path contained in that tree.
Example 1:
       1
        \
         1
        / \
       1   1
           / \
          1    1
          \
           1
            \
             1
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:
         1
        / \
       1   1
      / \  
     1   1   
      \  
       1
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:
Input: root = [1]
Output: 0
Constraints:
The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.res = 0  # Global max length (edges)
        
        def dfs(node):
            if not node:
                return -1, -1  # For math: 1 + (-1) = 0 if no child
            left = dfs(node.left)
            right = dfs(node.right)
            # Max starting left: 1 + left child's max starting right
            start_left = 1 + left[1]
            # Max starting right: 1 + right child's max starting left
            start_right = 1 + right[0]
            # Update global max
            self.res = max(self.res, start_left, start_right)
            # Return maxes for this node
            return start_left, start_right
        
        dfs(root)
        return self.res
    
# Time Compleixty: O(n) — visit each node once 
# Space Complexity:  O(h) — recursion stack, where h is tree height (O(n) worst-case, 
# O(log n) average for balanced tree) 

# We do a single DFS returning the longest ZigZag starting-left and starting-right for each node; 
# each node’s values are computed from its children (start_left = 1 + child.start_right, etc.). 
# This yields O(n) time and O(h) space and updates a global maximum during traversal