"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:
Input: lists = []
Output: []
Example 3:
Input: lists = [[]]
Output: []
Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
import heapq
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
            dummy = ListNode()
            current = dummy
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        return dummy.next
    
# Say: “We use a min-heap to always get the smallest available node in O(log k) time.”
# Time: O(N log k) where N is total nodes
# Space: O(k) for heap
#------------------------------------------------------------------------------------------------
# Helper to create list: [1,4,5] → 1→4→5
def create_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Test
lists = [
    create_list([1,4,5]),
    create_list([1,3,4]),
    create_list([2,6])
]

result = Solution().mergeKLists(lists)

# Print result
while result:
    print(result.val, end=" → ")
    result = result.next
print("None") 
