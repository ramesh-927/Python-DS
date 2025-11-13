"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
Follow up: If you have figured out the O(n) solution, try coding another solution using the 
divide and conquer approach, which is more subtle.
"""
class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        max_sum = curr_sum = nums[0]
        for number in nums[1:]:
            curr_sum = max(number, curr_sum + number)
            max_sum = max(max_sum, curr_sum)
        return max_sum

if __name__ == "__main__":
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    out = sol.maxSubArray(nums)
    print(f"The Maxiumm subarray of '{nums}' has the largest sum is :  ",out)

# it's kadane Algorithem .

# Time Compexity : O(n) — one pass through the array.
# Space Complexity: O(1) — only a couple of variables

