"""
Docstring for LeetCode-Easy.Arrarys.01-485.MaxConsecutiveOnes
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):

        max_count = current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        return max_count

if __name__ == '__main__':

    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1,0,1,1,0,1]))
    print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))


# Time is O(n) – "n" is the array size, so for 10,000 items, it's just 10,000 steps. Space is O(1) – we 
# only use a couple of tiny counters, no extra lists.

# For finding the maximum consecutive elements (like streaks in binary arrays or subarrays with conditions), 
# the best algo is a linear scan with tracking variables. It's like a simplified sliding window: Use 
# two pointers or counters to track the "window" of consecutives without nested loops. This beats 
# brute force by avoiding redundant checks, making it O(n) time – perfect for arrays up to millions of 
# elements.

# I used a single-pass linear scan to iterate through the array once, maintaining a current streak counter 
# that increments on 1's and resets on 0's, while updating a maximum streak variable whenever the 
# current exceeds it. This achieves O(n) time and O(1) space, optimal for finding the longest consecutive 
# 1's without unnecessary recomputations.