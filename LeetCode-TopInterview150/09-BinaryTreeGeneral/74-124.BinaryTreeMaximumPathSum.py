"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
Example 1:
             1
            / \
           2   3
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:
                -10
                / \
               9  20
                   / \
                   15 7

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
Constraints:
The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self,root):
        self.max_sum = -10**18

        def max_gain(node):
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            price_newpath = node.val + left_gain + right_gain

            if price_newpath >  self.max_sum:
                self.max_sum = price_newpath
            return node.val + max(left_gain, right_gain)
        max_gain(root)
        return self.max_sum

# build tree [1,2,3]
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().maxPathSum(root))  # 6

# build tree [-10,9,20,null,null,15,7]
root = TreeNode(-10,
                TreeNode(9),
                TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().maxPathSum(root))  # 42

# Time Compelxity:	O(N) — visit each node exactly once
# Space Complexity: 	O(H) recursion stack / call depth (H = height of tree). 
# Worst-case O(N) for skewed tree, average O(log N) for balanced tree
