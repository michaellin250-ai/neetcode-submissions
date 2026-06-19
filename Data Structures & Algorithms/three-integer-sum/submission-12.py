class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            first = nums[i] 
            L = i + 1
            R = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            while L < R:
                total = first + nums[L] + nums[R]
                if total < 0:
                    L += 1 
                elif total > 0:
                    R -= 1
                else:
                    result.append([first, nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
        return result 
                    
                    

                    
            



