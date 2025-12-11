"""
Docstring for AppleInterview.001-AppleSpring23HighFrequency.18-692.TopKFrequentWords
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency 
by their lexicographical order.

Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of 
occurrence being 4, 3, 2 and 1 respectively.
Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""
class Solution:
    def topKFrequent(self, words, k):

        freq = {}

        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        unique_words = list(freq.keys())
        unique_words.sort(key=lambda word: (-freq[word], word))   # Since Python sorts ascending by 
        # default, I use -frequency so higher counts become smaller numbers and come first. When 
        # frequencies tie, it naturally falls back to sorting by the word itself alphabetically.
        return unique_words[:k]

if __name__== "__main__":
    sol = Solution()
    print(sol.topKFrequent(["i","love","leetcode","i","love","coding"], 2))    # ['i', 'love']
    print(sol.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))
                                                                        #['the', 'is', 'sunny', 'day']

# I count each word's frequency using a hash map. Then I sort the unique words by frequency descending 
# and alphabetically ascending using a custom sort key, and return the first k.