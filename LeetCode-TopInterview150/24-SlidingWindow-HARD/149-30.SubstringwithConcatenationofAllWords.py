"""
You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" 
are all concatenated strings. "acdbef" is not a concatenated string because it is not the 
concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. 
You can return the answer in any order.
Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation:
There is no concatenated substring.
Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
Constraints:
1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""
from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words or not words[0]:
            return []
        
        target = Counter(words)
        word_len = len(words[0])
        total_len = len(words) * word_len
        result = []
        
        for start in range(word_len):
            window = Counter()
            left = start
            
            for i in range(start, len(s) - word_len + 1, word_len):
                word = s[i:i + word_len]
                
                if word not in target:             
                    window.clear()
                    left = i + word_len
                    continue
                
                window[word] += 1
                
                # Shrink from left if we have too many of current word
                while window[word] > target[word]:
                    window[s[left:left + word_len]] -= 1
                    left += word_len
                
                # If window matches exactly total_len → valid substring
                if i - left + word_len == total_len:
                    result.append(left)
        
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findSubstring("barfoothefoobarman", ["foo","bar"]))
    # Output: [0, 9]

    print(sol.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
    # Output: [8]

    print(sol.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", 
                            ["fooo","barr","wing","ding","wing"]))
    # Output: [13]
"""
Since all words have the same length, we only need to check word_len possible starting positions.
For each starting offset, we slide a window across the string in steps of word_len.
We maintain a window counter of words seen.
If we see an invalid word → reset the window.
If we have too many of a word → shrink from the left.
When the window size equals total_len and all counts match → we found a valid substring starting at left.
"""
# Time is O(n) because each character is visited at most twice — once when expanding the window, once when shrinking.
# Space is O(number of unique words) for the two hash maps."