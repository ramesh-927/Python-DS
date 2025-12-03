"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of 
the first two lists.
Return the head of the merged linked list.
Example 1:
            1   ->  2   ->  4
            1   ->  3   ->  4
--------------------------------------
    1   ->  1   ->  2   ->  3   ->  4   ->  4
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
Input: list1 = [], list2 = []
Output: []
Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwolist(self, list1, list2):
        
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
        return dummy.next

# Time Complexity: O(n + m) – where n and m are lengths of the two lists
# Space Complexity: O(1) – only using a few pointers (best possible!)

# "I used the classic two-pointer iterative merge technique – just like merging in merge sort.
# We maintain a pointer for each list and always attach the smaller current node to the result, 
# achieving O(n+m) time and O(1) extra space."