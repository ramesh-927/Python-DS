"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
Example 4:
Input: s = "([])"
Output: true
Example 5:
Input: s = "([)]"
Output: false
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
class Solution:
    def isValidParaenthese(self, s):

        mapping = {"}": "{", "]": "[", ")": "("}
        stack  = []

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
    
if __name__ == "__main__":
    sol = Solution()
    tests = [
    "()",       # True
    "()[]{}",   # True
    "(]",       # False
    "([)]",     # False
    "{[]}",     # True
    "]",        # False
    ]

    for t in tests:
        res = sol.isValidParaenthese(t)
        print(f"{t:8} -> {res}")

# Time	O(n)	Each bracket is pushed/popped once
# Space	O(n)	Stack can grow up to n/2 for all open brackets