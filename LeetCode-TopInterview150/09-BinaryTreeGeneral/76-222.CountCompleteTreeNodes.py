"""
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, 
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.
Example 1:
      1
     / \
    2   3
   / \  /
  4  5 6
Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:
Input: root = []
Output: 0
Example 3:
Input: root = [1]
Output: 1 
Constraints:
The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def left_depth(node: TreeNode) -> int:
            d = 0
            while node:
                d += 1
                node = node.left
            return d

        def right_depth(node: TreeNode) -> int:
            d = 0
            while node:
                d += 1
                node = node.right
            return d

        ld = left_depth(root)
        rd = right_depth(root)

        # If left and right depths equal, it's a perfect tree.
        if ld == rd:
            return (1 << ld) - 1  # 2^ld - 1

        # Otherwise, recursively count left and right.
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    

# Helper to build a tree from list (level-order, use None for missing)
from collections import deque
def build_tree_from_list(values):
    if not values: 
        return None
    it = iter(values)
    root = TreeNode(next(it))
    q = deque([root])
    for val in it:
        node = q[0]
        if node.left is None:
            if val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
        elif node.right is None:
            if val is not None:
                node.right = TreeNode(val)
                q.append(node.right)
            q.popleft()
    return root

# Example usage:
vals = [1,2,3,4,5,6]
root = build_tree_from_list(vals)
print(Solution().countNodes(root))

# Approach	Time complexity	Space complexity
# Brute force (DFS/BFS)	O(n)	O(h) (recursive) / O(n) (BFS queue)
# Optimal (depth checks + recursion)	O((log n)^2)	O(log n) (recursion stack)