"""
You're playing Battleship on a grid with R rows and C columns.
Each cell either contains a battleship (G[i][j] = 1) or not (G[i][j] = 0). 
You fire a single shot at a uniformly random cell among the R * C cells. 
Compute the probability that the shot hits a battleship
Your task is to implement the function getHitProbability(R, C, G) which returns this probability.
Return the probability as a floating point number. Absolute or relative error must be ≤ 1e-6.
Constraints:
1 ≤ R, C ≤ 100
G[i][j] ∈ {0, 1}
Examples:
Example 1:
R = 2, C = 3
G = [[0,0,1],[1,0,1]]
Expected return: 0.50000000
Example 2:
R = 2, C = 2
G = [[1,1],[1,1]]
Expected return: 1.00000000
"""
def getHitProbability(R, C, G):
    total = R * C
    count = sum(sum(row) for row in G)
    return count / total

if __name__ == "__main__":
    # Sample test #1
    R1, C1 = 2, 3
    G1 = [
        [0, 0, 1],
        [1, 0, 1]
    ]
    print("{:.8f}".format(getHitProbability(R1, C1, G1)))  # 0.50000000

    # Sample test #2
    R2, C2 = 2, 2
    G2 = [
        [1, 1],
        [1, 1]
    ]
    print("{:.8f}".format(getHitProbability(R2, C2, G2)))  # 1.00000000

    # Replace with custom input or hook to stdin as needed.
