"""
Docstring for AppleInterview.05-SortingAndSearching.39-33.SearchinRotatedSortedArray

There is an integer array nums sorted in ascending order (with distinct values)
Prior to being passed to your function, nums is possibly left rotated at an unknown index 
k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], 
nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 
indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if 
it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:
Input: nums = [1], target = 0
Output: -1
Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
        
            # Left half is sorted
            if nums[l] <= nums[mid]:
                # target is in the left sorted half?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right half is sorted
            else:
                # target is in the right sorted half?
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__== "__main__":
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2], 0))     # pirnts : 4
    print(sol.search([4,5,6,7,0,1,2], 3))    # pirnts : -1

# We use a modified binary search. At each step at least one half of the array is guaranteed to be 
# sorted, so we determine which half is sorted and decide whether the target can be in that 
# half – if not, we discard it and continue on the other half. This keeps O(log n) time.

# Time Complexity : O(log n)
# Space Complexity : O(1) space

