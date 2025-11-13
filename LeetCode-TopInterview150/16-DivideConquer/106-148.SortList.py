"""
Given the head of a linked list, return the list after sorting it in ascending order.
Example 1:
 4  ->  2  ->  1  ->  3
 1  ->  2  ->  3  ->  4
Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:
-1  ->  5  ->  3  ->  4  ->  0
-1  ->  0  ->  3  ->  4  ->  5
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:
Input: head = []
Output: []
Constraints:
The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def sortList(self, head):
        if not head or head.next:
            return None
        
        # Step 1: Find middle and split
        mid = self.getMid(head)
        left, right = head, mid.next
        mid.next = None

        # Step  2: Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)

        # Step 3 : Merge the sorted halves
        return self.merge(left, right)
    
    def getMid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next  = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return dummy.next

# | Metric               | Value                        |
# | -------------------- | ---------------------------- |
# | **Time Complexity**  | `O(n log n)`                 |
# | **Space Complexity** | `O(log n)` (recursion stack) |
# | **Stable Sort**      |   Yes                        |
# | **In-place**         |   Reuses original nodes      |



    



       