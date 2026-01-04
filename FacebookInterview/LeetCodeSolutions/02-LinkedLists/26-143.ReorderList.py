"""
Docstring for FacebookInterview.LeetCodeSolutions.02-LinkedLists.26-143.ReorderList
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
Example 1:
1   ->  2   ->  3   ->  4
            |
            V
1   ->  4   ->  3   ->  2

Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:
1   ->  2   ->  3   ->  4   ->  5
            |
            V
1   ->  5   ->  2   ->  4   ->  3
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next:
        return
    
    # 1. Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # 2. Reverse second half
    prev, curr = None, slow.next
    slow.next = None  # Split into two lists
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    # 3. Merge two halves
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

# Time Complexity: O(n) - We traverse the list multiple times but each is O(n)
# Space Complexity: O(1) - Only using a few pointers, no extra memory

# Method used:
# i) Find middle using slow/fast pointers,
# ii) Reverse second half,
# iii) Merge two halves alternately.

# This achieves O(n) time and O(1) space by avoiding extra memory while rearranging nodes in-place.
# For reordering or rearranging linked lists (e.g., odd-even reorder, palindrome check), the best algo 
# is the "split-reverse-merge" pattern: use two pointers to split, reverse one part, then merge. It's 
# efficient (O(n) time, O(1) space) and handles edge cases like empty or single-node lists well.