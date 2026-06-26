class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() 


        for i in range(len(nums)):

            first = nums[i]
            l = i + 1
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            
            while l < r:
                if first + nums[l] + nums[r] < 0:
                    l += 1
                elif first + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    result.append([first, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return result 


                    
            



