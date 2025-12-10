"""
Docstring for AppleInterview.001-AppleSpring23HighFrequency.07-4.MedianofTwoSortedArrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Ensure nums1 is smaller

        m, n = len(nums1), len(nums2)
        left, right, half_len = 0, m, (m + n + 1) // 2

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = half_len - partitionA

            maxLeftA = float('-inf') if partitionA == 0 else nums1[partitionA - 1]
            minRightA = float('inf') if partitionA == m else nums1[partitionA]
            maxLeftB = float('-inf') if partitionB == 0 else nums2[partitionB - 1]
            minRightB = float('inf') if partitionB == n else nums2[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 1:
                    return max(maxLeftA, maxLeftB)
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
            elif maxLeftA > minRightB:
                right = partitionA - 1
            else:
                left = partitionA + 1

        raise ValueError("Input arrays are not sorted.")  # Should never reach here

if __name__== "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1,3], [2]))  # prints 2
    print(sol.findMedianSortedArrays([1,2], [3,4]))   # prints 2.5

# Time: O(log(min(m, n))) – Super fast, as binary search halves the search space each step.
# Space: O(1) – No extra space needed beyond a few variables.

# I used binary search to find the optimal partition in the smaller array, ensuring the left halves of 
# both arrays are balanced for the median. This achieves O(log(min(m,n))) time by checking cross-partition 
# conditions and adjusting the search range accordingly.
