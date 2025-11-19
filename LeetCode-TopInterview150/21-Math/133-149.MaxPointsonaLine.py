"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the 
maximum number of points that lie on the same straight line.
Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Constraints:
1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
from collections import defaultdict
class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2: return n
        
        def get_slope(p1, p2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx == 0: return float('inf')
            if dy == 0: return 0
            return dy / dx  # float is fine in Python for this problem
        
        ans = 1
        for i in range(n):
            count = defaultdict(int)
            same = 1  # count itself
            for j in range(i+1, n):
                if points[i] == points[j]:
                    same += 1
                else:
                    s = get_slope(points[i], points[j])
                    count[s] += 1
            # max from slopes + same points
            cur_max = same
            for v in count.values():
                cur_max = max(cur_max, v + same)
            ans = max(ans, cur_max)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPoints([[1,1],[2,2],[3,3]]))                        # Output : 3
    print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))      # Output : 4 

# Time Complexity: O(n²) — nested loop over points (each pair processed once).
# Space Complexity: O(n) additional (hash map per outer loop).


