"""
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the
next node in the list and the left child pointer is always null
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
Example 1:

      1                        1
     / \                        \
    2   5         ==>            2
   / \   \                        \
  3   4   6                        3
                                    \
                                     4
                                      \
                                       5
                                        \
                                         6
                                          \
                                           7
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:
Input: root = []
Output: []
Example 3:
Input: root = [0]
Output: [0]
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
# We are using Recursive (Postorder) Approach
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        def helper(node):
            if not node:
                return None

            left_tail = helper(node.left)
            right_tail = helper(node.right)

            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            # Return the tail of the flattened tree
            return right_tail or left_tail or node

        helper(root)
        
# Build tree
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(5, None, TreeNode(6))

Solution().flatten(root)

# Print flattened tree
cur = root
while cur:
    print(cur.val, end=" -> ")
    cur = cur.right

# Time	 O(n) – each node visited once
# Space	 O(h) – recursion stack (height of tree)