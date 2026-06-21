class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        L = 0
        Total = 0

        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1
            charSet.add(s[R])
            Total = max(Total, R - L + 1)
        return Total 
            


        