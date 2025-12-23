"""
Docstring for LeetCode-Easy.Arrarys.14-487.MaxConsecutiveOnesII
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip 
at most one 0.
Example 1:
Input: nums = [1,0,1,1,0]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.
Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you 
can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve 
it efficiently?
"""
class Solution:
    def maxConsecutiveOnes(self, nums):
        left = zeros = max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
    
if __name__== "__main__":
    sol = Solution()
    print(sol.maxConsecutiveOnes([1,0,1,1,0,1]))        # Print : 4
    print(sol.maxConsecutiveOnes([1,0,1,1,0]))         # Print : 4

# I used the sliding window technique with two pointers to maintain a subarray containing at most 
# one zero, expanding the right pointer and shrinking from the left when needed. This achieves O(n) 
# time complexity and O(1) space, efficiently finding the maximum length after at most one flip.

# Why this is the best algorithm for this kind of problem: Problems like finding the longest subarray 
# with at most K constraints (here, K=1 for zeros) are perfect for sliding window with two pointers.
# It avoids rechecking parts of the array, making it optimal for interviews where time efficiency 
# matters.