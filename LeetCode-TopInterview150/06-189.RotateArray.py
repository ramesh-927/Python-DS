"""
Given an integer array nums, rotate the array to the right  by k steps, where is k is non-negetive.
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
Follow up:
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n   # Step 1

        # helper to reverse array in-place
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1     # <-- moved inside while
                right -= 1    # <-- moved inside while

        # Step 2: reverse whole array
        reverse(0, n - 1)
        # Step 3: reverse first k
        reverse(0, k - 1)
        # Step 4: reverse rest
        reverse(k, n - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    expected = [5, 6, 7, 1, 2, 3, 4]
    sol = Solution()
    sol.rotate(nums, k)
    print("Output")
    print(nums)
    print("Expected")
    print(expected)


# Time Complexity = O(n) → each element is swapped at most twice.
# Space Complexity = O(1) → only a few variables used, done in-place.
