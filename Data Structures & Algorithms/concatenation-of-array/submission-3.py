class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #First, we need to create a new array that is double the length of the nums list.
        new_length = 2 * len(nums) #Create new array length, that is double the length of the old array
        new_array = [0] * new_length #fill the array with 0's, with our new length

        #Then, we need to iterate through the nums list. Assigning every value of the 
        #old array into our new array. While also ensuring, that the second half of our array
        #will also contain the array. We can do this, by doing the length of our new array 
        #plus i. And assigning that value to what the old array at I is.

        for i in range(len(nums)): #go through each number in our old array set.
            new_array[i] = nums[i] #Assign our first half of our new array with the numbers
            new_array[len(nums) + i] = nums[i] #Assign our second half of our new array with the numbers as well
        return new_array #Return the array



