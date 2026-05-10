# ============================================
# BEST TIME TO BUY AND SELL STOCK
# Link: leetcode.com/problems/best-time-to-buy-and-sell-stock/
# ============================================

# ---------------------------
# Approach 1: Brute Force
# Time: O(n²) | Space: O(1)
# ---------------------------
# This approach is not efficient because it checks every possible pair of buy and sell prices,
# leading to O(n²) time complexity.

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         for i in range(len(prices)):
#             buy_price = prices[i]
#             for j in range(i+1, len(prices)):
#                 max_profit = max(max_profit, prices[j] - buy_price)
#         return max_profit

# ---------------------------
# Approach 2: Sliding Window
# Time: O(n) | Space: O(1)
# ---------------------------

'''
--- Submission 1 : Wrong Answer ❌
Thought: find global min to buy, global max to sell.
Trap: max price might come BEFORE min price — can't sell before buying!

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Buy = min(prices)
        if Buy == prices[-1]:
            return 0
        else:
            Sell = max(prices)
            while prices.index(Sell) < prices.index(Buy):
                prices.remove(Sell)
                Sell = max(prices)
            Profit = Sell - Buy
            return Profit

--- Submission 2: Accepted ✅ (53ms)
Used float('inf') as starting minimum — safer than prices[0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit

--- Submission 3: Accepted ✅ (42ms)
Added empty list edge case check — squeezed out extra milliseconds!

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
'''

# This approach is efficient because it iterates through the list once,
# keeping track of the minimum price seen so far and
# calculating the maximum profit at each step.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]  # start with first day as minimum
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price  # update minimum
            else:
                max_profit = max(max_profit, price - min_price)  # calculate profit and update maximum
        return max_profit
    
# What I learned:
# - Finding global min and max is a trap — order matters in this problem.
# - Sliding window tracks min price seen so far, updating max profit each step.
# - float('inf') is a safer initialiser than prices[0] for minimum tracking.