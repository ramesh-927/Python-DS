"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
determine if a person could add all meetings to their schedule without any conflicts.
Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]
Output: true
Note:
(0,8),(8,10) is not considered a conflict at 8
Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

class Solutions:
    def canAttendMeeting(self, intervals):
        intervals.sort(key = lambda  x : x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i -1] [1]:
                return False

        return True


sol = Solutions()
intervals = [(5,8),(9,15)]
result = sol.canAttendMeeting(intervals)
print("Person can attend meeting:", result)

# Sorting: O(n log n)
# One pass for conflict check: O(n)
#Total: O(n log n)

"""
Why Greedy Works Here:
The greedy idea is:
Always pick the meeting that ends the earliest to avoid overlap.
But for this particular problem (just checking if a person can attend all meetings), it becomes even simpler:
Sort the meetings by start time.
Then, check for any overlaps by comparing each meeting’s start time with the previous meeting’s end time.
You're essentially greedily choosing the next available meeting that starts after the previous one ends — which aligns with greedy strategy principles.
"""