"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        last_index = {}

        for i, v in enumerate(nums):
            if v in last_index and i - last_index[v] <= k:
                return True
            last_index[v] = i
        return False

if __name__=="__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
        ([], 0, False),
        ([1,1], 0, False),  # indices must be distinct and |i-j|<=0 means same index -> not allowed
    ]
    for nums, k, expected in tests:
        res_map = sol.containsNearbyDuplicate(nums, k)
        print(f"nums={nums}, k={k} -> map:{res_map}, (expected: {expected})")

# Time Complexity :  O(n)
# Space Complexity : O(d) where d = number of distinct values (≤ n