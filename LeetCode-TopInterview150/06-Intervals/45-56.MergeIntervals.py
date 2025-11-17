"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
class Solution:
    def mergeIntervals(self, intervals):
        if not intervals:
            return []
        merged = []
        intervals.sort(key=lambda x: x[0])

        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([], []),
        ([[1,4],[0,2],[3,5]], [[0,5]]),
    ]
    for input, expected in tests:
        output = sol.mergeIntervals(input)
        print(f"{input} -> {output}   (expected: {expected})")

# Time Complexity: 	O(n log n)	Sorting dominates: O(n log n). Single pass to merge is O(n).
# Space	Complexity: O(n)	Output list may hold up to n intervals. 
# Sorting in-place uses O(1) extra if language sort is in-place, 
# but overall extra space is O(n) for result (and sort may use O(log n) or more depending on implementation).