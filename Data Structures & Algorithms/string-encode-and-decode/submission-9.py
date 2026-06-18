

class Solution:

    def encode(self, strs: List[str]) -> str:
       encoded_string = ""
       for string in strs:
            encoded_string += str(len(string)) + '#' + string
       return encoded_string

        #1.Create the empty string with ""
        #2.For every string in strs: obviously 
        #3.The encoded string since its a string we have to do a +=, and we have to do the length and a hashtag. 
        #Length is so we can count how many charcaters we should count within that string and the hashtag is like a separator. 
        # [Length]#[string]
        #4. Return the encoded_string 





    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            start = j + 1
            end = start + length 

            result.append(s[start:end])

            i = end 
        return result 

        #For decode.
        #1.Create the result with the list [] and create our i = 0
        #.2. Create the while loop, while its less then the len(s) the big string.
        #3. Since this is a pointer problem, we need j = i so that j can like be pushed to the hashtag. 
        #4. the length of the string is calculated by our i and the j being pushed until we found the hashtag.
        #5. Then the start we increase it by j + 1 and our end result is the start + length. 
        #6. Then we just append the result with our start to end, which is our string! 
        #7. Then we increment i = end so that we can move onto the next string. 
       
    
        
        