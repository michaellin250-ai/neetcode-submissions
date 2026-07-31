class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        Max_left = height[l]
        Max_right = height[r]
        water = 0

        while l < r:
            if Max_left < Max_right:
                l += 1
                Max_left = max(Max_left, height[l])
                water += Max_left - height[l]
            else:
                r -= 1
                Max_right = max(Max_right, height[r])
                water += Max_right - height[r]
        return water 


    


