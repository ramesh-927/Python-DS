"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.18-283.MoveZeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order 
of the non-zero elements.
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
class Solution:
    def moveZeroes(self, nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums
 
if __name__ == "__main__":
    sol = Solution()
    print(sol.moveZeroes([0,1,0,3,12]))         # [1, 3, 12, 0, 0]
    print(sol.moveZeroes([0]))                  # [0]
    print(sol.moveZeroes([0,1,5,0,7,0,0,9]))    # [1, 5, 7, 9, 0, 0, 0, 0]

# Time Complexity: O(n) – We loop through the array once with the right pointer, and swaps happen 
# at most n times (but still linear).
# Space Complexity: O(1) – No extra space beyond a couple of variables.

# For this kind of problem (rearranging elements in an array based on a condition, like moving 
# zeros or sorting colors), the two-pointer technique is the best algorithm to choose. It works 
# by separating the array into "processed" (left side: non-zeros) and "unprocessed" (right side: 
# scanning) sections, like herding sheep into one corner of a field while scanning the whole 
# area.

# I used the two-pointer technique: One pointer tracks the next position for non-zero elements, 
# and as we iterate with the second pointer, we swap non-zeros to the front, effectively moving 
# zeros to the end in O(n) time with O(1) space.