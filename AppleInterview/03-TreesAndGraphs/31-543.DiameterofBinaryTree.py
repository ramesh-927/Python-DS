"""
Docstring for AppleInterview.03-TreesAndGraphs.31-543.DiameterofBinaryTree
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
Example 1:
#      1
#     / \ 
#    2   3
#   / \ 
#  4    5
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:
Input: root = [1,2]
Output: 1
Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            # update diameter
            self.ans = max(self.ans, left + right)
            # return height
            return 1 + max(left, right)

        dfs(root)
        return self.ans
    
# I used a single post-order DFS that computes subtree heights while tracking the maximum diameter 
# using a class variable.
# At each node, the diameter candidate is left_height + right_height, and we return the actual height 
# upward — all in O(n) time.
    
# Time Complexity: O(n), where n is the number of nodes (visits each node once). This is the best 
# possible, as we must check every node.
# Space Complexity: O(h), where h is the tree height (due to recursion; worst-case O(n) for skewed 
# trees).