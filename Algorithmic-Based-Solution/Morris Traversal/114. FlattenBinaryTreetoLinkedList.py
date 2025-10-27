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
# We can flatten in-place using no recursion — just a while loop:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root):
        curr = root

        while curr:
            if curr.left:
                # Find rightmost node of left subtree
                pre = curr.left
                while pre.right:
                    pre = pre.right
                
                pre.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right

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

# Time Complexity : O(n)
# Space Complexity : O(1)