class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s) 

        l = 0
        res = 0 
        charSet = set() #Keep track of characters we've seen so far

        for r, char in enumerate(s):
            #If the char is already in the set
            while char in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(char)

            res = max(res, r - l + 1) 
        return res 
        
            
            

        # T: O(N) where N is the length of the string
        # S: O(N) 



        