"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
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
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache[key]
        # Remove and re-insert to mark as most recently used
        del self.cache[key]
        self.cache[key] = value
        return value

    def put(self, key, value):
        if key in self.cache:
            # Remove old value
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            # Remove least recently used item (first one)
            self.cache.popitem(last=False)
        # Insert as most recently used
        self.cache[key] = value

if __name__ =="__main__":
    lru = LRUCache(2)
    lru.put(1, 1)      # {1=1}
    lru.put(2, 2)      # {1=1, 2=2}
    print(lru.get(1))  # returns 1, order: {2=2, 1=1}
    lru.put(3, 3)      # removes 2 (oldest), adds 3 → {1=1, 3=3}
    print(lru.get(2))  # -1 (not found)
    print(lru.get(3))  # 3

# Operation	 Time	 Space
# get()	     O(1)	  Depends on capacity
# put()	     O(1)	  Depends on capacity