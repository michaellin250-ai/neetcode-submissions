class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        max_left = height[L]
        max_right = height[R]
        result = 0

        while L < R:
            max_left = max(height[L], max_left) 
            max_right = max(height[R], max_right) 
            

            if max_left < max_right:
                L += 1
                max_left = max(max_left, height[L])
                result += (max_left - height[L])
            else:
                R -= 1
                max_right = max(max_right, height[R])
                result += (max_right - height[R])
        return result 
        




            
    


