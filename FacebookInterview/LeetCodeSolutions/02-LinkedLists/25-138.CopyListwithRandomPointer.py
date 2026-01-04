"""
Docstring for FacebookInterview.LeetCodeSolutions.02-LinkedLists.25-138.CopyListwithRandomPointer

A linked list of length n is given such that each node contains an additional random pointer, which could 
point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,where each 
new node has its value set to the value of its corresponding original node. Both the next and random 
pointer of the new nodes should point to new nodes in the copied list such that the pointers in the 
original list and copied list represent the same list state. None of the pointers in the new list 
should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the 
corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.
The linked list is represented in the input/output as a list of n nodes. Each node is represented as a 
pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if 
it does not point to any node.
Your code will only be given the head of the original linked list.
Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Constraints:
0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""
class Node:
    def __init__(self, x, next= None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(head):
        if not head:
            return None
    
        # Step 1: Insert copies after each node
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
    
            # Step 2: Set random pointers for copies
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
    
        # Step 3: Separate the copied list
        curr = head
        copy_head = head.next
        copy_curr = copy_head
        while curr:
            curr.next = copy_curr.next
            curr = curr.next
            if curr:
                copy_curr.next = curr.next
                copy_curr = copy_curr.next
        return copy_head

# I used the interleaving nodes method: insert copy nodes after originals, set copy randoms using 
# original.random.next, then extract the copy list by rewiring next pointers. This achieves O(n) time 
# and O(1) space.

# Time is O(n) (three walks), space is O(1) (no extra storage beyond the clones themselves). It's the 
# best for interviews as it shows clever pointer tricks without hashes. Best algorithm for this kind of 
# problem (linked lists with extra pointers): Use "interleaving" or "weaving" to temporarily merge old 
# and new structures, adjust pointers in-place, then unwind. It avoids hash maps when space matters.