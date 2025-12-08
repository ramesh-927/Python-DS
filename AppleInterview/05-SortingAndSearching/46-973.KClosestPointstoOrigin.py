"""
Docstring for AppleInterview.05-SortingAndSearching.46-973.KClosestPointstoOrigin
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer 
k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance 
(i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order 
that it is in).
Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
Constraints:
1 <= k <= points.length <= 104
-104 <= xi, yi <= 104
"""
import heapq
class Solution:
    def kClosest(self, points, k):

        heap = []
        for x, y in points:
            dist_sq = x * x + y * y

            heapq.heappush(heap, (-dist_sq, x, y)) # Negative for max-heap simulation

            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]

if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([[1,3],[-2,2]], 1))                #  [[-2,2]]
    print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))         #  [[-2, 4], [3, 3]]

# Time Compleixty : O(n log k) where n is the number of points. This is better than full sorting when 
# k is much smaller than n (e.g., find 10 closest out of 10,000). 
# Space Complexity :  O(k), just for the heap.

# I used a max-heap (simulated with Python's min-heap and negative distances) to maintain the k 
# closest points, efficiently replacing the farthest as I process each point for O(n log k) time.

# Smart Trick: Instead of calculating full distances (which involve slow square roots), we use 
# "distance squared" (x² + y²). This is faster and works the same for comparisons—smaller squared 
# means closer.