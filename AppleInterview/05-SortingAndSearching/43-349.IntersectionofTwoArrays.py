"""
Docstring for AppleInterview.05-SortingAndSearching.43-349.IntersectionofTwoArrays
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

        nums1.sort()
        nums2.sort()
        result = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] == nums2[j]:
                if not result or result[-1] != nums1[i]:     # Skip duplicates
                    result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.interSection([1,2,2,1], [2,2]))   # Prints : [2]
    print(sol.interSection([4,9,5], [9,4,9,8,4]))    # Prints : [4, 9]
    print(sol.interSection([2,4,5,6,7,8], [8,2,5,6,7,9]))     # Prints : [2, 5, 6, 7, 8]

# Time Complexity : O(n log n + m log m) due to sorting.
# Space Complexity : O(1) extra (besides sorting space).

# I'd use Python sets for intersection since they're efficient (O(n + m) time) and handle uniqueness 
# automatically: convert both arrays to sets and return list(set1 & set2).
# Remembered a trick: if avoiding sets, sort both and use two pointers to merge uniques—skipping 
# duplicates while comparing.
