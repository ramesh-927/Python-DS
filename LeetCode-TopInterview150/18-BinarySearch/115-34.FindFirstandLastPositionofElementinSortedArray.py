"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position 
of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List

class Solution:
    def searchRange(self, nums, target):
        def find_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        left_pos = find_left(nums, target)
        if left_pos == len(nums) or nums[left_pos] != target:
            return [-1, -1]
        
        right_pos = find_left(nums, target + 1) - 1
        return [left_pos, right_pos]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5,7,7,8,8,8,10], 8))  # [3, 5]
    print(sol.searchRange([5,7,7,8,8,8,10], 6))  # [-1, -1]
    print(sol.searchRange([], 0))                # [-1, -1]
    print(sol.searchRange([1], 1))               # [0, 0]


# Time Complexity,O(log n) – two binary searches
# Space Complexity,O(1) – only a few variables

# I reuse the same binary search logic twice: once to find the left boundary, and again to find the 
# right boundary by searching for target + 1. This avoids writing two nearly identical functions.