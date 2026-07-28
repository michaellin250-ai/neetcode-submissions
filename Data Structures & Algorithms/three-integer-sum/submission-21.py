class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() 

        for i, num in enumerate(nums):
            L = i + 1
            R = len(nums) - 1
            
            if i > 0 and nums[i] == nums[i - 1]: #skipping the first number 
                continue 
            
            while L < R:
                if num + nums[L] + nums[R] < 0:
                    L += 1
                elif num + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    result.append([num, nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L - 1]: #Skipping the inner numbers 
                        L += 1
        return result 
            
            

