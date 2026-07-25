
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        S_count, T_count = {}, {} 

        for i in range(len(s)):
            S_count[s[i]] = 1 + S_count.get(s[i], 0)
            T_count[t[i]] = 1 + T_count.get(t[i], 0)
        return S_count == T_count 
        