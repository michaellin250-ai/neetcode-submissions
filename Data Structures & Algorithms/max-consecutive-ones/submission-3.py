class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        best_streak = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                counter = 0
            
            if counter > best_streak:
                best_streak = counter
        
        return best_streak