"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')    # initialize to infinity
        max_profit = 0              # no profit initially

        for price in prices:
            if price < min_price:
                min_price = price      # found a new lower buy price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit =  profit        # update max profit if better
        return max_profit
    
if __name__ == "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    res = sol.maxProfit(prices)
    print(res)

# Complexity
# Time: O(n) → single scan through the array
# Space: O(1) → just two variables
# Brute force: check every pair (buy, sell) → O(n²) time, O(1) space.
# Greedy one-pass (this solution):
# Keep track of the minimum price so far (min_price) and
# The maximum profit so far (max_profit).
# Each day is processed once, in constant work per step.
# Therefore, no faster exact algorithm exists, since you must at least look at every price once.