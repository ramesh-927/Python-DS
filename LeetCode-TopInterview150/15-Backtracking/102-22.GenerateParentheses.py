"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]
Constraints:
1 <= n <= 8
"""
class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def backtrack(current, open_count, close_count):
            # If we have used all 2*n parentheses, add to result
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Option 1: Add an opening '(' if we have any left
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
                
            # Option 2: Add a closing ')' only if it won't make it invalid
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack('', 0, 0)
        return result

if __name__ == "__main__":
    sol = Solution()
    for num in [1, 3, 4]:
        out = sol.generateParenthesis(num)
        print(num, out)
