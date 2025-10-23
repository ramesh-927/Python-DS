"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node 
down to the farthest leaf node.
Example 1:
       3
      / \
     9   20
         / \
        15  7
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:
Input: root = [1,null,2]
Output: 2 
Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self,root):
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
sol = Solution()
print(sol.maxDepth(root)) 


# Time Complexity:	Visits every node once-----	O(N)
# Space Complexity:	Recursion stack height = tree height---	O(H) (worst O(N) for skewed tree)
