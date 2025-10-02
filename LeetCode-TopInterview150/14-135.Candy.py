"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
Constraints:
n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
***EASY Exaplnation *** -  https://www.youtube.com/watch?v=aIdVzwBEKM8
"""
class Solution:
    def candy(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0

        left = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1

        right = [1] * n
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1

        return sum(max(left[i], right[i]) for i in range(n))

if __name__== "__main__":
    sol = Solution()
    ratings = [1,0,2]
    result = sol.candy(ratings)
    print(result)

# Time complexity: O(n) — two linear passes and a linear sum.
# Space complexity: O(n) for the two auxiliary arrays (you can optimize to O(1) with a more advanced one-pass approach).
# I do a two-pass greedy: left-to-right to build minimal candies satisfying left neighbor, right-to-left for right neighbor, then take max per child. 
# It’s O(n) time and O(n) space and provably minimal because each pass gives a lower bound on any valid solution; taking the max meets both bounds.