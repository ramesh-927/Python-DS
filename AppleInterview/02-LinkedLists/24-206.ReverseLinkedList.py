"""
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
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        
        prev = None
        current = head

        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev
    
if __name__== "__main__":
    # build list 1->2->3->None
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = Solution().reverseList(a)

    # print result
    out = []
    cur = res
    while cur:
        out.append(str(cur.val))
        cur = cur.next
    print(" -> ".join(out) + " -> None")   # prints: 5 -> 4 -> 3 -> 2 -> 1 -> None

# Time Complexity : O(n) — one pass through the list 
# Space Complexity :  O(1) — constant extra space    

# I'll use the iterative three-pointer approach — maintain prev, curr, and temporarily store next to 
# reverse each link in O(1) space.
# It's optimal O(n) time and O(1) space, and safer than recursion for very long lists.
