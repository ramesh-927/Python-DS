"""
Given the head of a linked list and a value x, partition it such that all nodes less than x 
come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:
Input: head = [2,1], x = 2
Output: [1,2] 
Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):

        big_list = ListNode(0)
        small_list = ListNode(0)

        big = big_list
        small = small_list

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        big.next = None
        small.next = big_list.next
        return small_list.next
    
#------------------------------------------------------------

# Helper functions
def make_list(nums):
    dummy = ListNode(0)
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next

def to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

# Test
sol = Solution()
head = make_list([1, 4, 3, 2, 5, 2])
new_head = sol.partition(head, 3)
print(to_array(new_head))  # Output: [1, 2, 2, 4, 3, 5]

# Time Complexity:  O(n)
# Space Complexity:		O(1) (in-place)