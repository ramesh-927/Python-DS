"""
Docstring for AppleInterview.05-SortingAndSearching.38-4.MedianofTwoSortedArrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two 
sorted arrays.
The overall run time complexity should be O(log (m+n))
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
    def findMedianSortedArray(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            part1 = (left + right) // 2
            part2 = (m + n + 1) // 2 - part1

            maxLeft1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            minRight1 = float('inf') if part1 == m else nums1[part1]

            maxLeft2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            minRight2 = float('inf') if part2 == n else nums2[part2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                right = part1 - 1
            else:
                left = part1 + 1

        raise ValueError("Values are not sorted!")

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArray([1,3], [2]))  # -> 2.0
    print(sol.findMedianSortedArray([1,2], [3,4]))  # -> 2.5

# I used binary search on the smaller array to find a partition where every left element ≤ every right 
# element, then took either the max of lefts (odd) or the average of max(lefts) and min(rights) (even).
#  This yields O(log(min(m,n))) time and O(1) extra space.

#  Time Complexity :  O(log(min(m, n))) 
#  Space Complexity : O(1) 
