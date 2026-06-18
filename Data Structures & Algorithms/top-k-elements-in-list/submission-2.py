class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for number in nums:
            count[number] += 1
        
        
        res = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        return res[:k]