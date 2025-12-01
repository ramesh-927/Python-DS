"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored 
in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the 
sum as a linked list.
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
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1:
                l1 = l1.next   
            if l2:
                l2 = l2.next  
        return dummy.next

# --- helpers for testing / printing in "LeetCode style" ---
def build_list(nums):
    """Create linked list from Python list, return head (ListNode)."""
    dummy = ListNode(0)
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next

def to_pylist(node):
    """Convert ListNode to Python list like LeetCode prints."""
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out

if __name__ == "__main__":
    sol = Solution()

    # example inputs (LeetCode example)
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    res = sol.addTwoNumbers(l1, l2)
    print(to_pylist(res))   # prints: [7, 0, 8]

# Time Complexity: O(max(N, M))
# Space Complexity: O(max(N, M))

#"I traverse both linked lists simultaneously, adding corresponding digits plus carry, and build the 
# result list on the fly using a dummy head.
# I handle remaining nodes and final carry in the same loop — runs in O(max(N,M)) time and is the 
# standard optimal approach for this problem."