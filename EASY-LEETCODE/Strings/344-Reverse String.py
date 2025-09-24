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
class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        # modifies s in place

def format_list(lst):
    return "[" + ",".join(f'"{ch}"' for ch in lst) + "]"

if __name__ == "__main__":
    sol = Solution()
    s = ["h", "e", "l", "l", "o"]   # input
    print("s =", format_list(s))
    sol.reverseString(s)            # modifies s in place
    print("Output")
    print(format_list(s))
    print("Expected")
    print(format_list(["o","l","l","e","h"]))

   
# Complexity
# Time: O(n) → every element is swapped once.
# Space: O(1) → no extra data structures.