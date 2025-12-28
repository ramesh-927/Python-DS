"""
Docstring for FacebookInterview.LeetCodeSolutions.01-ArrayAndStrings.08-49.GroupAnagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
class Solution:
    def groupAnagram(self, strs):
        groups = {}

        for word in strs:
            sorted_groups = "".join(sorted(word))

            if sorted_groups in groups:
                groups[sorted_groups].append(word)
            else:
                groups[sorted_groups] = [word]
        return list(groups.values())

if __name__== "__main__":
    sol = Solution()
    print(sol.groupAnagram(["eat","tea","tan","ate","nat","bat"]))     # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(sol.groupAnagram([""]))                                      #  [['']]
    print(sol.groupAnagram(["a"]))                                     #  [['a']]

# Non- Techincal Analogy : 
# You're sorting a pile of scrambled word tiles into boxes.
# You decide: "I'll sort the letters on each tile alphabetically and put all tiles with the same sorted letters into the same box."
# That sorted letter string becomes the label on the box.

#I group the words using a hash map where the key is the sorted version of each word, since anagrams 
# will have the same sorted string.This way, all anagrams automatically go into the same group in O(n * m log m) time.