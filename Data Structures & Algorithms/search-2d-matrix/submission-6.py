class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        L, R = 0, (rows * cols) - 1

        while L <= R:
            mid = (L + R) // 2
            row = mid // cols
            col = mid % cols 

            if matrix[row][col] < target:
                L = mid + 1 
            elif matrix[row][col] > target:
                R = mid - 1
            else:
                return True
        return False 




            #Our mid point 
            #What row are we at? 
              #What col are we at? 

             #If our value at that specific part in the matrix is less then the target, increase our left pointer 
                
             #If our value at the specific part in the matrix is greater then the target, increase our right pointer 
                
           
                #If all goes well, return true but if not then return False
       
