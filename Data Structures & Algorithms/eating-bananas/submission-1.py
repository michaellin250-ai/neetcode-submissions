class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) #Slowest speed and fastest speed 
        res = r#result is set to our fastest speed by default because we know that it would work automatically 

        while l <= r:#By default l <= r typical pattern 
            mid = (l + r) // 2 #calculate our mid point 
            hours = 0 #Set our hour to 0 
            for pile in piles: #For every pile in piles 
                hours += math.ceil(pile / mid) #Add onto our hours by whatever the pile is divided by our mid 

            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res 
        
                