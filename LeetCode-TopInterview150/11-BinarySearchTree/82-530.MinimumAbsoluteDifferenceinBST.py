"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the 
values of any two different nodes in the tree.
Example 1:
    4
   / \
  2   6
 / \
1   3
Input: root = [4,2,6,1,3]
Output: 1
    1
   / \
  0   48
      / \
    12   49
Input: root = [1,0,48,null,null,12,49]
Output: 1
Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
"""
# Definition for a binary tree node (LeetCode style).
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                # node.val and self.prev are ints; subtraction safe
                diff = node.val - self.prev
                if diff < self.min_diff:
                    self.min_diff = diff
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return int(self.min_diff) 
if __name__ == "__main__":
    root = TreeNode(4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(6))
    sol = Solution()
    print(sol.getMinimumDifference(root))
