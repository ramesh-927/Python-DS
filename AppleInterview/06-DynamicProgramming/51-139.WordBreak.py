"""
Docstring for AppleInterview.06-DynamicProgramming.51-139.WordBreak
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a 
space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
class Solution:
    def wordBreak(self, s, wordDict):
        
        word_set = set(wordDict)  # Quick lookup
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further for this i
        return dp[len(s)]

if __name__== "__main__":
    sol = Solution()
    print(sol.wordBreak("leetcode", ["leet","code"]))            # True
    print(sol.wordBreak("applepenapple", ["apple","pen"]))       # True
    print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))     # False

#  Time Complexity: O(n²) in worst case (n = length of s), because we might check up to n substrings 
#  per position, each up to length n. But in practice, it's fast for typical inputs 
# (n up to 300 on LeetCode). 
# Space Compleixty : O(n).

#For "can we break/segment a sequence using given parts?" problems (like word break, or similar in 
# knapsack/partitioning), bottom-up dynamic programming is best. It's efficient, handles overlaps/reuse 
# (words can be used multiple times), and avoids recursion stack issues.

# I used dynamic programming with a boolean DP array where dp[i] is true if the substring up to i can 
# be segmented. We iterate through all possible break points, checking if prior segments are valid and 
# the remaining part matches a word in the set, achieving O(n²) time.