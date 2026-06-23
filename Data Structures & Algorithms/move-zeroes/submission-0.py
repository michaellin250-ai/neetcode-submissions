class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                #We found a non-zero element 
                #Swap it with the lemenet at the 'l' position
                nums[l], nums[r] = nums[r], nums[l]

                l += 1
        