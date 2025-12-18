"""
Docstring for LeetCode-Easy.Arrarys.04-1089.DuplicateZeros
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements 
to the right.
Note that elements beyond the length of the original array are not written. Do the above modifications to
 the input array in place and do not return anything.
Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 9
"""
class Solution:
    def duplicateZeros(self, arr):
        
        n = len(arr)
        zeros = arr.count(0)
        i = n - 1
        j = n + zeros - 1

        while i >= 0 and j >= 0:
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            i -= 1
            j -= 1
        return arr

if __name__ == "__main__":
    sol =Solution()
    print(sol.duplicateZeros([1,0,2,3,0,4,5,0]))
    print(sol.duplicateZeros([1,2,3]))

# Time: O(n) – One pass to count zeros, one pass to modify the array.
# Space: O(1) – No extra space used beyond a few variables.

# For problems involving in-place array modifications with insertions or deletions (like duplicating or 
# removing elements), use backward traversal with a shift counter. This avoids overwriting unread data 
# and handles boundary truncations efficiently, achieving O(n) time and O(1) space.

# I used a backward traversal with a dynamic shift counter initialized to the total zero count. For each 
# element from the end, I shift it right by the current count if it fits, and for zeros, I place two 
# zeros (decrementing the count between placements) to simulate duplication without extra space.