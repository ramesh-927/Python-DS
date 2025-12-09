"""
Docstring for AppleInterview.07-Design.55.380.InsertDeleteGetRandomO(1)
Implement the RandomizedSet class:
1. RandomizedSet() Initializes the RandomizedSet object.
2. bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was 
not present, false otherwise.
3. bool remove(int val) Removes an item val from the set if present. Returns true if the item was 
present, false otherwise.
4. int getRandom() Returns a random element from the current set of elements (it's guaranteed that at 
least one element exists when this method is called). Each element must have the same probability of 
being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""
import random
class RandomizedSet:
    def __init__(self):
        self.idx_map = {}
        self.vals = []

    def insert(self, val):

        if val in self.idx_map:
            return False
        self.vals.append(val)
        self.idx_map[val] = len(self.vals) - 1
        return True
    
    def remove(self, val):

        if val not in self.idx_map:
            return False
        
        idx = self.idx_map[val]
        last_val = self.vals[-1]
        self.vals[idx] = last_val            # Swap with last
        self.idx_map[last_val] = idx         # Update index of last_val
        self.vals.pop()                      # Remove last
        del self.idx_map[val]                # Delete from map
        return True
        
    def getRandom(self):
        return random.choice(self.vals)

if __name__== "__main__":
    rs = RandomizedSet()
    print(rs.insert(1))   # True
    print(rs.insert(2))   # True
    print(rs.insert(1))   # False (already present)
    print(rs.getRandom()) # 1 or 2
    print(rs.remove(1))   # True
    print(rs.getRandom()) # 2

# Time Complexity: O(1) for each insert, remove, getRandom.
# Space Complexity: O(n), where n is the number of elements (stores them twice, essentially).
# Edge Cases Handled: Empty set, duplicates, removing non-existent, single element.

# For "insert/delete/random in O(1)" problems (like randomized sets or similar), the best approach 
# is always array + hashmap.
# Array for O(1) random access (via index).
# Hashmap for O(1) lookups and index tracking.
# Key trick: Swap-and-pop for deletion to avoid O(n) shifts in array.

# I used a list for O(1) random selection via indexing and a dictionary to map values to their list indices for O(1) lookups.
# For deletion, I swap the target with the last element, update the map, pop the last, and delete from 
# the map—ensuring no gaps and constant time.
