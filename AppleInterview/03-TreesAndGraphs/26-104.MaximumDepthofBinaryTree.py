"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to 
the farthest leaf node.
Example 1:
    3
   / \
  9  20
    /  \
   15   7
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
    def maxDepth(self, root):

        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
if __name__ =="__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
    root1 = TreeNode(1, TreeNode(2))
    sol = Solution()
    print(sol.maxDepth(root))  # output: 3
    print(sol.maxDepth(root1))  # output: 2

# Time complexity :  O(n) — we visit each node once 
# Space complexity : O(h) — recursion call stack, where h is tree height (worst-case O(n) for a chain)

# I used recursive DFS because finding the maximum depth of a tree is naturally recursive:
# the depth of a node is 1 + the maximum depth of its left and right subtrees.
# Base case: empty node has depth 0. This is O(n) time and very clean.
