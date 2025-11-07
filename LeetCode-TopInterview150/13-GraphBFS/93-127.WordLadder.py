"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence 
of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the 
shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        # build pattern -> words map
        patterns = defaultdict(list)
        for w in wordList:
            for i in range(L):
                patterns[w[:i] + '*' + w[i+1:]].append(w)

        # include beginWord patterns so neighbors are found from start
        if beginWord not in wordList:
            for i in range(L):
                patterns[beginWord[:i] + '*' + beginWord[i+1:]].append(beginWord)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist

            for i in range(L):
                pat = word[:i] + '*' + word[i+1:]
                for neigh in patterns.get(pat, []):
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh, dist + 1))
                # clear the list so we don't revisit same neighbors again
                patterns[pat] = []   # <-- fixed (was = 0)
        return 0

# quick test
sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # -> 5

# Time: O(N * L) in practice (preprocessing) plus the BFS expansions. For each visited word, 
# generating its L patterns is O(L) and iterating neighbors is proportional to number of neighbors. 
# Summed across all words this remains O(N * L) (times a small factor for alphabet checks).
#  So overall time ~ O(N * L).

# Space: O(N * L) for the pattern map plus O(N) for visited maps and frontier sets → space O(N * L).



