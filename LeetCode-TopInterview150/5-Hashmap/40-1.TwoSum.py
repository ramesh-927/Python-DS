"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists. 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
class Solution:
    def twoSum(self, nums, target):

        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 7, 11, 15], 9),      # [0, 1]
        ([3, 2, 4], 6),           # [1, 2]
        ([3, 3], 6),              # [0, 1]
        ([1, 5, 1, 5], 10),       # [1, 3]
    ]
    for nums, target in tests:
        res = sol.twoSum(nums, target)
        print(f"{nums}  -> target = {target} : {res}")

# Time Complexity :	O(n)	- Each element visited once
# Space Complexity :	O(n) - Hash map stores up to n elements
 