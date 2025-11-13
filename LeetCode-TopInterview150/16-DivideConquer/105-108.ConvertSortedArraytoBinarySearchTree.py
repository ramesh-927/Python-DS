"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
Example 1:
       0
     /   \
   -3      9
  /       /
-10      5
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also  accepted
       0
     /   \
   -10     5
    \       \
    -3       9
Example 2:
        3   1
       /      \
     1          3
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):

        def helper(left, right):

            if left > right:
                return None 
            
            mid  = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) - 1)
    
# ---------- Helper to print the tree in LeetCode format ----------
from collections import deque

def level_order(root):
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        node = q.popleft()
        if node is None:
            res.append(None)               # keep `null` placeholders
            continue
        res.append(node.val)
        q.append(node.left)
        q.append(node.right)
    # remove trailing None's (LeetCode does not include them)
    while res and res[-1] is None:
        res.pop()
    return res


# -------------------------- Test --------------------------
if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    sol = Solution()
    root = sol.sortedArrayToBST(nums)

    print(level_order(root)) 

# Time Complexity : O(n)
# Space Complexity : O(log n)