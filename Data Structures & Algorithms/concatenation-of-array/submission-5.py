class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if len(nums) < 0:
            return 0
        
        
        new_length = 2 * len(nums)
        new_array = [0] * new_length

        for i in range(len(nums)):
            new_array[i] = nums[i]
            new_array[len(nums) + i] = nums[i]
        return new_array