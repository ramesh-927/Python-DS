"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]
Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

class Solutions:
    def moveZeros(self, nums):
        non_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero],nums[i] = nums[i], nums[non_zero]
                non_zero += 1
        return []

sol = Solutions()
s1 = [0,1,0,3,12]
s2 = [5,0,6]

input1 = sol.moveZeros(s1)
print("S1=", s1)

input2 = sol.moveZeros(s2)
print("S2= ", s2)