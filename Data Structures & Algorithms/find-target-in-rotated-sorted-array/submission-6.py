class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]: #If the left side is sorted 
                if target > nums[m] or target < nums[l]: #If our target > mid or target < left pointer 
                    l = m + 1 #Target is outside the sorted left range 
                else:
                    r = m - 1 #Target is inside the sorted left range 

            else: #If the right side is sorted 
                if target < nums[m] or target > nums[r]:
                    r = m - 1 #Target is outside the sorted right range 
                else:
                    l = m + 1 #Target is inside the sorted right range 
        return -1 
