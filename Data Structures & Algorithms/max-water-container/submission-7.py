class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        res = 0 

        while L < R:
            height = min(heights[L], heights[R])
            width = R - L 
            area = height * width 

            res = max(res, area) 

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return res 
            
        
            