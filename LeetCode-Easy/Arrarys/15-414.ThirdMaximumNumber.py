"""
Docstring for LeetCode-Easy.Arrarys.15-414.ThirdMaximumNumber
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum 
does not exist, return the maximum number.
Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
Follow up: Can you find an O(n) solution?
"""
class Solution:
    def thirdMaxium(self, nums):
        first = second = third = None

        for n in nums:
            if n == first or n == second or n == third:
                continue
            if first is None or n > first:
                third = second
                second = first
                first = n
            elif second is None or n > second:
                third = second
                second = n
            elif third is None or n > third:
                third = n
        return third if third is not None else first

if __name__== "__main__":
    sol = Solution()
    print(sol.thirdMaxium([3,2,1]))                    # Prints : 1
    print(sol.thirdMaxium([1,2]))                      # Prints : 2
    print(sol.thirdMaxium([2,2,3,1]))                  # Prints : 1

# I used a single-pass approach to track the top three distinct maximum values without sorting. This 
# achieves O(n) time and constant space by updating three variables dynamically.

# Time complexity: O(n) – we look at each number exactly once, no extra work like sorting.
# Space complexity: O(1) – we use fixed space (just three variables), no matter how big the list is.