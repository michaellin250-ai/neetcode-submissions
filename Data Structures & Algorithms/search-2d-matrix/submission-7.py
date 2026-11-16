class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix) #Counts the inner arrays 
        num_cols = len(matrix[0]) #counts the elements in the first row 

        l = 0 
        r = num_rows * num_cols - 1 #Matrix 3 x 3 = 9 elements, indexes 0 - 8 

        while l <= r:
            m = (l + r) // 2
            value = matrix[m // num_cols][m % num_cols]
            #              row             column 
            if value < target:
                l = m + 1
            elif value > target:
                r = m - 1
            else:
                return True 
        return False 




