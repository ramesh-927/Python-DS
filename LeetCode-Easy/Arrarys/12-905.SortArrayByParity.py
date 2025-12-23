"""
Docstring for LeetCode-Easy.Arrarys.12-905.SortArrayByParity
Given an integer array nums, move all the even integers at the beginning of the array followed by 
all the odd integers.
Return any array that satisfies this condition.
Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:
Input: nums = [0]
Output: [0]
Constraints:
1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""
class Solution:
    def sortByParity(self, nums):

        left = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
    
if __name__== "__main__":
    sol = Solution()
    print(sol.sortByParity([3,1,2,4]))        # 2, 4, 3, 1]
    print(sol.sortByParity([0]))              # [0]

# Time Complexity : O(n) – single pass through the array.
# Space Complexity : O(1) – only uses a few variables.

# I used a two-pointer approach to solve this in-place in O(n) time and O(1) space. I maintained a 
# 'left' pointer starting at index 0, which represents the position where the next even number should 
# be placed. I iterated through the array with a 'right' pointer from 0 to n-1. Whenever I encounter 
# an even number at the right pointer, I swap it with the element at the left pointer and increment 
# the left pointer. This way, all even numbers naturally move to the left side, and odds get pushed 
# to the right.Since we only do a single pass and constant extra space, it's optimal.