"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).
Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 105
"""
class Solution:
    def maxProfits(self, prices):
        if not prices:
            return 0
    
        # These represent the max profit after certain actions
        first_buy = float('-inf')    # Max profit after buying 1st stock
        first_sell = 0               # Max profit after selling 1st stock
        second_buy = float('-inf')   # Max profit after buying 2nd stock
        second_sell = 0              # Max profit after selling 2nd stock
    
        for price in prices:
            # We can buy first stock (pay price) or do nothing
            first_buy = max(first_buy, -price)
        
            # Sell first stock: previous first_buy + current price
            first_sell = max(first_sell, first_buy + price)
        
            # Buy second stock: use profit from first sell, then pay for new stock
            second_buy = max(second_buy, first_sell - price)
        
            # Sell second stock: take second_buy profit + current price
            second_sell = max(second_sell, second_buy + price)
    
        return second_sell
    
if __name__ =="__main__":
    sol = Solution()
    print(sol.maxProfits([3,3,5,0,0,3,1,4])) # prints 6
    print(sol.maxProfits([1,2,3,4,5])) # prints 4
    print(sol.maxProfits([7,6,4,3,1])) # prints 0
    
# Time Complexity: O(n)
# Space Complexity: O(1)

# We do a single linear scan maintaining four state variables: best cost and profit after the 
# first transaction, and best effective cost and profit after the second. 
# This compresses the DP into O(1) space and yields the maximum profit for up to two transactions 
# in O(n) time.