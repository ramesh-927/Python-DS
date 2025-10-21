"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:
Input: digits = ""
Output: []
Example 3:
Input: digits = "2"
Output: ["a","b","c"]
Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""
class Solutions:
    def letterCombination(self, digits):

        # 1) Edge case: if input is empty, there are no combinations
        if not digits:
            return []
        
        phone = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        res = []
        path = []

        def backtrack(i):
            if i ==len(digits):
                res.append("".join(path))
                return
            
            for ch in phone[digits[i]]:
                path.append(ch)
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return res
        
sol = Solutions()
result =sol.letterCombination("234")
print(result)