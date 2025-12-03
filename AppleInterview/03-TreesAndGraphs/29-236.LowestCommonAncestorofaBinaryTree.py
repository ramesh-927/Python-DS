"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two 
nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to 
be a descendant of itself).”
Example 1:
#      3
#     / \ 
#    5   1
#   / \ / \ 
#  6  2 0  8
#    / \ 
#   7   4
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:
#      3
#     / \ 
#    5   1
#   / \ / \ 
#  6  2 0  8
#    / \ 
#   7   4
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p , q)

        if left  and right:
            return root
        
        return left or right

if __name__== "__main__":
    # Tree: [3,5,1,6,2,0,8,null,null,7,4]
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    sol = Solution()
    p = root.left    # node with val 5
    q = root.right   # node with val 1
    print(sol.lowestCommonAncestor(root, p, q).val)

# Time Complexity: O(n), where n is the number of nodes—we visit each node exactly once.
# Space Complexity: O(h), where h is the tree height (worst case O(n) for a skewed tree, but usually 
# closer to O(log n) for balanced trees).

# I used a recursive DFS approach to traverse the tree post-order. We check if p and q are in different 
# subtrees of the current node—if yes, it's the LCA; otherwise, propagate the result from the subtree 
# containing both.



