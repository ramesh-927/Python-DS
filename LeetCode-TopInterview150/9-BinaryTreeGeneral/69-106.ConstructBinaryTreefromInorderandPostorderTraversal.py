"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a 
binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
Example 1:
    3
   / \
  9  20
    /  \
   15   7
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
Constraints:
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder or len(inorder) != len(postorder):
            return None

        # Map from value -> index in inorder
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        # Use a mutable integer (list) so nested function can modify it
        post_idx = [len(postorder) - 1]

        def build(left, right):
            # build subtree from inorder[left:right] inclusive
            if left > right:
                return None

            root_val = postorder[post_idx[0]]
            post_idx[0] -= 1
            root = TreeNode(root_val)

            # index of root in inorder
            in_index = idx_map[root_val]

            # Important: build right subtree first
            root.right = build(in_index + 1, right)
            root.left = build(left, in_index - 1)
            return root

        return build(0, len(inorder) - 1)
# Helper to print preorder traversal for verification
def preorder_traversal(root):
    res = []
    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res

# Example usage
if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    sol = Solution()
    root = sol.buildTree(inorder, postorder)
    print("Preorder of constructed tree:", preorder_traversal(root))
    # Expected: [3, 9, 20, 15, 7]

# Time Complexity	O(n) — each node is created once, hashmap guarantees O(1) splits
# Space Complexity	O(n) — hashmap + recursion stack (O(n) worst-case for skewed tree)