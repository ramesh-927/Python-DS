"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters 
and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line does not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified, and no extra space is inserted between words.
Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            # Step 1: Determine words for the current line
            start = i
            line_length = len(words[i])
            i += 1
            while i < n and line_length + len(words[i]) + (i - start) <= maxWidth:
                line_length += len(words[i])
                i += 1

            # Step 2: Build the line
            num_words = i - start
            num_spaces = maxWidth - line_length
            line_words = words[start:i]

            if i == n or num_words == 1:
                # Left-justify for last line or single word
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                # Fully justify
                spaces_per_gap = num_spaces // (num_words - 1)
                extra_spaces = num_spaces % (num_words - 1)
                line_parts = []
                for k in range(num_words - 1):
                    line_parts.append(line_words[k])
                    spaces = spaces_per_gap + (1 if k < extra_spaces else 0)
                    line_parts.append(" " * spaces)
                line_parts.append(line_words[-1])
                line = "".join(line_parts)

            res.append(line)

        return res
    
    ### STILL i NEED TO UNDERSTAND