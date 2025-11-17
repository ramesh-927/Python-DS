"""
A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list 
such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.
For example, if there are two nodes X and Y in the original list, where X.random --> Y, 
then for the corresponding two nodes x and y in the copied list, x.random --> y
Return the head of the copied linked list.
The linked list is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
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
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: Create new nodes interleaved with original nodes
        cur = head
        while cur:
            new_node = Node(cur.val, cur.next)
            cur.next = new_node
            cur = new_node.next

        # Step 2: Assign random pointers to the new nodes
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # Step 3: Separate the two lists
        cur = head
        copy_head = head.next
        copy = copy_head

        while copy.next:
            cur.next = cur.next.next
            copy.next = copy.next.next
            cur = cur.next
            copy = copy.next
        cur.next = None  # restore last link of original list
        return copy_head
# Example construction:
# Original: 1 -> 2 -> 3
# Random: 1->3, 2->1, 3->2

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next, n2.next = n2, n3
n1.random, n2.random, n3.random = n3, n1, n2

sol = Solution()
copy_head = sol.copyRandomList(n1)

# Verify the copy
cur = copy_head
while cur:
    rand_val = cur.random.val if cur.random else None
    print(f"Node({cur.val}) -> random({rand_val})")
    cur = cur.next
