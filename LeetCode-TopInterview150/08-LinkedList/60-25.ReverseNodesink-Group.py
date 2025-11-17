"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
Follow-up: Can you solve the problem in O(1) extra memory space?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        if k <= 1 or not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Check if there are k nodes ahead
            kth = group_prev
            count = 0
            while count < k and kth:
                kth = kth.next
                count += 1
            if not kth:  # fewer than k nodes remaining
                break

            group_start = group_prev.next
            # Reverse the group by moving nodes after group_start to after group_prev
            curr = group_start
            for _ in range(k - 1):
                nxt = curr.next
                # remove nxt
                curr.next = nxt.next
                # insert nxt right after group_prev
                nxt.next = group_prev.next
                group_prev.next = nxt

            # after reversing, group_start is the tail of the group
            group_prev = group_start

        return dummy.next

# Helper utilities for testing
def build_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def list_to_pylist(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

# Example usage:
if __name__ == "__main__":
    sol = Solution()

    head = build_list([1,2,3,4,5])
    out = sol.reverseKGroup(head, 2)
    print(list_to_pylist(out))  # -> [2,1,4,3,5]

    head = build_list([1,2,3,4,5])
    out = sol.reverseKGroup(head, 3)
    print(list_to_pylist(out))  # -> [3,2,1,4,5]

# Time	O(n) — each node is visited and moved a constant number of times
# Extra Space	O(1) — only a few pointers (dummy, group_prev, curr, nxt, kth) used