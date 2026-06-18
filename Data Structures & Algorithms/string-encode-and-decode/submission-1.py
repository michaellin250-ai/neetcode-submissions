

class Solution:

    def encode(self, strs: List[str]) -> str:
        #Convert list of strings to a string
        #First step is to create an empty sting cause for every string in the list of strings, we attach it to that empty_string
        empty_string = ""
        for string in strs:
            empty_string += f"{len(string)}#{string}"
        return empty_string



    def decode(self, s: str) -> List[str]:
        #Then convert that string back into a list of strings
        result = []
        i = 0
        
        while i < len(s):
            #Find the # to get the length
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            result.append(word)
            i = j + 1 + length
        return result
            #Slice out exactly that many characters after # 
            #Then move i foward to the start of the next word 
