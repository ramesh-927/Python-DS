"""
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
     4                           4
   /   \                        / \ 
  2     7          =>          7    2
 / \   / \                    / \  / \ 
1   3 6   9                  9   6 3   1. 
 
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:
     2             2
    / \      =>   / \ 
   1    3       3     1
Input: root = [2,1,3]
Output: [2,3,1]
Example 3:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Build the tree [4,2,7,1,3,6,9]
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(7, TreeNode(6), TreeNode(9))

sol = Solution()
res = sol.invertTree(root)

# The output tree should be [4,7,2,9,6,3,1]
print(res.val)           # 4
print(res.left.val)      # 7
print(res.right.val)     # 2
print(res.left.left.val) # 9

# Time	O(n) — each node is visited once
# Space	O(h) for recursion (O(n) worst-case for skewed tree, O(log n) for balanced)
