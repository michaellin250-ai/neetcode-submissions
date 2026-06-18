

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
        #1. First we initialize our result = [], with i = 0
        #2. Create the while loop, while i < len(s): we also have to initalize j = i, cause we need our pointer to find the hashtag
        #3. Create the while s[j] != "#": j += 1
        #4.Then find the length of our string, by doing length = int(s[i:j])
        #5. Then we initalize our start to be j + 1, and our ending to be start + the length 
        #6. Then we append the string to our result utilizing result.append(s[start:end])
        #7. Make sure ot initalize i = end so that our i can keep moving foward throughout the string
        #8. Then return our result 
    
        
        