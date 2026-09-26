class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        best_profit = 0

        for price in prices[1:]:
            best_profit = max(best_profit, price - min_price)
            min_price = min(min_price, price)

        return best_profit