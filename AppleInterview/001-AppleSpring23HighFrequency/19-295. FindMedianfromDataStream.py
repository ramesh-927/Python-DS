"""
Docstring for AppleInterview.001-AppleSpring23HighFrequency.19-295. FindMedianfromDataStream
The median is the middle value in an ordered integer list. If the size of the list is even, there is 
no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer 
will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
Follow up:
If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your 
solution?

"""
import heapq

class MedianFinder:
    def __init__(self):
        self.maxh = []  # lower half (max-heap, store negated)
        self.minh = []  # upper half (min-heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxh, -num)
        heapq.heappush(self.minh, -heapq.heappop(self.maxh))
        
        if len(self.minh) > len(self.maxh):
            heapq.heappush(self.maxh, -heapq.heappop(self.minh))

    def findMedian(self) -> float:
        if len(self.minh) > len(self.maxh):
            return self.minh[0]
        return (self.minh[0] - self.maxh[0]) / 2.0


# Helper to simulate LeetCode test case exactly
def test_leetcode_style():
    mf = MedianFinder()
    operations = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    values    = [[],          [1],       [2],       [],           [3],       []]
    
    result = []
    for op, val in zip(operations, values):
        if op == "MedianFinder":
            result.append(None)
        elif op == "addNum":
            mf.addNum(val[0])
            result.append(None)
        elif op == "findMedian":
            result.append(mf.findMedian())
    
    print(result)  # This prints exactly like LeetCode!

# Run it
test_leetcode_style()

# I used two priority queues: a max-heap for the lower half of numbers (simulated with negatives in 
# Python's min-heap) and a min-heap for the upper half. This keeps them balanced for O(log n) 
# additions and O(1) median lookups by always having the median at the heap tops.