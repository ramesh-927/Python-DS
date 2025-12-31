"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.16-238.ProductofArrayExceptSelf

Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not 
count as extra space for space complexity analysis.)
"""
class Solution:
    def productOfArray(self, nums):
        n = len(nums)
        result = [1] * n

        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for j in range(n - 1, -1, -1):
            result[j] *= right_product
            right_product *= nums[j]
        return result
    
if __name__== "__main__":
    sol = Solution()
    print(sol.productOfArray([1,2,3,4]))        # [24, 12, 8, 6]
    print(sol.productOfArray([-1,1,0,-3,3]))    # [0, 0, 9, 0, 0]

# Time Complexity: O(n) – we pass through the array twice (once left, once right), which is 
# fast and linear.
# Space Complexity: O(1) extra space (ignoring output) – we reuse the answer list and one 
# variable.
# No division means it handles zeros perfectly without special checks. Minimal code: just two 
# loops, no extra arrays. For "product except self" or similar "all except one" computations 
# in arrays (e.g., sum except self), always go for prefix/suffix accumulation. It's efficient 
# because it builds running totals/products in one pass each direction, avoiding redundant 
# calculations. Choose it when you need O(n) time without division, especially with constraints 
# like zeros or large inputs

# I used the prefix and suffix product method, where I first compute cumulative products from 
# the left into the output array, then multiply each by cumulative products from the right 
# using a single variable.This achieves O(n) time and O(1) extra space by reusing the output 
# and avoiding division.