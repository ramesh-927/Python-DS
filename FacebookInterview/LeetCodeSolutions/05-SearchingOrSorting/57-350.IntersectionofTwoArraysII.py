"""
Docstring for FacebookInterview.LeetCodeSolutions.05-SearchingOrSorting.57-350.IntersectionofTwoArraysII

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
from collections import Counter

class Solution:
    def interSect(self, nums1, nums2):
        count = Counter(nums1)
        result = []

        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1
        return result            

# If Arrays Are Sorted
# class Solution:
#    def interSect(self, nums1, nums2):
#        nums1.sort()
#        nums2.sort()
#        i = j = 0
#        result = []
#        while i < len(nums1) and j < len(nums2):
#            if nums1[i] < nums2[j]:
#                i += 1
#            elif nums1[i] > nums2[j]:
#                j += 1
#            else:
#                result.append(nums1[i])
#                i += 1
#                j += 1
#        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.interSect([1,2,2,1], [2,2]))         # [2, 2]
    print(sol.interSect([4,9,5], [9,4,9,8,4]))     # [9, 4]

# BEST AGLO : Use hash map (Counter or dict) → most practical, fastest in practice, clean code, handles 
# all cases perfectly.

# I used a hash map (Counter) to count occurrences in the first array, then iterated through the second 
# array, adding elements to the result only if their count is greater than zero and decrementing the 
# count each time.

# Time Complexity: O(n + m) – we go through both arrays exactly once.
# Space Complexity: O(min(n, m)) – the counter stores at most the smaller array's unique elements.
# This is the best general solution when arrays are unsorted.
