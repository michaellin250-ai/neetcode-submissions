class Solution:
    def encode(self, strs: List[str]) -> str:
        
        #Convert the string into a string that cotnains the length of the string plus a # 
        #So for exampme ["Michael"]
        #O(N + M) because N is the total number of characters and m is the number of strings 

        #["Michael, Lin"] 
        #"7#Michael3#Lin"
        result = [] 
        for string in strs:
            encoded_string = str(len(string)) + "#" + string 
            result.append(encoded_string) 
        return "".join(result) 

        

    



    def decode(self, s: str) -> List[str]:
        result = [] 
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            number = int(s[i:j]) 
            string = s[j + 1: j + 1 + number] 
            result.append(string) 
            i = j + 1 + number 
        return result 

               
        