from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int) 
        result = [] 

        for num in nums:
            counts[num] += 1
        
        
        #The bucket index is how many times a number appears 
        #For ex {5: 3, 8: 1} buckets[3] = [5] and buckets[1] = [8]
        buckets = [[] for i in range(len(nums) + 1)] 
        
        for num, frequency in counts.items():
            buckets[frequency].append(num) 

        #[[], [8], [], [5], []] 

        for i in range(len(buckets) -1, -1, -1):
            for num in buckets[i]:
                result.append(num) 

                if len(result) == k:
                    return result 

        #Count each number
        #Group numbers by frequency 
        #Scan from highest frequency down
        #Stop after collecting k numbers 




        



