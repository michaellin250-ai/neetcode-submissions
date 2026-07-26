class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() 


        for i, num in enumerate(nums):
            if num > 0:
                break 
            
    

            if i > 0 and num == nums[i - 1]:
                continue 
            
            L = i + 1
            R = len(nums) - 1
            
            while L < R:
                current_sum = num + nums[L] + nums[R]
                if current_sum < 0:
                    L += 1
                elif current_sum > 0:
                    R -= 1
                else:
                    result.append([num, nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return result 



