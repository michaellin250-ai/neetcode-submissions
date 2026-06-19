class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_set = set(nums)
        longest = 0

        for num in max_set:
            if num - 1 in max_set:
                continue 
            length = 1
            longest = max(longest, length)

            while num + length in max_set:
                length += 1
                longest = max(longest, length)
        return longest 

        


       

       


        #We only start counting from numbers that have no predecessor (num - 1)
        #cause this prevents us from recounting the same sequence multiple times and keeps algorithm O(n)