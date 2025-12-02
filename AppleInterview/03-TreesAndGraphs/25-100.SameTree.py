"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the 
same value.
Example 1:
   1            1
  / \          / \ 
 2   3        2   3
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:
   1     1
  /        \ 
 2           2 
Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:
   1            1
  / \          / \ 
 2   1        1   2
Input: p = [1,2,1], q = [1,1,2]
Output: false
Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__=="__main__":
    # build tree p: [1,2,3]
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    # build tree q: [1,2,3]
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    sol = Solution()
    print(sol.isSameTree(p, q))  # True


# Time Complexity : O(n) — where `n` is the number of nodes compared. In the worst case we visit each 
# node once.                                   
# Space Complexity : O(h) — recursion stack up to tree height `h`. Worst-case `h = n` (skewed tree) 
# so O(n). Best-case balanced tree `h = log₂(n)`.

#I used a synchronized recursive DFS: compare corresponding nodes, return False on mismatch or missing 
# node, otherwise recurse on left and right subtrees. This checks structure and values in a 
# single O(n) traversal with O(h) stack space.
