"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
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
        hmap = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in hmap:
                return [hmap[diff], i]
            hmap[val] = i

if __name__== "__main__":
    sol = Solution()
    nums = [2,7,11,15] 
    target = 9
    res = sol.twoSum(nums, target)
    print(res)

# Time Complexity
# O(n) – The algorithm iterates through the input array of size n once. 
# Inside the loop, it performs a constant-time lookup in a hash table (or dictionary) to check for the complement. 
# Inserting an element into the hash table also takes constant time on average. 
# Therefore, the dominant operation is the single pass through the array, resulting in a time complexity of O(n).
# Space Complexity
# O(N) – The provided algorithm uses a lookup tool, which can be implemented using a hash map or dictionary. 
# This data structure stores each number encountered in the input list along with its index. 
# In the worst-case scenario, where no two numbers sum up to the target, the hash map will store all N numbers from the input list. 
# Therefore, the auxiliary space required grows linearly with the input size N, leading to a space complexity of O(N).
