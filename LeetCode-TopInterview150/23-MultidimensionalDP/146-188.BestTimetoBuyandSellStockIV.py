"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
Find the maximum profit you can achieve. You may complete at most k transactions: 
i.e. you may buy at most k times and sell at most k times.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. 
Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Constraints:
1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""
class Solution:
    def maxProfit(self, k, prices):
        if not prices:
            return 0
        
        n = len(prices)
        # Special case: if k is very large, just add all upward moves
        if k >= n // 2:
            return sum(prices[i + 1] - prices[i] for i in range(n - 1) if prices[i + 1] > prices[i])
        
        # buy[j]: max profit after buying the j-th stock (we are holding it)
        # sell[j]: max profit after selling the j-th stock (we completed j transactions)
        buy = [float('-inf')] * ( k + 1)
        sell = [0] * (k + 1)
        # Initialize for 0 transactions
        buy[0] = float('-inf')  # can't buy if no transaction allowed
        sell[0] = 0             # no transaction = 0 profit

        for price in prices:
            for j in range(1, k + 1):
                # Option 1: Keep previous buy state
                # Option 2: Buy now, using profit from (j-1) sells
                buy[j] = max(buy[j], sell[j - 1] - price)
                # Option 1: Keep previous sell state
                # Option 2: Sell now (must have bought before)
                sell[j] = max(sell[j], buy[j] + price)

        return sell[k]
    
if __name__ =="__main__":
    sol = Solution()
    print(sol.maxProfit(2, [3, 2, 6, 5, 0, 3]))    # Output: 7
    print(sol.maxProfit(3, [1, 2, 4, 2, 5, 7, 2, 4, 9]))  # Output: 13 or 15
    print(sol.maxProfit(2, []))  # Output: 0

# Time Complexity: O(n × k)
# Space Complexity: O(n × k)


# Since k can be up to 100 and n ≤ 1000, O(nk) is perfect.
# If k is very large (≥ n/2), we can do unlimited transactions — just sum all positive differences.
# Otherwise, we use a space-optimized DP tracking the best buy/sell state for each transaction count.