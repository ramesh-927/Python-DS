"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], 
nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        n = len(nums)
    
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:    # skip duplicates
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # skip duplicates
                    continue
                
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res
    
if __name__ =="__main__":
    sol = Solution()
    print(sol.fourSum([1,0,-1,0,-2,2], 0))   # prints : [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    print(sol.fourSum([2,2,2,2,2], 8))     # prints :[[2,2,2,2]]

# Time Complexity: O(n³) → best possible for this problem
# Space Complexity: O(1) → ignoring output and sorting space

# I used the classic two-pointer approach after sorting, with two nested loops for the first 
# two elements and two pointers for the last two — this gives O(n³) time.
# I skipped duplicates at each level to avoid repeated quadruplets, which is crucial for correctness 
# and efficiency.

