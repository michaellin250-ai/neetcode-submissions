
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        countS, countT = defaultdict(int), defaultdict(int) 

        for character in s: 
            countS[character] += 1

        for character in t:
            countT[character] += 1
        
        return countS == countT
        
       



        
        