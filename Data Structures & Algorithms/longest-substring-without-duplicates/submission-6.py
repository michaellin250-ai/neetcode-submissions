class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        pos_dict = {}
        
        l = 0
        res = 0

        for r, char in enumerate(s):
            if char in pos_dict:
                if pos_dict[char] >= l:
                    l = pos_dict[char] + 1
            res = max(res, r - l + 1)

            pos_dict[char] = r
        return res
            

        # T: O(N) where N is the length of the string
        # S: O(N) 



        