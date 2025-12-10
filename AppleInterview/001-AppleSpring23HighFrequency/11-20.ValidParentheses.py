"""
Docstring for AppleInterview.001-AppleSpring23HighFrequency.11-20.ValidParentheses
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
    def isValid(self, s):

        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack
    
if __name__== "__main__":
    sol = Solution()
    print(sol.isValid("()"))                       # True
    print(sol.isValid("()[]{}"))                   # True
    print(sol.isValid("(]"))                       # False
    print (sol.isValid( "([])"))                   # True
    print(sol.isValid("([)]"))                     # False

# For bracket/parentheses validation (or similar matching problems like HTML tags or quotes), always 
# use a stack. It's the go-to because it naturally handles "last in, first out" (LIFO) order, 
# which matches how pairs nest. Alternatives like recursion work but can overflow for long strings; 
# stack is efficient and simple.

# I used a stack to track opening brackets: push openings, and for closings, pop and check if it 
# matches the expected opening."This ensures correct order and pairing in O(n) time with minimal code."
