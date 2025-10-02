"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
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
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
class Solutions:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [0] * n

        left = 1  # Left products
        for i in range(n):
            ans[i] = left
            left *= nums[i]
        
        right = 1    # Right products (on the fly)
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right  *= nums[i]
        return ans

    
if __name__ == "__main__":
    sol = Solutions()
    nums = [1,2,3,4]
    result = sol.productExceptSelf(nums)
    print(result)

# Edge cases & notes
# Zeros: This approach naturally handles zeros.
# If one zero exists, only the position of that zero will have the product of all non-zero elements; all others will be zero.
# If two or more zeros exist, all outputs are zero.
# Single element: By convention return [1] (product of no other elements = 1).
# Avoid the division-based approach (total_product / nums[i]) — it fails with zeros and is typically disallowed by the problem.

# Complexity
# Time: O(n) (two linear passes)
# Space: O(1) extra (output array excluded by problem statement); overall output is O(n).

# Do a two-pass solution: first pass fill an output array with prefix products (product of elements to the left of each index), 
# second pass traverse right-to-left keeping a running suffix product and multiply it into the output. 
# That yields O(n) time and O(1) extra space and avoids division which fails with zeros."