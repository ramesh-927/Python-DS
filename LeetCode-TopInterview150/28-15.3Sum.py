"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        if n < 3:
            return res

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left, right = i + 1, n - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left_val = nums[left]
                    right_val = nums[right]
                    # skip duplicates for left and right
                    while left < right and nums[left] == left_val:
                        left += 1
                    while left < right and nums[right] == right_val:
                        right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    res = sol.threeSum(nums.copy())   # pass a copy if you want to keep 'nums' unsorted
    print("Input:", nums)
    print("Triplets:", res)
    print("Number of triplets:", len(res))
