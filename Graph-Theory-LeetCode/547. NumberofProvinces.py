"""
547. Number of Provinces
There are n cities. Some of them are connected, while some are not. If city a is connected directly with 
city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city 
are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.
xample 1:
1   ---    2
    3

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:
 1              2
        3
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""
class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    parent[find(i)] = find(j)
        return len(set(find(i) for i in range(n)))

if __name__== "__main__":
    sol = Solution()
    print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))            # 2
    print(sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))           # 3

# Time complexity: O(n²) – We scan half the matrix (O(n²)), and each find operation is nearly O(1) thanks 
# to path compression.
# Space complexity: O(n) – Just the parent list.

# For finding the number of connected components in an undirected graph (especially when given as an 
# adjacency matrix), the best algorithm is Union-Find (Disjoint Set Union) with path compression. It's 
# efficient for dense graphs (many connections), has near-constant time per operation, and avoids recursion 
# stack issues. If the graph were sparse (few connections), DFS or BFS might edge it out, but here the 
# matrix implies potential density, so Union-Find is ideal.

# I used Union-Find with path compression to merge directly connected cities into the same set, then counted 
# the distinct root parents as the number of provinces.This achieves O(n²) time by scanning the matrix 
# once and performing amortized O(1) unions/finds per connection.

