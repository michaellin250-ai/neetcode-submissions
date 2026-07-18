from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count how many times each number appears
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        # Step 2: Create buckets
        # buckets[f] will contain all numbers that appear exactly f times
        buckets = [[] for i in range(len(nums) + 1)]

        # Step 3: Put each number into the bucket matching its frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 4: Go through buckets from high frequency to low frequency
        # and collect the top k frequent numbers
        res = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res


        