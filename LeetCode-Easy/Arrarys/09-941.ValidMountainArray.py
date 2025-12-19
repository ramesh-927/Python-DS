"""
941. Valid Mountain Array.
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Example 1:
Input: arr = [2,1]
Output: false
Example 2:
Input: arr = [3,5,5]
Output: false
Example 3:
Input: arr = [0,3,2,1]
Output: true
Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 104
"""
class Solution:
    def VaildMountain(self, arr):
        if len(arr) < 3:
            return False
        
        left, right = 0, len(arr) - 1
        while left < len(arr) - 1 and arr[left] < arr[left + 1]:
            left += 1
        while right > 0 and arr[right - 1] > arr[right]:
            right -= 1
        
        return left == right and left > 0 and left < len(arr) - 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.VaildMountain([0,3,2,1]))
    print(sol.VaildMountain([3,5,5]))

# The optimal approach uses a two-pointer technique to simulate climbing the mountain from both ends 
# in a single effective pass. This is the best algorithm for this kind of problem (validating a 
# unimodal sequence with a single peak), as it efficiently checks the increasing and decreasing parts 
# without redundant scans. It achieves the best time complexity of O(n) (we traverse the array at 
# most twice) and O(1) space, with minimal code—just a few lines.

