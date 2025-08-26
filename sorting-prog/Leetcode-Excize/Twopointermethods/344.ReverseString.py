"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
"""
class Solutions:
    def reversString(self, s1):
        left , right = 0, len(s1) - 1

        while  left < right:
            s1[left], s1[right] = s1[right], s1[left]
            left += 1
            right -= 1
        return []

sol = Solutions()
s1 = ["h","e","l","l","o"]
s2 = ["H","a","n","n","a","h"]

input1 = sol.reversString(s1)
print("S1- String reversed", s1)

input2 = sol.reversString(s2)
print("S2- String reversed", s2)



