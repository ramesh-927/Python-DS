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
class TreeNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = TreeNode()
        curr = dummy
        carry = 0

        while l1 and l2 and carry:
            val1 = l1.next if l1 else 0
            val2 = l2.next if l2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            curr.next = TreeNode(total % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        
# For adding numbers represented as linked lists (or arrays) in reverse order, always choose the 
# "digit-by-digit addition with carry propagation" algorithm. It's optimal because it handles arbitrary 
# lengths without overflow issues, is O(n) time, and easy to implement/extend (e.g., for non-reverse 
# order, reverse the lists first).

# Time Complexity: O(max(N, M))
# Space Complexity: O(max(N, M))