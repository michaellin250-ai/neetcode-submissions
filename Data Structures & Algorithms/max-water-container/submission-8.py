class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        Res = 0

        while L < R: 
            Left = heights[L] 
            Right = heights[R]

            height = min(Left, Right)
            width = R - L 
            Res = max(Res, height * width) 
            
            if Left < Right:
                L += 1
            else:
                R -= 1

        return Res 

