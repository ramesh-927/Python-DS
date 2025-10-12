"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:
Input: s = "A", numRows = 1
Output: "A"
Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
class Solution:
    def convert(self, s, numRows):

        if numRows == 1 or numRows == len(s):
            return s
        
        rows = [[] for _ in range(numRows)]
        curr_idx = 0
        step = 1

        for ch in s:
            rows[curr_idx].append(ch)
            if curr_idx == 0:
                step  = 1
            elif curr_idx == numRows - 1:
                step = - 1
            curr_idx += step
        return "".join("".join(r) for r in rows)
        
if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING" 
    numRows = 4
    res = sol.convert(s, numRows)
    print(f"Zigzag of '{s}' in numRows is'{numRows}' is : ", res)

#Complexities: Time O(n), Space O(n).

