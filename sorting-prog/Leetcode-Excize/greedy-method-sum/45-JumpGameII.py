"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1]. 

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""
class Solutions:
    def jumpGame(self, nums):
        result  = 0
        max_jump = 0
        next_jump = 0

        for i in range(len(nums) - 1):
            next_jump = max(next_jump, i + nums[i])
            if i == max_jump:
                result += 1
                max_jump = next_jump
        return result


    
sol = Solutions()
nums = [2,3,1,1,4]
res = sol.jumpGame(nums)
nums1 = [2,3,0,1,4]
res1 = sol.jumpGame(nums1)

print("Input- 1", res)
print("Input- 2", res1)

# Time Complexity: O(n) – single pass through the array.
# Space Complexity: O(1) – constant extra space.