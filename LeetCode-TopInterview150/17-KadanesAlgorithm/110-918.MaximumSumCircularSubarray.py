"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray 
of nums.
A circular array means the end of the array connects to the beginning of the array. Formally, the next
element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray 
nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
Constraints:
n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""
class Solution:
    def maxSubarraySumCircular(self, nums):
        # Kadane for max and min subarray sum
        max_sum = min_sum = nums[0]
        max_curr = min_curr = nums[0]
        total = nums[0]
        
        for num in nums[1:]:
            total += num
            
            # Max Kadane
            max_curr = max(num, max_curr + num)
            max_sum = max(max_sum, max_curr)
            
            # Min Kadane
            min_curr = min(num, min_curr + num)
            min_sum = min(min_sum, min_curr)
        
        # If all numbers are negative, return the max element
        if total == min_sum:
            return max_sum
        
        # Otherwise, return max of (non-circular, circular)
        return max(max_sum, total - min_sum)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubarraySumCircular([1,-2,3,-2])) 
    print(sol.maxSubarraySumCircular([5,-3,5]))    
    print(sol.maxSubarraySumCircular([-3,-2,-3]))   

# How the Code Works (Step-by-Step)
# Case 1: Normal max sum
# Use Kadane’s Algorithm to find the best group without wrapping.
# Case 2: Wrapping max sum
# Trick:Best wrapping sum = Total sum − Smallest group in the middle

# Time Complexity: O(n)
# Space Complexity: O(1)


        



