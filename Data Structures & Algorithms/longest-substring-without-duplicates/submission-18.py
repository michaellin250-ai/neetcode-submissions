class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 #left pointer 
        longest = 0 #longest we've had so far
        string = "" #Holding the current window's characters 

        for r in range(len(s)): #l = 0, r = 0 
            while s[r] in string:
                string = string[1:] 
                l += 1
            
            string += s[r] 
            longest = max(longest, len(string)) 
        return longest 

            

        #pwwkew 
        #pwke
        

        



        