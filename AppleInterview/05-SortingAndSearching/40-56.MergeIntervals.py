"""
Docstring for AppleInterview.05-SortingAndSearching.40-56.MergeIntervals
Given an array of intervals where intervals[i] = [starti, endi],merge all overlapping intervals, and 
return an array of the non-overlapping intervals that cover all the intervals in the input.
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
        
        intervals.sort(key=lambda x : x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged

if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))   # prints : [[1, 6], [8, 10], [15, 18]]
    print(sol.mergeIntervals([[1,4],[4,5]]))        # [[1, 5]]
    print(sol.mergeIntervals([[4,7],[1,4]]))        # [[1, 7]]

# Time Complexity: O(n log n) – Sorting dominates; the loop is O(n).
# Space Complexity: O(n) – For the sorted list and result (but we modify in place where possible).

#I sorted the intervals by start time to process them in order.Then, I iterated through them, merging 
# overlaps by updating the end of the previous interval if the current one starts before or at its end.

# "It's the standard greedy approach: sort by start time, then merge in a single pass."
        
