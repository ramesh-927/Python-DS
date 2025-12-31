"""
Docstring for FacebookInterview.LeetCodeSolutions.02-LinkedLists.24-21.MergeTwoSortedLists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the 
first two lists.
Return the head of the merged linked list.
Example 1:

List1: 1 → 2 → 4
List2: 1 → 3 → 4
Result: 1 → 1 → 2 → 3 → 4 → 4

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
Input: list1 = [], list2 = []
Output: []
Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""
class ListNode:
    def __init__(self, val = 0 , next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next
# ----------------------- 
def printList(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
        print(res)

# Create test lists
a = ListNode(1, ListNode(2, ListNode(4)))
b = ListNode(1, ListNode(3, ListNode(4)))

sol = Solution()
merged = sol.mergeTwoLists(a, b)
printList(merged)

# Time Complexity: O(m + n) – You traverse each list at most once.
# Space Complexity: O(1) – Only a few extra variables (dummy and pointers); the output list is required 
# anyway.

# The best algorithm here is the two-pointer merge technique, inspired by the merge step in merge sort. 
# It's ideal for merging any two sorted structures (lists, arrays) because it exploits the pre-sorted 
# order to achieve linear time without extra space for temporary storage.

# I used a two-pointer approach to iteratively compare and link the smaller nodes from each sorted list, building 
# the merged list in-place. This achieves O(m + n) time and O(1) space, efficiently handling the sorted 
# inputs without additional sorting.