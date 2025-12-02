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
class Soltuions:
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]   # Handle edge cases
        
        prefix = strs[0]   # Start with first string as prefix

        for s in strs[1:]:    # Compare with other strings
            while s[:len(prefix)] != prefix:     # Reduce prefix length until it matches the start of s
                prefix = prefix[:-1]      # Remove last character

                if not prefix:
                    return ""
        return prefix

if __name__ == "__main__":
    sol = Soltuions()
    strs = ["flower","flow","flight"]
    res = sol.longestCommonPrefix(strs)
    print(res)

#Time Complexity: O(S).  # Space Complexity: O(1).

