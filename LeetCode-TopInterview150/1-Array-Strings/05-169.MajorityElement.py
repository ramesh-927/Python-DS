"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""
class Solutions(object):
    def majorityElement(self, nums):
        major_ele = 0
        count = 0
        for num in nums:
            if count == 0:
                major_ele = num
            if num == major_ele:
                count += 1
            else:
                count -= 1
        return major_ele
if __name__ == "__main__":
    sol = Solutions()
    nums = [2, 2, 1, 1, 1, 2, 2]
    res = sol.majorityElement(nums)
    print("Input:", nums)
    print("Output:", res) 

# Complexity
# Time: O(n) (single pass).
# Space: O(1) (constant extra variables).