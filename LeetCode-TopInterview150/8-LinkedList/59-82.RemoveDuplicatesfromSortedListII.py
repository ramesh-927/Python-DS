"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.
Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def removeDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            if prev.next != curr:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next

# ___________________________________________________________________________
def list_to_linked(lst):
    dummy = ListNode(0)
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

def linked_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

sol = Solution()
tests = [
    [1,2,3,3,4,4,5],
    [1,1,1,2,3],
    [1,1,2,3,3],
    [1,2,2],
    [1,2,3,4,5],
]

for lst in tests:
    head = list_to_linked(lst)
    res = sol.removeDuplicates(head)
    print(f"{lst} -> {linked_to_list(res)}")
	
# Time Complexity	 :	O(n)	
# Space Complexity :  O(1)