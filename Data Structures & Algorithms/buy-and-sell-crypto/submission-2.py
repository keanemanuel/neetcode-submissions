class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best, left, right = 0, 0, 0
        while right < len(prices):
            if len(prices) <= 1:
                return 0
            if left == right:
                right += 1
            diff = prices[right] - prices[left]
            if prices[right] - prices[left] <= 0: 
                left = right
                right += 1
            if diff > 0:
                right += 1
                if diff > best:
                    best = diff
        return best