class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        max_set = set(nums)

        for num in max_set:
            if num - 1 in max_set:
                continue 
            length = 1 
            longest = max(length, longest)
            
            while num + length in max_set:
                length += 1
                longest = max(length, longest)
        return longest 


        


       

       


        #We only start counting from numbers that have no predecessor (num - 1)
        #cause this prevents us from recounting the same sequence multiple times and keeps algorithm O(n)