"""
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, 
return the shortest distance between these two words in the list. 
Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
Constraints:
2 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
"""
class soluitions:
    def shortestDistance(self, wordsDict, word1, word2):
        idx1, idx2  = - 1, - 1
        min_dist = float('inf')

        for i, word in enumerate(wordsDict):
            if word == word1:
                idx1 = i
            elif word == word2:
                idx2 = i
            
            if idx1 != - 1 and idx2 != - 1:
                min_dist = min(min_dist, abs(idx1 - idx2))
        return min_dist
if __name__ == "__main__":
    
    sol = soluitions()
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "makes"
    word2 = "coding"
    result = sol.shortestDistance(wordsDict, word1, word2)
    print(result)


# Time Complexity: O(n)
# Space Complexity: O(1)