"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e.,symmetric around its center).
Example 1:
        1
      /   \
     2     2
    / \   / \
   3  4  4   3
Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:
        1
       /  \
      2     2
      \      \
       3       3
Input: root = [1,2,2,null,3,null,3]
Output: false
Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
Follow up: Could you solve it both recursively and iteratively?
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        return isMirror(root.left, root.right)


# Build the tree:
#        1
#      /   \
#     2     2
#    / \   / \
#   3  4  4   3

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))

sol = Solution()
print(sol.isSymmetric(root))  # Output: True

	
# Time Complexity: 	O(n) — each node is visited once
# Space Complexity: 	O(h) — recursion stack (h = height of tree)
