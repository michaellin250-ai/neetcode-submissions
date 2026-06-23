class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m 
            
            if nums[m] >= nums[l]: #This line tells us if we're in the left sorted array 
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1 
            

            else: #Right half is sorted 
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1 
