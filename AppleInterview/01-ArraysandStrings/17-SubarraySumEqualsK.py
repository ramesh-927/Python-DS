"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum 
equals to k.
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
        count = defaultdict(int)   # auto-initializes missing keys to 0
        count[0] = 1               # crucial: handles subarrays starting from index 0
        prefix = 0
        result = 0

        for num in nums:
            prefix += num
            result += count[prefix - k]      # how many times (prefix - k) was seen before?
            count[prefix] += 1            # record current prefix
        return result
    
if __name__== "__main__":
    sol =Solution()
    print(sol.subarraySum([1,1,1], 2))                  # Prints : 2
    print(sol.subarraySum([1,2,3], 3))                  # Prints : 2
    print(sol.subarraySum([3,4,5,-1,-1,2,1], 6))        # Prints : 1

# "O(n) time using prefix sums with a hashmap. I used defaultdict(int) to cleanly count how many times 
# each prefix sum occurred, and check for current_prefix - k on the fly."
# Time Complexity : O(n) → One pass
# Space Complexity : O(n) → Store prefix sums