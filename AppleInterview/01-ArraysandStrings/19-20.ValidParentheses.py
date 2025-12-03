"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the 
input string is valid.
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

        return len(stack) == 0

if __name__ == "__main__":

    sol = Solution()
    print(sol.isValid("()"))         # Output : True
    print(sol.isValid("()[]{}"))     # Output : True
    print(sol.isValid("(]"))         # Output : False
    print(sol.isValid("([])"))       # Output : True
    print(sol.isValid("([)]"))       # Output : False

# "I used a stack to keep track of opening brackets. For each closing bracket, I check 
# if the top of the stack has the matching opening bracket — if not or stack is empty, return false. 
# At the end, return true only if stack is empty."

# Time Complexity : O(n) → We scan the string once
# Space Complexity : O(n) → In worst case (all opening), stack stores n/2 chars