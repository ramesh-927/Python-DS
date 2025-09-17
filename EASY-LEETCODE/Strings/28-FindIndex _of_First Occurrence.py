"""
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
class Solutions:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        n, m = len(haystack), len(needle) 

        for i in range(n - m + 1):
            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1
                if j == m:
                    return i
        return -1

if __name__ == "__main__":
    sol = Solutions()
    haystack = "sadbutsad"
    needle = "sad"
    res = sol.strStr(haystack, needle)
    print(res)

#Time Complexity:
# Worst case: O((n-m+1) * m) ≈ O(n * m)
# (e.g., haystack = "aaaaa...aaaaa", needle = "aaaab")
# Space: O(1)
    
            

