"""
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
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        while low <= high:
            # Partition point in nums1
            part1 = (low + high) // 2
            # Corresponding partition in nums2
            part2 = (m + n + 1) // 2 - part1
        
            # Handle edge cases: left/right of partition
            left1  = float('-inf') if part1 == 0 else nums1[part1 - 1]
            right1 = float('inf')  if part1 == m else nums1[part1]
            left2  = float('-inf') if part2 == 0 else nums2[part2 - 1]
            right2 = float('inf')  if part2 == n else nums2[part2]
        
            # Valid partition?
            if left1 <= right2 and left2 <= right1:
                # Odd total length → median is max of left halves
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                # Even → average of max(left) and min(right)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            # Move search: need more from nums1
            elif left1 > right2:
                high = part1 - 1
            # Need more from nums2
            else:
                low = part1 + 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1,3], [2]))         # 2.0
    print(sol.findMedianSortedArrays([1,2], [3,4]))       # 2.5
    print(sol.findMedianSortedArrays([], [1]))            # 1.0
           

# Time complexity	O(log(min(m, n)))
# Space complexity	O(1) (constant extra space)
