class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = float('-inf')
        minPrice = float('inf')
        for idx, price in enumerate(prices):
            minPrice = min(price, minPrice)
            maxProfit = max(price - minPrice, maxProfit)
        return maxProfit

        