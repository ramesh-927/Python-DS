"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
class Solution:
    def lengthOfLIS(self, nums):
        # tails[i] = smallest tail of all increasing subsequences with length i+1
        tails = []

        for num in nums:
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num
        return len(tails)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))  # -> 4
    print(sol.lengthOfLIS([0,1,0,3,2,3]))  # -> 4
    print(sol.lengthOfLIS([7,7,7,7,7,7,7]))  # -> 1

# Solution,Time,Space,When to Use
# DP O(n²),O(n²),O(n),"Simple, easy to explain"
# Binary Search O(n log n),O(n log n),O(n),Best choice for interviews

# def lengthOfLIS(nums: list[int]) -> int:
#   if not nums:
#        return 0
    
#    dp = [1] * len(nums)              # dp[i] = length of LIS ending at i
    
#    for i in range(1, len(nums)):
#        for j in range(i):
#            if nums[j] < nums[i]:
#                dp[i] = max(dp[i], dp[j] + 1)
    
#    return max(dp)