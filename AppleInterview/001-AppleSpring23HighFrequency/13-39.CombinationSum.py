"""
Docstring for AppleInterview.001-AppleSpring23HighFrequency.13-39.CombinationSum

Given an array of distinct integers candidates and a target integer target, return a list of all 
unique combinations of candidates where the chosen numbers sum to target. You may return the 
combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are 
unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less 
than 150 combinations for the given input.
Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:
Input: candidates = [2], target = 1
Output: []
Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""
class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, path, total):

            if total == target:
                result.append(path[:])

            if total > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2,3,6,7], 7))    #  prints : [[2, 2, 3], [7]]
    print(sol.combinationSum([2,3,5], 8))       # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print(sol.combinationSum([2], 1))           # []

# Time Complexity: O(2^{target / min(candidates)}) in worst case (exponential, as we may explore many combinations), but practical due to pruning. 
# Space is O(target / min(candidates)) for recursion depth.

# I used a backtracking approach to recursively build combinations by adding candidates to a path while 
# tracking the sum, allowing reuse by passing the same starting index in the loop.This ensures we 
# explore all unique paths efficiently, pruning when the sum exceeds the target to optimize performance.

# Interviews love backtracking questions (e.g., subsets, permutations, N-Queens), so memorize a simple
#  "recipe" or template. Think of it as "B.A.C.K." mnemonic to recall the key precautions quickly:
# Base Cases: Stop when done or over (success/fail).
# Add and Explore: Pick a choice, add it, recurse deeper.
# Clean Up: Always backtrack (undo) after trying.
# Kill Duplicates/Prune: Sort, skip repeats, cut bad paths early.       
#  Just remember this 3-word magic sentence:
#______________________________________
# "Choose → Explore → Unchoose"
#_________________________________________
# Word,What you do in code,Real life example
# 1. Choose,path.append(candidate),Pick a number and put it in your bag
# 2. Explore,recurse(...),Keep walking deeper with that number
# 3 .Unchoose,path.pop(),Take it out the number if it failed
# 
#
#    def backtrack(whatever parameters you need):
#   result = []                                      # final answer list
#
#     def helper(current_path, other_variables...):
#        
#        # 1. Base cases (STOP conditions)
#        if success_condition:
#            result.append(current_path.copy())
#            return
#        if fail_condition:          # optional early stop
#            return
#        # 2. Try every choice
#        for choice in possible_choices:
#            # Optional pruning (very common)
#            if choice makes it impossible: continue
#            # Choose
#            current_path.append(choice)          # or update any state
#            # Explore
#            helper(current_path, updated_variables)
#            # Unchoose (BACKTRACK!)
#            current_path.pop()                   # or undo the state

#        helper(empty_path, starting_values)
#        return result