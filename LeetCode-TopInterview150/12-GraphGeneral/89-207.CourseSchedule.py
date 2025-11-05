"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        
        # Build adjacency list
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        state = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited
        
        def dfs(course):
            if state[course] == 1:  # Found a cycle
                return False
            if state[course] == 2:  # Already processed
                return True
            
            state[course] = 1  # Mark as visiting
            
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            state[course] = 2  # Mark as visited
            return True
        
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False
        
        return True

if __name__=="__main__":
    sol = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    out = sol.canFinish(numCourses, prerequisites)

    print(f"'{numCourses}' and '{prerequisites}' are : ", out)    
# Time  Complexity   :- **O(V + E)**                                            
# Space Complexity   :-  **O(V + E)** (graph + recursion stack + state tracking) 
