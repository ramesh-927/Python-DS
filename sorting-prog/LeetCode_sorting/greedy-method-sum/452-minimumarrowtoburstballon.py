"""
452. Minimum Number of Arrows to Burst Balloons

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:
1 <= points.length <= 105
points[i].length == 2
-231 <= xstart < xend <= 231 - 1
"""
#1. If points is empty, return 0
#2. Sort points by the end value
#3. Initialize arrows = 1
#4. Set current_end = end of the first balloon
#5. For each balloon from second onwards:
#    a. If start > current_end:
#        - Need new arrow
#       - arrows += 1
#        - current_end = end of this balloon
#6. Return arrows

class Solutions:
    def findMinArrowShots(self, points):
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])

        arrows = 1
        current_end = points[0][1]

        for strt, end in points[1:]:
            if strt > current_end:
                arrows += 1
                current_end = end
        return arrows

sol = Solutions()
points1 = [[1,2],[3,4],[5,6],[7,8]]
points2 = [[10,16],[2,8],[1,6],[7,12]]

intput1 = sol.findMinArrowShots(points1)
print("first Input: ", intput1)

intput2 = sol.findMinArrowShots(points2)
print("Second Input: ", intput2)