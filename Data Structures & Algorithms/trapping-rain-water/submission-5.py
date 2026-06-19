class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        max_left = height[L]
        max_right = height[R]
        result = 0

        while L < R:
            if max_left < max_right:
                L += 1
                max_left = max(height[L], max_left)
                result += (max_left - height[L]) #Add water trapped above the current bar 
            else:
                R -= 1
                max_right = max(height[R], max_right)
                result += (max_right - height[R]) #Add water trapped above the current abr 
        return result 


        




            
    


