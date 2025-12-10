"""
Docstring for AppleInterview.001-AppleSpring23HighFrequency.09-53.MaximumSubarray
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
    def findMaxSubArray(self, nums):

        current_sum = max_sum =nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxSubArray([-2,1,-3,4,-1,2,1,-5,4]))     # prints : 6
    print(sol.findMaxSubArray([1]))                         # pritns : 1
    print(sol.findMaxSubArray([5,4,-1,7,8]))                # prints : 23

# Another Solution Divde & Concur
def maxSubArray_divide_conquer(nums):
    def helper(left, right):
        if left > right:
            return float('-inf')
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        
        # Case 1 & 2: max in left or right half
        left_max = helper(left, mid)
        right_max = helper(mid + 1, right)
        
        # Case 3: crosses the midpoint
        # Max suffix sum on left side
        left_suffix = curr = nums[mid]
        for i in range(mid - 1, left - 1, -1):
            curr += nums[i]
            left_suffix = max(left_suffix, curr)
        
        # Max prefix sum on right side
        right_prefix = curr = nums[mid + 1]
        for i in range(mid + 2, right + 1):
            curr += nums[i]
            right_prefix = max(right_prefix, curr)
        
        cross_max = left_suffix + right_prefix
        
        return max(left_max, right_max, cross_max)
    
    return helper(0, len(nums) - 1)
    
    # Kadane's Algorithm : -
        # Time Compleixty :  O(n) 
        # Space Complexity : O(1) Optimal, most commonly used
        
    # Divide & Conquer : - 
        # Time Complexity : O(n log n)
        # Sapce Complexity :  O(log n) Elegant, good for interviews