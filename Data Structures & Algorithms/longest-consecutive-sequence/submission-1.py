class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums) 

        for num in nums:
            if num - 1 not in num_set: #Only start counting when I'm the first number in sequence 
                length = 1 
                
                while num + length in num_set: #Keep extending as long as th enext consecutive number exists 
                    length += 1
                
                longest = max(longest, length)
        
        return longest 