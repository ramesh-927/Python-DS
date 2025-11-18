"""
You are given a large integer represented as an integer array digits, where each digits[i] is 
the ith digit of the integer. The digits are ordered from most significant to least significant in 
left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""
class Solution:
    def plusOne(self, digits):
        n = len(digits)
    
        # Start from the last digit
        for i in range(n - 1, -1, -1):  # go backwards: n-1, n-2, ..., 0
            if digits[i] < 9:
                digits[i] += 1     # just increase this digit by 1
                return digits      # done! no carry left
            digits[i] = 0          # this was 9 → becomes 0, carry over 1
    
        # If we are here, means all digits were 9 → like [9,9,9]
        return [1] + digits        # becomes [1, 0, 0, 0]

if __name__=="__main__":
    sol = Solution()
    print(sol.plusOne([4,3,2,7])) # [4, 3, 2, 8]
    print(sol.plusOne([1,2,3]))   # [1, 2, 4]
    print(sol.plusOne([4,3,2,1])) # [4, 3, 2, 2]
    print(sol.plusOne([9,9,9]))   # [1, 0, 0, 0]

# Time Complexity: O(n) – we may touch each digit once
# Space Complexity: O(1) – we modify the list in-place (except the rare case of all 9s, which needs O(n) anyway)