"""
Floyd’s Cycle Detection Algorithm, also known as the Tortoise and Hare Algorithm, 
detects a cycle in a linked list (or sequence) by using two pointers moving at different speeds. 
If a cycle exists, the pointers will eventually meet. Heres how it works.
Explanation
Two pointers: The "tortoise" moves one step at a time, and the "hare" moves two steps at a time.
Cycle detection: If the hare catches up to the tortoise (i.e., they point to the same node), a cycle exists.
No cycle: If the hare reaches the end (null in a linked list or undefined in a sequence), there’s no cycle.
Optional: The algorithm can also find the cycle’s starting point and length.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def floyd_cycle_detection(head):
    # Handle empty list or single node
    if not head or not head.next:
        return False, None  # No cycle, no meeting point
    
    tortoise = head
    hare = head

    # Phase 1: Detect cycle
    while hare and hare.next:
        tortoise = tortoise.next      # Move one step
        hare = hare.next.next         # Move two steps
        if hare == tortoise:          # Meeting point found
            break
    else:
        return False, None            # No cycle if hare reaches end
    
    # Phase 2: Find cycle start
    tortoise = head
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next
    meeting_point = tortoise

    # Phase 3: Find cycle length
    cycle_length = 1
    hare = hare.next
    while hare != tortoise:
        cycle_length += 1
        hare = hare.next
    return True, meeting_point, cycle_length

def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    head = Node(values[0])
    current = head
    cycle_node = None
    # Keep track of all nodes to find the cycle node later
    nodes = [head]
    
    # Create the linked list
    for i in range(1, len(values)):
        current.next = Node(values[i])
        current = current.next
        nodes.append(current)
        if i == pos:  # Store the node where cycle should start
            cycle_node = current
    
    # Create cycle if pos is valid
    if pos >= 0 and cycle_node:
        current.next = nodes[pos]  # Link last node to cycle start
    
    return head

# Test
if __name__ == "__main__":
    values = [3, 2, 0, -4]
    pos = 1  # Cycle starts at index 1 (node with value 2)
    head = create_linked_list_with_cycle(values, pos)
    has_cycle, meeting_point, cycle_length = floyd_cycle_detection(head)
    print("Cycle exists:", has_cycle)
    print("Meeting point value:", meeting_point.value if meeting_point else None)
    print("Cycle length:", cycle_length if has_cycle else None)


