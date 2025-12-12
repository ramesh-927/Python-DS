"""
Docstring for AppleInterview.001-AppleSpring23HighFrequency.14-273.IntegertoEnglishWords
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
    def numberToWords(self, num):
        if num == 0:
            return 'Zero'
        ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 
                'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 
                'Seventeen', 'Eighteen', 'Nineteen']
        
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        thousands = ['', 'Thousand', 'Million', 'Billion']

        def words(n):
            if n == 0:
                return []
            if n < 20:
                return [ones[n]]
            if n < 100:
                return [tens[n // 10]] + words(n % 10)
            if n < 1000:
                quotient, reminder =  n// 100, n % 100
                return [ones[quotient], "Hundered"] + words(reminder)
            for power, chunk in enumerate(thousands[1:], 1):  # Start from Thousand
                if n < 1000 ** (power + 1):
                    quotient, remainder = n // (1000 ** power), n % (1000 ** power)
                    return words(quotient) + [chunk] + words(remainder)
        
        return ' '.join(words(num))
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numberToWords(123))            # One Hundered Twenty Three
    print(sol.numberToWords(12345))          # Twelve Thousand Three Hundered Forty Five
    print(sol.numberToWords(1234567))# One Million Two Hundered Thirty Four Thousand Five Hundered Sixty Seven

# Time Complexity : O(1)
# Space Compleixty: O(1)

# I used a recursive divide-and-conquer method: a helper function breaks the number into quotients and 
# remainders by powers of 1000, converts each part using predefined word mappings for 
# units/teens/tens/hundreds, and combines them with scale words like "Million".This ensures clean code, 
# handles all scales recursively in O(1) time, and avoids extra spaces by building a list of words 
# before joining.
        