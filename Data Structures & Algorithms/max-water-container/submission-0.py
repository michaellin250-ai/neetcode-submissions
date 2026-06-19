class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1 
        product = 0

        while L < R:
            current_area = min(heights[L], heights[R]) * (R - L)
            if current_area > product:
                product = current_area
            
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return product

