"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character
Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""
class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)

        # dp[i][j] = min operations to convert word1[0:i] to word2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for i in range(m + 1):
            dp[i][0] = i   # Delete i char 
        for j in range(n + 1):
            dp[0][j] = j   # Insert j char
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # No Operations needed
                    dp[i][j] = dp[i -1][j -1]
                else:
                    # Min of: insert, delete, replace
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        return dp[m][n]
    
if __name__== "__main__":
    sol = Solution()
    print(sol.minDistance("intention","execution"))   # prints 5
    print(sol.minDistance("horse","ros"))            # prints 3
    # explanation: horse -> rorse (replace h->r) -> rose (delete 'r'?? wait) ...
    # typical sequence: horse -> rorse (replace h->r) -> rose (delete 'r'?) -> ros (delete 'e') yields 3 ops

# Time Complexity: O(m × n)
# Space Complexity: O(m × n) 

# This is a classic dynamic programming problem. We use a 2D table where dp[i][j] represents 
# the min edits to convert the first i chars of word1 to first j chars of word2. 
# We fill it by checking if characters match, otherwise taking the min of insert/delete/replace.