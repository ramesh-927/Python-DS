"""
Docstring for LeetCode-Easy.Arrarys.01-485.MaxConsecutiveOnes
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = current_count = 0
        
        for num in nums:
            current_count = current_count + 1 if num == 1 else 0
            max_count = max(max_count, current_count)
            max_count += 1
        return max_count

if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1]
    solution = Solution()
    print(solution.findMaxConsecutiveOnes(nums))

        