class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l = 0
        charSet = set()
        result = 0 

        for r, char in enumerate(s):
            while char in charSet:
                charSet.remove(s[l]) 
                l += 1
            charSet.add(s[r])
            result = max(result, len(charSet))
        return result 

        
            
            

        # T: O(N) where N is the length of the string
        # S: O(N) 



        