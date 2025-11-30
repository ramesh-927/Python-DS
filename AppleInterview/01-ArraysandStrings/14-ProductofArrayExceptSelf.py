"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all 
the elements of nums except nums[i].
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
Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
"""
class Solution:
    def productExceptSelf(self, nums):

        n = len(nums)
        result = [1] * n

        left_product = 1
        for x in range(n):
            result[x] = left_product
            left_product *= nums[x]
        
        right_product = 1
        for x in range(n -1, -1, -1):
            result[x] *= right_product
            right_product *= nums[x]
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))      # Prints : [24, 12, 8, 6]
    print(sol.productExceptSelf([-1,1,0,-3,3]))   # Prints : [0, 0, 9, 0, 0]

# "I used the two-pass prefix product approach — first compute the product of all elements to the 
# left and store it in the result array, then in a reverse pass multiply by the running product from 
# the right. This gives O(n) time and O(1) extra space without using division."

# Time Complexity : O(n) 
# Space Complexity : O(1)
