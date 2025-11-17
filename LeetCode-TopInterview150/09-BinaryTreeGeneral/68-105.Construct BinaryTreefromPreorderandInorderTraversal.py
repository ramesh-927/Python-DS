"""
105. Construct Binary Tree from Preorder and Inorder Traversal.
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a 
binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
Example 1:
    3
   / \
  9  20
    /  \
   15   7
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildBinaryTree(self, preorder, inorder):

        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        
        indx_map = {val:idx for idx, val in enumerate(inorder)}   # Build hashmap value -> its index in inorder

        self.pre_idx = 0    # pre_idx will track root position in preorder
        n = len(preorder)

        def helper(in_left, in_right):

            if in_left > in_right:  # if there is no elements to construct subtrees
                return None
            
            # pick up pre_idx element as a root
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)    # build the root node

            root_in_index = indx_map[root_val]   # root splits inorder list into left and right subtrees

            root.left  = helper(in_left, root_in_index - 1)
            root.right  = helper(root_in_index + 1, in_right)

            return root
        return helper(0, n -1)
            

def print_inorder(node):
    if not node:
        return []
    return print_inorder(node.left) + [node.val] + print_inorder(node.right)

preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]

sol = Solution()
root = sol.buildBinaryTree(preorder, inorder)

print(print_inorder(root))  # should print [9, 3, 15, 20, 7]

# TimeComplexity: 	O(n) — each node is created and visited once; hashmap lookups O(1)
# SpaceComplexity: 	O(n) — hashmap + recursion stack (O(n) worst-case)