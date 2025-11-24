"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
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

        counts = defaultdict(int)
        counts[0] = 1
        prefix = 0
        result = 0

        for num in nums:
            prefix += num
            result += counts[prefix - k]
            counts[prefix] += 1
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1,1,1], 2))   # prints 2
    print(sol.subarraySum([1,2,3], 3))   # prints 2


# | Resource |                                 Complexity |
# | -------- | -----------------------------------------: |
# | Time     |           O(n) — single pass through array |
# | Space    | O(n) — hashmap of prefix sums (worst case) |

# We use prefix sums with a hashmap to store frequency of sums seen so far. 
# For each position, we check if (current_sum - k) exists — that means a subarray ending here sums to k.