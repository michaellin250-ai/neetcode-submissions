class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_val = 0

        if len(nums) == 0:
            return 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            elif nums[i] == 0:
                counter = 0 
            
            if counter > max_val:
                max_val = counter
        
        return max_val