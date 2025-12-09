"""
Docstring for AppleInterview.08-Others.60-771.JewelsandStones
You're given strings jewels representing the types of stones that are jewels, and stones representing 
the stones you have. Each character in stones is a type of stone you have. You want to know how many 
of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
Constraints:
1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""
class Solution:
    def numJewelsInStones(self, jewels, stones):
        jewel_set = set(jewels)
        return sum(1 for stone in stones if stone in jewel_set)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numJewelsInStones("aA", "aAAbbbb"))      # prints : 3
    print(sol.numJewelsInStones("z", "ZZ"))           # prints : 0

# I converted the jewels string to a set for O(1) average-time lookups. Then, I iterated through the 
# stones, counting each one that exists in the set, achieving O(M + N) time overall.

# Time Complexity : O(m + n)
# Space Complexity : O(m)

