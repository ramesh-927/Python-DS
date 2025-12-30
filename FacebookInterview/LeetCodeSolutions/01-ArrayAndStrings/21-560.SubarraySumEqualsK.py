"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.21-560.SubarraySumEqualsK

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals 
to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
from collections import defaultdict
class Solution:
   def subarraySum(self, nums, k):
        
        count = 0
        prefix_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1              # For subarrays starting from index 0

        for num in nums:
            prefix_sum += num
            count += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] += 1
        return count
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1,1,1], 2))
    print(sol.subarraySum([1,2,3], 3))

# For problems counting subarrays (or substrings) with a specific sum/property, the best go-to algorithm 
# is prefix sums combined with a hashmap. It turns the sum check into a quick lookup, reducing time from 
# O(n^2) to O(n). Use it when the array can have negatives (no two-pointers or sliding windows work reliably 
# then). If no negatives, consider sliding window for optimization, but hashmap is more general.

# I used a prefix sum approach with a hashmap to efficiently count subarrays summing to k. By tracking 
# frequencies of prefix sums in O(n) time, we instantly find matches for each position without nested 
# loops.

# Time Complexity: O(n) — one pass through the array
# Space Complexity: O(n) — for storing prefix sums in hash map

# Bruteforce Approach
#  n = len(nums)
#  count = 0
# for i in range(n):
# current_sum = 0
# for j in range(i, n):
# current_sum += nums[j]
# if current_sum == k:
# count += 1