from collections import defaultdict 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #s1 = abc  , a:1, b:1, c: 1
        #s2 = abceeel , 
        s1_counts = defaultdict(int) #holds counts for all of s1
        s2_counts = defaultdict(int) #holds counts for only the current window in s2 

        #[a: 1, b:1, c:1] 
        for char in s1:
            s1_counts[char] += 1 
        
        l = 0 

        for r in range(len(s2)):
            s2_counts[s2[r]] += 1
        
            if r - l + 1 > len(s1):
                s2_counts[s2[l]] -= 1
                if s2_counts[s2[l]] == 0:
                    del s2_counts[s2[l]] 
                l += 1
        
            if r - l + 1 == len(s1):
                if s2_counts == s1_counts: 
                    return True 
        return False 
        
            