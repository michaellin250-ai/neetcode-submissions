import string 


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freqs = defaultdict(int)
        for char in s:
            freqs[char] += 1
        
        freqt = defaultdict(int)
        for char in t:
            freqt[char] += 1
        
        return freqs == freqt