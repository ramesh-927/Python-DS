"""
Docstring for FacebookInterview.LeetCodeSolutions.05-SearchingOrSorting.51-34.FindFirstandLastPositionofElementinSortedArray

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position 
of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
class Solution:
    def findFirstLastPostion(self, nums, target):

        def binarySearch(first_pos):

            left, right = 0 , len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    index = mid
                    if first_pos:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index
        return [binarySearch(True), binarySearch(False)]
    
if __name__=="__main__":
    sol = Solution()
    print(sol.findFirstLastPostion([5,7,7,8,8,10], 8))     # [3, 4]
    print(sol.findFirstLastPostion([6,7,7,8,8,10], 6))     # [0, 0]
    print(sol.findFirstLastPostion([5,7,7,8,8,10], 6))     # [-1, -1]

# Time Complexity :  O(log n)
# Space Complexity : 	O(1)

# I used binary search twice to find the first and last occurrence separately.This leverages the sorted 
# array and achieves O(log n) time complexity.