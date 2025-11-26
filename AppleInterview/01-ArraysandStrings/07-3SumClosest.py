"""
Given an integer array nums of length n and an integer target,find three integers in nums such that 
the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
Constraints:
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closest - target):
                    closest = total
                
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return target
        return closest

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # Output : 2
    print(sol.threeSumClosest([0,0,0], 1))        # Output : 0


# Time Complexity :  O(n²)
# Space Complexity :  O(1)
# I sort the array first, then for each element, I use two pointers to find the best pair that, 
# together with the current element, gives a sum closest to the target.
# This reduces the problem from O(n³) brute force to O(n²) time — which is optimal