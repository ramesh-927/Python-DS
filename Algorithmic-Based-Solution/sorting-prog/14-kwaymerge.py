import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        node = self
        while node:
            result.append(str(node.val))
            node = node.next
        return " -> ".join(result)

def merge_k_elements(lists):
    heap = []
    for i , node in enumerate(lists):
        if node:
            heapq.heappush(heap,(node.val, i ,node))
    
    dummy = ListNode(0)
    current = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next


        