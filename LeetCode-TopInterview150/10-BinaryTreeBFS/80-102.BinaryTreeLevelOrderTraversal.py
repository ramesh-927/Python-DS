"""
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).
Example 1:
       3
     /   \
    9    20
        /  \
       15   7
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result  = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    sol = Solution()
    print(sol.levelOrder(root))

# Time Complexity:	O(N) — visiting each node once
# Space Complexity:	O(N) — queue stores up to all nodes