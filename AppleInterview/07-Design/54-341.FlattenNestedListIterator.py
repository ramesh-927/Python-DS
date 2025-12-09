"""
Docstring for AppleInterview.07-Design.54-341.FlattenNestedListIterator
You are given a nested list of integers nestedList. Each element is either an integer or a list whose 
elements may also be integers or other lists. Implement an iterator to flatten it.
Implement the NestedIterator class:
1. NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
2. int next() Returns the next integer in the nested list.
3. boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.
Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by 
next should be: [1,1,2,1,1].
Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by 
next should be: [1,4,6].
Constraints:
1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-106, 106].

"""
# The NestedInteger interface is assumed provided by LeetCode:
#   - isInteger() -> bool
#   - getInteger() -> int
#   - getList() -> [NestedInteger]

class NestedIterator:
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]   # reverse so we can pop from end (LIFO)

    def next(self):
        # hasNext() guarantees top is integer, so safe to pop
        return self.stack.pop().getInteger()
    
    def hasNext(self):
        # Keep unfolding until we see an integer on top (or stack empty)
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            # It's a list → pop it and push its contents (reversed)
            self.stack.pop()
            self.stack.extend(top.getList()[::-1])
        return False
# I used a stack-based lazy iterator. I push the input list in reverse onto the stack, and in hasNext(), 
# I repeatedly pop nested lists and push their reversed contents until an integer is on top. 
# This gives O(1) amortized time per operation and O(depth) space — optimal for deep nesting.