"""
Docstring for AppleInterview.04-Recurrsion.36-78.Subsets
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:
Input: nums = [0]
Output: [[],[0]]
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
class Solution:
    def subSets(self, nums):

        result = []
        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return result

if __name__== "__main__":
    sol = Solution()
    print(sol.subSets([1,2,3]))   # Output : [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    print(sol.subSets([0]))     # Output : [[], [0]]

# I used backtracking with DFS. At each number, I make two recursive calls: one including the current 
# number, and one excluding it — this naturally generates all 2ⁿ subsets.
# We add a copy of the current path at every step, and backtrack by popping the last element. It's 
# clean, optimal, and the most common approach companies expect.

# Time Complexity : O(n * 2^n) | There are 2^n subsets; copying a subset can cost up to n, so multiply.
# Space Complexity : O(n * 2^n) (output) + O(n) recursion.
#  Output stores all subsets; recursion depth up to n.                    |
