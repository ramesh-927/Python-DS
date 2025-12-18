"""
Docstring for LeetCode-Easy.Arrarys.03-977.SquaresofaSortedArray
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number 
sorted in non-decreasing order.
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order. 
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) 
solution using a different approach?
"""
class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result
    
if __name__ == "__main__":
     sol = Solution()
     print(sol.sortedSquares([-4,-1,0,3,10]))
     print(sol.sortedSquares([-7,-3,2,3,11]))

# Time: O(n) – We go through the list once, like reading a book from start to end.
# Space: O(n) – We need a new list of the same size.

# For problems with sorted arrays where a transformation (like squaring) changes values but the order is 
# predictable (e.g., negatives become large positives), use the two-pointer technique. It efficiently 
# "merges" the transformed parts from both ends without re-sorting, ideal for interview questions on arrays 
# or optimization.

# I used a two-pointer approach starting from both ends of the sorted array. By comparing absolute values 
# and placing the larger square at the end of the result list, we build the sorted squares in O(n) time 
# without extra sorting