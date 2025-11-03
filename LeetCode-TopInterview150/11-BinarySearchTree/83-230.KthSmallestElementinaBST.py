"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Example 1:
root = [3,1,4,null,2], k = 1

        3
       / \
      1   4
       \
        2
Output: 1
Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
        5
      /   \
     3     6
    / \
   2   4
  /
 1
Output: 3
Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        
        while True:
            # Go to the leftmost node
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val 
            # Move to right
            root = root.right

if __name__== "__main__":
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4)), TreeNode(6))
    k = 3
    sol = Solution()
    print(sol.kthSmallest(root, k))

# | Time   | **O(H + k)** where H = tree height |
# | Space  | **O(H)** for stack                 |
