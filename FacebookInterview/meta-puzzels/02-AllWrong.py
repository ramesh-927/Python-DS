"""
There's a multiple-choice test with N questions, numbered from 1 to N.
Each question has 2 answer options, labelled A and B. 
You know that the correct answer for the ith question is the ith character in the string C, 
which is either "A" or "B", but you want to get a score of 0 on this test by answering every question incorrectly.

Your task is to implement the function getWrongAnswers(N, C) which returns a string with N characters, the ith of which is the answer you should give for question 
i in order to get it wrong (either "A" or "B").

Constraints
1 ≤ N ≤ 100
Ci ∈ {"A", "B"}

Sample test case #1
N = 3.  C = ABA
Expected Return Value = BAB

Sample test case #2
N = 5. C = BBBBB
Expected Return Value = AAAAA

"""

class Solutions:
    def getWrongAnswers(self, N, C):
        wrong_answer = []
        for ch in C:
            if ch == 'A':
                wrong_answer.append('B')
            if ch == 'B':
                wrong_answer.append('A')
        return ''.join(wrong_answer)
            
sol = Solutions()
test_cases = [
    (3, "ABA", "BAB"),
    (5, "BBBBB", "AAAAA")
]

for N, C, expected in test_cases:
    result = sol.getWrongAnswers(N, C)
print(f"For N = {N} and C = {C}, expected output: {expected}, actual output: {result}")

# Time Complexity =  O(N)
# Space Complexity  = O(N)