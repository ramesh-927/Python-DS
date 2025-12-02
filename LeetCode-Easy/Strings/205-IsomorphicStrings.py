"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.
Example 3:
Input: s = "paper", t = "title"
Output: true
Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solutions:
    def isIsomorphic(self, s, t):

        if len(s) != len(t):
            return False
        map_st = {}
        map_ts = {}
        for cs, ct in zip(s, t):
            if cs in map_st:
                if map_st[cs] != ct:
                    return False
            else:
                if ct in map_ts:
                    return False
            map_st[ct] = cs
            map_ts[cs] = ct
        return True
if __name__ == "__main__":
    sol = Solutions()
    s = "egg"
    t = "add"
    result = sol.isIsomorphic(s, t)
    print(result)

# Time Complexity : O(n) where n = len(s) (single pass).

# Space Complexity : O(min(n, k)) where k is the alphabet size (two maps). If alphabet is bounded (e.g., ASCII), you can consider it O(1).
# Edge cases:
# Empty strings: returns True.
# Different lengths: False.
# Works for unicode chars too (using dicts).