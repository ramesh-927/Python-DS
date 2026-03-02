"""
Docstring for LeetCode396questions-Apple.01-1.TwoSum

Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element 
twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
class Solution:
    def twoSum(self, nums, target):
        char_set = {}

        for i, num in enumerate(nums):
            complment = target - num

            if complment in char_set:
                return [char_set[complment], i]
            char_set[num] = i
        return ValueError("Indexes Num not Found!")

if __name__== "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))        # [0, 1]
    print(sol.twoSum([3,2,4], 6))            # [1, 2]
    print(sol.twoSum([3,3], 6))              # [0, 1]


# Time complexity  :        O(n) — single pass through the array 
# Space complexity :     O(n) — extra dictionary storing seen values 

# The smarter way is like keeping a quick-reference notebook as you go through the list. You use a 
# "dictionary" (a simple lookup table in Python) to remember each number you've seen and where it was. 
# For each new number, you first check if the "missing piece" (target minus this number) is already in 
# your notebook. If yes, you've found the pair—return their positions. If not, add the current number 
# and its position to the notebook.

# I used a one-pass hash map: store seen values → indices and for each element check if the complement 
# target - num exists. This gives O(n) time and O(n) space with a single traversal.
