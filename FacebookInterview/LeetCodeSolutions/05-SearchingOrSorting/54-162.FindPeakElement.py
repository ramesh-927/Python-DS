"""
Docstring for FacebookInterview.LeetCodeSolutions.05-SearchingOrSorting.54-162.FindPeakElement
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains 
multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be 
strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 
5 where the peak element is 6.
Constraints:
1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""
class Solution:
    def findPeakElement(self, nums):
        
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
    
if __name__ =="__main__":
    sol = Solution()
    print(sol.findPeakElement([1,2,3,1]))           # Index 2
    print(sol.findPeakElement([1,2,1,3,5,6,4]))     # Index 5

# Time Complexity : O(log n) – super fast.
# Space Complexity: O(1) – no extra storage.

# For a faster way, we use "binary search," which is like guessing games where you halve the options 
# each time (e.g., "Is it higher or lower?"). Since neighbors are always different, the list has ups 
# and downs, guaranteeing a peak somewhere. We pick the middle, check if it's a peak. If not, we see 
# which side is going "uphill" (bigger neighbor) and search only there, because a peak must be on that 
# uphill side. Repeat until we find one. This is quick, finishing in steps like log base 2 of the list
#  size (O(log n) time).

# I used binary search to find a peak in O(log n) time by repeatedly checking the middle element and 
# moving to the half with the uphill slope, guaranteeing a peak exists there due to no plateaus. This 
# beats linear scan's O(n) by halving the search space each step.
