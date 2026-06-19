class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        max_left = height[L] #Tallest left wall I've seen 
        max_right = height[R] #Tallest right wall I've seen 
        result = 0

        while L < R:
            

            if max_left < max_right: #The left side is the bottleneck 
                L += 1
                max_left = max(max_left, height[L])
                result += (max_left - height[L]) #How much water we can hold 
            else: #The right side is the bottleneck 
                R -= 1
                max_right = max(max_right, height[R])
                result += (max_right - height[R])
        return result 
        




            
    


