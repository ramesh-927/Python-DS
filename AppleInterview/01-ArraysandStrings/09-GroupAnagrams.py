"""
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
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):

        groups = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())

if __name__== "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  
                # prints : [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(sol.groupAnagrams([""]))     # prints [['']]
    print(sol.groupAnagrams(["a"]))    # prints [['a']]

# I used a hashmap where the key is the sorted version of each string (as a tuple), and the 
# value is the list of original anagrams. Since strings with the same letters sort to the same sequence, 
# they automatically group together — this is the standard and optimal way for anagram grouping.

# Time Complexity: O(N × K × log K)
# N = number of strings
# K = maximum length of a string
# sorted(s) takes O(K log K)
# Space Complexity: O(N × K)