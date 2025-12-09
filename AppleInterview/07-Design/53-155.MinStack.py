"""
Docstring for AppleInterview.07-Design.53-155.MinStack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
1. MinStack() initializes the stack object.
2. void push(int val) pushes the element val onto the stack.
3. void pop() removes the element on the top of the stack.
4. int top() gets the top element of the stack.
5. int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]
Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""
class MinStack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self):
        if self.stack:
            self.stack.pop() 

    def top(self):
        return self.stack[-1][0] if self.stack else -1

    def getMin(self):
        return self.stack[-1][1] if self.stack else -1

if __name__ == "__main__":
    ms = MinStack()
    ms.push(3)
    ms.push(5)
    ms.push(2)
    print(ms.getMin())  # 2
    ms.pop()
    print(ms.getMin())  # 3
    print(ms.top())     # 5

# Time complexity: O(1) for push, pop, top, getMin.
# Space complexity: O(n), where n is the number of elements (we store extras, but it's minimal).

# I used a single stack storing tuples of (value, current_min), updating the min on each push by 
# comparing with the previous min.
# This ensures all operations (push, pop, top, getMin) run in O(1) time with O(n) space, making it 
# efficient and simple.