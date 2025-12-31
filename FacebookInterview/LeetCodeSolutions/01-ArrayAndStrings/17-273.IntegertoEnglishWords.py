"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.17-273.IntegertoEnglishWords

Convert a non-negative integer num to its English words representation.
Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Constraints:
0 <= num <= 231 - 1
"""
class Solution:
    def numToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
                'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
                'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
                'Seventeen', 'Eighteen', 'Nineteen']

        tens = ['', '', 'Twenty', 'Thirty', 'Forty',
                'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        def chunk(n):
            if n == 0:
                return []
            if n < 20:
                return [ones[n]]
            if n < 100:
                return [tens[n // 10]] + chunk(n % 10)
            return [ones[n // 100], 'Hundred'] + chunk(n % 100)

        res = []
        units = ['','Thousand','Million','Billion']
        i = 0

        while num > 0:
            if num % 1000 != 0:
                res = chunk(num % 1000) + [units[i]] + res
            num //= 1000
            i += 1

        return ' '.join(res).strip()

if __name__ == "__main__":
    sol = Solution()
    print(sol.numToWords(12345))
    print(sol.numToWords(98675))
    print(sol.numToWords(1234567))

# Time Complexity  : **O(1)** (bounded by 32-bit integer size) 
# Space Complexity : **O(1)**                                  

# Chunking + Recursion (or Iteration)
# Because English words repeat every 3 digits, dividing the number into thousand-sized chunks 
# gives clean, scalable logic.

# I split the number into 3-digit chunks and convert each chunk into words.
# Then I append the correct place value like Thousand, Million, or Billion.
