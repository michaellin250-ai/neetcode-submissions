class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        smallest = prices[0]

        for i in range(len(prices)):
            smallest = min(smallest, prices[i])

            profit = prices[i] - smallest

            max_profit = max(max_profit, profit)

        return max_profit 
        