"""
Docstring for AppleInterview.04-Recurrsion.35-46.Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the 
answer in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]
Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
class Solution:
    def permute(self, nums):
        
        result = []
        def backtrack(start):
            if start == len(nums):              # We filled all positions
                result.append(nums[:])          # Copy current permutation
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)                                # Recurse
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack (restore)
        backtrack(0)
        return result

if __name__== "__main__":
     sol = Solution()
     print(sol.permute([1,2,3]))         # Prints :[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
     print(sol.permute([0,1]))           # Prints : [[0,1],[1,0]]
     print(sol.permute([1]))             #  Prints : [[1]]

# Time: O(n! × n) → n! permutations, each takes O(n) to copy
# Space: O(n) recursion depth + O(n! × n) for output

# I used backtracking with in-place swapping (the standard and most efficient approach for generating permutations).
# We fix one position at a time, recursively generate permutations of the remaining elements, and 
# backtrack by undoing the swap — this naturally explores all n! possibilities in O(n!) time.