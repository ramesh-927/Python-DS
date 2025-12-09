"""
Docstring for AppleInterview.07-Design.52-146.LRUCache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
1. LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
2. int get(int key) Return the value of the key if the key exists, otherwise return -1.
3. void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value 
pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least 
recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

"""
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):

        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):

        if key not in self.cache:
            return - 1
        self.cache.move_to_end(key)     # Make it most recently used
        return self.cache[key]

    def put(self, key, value):

        if key in self.cache:
            self.cache.move_to_end(key)     # Update and move to end
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)    # Remove least recently used (first item)

if __name__== "__main__":
    c = LRUCache(2)
    c.put(1, 1)       # cache: {1=1}
    c.put(2, 2)       # cache: {1=1, 2=2}
    print(c.get(1))   # returns 1, cache order -> {2=2, 1=1}
    c.put(3, 3)       # evicts key 2, cache -> {1=1, 3=3}
    print(c.get(2))   # returns -1 (not found)

# Time complexity: O(1) for both get and put operations (super fast, no loops that grow with size).
# Space complexity: O(capacity) to store the items.

# I used Python's OrderedDict, which combines a hash map for O(1) lookups with a doubly linked list 
# for maintaining order, allowing efficient moves to the most recent position and removal of the least 
# recent item.

# The best way is to use a hash map (like a quick-lookup dictionary) combined with a doubly linked 
# list (a chain of items where each points to the next and previous, allowing fast moves/removals 
# without shifting everything).