class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        smallest = prices[0] 

        for i in range(len(prices)):
            smallest = min(smallest, prices[i])
            profit = prices[i] - smallest
            maxprofit = max(profit, maxprofit)
        return maxprofit 