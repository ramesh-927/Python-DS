"""
Docstring for FacebookInterview.LeetCodeSolutions.05-SearchingOrSorting.53-56.MergeIntervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
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

        intervals.sort(key = lambda x : x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])
        return merged

if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))  # [[1, 6], [8, 10], [15, 18]]
    print(sol.mergeIntervals([[4,7],[1,4]]))            # [[1, 7]]
    print(sol.mergeIntervals([[1,4],[4,5]]))            # [[1, 5]]

# Time complexity: O(n log n) – the "log n" from sorting (like quickly organizing a deck of cards), 
# and "n" from the single walk-through. Super efficient for big lists.
# Space complexity: O(n) for the result list, but minimal extra space otherwise.

# For merging intervals or similar "overlapping ranges" problems (like scheduling or timeline grouping), 
# the sorting + single-pass merge is the go-to algorithm. It's optimal because sorting ensures order, 
# and the pass handles merges efficiently. Alternatives like interval trees are overkill for this 
# (more complex, same time complexity).

# I sorted the intervals by their start times to ensure chronological order. Then, I iterated through 
# them in a single pass, merging overlapping ones by updating the end of the previous interval if the 
# current starts before it ends.