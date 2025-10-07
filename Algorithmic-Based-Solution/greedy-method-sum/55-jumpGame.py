"""
55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

class Solutions:
    def canJump(self, nums):
        max_jump = 0
        for i in range(len(nums)):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + nums[i])
            if i >= len(nums) - 1:
                return True
        return True



sol = Solutions()
nums = [2,3,1,1,4]
nums1 = [3,2,1,0,4]
result = sol.canJump(nums)
result1 = sol.canJump(nums1)

print("Input- 1", result)
print("Input- 2", result1)

# Time Complexity: O(n) – single pass through the array.
# Space Complexity: O(1) – uses only a single variable.

