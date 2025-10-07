class Solution:
    def move_zeros(self, nums):
        non_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1

sol = Solution()
nums = [1,3,0,12,0, 3, 1]
sol.move_zeros(nums)

print(nums)