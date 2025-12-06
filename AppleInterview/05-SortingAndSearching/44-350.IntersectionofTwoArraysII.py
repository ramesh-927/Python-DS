"""
Docstring for AppleInterview.05-SortingAndSearching.44-350.IntersectionofTwoArraysII

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the 
result must appear as many times as it shows in both arrays and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all 
elements into the memory at once?
"""
class Solution:
    def intersectTwo(self, nums1, nums2):
        # Step 1: sort both arrays first
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        i = j = 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:                     # nums1[i] == nums2[j]
                result.append(nums1[i])
                i += 1
                j += 1
        return result

# Test
sol = Solution()
print(sol.intersectTwo([1,2,2,1], [2,2]))          # [2, 2]
print(sol.intersectTwo([4,9,5], [9,4,9,8,4]))      # [4, 9]   

# Time Complexity : O(n + m) 
# Space Complexity : O(1)

# Default: hash map on smaller array → O(n+m).
# If sorted → two pointers for O(1) space.