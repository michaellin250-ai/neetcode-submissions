class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest =  max(longest, length)
        return longest 
       

       


        #We only start counting from numbers that have no predecessor (num - 1)
        #cause this prevents us from recounting the same sequence multiple times and keeps algorithm O(n)