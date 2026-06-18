class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for number in nums:
            count[number] = 1 + count.get(number, 0) 
        for number, c in count.items():
            freq[c].append(number)
        
        result = [] 
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result


