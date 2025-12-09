"""
Docstring for AppleInterview.08-Others.59-412.FizzBuzz
Given an integer n, return a string array answer (1-indexed) where:
1. answer[i] == "FizzBuzz" if i is divisible by 3 and 5
2. answer[i] == "Fizz" if i is divisible by 3.
3. answer[i] == "Buzz" if i is divisible by 5.
4. answer[i] == i (as a string) if none of the above conditions are true.
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]
Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
1 <= n <= 104
"""
class Solution:
    def fizzBuzz(self, n):
        
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
    
if __name__== "__main__":
    sol = Solution()
    print(sol.fizzBuzz(3))        # ['1', '2', 'Fizz']
    print(sol.fizzBuzz(5))        # ['1', '2', 'Fizz', '4', 'Buzz']
    print(sol.fizzBuzz(15))       # ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

# Time Complexity: O(n) – We visit each number exactly once (best possible, as we must generate n items).
# Space Complexity: O(1) extra space (besides the output list, which is required).

# I used a simple loop to iterate from 1 to n, checking divisibility with modulo: first for 15 (FizzBuzz), then 3 (Fizz), then 5 (Buzz), else the number as a string.
# This ensures O(n) time complexity with minimal code,
