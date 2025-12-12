"""
Docstring for LeetCode-Top75-Solutions.ArrayAndStrings.01-1768.MergeStringsAlternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end 
of the merged string.
Return the merged string.
Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""
class Solution:
    def mergeAlternatively(self, word1, word2):

        result = []

        for a, b in zip(word1, word2):
            result.append(a)
            result.append(b)

        result.extend(word1[len(word2):])
        result.extend(word2[len(word1):])

        return ".".join(result)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeAlternatively("abc", "pqr"))    #.  a.p.b.q.c.r
    print(sol.mergeAlternatively("ab", "pqrs"))    #   a.p.b.q.r.s

# I used a list to build the result by looping through both strings in parallel using zip to add 
# characters alternately. Then I appended any remaining characters from the longer string using 
# slicing — this runs in linear time and is very easy to follow.

# best time complexity: O(n + m)

