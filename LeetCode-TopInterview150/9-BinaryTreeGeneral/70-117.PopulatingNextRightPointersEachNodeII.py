"""
Given a binary tree
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next; }
Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
#        1
#      / \ 
#      2   3
#     / \   \ 
#    4   5   7
Level 0: 1 -> None
Level 1: 2 -> 3 -> None
Level 2: 4 -> 5 -> 7 -> None
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. 
The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

"""
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root  # start of current level
        while head:
            dummy = Node(0)   # dummy head for next level
            tail = dummy     # tail builds the next level list
            node = head      # iterate current level using .next
            while node:
                if node.left:
                    tail.next = node.left
                    tail = tail.next
                if node.right:
                    tail.next = node.right
                    tail = tail.next
                node = node.next
            head = dummy.next  # move to first node of next level
        return root
def print_levels_with_next(root: Node):
    level_start = root
    while level_start:
        cur = level_start
        line = []
        next_level_start = None
        while cur:
            line.append(str(cur.val))
            if not next_level_start:
                # find the start of the next level (first existing child)
                next_level_start = cur.left or cur.right
            cur = cur.next
        print(" -> ".join(line) + " -> None")
        level_start = next_level_start

# Example usage:
# Build tree: [1,2,3,4,5,null,7]
n1 = Node(1)
n2 = Node(2); n3 = Node(3)
n4 = Node(4); n5 = Node(5); n7 = Node(7)
n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n3.right = n7

sol = Solution()
root = sol.connect(n1)
print_levels_with_next(root)
# Expected:
# 1 -> None
# 2 -> 3 -> None
# 4 -> 5 -> 7 -> None
# Time	O(n) — visit each node constant times
# Extra Space	O(1) auxiliary (dummy/tail pointers). Recursion stack not used.