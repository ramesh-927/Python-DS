"""
You are a professional robber planning to rob houses along a street.Each house has a certain amount of money stashed, the only
constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of 
money you can rob tonight without alerting the police.
Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        rob1 = rob2 = 0
        # rob2 = max money we could rob up to house i-2
        # rob1 = max money we could rob up to house i-1

        for money in nums:
            current = max(money + rob2, rob1)
            rob2 = rob1   # move forward
            rob1 = current
        return current 
    
if __name__ == "__main__":

    print(Solution().rob([2,7,9,3,1]))   # 12
    print(Solution().rob([1,2,3,1]))     # 4
    print(Solution().rob([1]))           # 1
    print(Solution().rob([]))            # 0

# Time Complexity: O(n) – visit each house once
# Space Complexity: O(1) – only 2 variables