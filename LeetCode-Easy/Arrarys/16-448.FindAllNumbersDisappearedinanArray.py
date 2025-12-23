"""
Docstring for LeetCode-Easy.Arrarys.16-448.FindAllNumbersDisappearedinanArray

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the 
integers in the range [1, n] that do not appear in nums.
Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:
Input: nums = [1,1]
Output: [2]
Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list 
does not count as extra space.
"""
class Solution:
    def findDisapperedNum(self, nums):
        seen = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in seen:
                result.append(i)
        return result

if __name__== "__main__":
    sol = Solution()
    print(sol.findDisapperedNum([4,3,2,7,8,2,3,1]))           # Prints : [5 ,6]
    print(sol.findDisapperedNum([1,1]))                       # Prints : [2]

# As per the Follow up: this is not Optimal  becasue  it it takes  extra space O(n)

# This is Optimal Soltuion:
#class Soltuion:
#    def findDisappeardNum(self, nums):
#        for i in range(len(nums)):
#            idx = abs(nums[i]) - 1
#            nums[idx] = -abs(nums[idx])
#        return [i + 1 for i in range(len(nums)) if nums[i] > 0 ]

#  Time Complexity  : O(n)                  
#  Space Complexity :  O(1) (no extra space) 

