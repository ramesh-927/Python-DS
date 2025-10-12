"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""
class Solution:
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]

        for s in strs[1:]:
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]

        return prefix

if __name__ == "__main__":
    sol = Solution()
    strs = ["flower","flow","flight"]
    res = sol.longestCommonPrefix(strs)

    print(f"Prefix of {strs} is :", res)

# Time Complexity: O(S).
# Space Complexity: O(1).