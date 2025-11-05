"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, 
return any of them. If it is impossible to finish all courses, return an empty array.
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)

        state = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = done
        order = []
        def dfs(node):
            if state[node] == 1:     # found a back-edge -> cycle
                return False
            if state[node] == 2:     # already processed
                return True

            state[node] = 1          # mark visiting
            for nxt in graph[node]:
                if not dfs(nxt):
                    return False
            state[node] = 2          # mark done
            order.append(node)       # post-order append
            return True

        # Run DFS from every node (handles disconnected graph)
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return []        # cycle detected -> no valid order

        return order[::-1]          # reverse post-order => topological order

if __name__ == "__main__":
    sol = Solution()
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    out = sol.findOrder(numCourses, prerequisites)
    print(f"'{numCourses}' and '{prerequisites}' are : ", out)  

# Time complexity: O(V + E).
# Space: O(V + E) for graph + O(V) recursion stack (worst-case).
# Returns [] immediately if a cycle is detected.