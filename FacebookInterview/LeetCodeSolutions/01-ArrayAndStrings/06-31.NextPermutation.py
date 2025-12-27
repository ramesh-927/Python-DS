"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.06-31.NextPermutation
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are all the permutations of arr: 
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its 
integer. More formally, if all the permutations of the array are sorted in one container according to 
their lexicographical order, then the next permutation of that array is the permutation that follows 
it in the sorted container. If such arrangement is not possible, the array must be rearranged as the 
lowest possible order (i.e., sorted in ascending order).
For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical 
larger rearrangement.
Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.
Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
             
if __name__== "__main__":
    sol = Solution()
    print(sol.nextPermutation([1,2,3]))          # [1, 3, 2]
    print(sol.nextPermutation([3,2,1]))          # [1, 2, 3]
    print(sol.nextPermutation([1,1,5]))          # [1, 5, 1]


#  Time Complexity  :  **O(n)** 
#  Space Complexity :  **O(1)** 

# I used a greedy approach to find the first decreasing element from the right, swapped it with the 
# next larger element, and reversed the suffix.This guarantees the next lexicographically smallest 
# permutation in linear time and constant space.

# Best Algorithm for This Kind of Problem, For "next permutation" or similar rearrangement problems 
# (like finding the k-th permutation), the standard algorithm above is the best—it's from STL in 
# C++ and widely used. It avoids generating all options by exploiting the sorted nature of permutations. 
# For variations, sometimes use heaps algorithm or recursion, but this is optimal for "next" in lex 
# order.
        


