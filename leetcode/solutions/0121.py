# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = math.inf

        for price in prices:
            min_price = price if price < min_price else min_price
            max_profit = price - min_price if price - min_price > max_profit else max_profit

        return max_profit
