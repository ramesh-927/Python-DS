"""
Docstring for FacebookInterview.LeetCodeSolutions.07-Design.66-173.BinarySearchTreeIterator

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary 
search tree (BST):
1. BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given 
as part of the constructor. The pointer should be initialized to a non-existent number smaller than any 
element in the BST.
2. boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, 
otherwise returns false.
3. int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will 
return the smallest element in the BST.
You may assume that next() calls will always be valid. That is, there will be at least a next number in 
the in-order traversal when next() is called.
Example 1:
      7
     / \
    3   15
       /  \
      9    20
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
Constraints:
The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.

Follow up:
Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the 
height of the tree
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BST Iterator Implementation
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Helper function to build a simple BST for demo
def build_demo_bst():
    # Construct the following BST:
    #       7
    #      / \
    #     3   15
    #        /  \
    #       9    20
    n3 = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15, n9, n20)
    root = TreeNode(7, n3, n15)
    return root

# Main code to test the iterator
if __name__ == "__main__":
    root = build_demo_bst()
    iterator = BSTIterator(root)
    
    print("BST Iterator Output:")
    while iterator.hasNext():
        print(iterator.next())

# I used an iterative inorder traversal with a stack to simulate a BST iterator. This allows returning 
# the next smallest element in O(1) amortized time with O(h) space.

#  For iterating over a BST in sorted order without using extra space for all elements, the best algorithm 
# is to use a stack to control/simulate an in-order traversal. This is a standard technique for tree 
# iterators, as it leverages the BST's sorted property and avoids recursion (which could also use O(h) 
# stack space implicitly).

#| Operation | Time           | Space |
#| --------- | -------------- | ----- |
#| next()    | O(1) amortized | O(h)  |
#| hasNext() | O(1)           | O(h)  |
