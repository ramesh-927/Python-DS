"""
Docstring for AppleInterview.001-AppleSpring23HighFrequency.16-14.LongestCommonPrefix

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
    
        # Take the first string as our "candidate" prefix
        prefix = strs[0]
    
        # Compare this prefix with every other string
        for s in strs[1:]:
            # While the current string doesn't start with our prefix, shrink the prefix
            while not s.startswith(prefix):
                prefix = prefix[:-1]        # remove last character
                if not prefix:              # if prefix becomes empty
                    return ""
    
        return prefix
        
if __name__== "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))     #  fl
    print(sol.longestCommonPrefix(["dog","racecar","car"]))       # ""

# This is optimal with time complexity O(N * M) (N = number of strings, M = min string length), 
# as we may check every character in the worst case (all strings identical). Space is O(1) ignoring input. No better asymptotic time exists since we must read all relevant characters.