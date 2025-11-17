""" 
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:
Input: nums = [1,0,1,2]
Output: 3
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        numSet = set(nums)
        best = 0

        for num in numSet:
            if num - 1 not in numSet:
                current = num
                length = 1
                while current + 1 in numSet:
                    current += 1
                    length += 1
                if length  > best:
                    best = length
        return best 
    
if __name__== "__main__":
    sol = Solution()
    tests = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([], 0),
        ([1,2,0,1], 3),  # sequence 0,1,2
        ([9,1,4,7,3,-1,0,5,8,-1,6], 7)  # sequence 3,4,5,6,7,8,9
    ]
    for arr, expected in tests:
        result = sol.longestConsecutive(arr)
        print(f"{arr} -> {result} (expected {expected})")

# Time: O(n)	Building the set is O(n); each element is examined at most a constant number of times.
# Space: O(n)	The set stores at most n distinct numbers.