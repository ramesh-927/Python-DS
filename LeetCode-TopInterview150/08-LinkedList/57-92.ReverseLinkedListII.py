"""
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list
Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
Follow up: Could you do it in one pass?
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseLinkedlist(self, head, left, right):
        if not head or left == right:
            return head
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        for i in range(left - 1):    # Step 1: Move `prev` to the node just before `left`
            prev = prev.next

        curr = prev.next     # `curr` points to the first node in the sublist to reverse

        for i in range(right - left):    # Step 2: Reverse the sublist between left and right
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next
#------------------------------------------------------------------------------
def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
# Helper to create linked list from list
def create_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next
sol = Solution()
tests = [
    ([1,2,3,4,5], 2, 4),    # reverse 2-4
    ([1,2,3,4,5], 1, 5),    # reverse entire list
    ([1,2,3,4,5], 3, 3),    # no reversal
]
for arr, l, r in tests:
    head = create_list(arr)
    res = sol.reverseLinkedlist(head, l, r)
    print(f"{arr}, left={l}, right={r}  ->  {print_list(res)}")

# Time Complexity : O(N) – traverse and reverse once
# Space	Complexity : O(1) – in-place reversal


