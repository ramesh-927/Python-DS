"""
Given three integers A, B, and C, determine their sum.
Your task is to implement the function getSum(A, B, C) which returns the sum A + B + C.

Constraints
1 ≤ A, B, C ≤ 100

Sample test case #1
A = 1
B = 2
C = 3
Expected Return Value = 6
Sample test case #2
A = 100
B = 100
C = 100
Expected Return Value = 300
Sample test case #3
A = 85
B = 16
C = 93
Expected Return Value = 194
"""

class Solutions:
    def getSum(self, A, B, C ):

        if not (1 <= A <= 100):
            raise ValueError("A must be between 1 to 100")
        if not (1 <= B <= 100):
            raise ValueError("B must be between 1 to 100")
        if not (1 <= C <= 100):
            raise ValueError("C must be between 1 to 100")
        
        return A + B  + C
    
sol = Solutions()
A = 1
B = 2
C = 3
result = sol.getSum(A, B, C)
print("sum of A, B, C is : ", result)

A1 = 85
B2 = 16
C3 = 93
result = sol.getSum(A1, B2, C3)
print("sum of A1, B2, C3 is : ", result)
    