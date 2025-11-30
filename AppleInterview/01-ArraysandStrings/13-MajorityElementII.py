"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Example 1:
Input: nums = [3,2,3]
Output: [3]
Example 2:
Input: nums = [1]
Output: [1]
Example 3:
Input: nums = [1,2]
Output: [1,2]
Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
Follow up: Could you solve the problem in linear time and in O(1) space?
"""
class Solution:
    def findMajorityElements(self, nums):

        if not nums:
            return []
        
        candid1 = candid2 = None
        count1 = count2 = 0

        for num in nums:
            if candid1 == num:
                count1 += 1
            elif candid2 == num:
                count2 += 1
            elif count1 == 0:
                candid1, count1 = num, 1
            elif count2 == 0:
                candid2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        # Step 2: Verify the candidates
        return [ x for x in {candid1, candid2} if nums.count(x) > len(nums) // 3]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMajorityElements([3,2,3]))     # prints : 3
    print(sol.findMajorityElements([1]))         # Prints : 1
    print(sol.findMajorityElements([1,2]))       # Prints : [1, 2]

# Since an element appearing more than n/3 times can be at most two, I used the generalized 
# Boyer-Moore Voting algorithm with two candidates and two counters – it finds the possible 
# majorities in O(n) time and O(1) space. Then I do one verification pass to return only the real ones.

# Time Complexity :  – O(n) 
# Space Complexity : – O(1)

