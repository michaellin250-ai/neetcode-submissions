class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_set = {} #Val : index

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prev_set:
                return [prev_set[diff], i]
            prev_set[n] = i
        
        
        
            

            
