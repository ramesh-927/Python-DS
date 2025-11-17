"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
Example 3:
Input: head = [1,2], n = 1
Output: [1] 
Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz 
Follow up: Could you do this in one pass?
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        first = second = dummy
        
        for i in range(n + 1):    # Move first n+1 steps ahead
            first = first.next
        
        while first:   # Move both until first reaches the end
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next
#____________________________________________

def list_to_linked(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

sol = Solution()
tests = [
    ([1,2,3,4,5], 2),
    ([1], 1),
    ([1,2], 1),
    ([1,2], 2),
]

for lst, n in tests:
    head = list_to_linked(lst)
    res = linked_to_list(sol.removeNthFromEnd(head, n))
    print(f"{lst}, n={n}  ->  {res}")

# Time Complexity:	O(L) – single traversal
# Space	Complexity: O(1) – constant extra space