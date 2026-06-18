class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_for_s = {}
        for char in s:
            if char in char_count_for_s:
                char_count_for_s[char] += 1
            else:
                char_count_for_s[char] = 1

        char_count_for_t = {}
        for char in t:
            if char in char_count_for_t:
                char_count_for_t[char] += 1
            else:
                char_count_for_t[char] = 1

        if char_count_for_s == char_count_for_t:
            return True
        return False

