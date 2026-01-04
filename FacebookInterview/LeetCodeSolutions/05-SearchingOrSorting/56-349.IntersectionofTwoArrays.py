"""
Docstring for FacebookInterview.LeetCodeSolutions.05-SearchingOrSorting.56-349.IntersectionofTwoArrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the 
result must be unique and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
class Solution:
    def interSection(self, nums1, nums2):

        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)

if __name__== "__main__":
    sol = Solution()
    print(sol.interSection([1,2,2,1], [2,2]))       # [2]
    print(sol.interSection([4,9,5], [9,4,9,8,4]))    # [9, 4]

# Time Complexity: O(n + m) on average, where n and m are the array lengths. (Worst case is rare and 
# still acceptable.) This is the best for this problem—much faster than brute force for big lists.
# Space Complexity: O(n + m), since we store the sets.

# For finding unique common elements between two arrays (intersection without duplicates), the best 
# algorithm is hash set intersection. Use hashing (via sets or dictionaries) for O(1) average lookups. 
# If arrays are sorted, you could use two pointers (O(n + m) time after sorting), but hashing is simpler 
# and faster in practice for unsorted data like this.

# I used Python sets to compute the intersection, converting both arrays to sets and using the '&' operator for overlap.
# This achieves O(n + m) average time complexity with O(n + m) space, efficiently handling uniques 
# and lookups via hashing.