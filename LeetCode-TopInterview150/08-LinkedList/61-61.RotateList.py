"""
Given the head of a linked list, rotate the list to the right by k places.
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1] 
Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Connect tail to head (circular)
        tail.next = head

        # Step 3: Find new tail -> (length - k % length - 1)th node
        k = k % length
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # Step 4: New head is next of new_tail
        new_head = new_tail.next
        new_tail.next = None  # Break the circle

        return new_head

def build_list(values):
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals

sol = Solution()
tests = [
    ([1,2,3,4,5], 2),
    ([0,1,2], 4),
]

for vals, k in tests:
    head = build_list(vals)
    res = sol.rotateRight(head, k)
    print(f"{vals}, k={k}  ->  {print_list(res)}")
# Time Complexity : O(n)
# Space Complexity: O(1)