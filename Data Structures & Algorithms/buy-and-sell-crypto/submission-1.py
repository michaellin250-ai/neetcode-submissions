class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 #Best profit we have seen so far 
        minBuy = prices[0] #Cheapest price we have seen so far 

        for price in prices: #Go through every price and pretend what if i sell today
            maxP = max(maxP, price - minBuy) #Compare my current best profit with the profit I would make if I sold today 
            minBuy = min(minBuy, price) #
        return maxP

        #O(n) time complexity 
        