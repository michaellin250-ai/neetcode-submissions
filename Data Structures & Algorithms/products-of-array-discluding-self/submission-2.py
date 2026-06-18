class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        preFix = 1

        for i in range(len(nums)):
            result[i] = preFix
            preFix *= nums[i]
        
        proFix = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= proFix
            proFix *= nums[i]

        return result


        