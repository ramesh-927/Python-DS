"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
         1         1
        / \       / \
       2   3     2   3
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:
       1          1
       /           \
      2             2
Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSameTree(self, p, q):
        # Both are None
        if not p and not q:
            return True
        # One of them is None
        if not p or not q:
            return False
        # Check current node and recurse
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))

# Example usage:

# Case 1
# p = [1,2,3], q = [1,2,3]
p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(3)

q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)

sol = Solution()
print("Case 1")
print("Input: p = [1,2,3], q = [1,2,3]")
print("Output:", sol.isSameTree(p1, q1))
print("Expected: true\n")

# Time Complexity: 	O(N)	Visit each node once
# Space	Complexity: O(H)	Recursive call stack (H = tree height)