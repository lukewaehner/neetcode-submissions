class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for l in range(len(prices) - 1):
            r = l + 1
            while r < len(prices):
                theorized = prices[r] - prices[l]
                profit = max(theorized, profit)
                r += 1

        return profit