"""
Docstring for AppleInterview.001-AppleSpring23HighFrequency.06-121.BestTimetoBuyandSellStock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different 
day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, 
return 0.
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
class Soltuion:
    def maxProfit(self, prices):

        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit

if __name__ == "__main__":
    sol = Soltuion()
    print(sol.maxProfit([7,1,5,3,6,4]))  # prints : 5
    print(sol.maxProfit([7,6,4,3,1]))    # Prints : 0


#  Time Complexity :         O(n) 
#  Space Complexity:         O(1) 

# buy/sell stock once for max profit" (or similar max difference problems), use a greedy one-pass scan. 
# It's greedy because you always grab the lowest buy price greedily as you go, ensuring optimal profit without revisiting.

#I used a greedy one-pass approach: Track the minimum price seen so far while iterating through the 
# array, and update the maximum profit if the current price minus min_price is higher. This gives O(n) 
# time and O(1) space, optimal for finding the best buy-sell pair without checking all combinations.


     