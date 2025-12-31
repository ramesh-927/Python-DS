"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in 
reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum 
as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
   2 ->  4 ->  3
    5 ->  6 ->  4
-------------------
    7 ->  0 ->  8
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumber(self, l1, l2):

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

# Time Complexity: O(max(n, m)) – we traverse the longer list once, best possible since we must read all 
# digits.
# Space Complexity: O(max(n, m)) for the new list, which is unavoidable.

# For adding numbers represented as linked lists (especially reversed), the best algorithm is the "carry-over 
# simulation" or "digit-by-digit addition with carry." It's optimal because it avoids full number conversion 
# (which can be slow or overflow), works in linear time, and directly builds the result without extra 
# space beyond the output. Choose this for similar problems like adding arrays of digits or multi-precision 
# arithmetic.

# I used the carry-over addition method by iterating through both linked lists simultaneously, summing 
# digits with any carry, and building the result list on the fly. This achieves O(max(n, m)) time and 
# space, handling varying lengths and final carries efficiently.