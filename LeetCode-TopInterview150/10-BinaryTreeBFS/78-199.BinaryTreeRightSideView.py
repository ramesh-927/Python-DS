"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Explanation:
        1      <---
       / \
      2   3    <----
       \   \
        5   4  <----
Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
Explanation:
        1      <---
       / \
      2   3    <----
    /      
   4         <----
  /
 5       <--------
Example 3:
Input: root = [1,null,3]
Output: [1,3]
Example 4:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if i == size - 1:  # last node of this level
                    result.append(node.val)
                    
        return result
                   
# Example usage:
# Build tree [1,2,3,None,5,None,4]

root = TreeNode(1)
root.left = TreeNode(2, None, TreeNode(5))
root.right = TreeNode(3, None, TreeNode(4))

sol = Solution()
print(sol.rightSideView(root))  # Output: [1, 3, 4]

# Time Complexity:	O(N)
# Space	Complexity: O(N)

