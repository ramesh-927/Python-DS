"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
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
class Solutions:
    def isValid(self, s: str) -> bool:   # <-- add self here
        if len(s) % 2 == 1:
            return False

        mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        stack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if mapping[ch] != top:
                    return False

        return len(stack) == 0


# --- Example usage ---
sol = Solutions()
s = "([])"
res = sol.isValid(s)
print(res)   # Output: True

            

# Time Complexity: O(1) for the length check.
# Space Complexity: O(1) as no additional space is used.