"""
Docstring for AppleInterview.001-AppleSpring23HighFrequency.05-206.ReverseLinkedList
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:
    1   ->  2   ->  3   ->  4   ->  5
                    ||
    5   ->  4   ->  3   ->  2   ->  1
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:
        1   ->  2
            ||
        2   ->  1
Input: head = [1,2]
Output: [2,1]
Example 3:
Input: head = []
Output: []
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseLinkedlist(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
        
if __name__== "__main__":
    # build list 1->2->3->None
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = Solution().reverseLinkedlist(a)

    # print result
    out = []
    cur = res
    while cur:
        out.append(str(cur.val))
        cur = cur.next
    print(" -> ".join(out) + " -> None") 

# Time Complexity: O(n) – We visit each node exactly once.
# Space Complexity: O(1) – No extra space proportional to input size; just a few variables.

# I used the iterative pointer reversal method, initializing previous as None and current as head, 
# then flipping next pointers in a loop while advancing. This achieves O(n) time and O(1) space, 
# making it optimal for interviews.