"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.
Example 1:
       3
     / \
    9  20
      / \
     15  7
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:
      3
     / \
    9  20
   / \
 15  7
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root):
        result = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum/ float(level_size))
        return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left =  TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    print(Solution().averageOfLevels(root))
# Time Complexity	O(N) → Each node is visited once
# Space Complexity	O(N) → Queue stores max one level of nodes