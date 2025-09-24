"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
Example 2:
Input: s = "leetcode"
Output: "leotcede"
Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""
class Solutions(object):
    def reverseVowels(self, s):

        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:

            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left],s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)
    
if __name__ == "__main__":
    sol = Solutions()

    s1 = "IceCreAm"
    print("Input:", s1)
    print("Output:", sol.reverseVowels(s1))
    print("Expected:", "AceCreIm")

    s2 = "leetcode"
    print("\nInput:", s2)
    print("Output:", sol.reverseVowels(s2))
    print("Expected:", "leotcede")

# Time Complexity: O(n) → each character is checked at most once.

# Space Complixty: O(1) → only a set of vowels + swap in-place.