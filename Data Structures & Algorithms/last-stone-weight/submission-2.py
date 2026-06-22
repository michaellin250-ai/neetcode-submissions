class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1: #Ensure's that we have two stones 
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0) #Just incase if our stones is empty, we should add 0 
        return abs(stones[0]) #Return our negative number turn it into absolute value. Or returns 0 if nothing haha 
