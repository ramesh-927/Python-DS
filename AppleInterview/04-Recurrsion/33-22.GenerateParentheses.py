"""
Docstring for AppleInterview.04-Recurrsion.33-22.GenerateParentheses
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
    def generateParenthesis(self, n):

        result = []
        def backtrack(s, open_count, close_count):

            if len(s) == 2 * n:
                result.append(s)
                return
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result

if __name__ == "__main__":

    sol = Solution()
    inp = 3
    print("Your Input : ", inp)
    print(sol.generateParenthesis(inp))   # ["((()))","(()())","(())()","()(())","()()()"]
    inp1 = 1
    print("Your Input : ", inp1)
    print(sol.generateParenthesis(inp1))

# I used backtracking to build valid parentheses combinations. At each step, I can add an opening 
# bracket if I have any left, or a closing one only if it won't make more closes than opens — this 
# ensures validity and generates all 2n-length well-formed strings.

#  Time Complexity :  **O(Cn)** where `Cn` = nth Catalan number ≈ **O(4^n / (n^{3/2}))**
#  Space Complexity : **O(n)** recursion stack (plus O(Cn * n)** for storing results) 