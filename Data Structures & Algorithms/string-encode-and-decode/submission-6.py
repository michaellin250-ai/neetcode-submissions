

class Solution:

    def encode(self, strs: List[str]) -> str:
        empty_string = ""
        for string in strs:
            empty_string += str(len(string)) + "#" + string
        return empty_string



    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length])
            i = 1 + j + length
        return result
        
        