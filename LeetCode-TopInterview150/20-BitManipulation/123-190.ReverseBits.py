"""
Reverse bits of a given 32 bits signed integer.
Example 1:
Input: n = 43261596
Output: 964176192
Explanation:
Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000
Example 2:
Input: n = 2147483644
Output: 1073741822
Explanation:
Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110
Constraints:
0 <= n <= 231 - 2
n is even.
Follow up: If this function is called many times, how would you optimize it?
"""
class Solution:
    def reverseBits(self, n):
        result = 0                    # Our NEW empty train (all 32 cars are 0 for now)
        for i in range(32):           # We do the same thing 32 times (once for each car)
            bit = n & 1               # "What number is written on the LAST car of the old train?"
            n >>= 1                   # "Remove the last car from the old train" (throw it away after reading)
            result = (result << 1) | bit   # TWO things happen here:
                                            # 1. Push all cars in the new train one step left (make space at the end)
                                            # 2. Put the number we just read into that new empty spot at the end
        return result                       # Yay! The new train is complete and perfectly reversed!

if __name__== "__main__":
    sol = Solution()
    inp = 43261596
    out = sol.reverseBits(inp)
    print(out)

#  Time Complexity :    O(32) → **O(1)** (constant) 
#  Space Complexity :   O(1)                        
