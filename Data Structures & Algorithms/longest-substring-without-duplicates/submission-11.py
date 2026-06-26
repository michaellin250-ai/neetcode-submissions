class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l = 0
        result = 0
        charSet = set()

        for r, char in enumerate(s):
            while char in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
        return result 
        
        #O(n) depending on the length of our string
        #O(n) because of our charSet 
        
        #The way our solution works, is that first we have our edge case of if our len(s) is less or equal to 1
        #In the case of that just reutrn the lenght of it
        #Then we do a sliding window approach, where we set up our l, result, and charSet to keep track of the characters
        #Then we do a for loop, with r to push our sliding window to the rgiht. So in our for loop, we have a while loop
        #That while loop wll keep check of if our char is in the charSet: then we will remove it from our left pointer cause 
        #That 
            

        

        