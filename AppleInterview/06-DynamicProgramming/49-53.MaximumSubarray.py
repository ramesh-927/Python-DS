"""
Docstring for AppleInterview.06-DynamicProgramming.49-53.MaximumSubarray
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
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and 
conquer approach, which is more subtle.
"""
class Solution:
    def maxSubArray(self, nums):

        max_sum = current_sum = nums[0]  # Start with the first element

        for num in nums[1:]:  # Loop through the rest
            current_sum = max(num, current_sum + num)    # Reset if negative streak
            max_sum = max(max_sum, current_sum)
        return max_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))      # Output : 6
    print(sol.maxSubArray([1]))                         # Output : 1
    print(sol.maxSubArray([5,4,-1,7,8]))               # Output: 23

# Time Complexity: O(n) – We loop through the array once.
# Space Complexity: O(1) – No extra space beyond a couple of variables.

# I used Kadane's algorithm to solve this in O(n) time. It tracks the current subarray sum, resetting 
# it to the current element if it goes negative, while updating the maximum sum found so far.