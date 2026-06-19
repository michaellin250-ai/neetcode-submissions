class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        max_left = height[L]
        max_right = height[R]
        result = 0 

        while L < R:
            max_left = max(max_left, height[L])
            max_right = max(max_right, height[R])

            if height[L] < height[R]:
                current = min(max_left, max_right) - height[L] 
                L += 1
            else:
                current = min(max_left, max_right) - height[R] 
                R -= 1
            result += current 
        return result 


    


