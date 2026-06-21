class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break 
            
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]: #This determines if we want to go to our left side or our right side, if our value at mid is greater then our left side then that meaans we need to go to oru left side
                                     #To find our smallest value and if our value is less then the left side then tht means we should go to our right side 
                l = mid + 1 
            else:
                r = mid - 1
        return res 