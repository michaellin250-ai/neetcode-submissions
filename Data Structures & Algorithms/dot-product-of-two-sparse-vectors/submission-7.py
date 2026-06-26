class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []

        for i, num in enumerate(nums):
            if num != 0:
                self.nums.append((i, num))
                
        
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0 
        i = 0
        j = 0 

        while i < len(self.nums) and j < len(vec.nums):
            i_index, i_num = self.nums[i]
            j_index, j_num = vec.nums[j]

            if i_index == j_index: #Our indexs are compatible
                dot_product += (i_num * j_num) 
                i += 1
                j += 1
            elif i_index > j_index:
                j += 1
            else:
                i += 1 
        return dot_product 
        
        #O(N + M) time complexity
        #O(N + M) space complexity 
       
            
        
        
        


#[<0, 1>, <3, 2>, <4, 3>]
#[<1, 3>, <3, 4>]
#dot_product = 8
#
#i = 2 j = 2
#
#3, 2
#3, 4


#O(N + M) N is the number of elements in the first input list and m is the number of elements in the second input list
#O(N + M)
#naive solution is just going through every index/number for dot product, hashsmap like if our hashmap sucks then we spend alot of time just iterating through
#so we use our tuple
#If one of our vectors is sparse then use binary search. 