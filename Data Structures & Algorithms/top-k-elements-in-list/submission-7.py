class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        result = sorted(count.keys(), key = lambda x: count[x], reverse = True)
        return result[:k]
        #1.Count.keys() gives all unique numbers
        #2. key = lambda x: count[x] tells python: "When comparing two numbers, compare their frequencies instead."
        #3. Sorted() orders them by those frequencies
        #4. Reverse=True makes the highest frequencies come first 
        #5. res[:k] grabs the first k most frequent elements 
        