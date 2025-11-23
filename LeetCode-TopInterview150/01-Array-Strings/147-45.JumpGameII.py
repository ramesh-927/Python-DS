"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, 
if you are at index i, you can jump to any index (i + j) where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that 
you can reach index n - 1.
Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, 
then 3 steps to the last index.
Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""
class Solution:
    def jump(self, nums):

        n = len(nums)
        if n < 1:
            return 0
        
        jumps = 0
        curr_end = 0   # where the current jump range ends
        farthest = 0   # farthest we can reach so far

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            # When we reach the end of current jump range
            if i == curr_end:
                jumps += 1
                curr_end = farthest   # update range to new farthest

                # If we can already reach the end, stop early
                if curr_end >= n - 1:
                    break
        return jumps

if __name__=="__main__":
    sol = Solution()
    print(sol.jump([2,3,1,1,4]))     # → 2
    print(sol.jump([2,3,0,1,4]))     # → 2
    print(sol.jump([1,1,1,1]))       # → 3
    print(sol.jump([5,0,0,0,0]))     # → 1

# We use a greedy approach: track the farthest we can reach. Each time we finish a jump's range, 
# we make one jump to the farthest point possible within current reach. 
# This gives minimum jumps in O(n) time.

# Time Complexity: O(n)
# Space Complexity: O(1)
