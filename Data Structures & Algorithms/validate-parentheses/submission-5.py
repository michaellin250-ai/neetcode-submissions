class Solution:
    def isValid(self, s: str) -> bool:
    
    #Stack makes sense for this problem, becuase of the LIFO. For example if we have like
    #"[ and ]" than that means our ] is the one thats closing it so we need a stack to utilize that.
    
        stack = []
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
    
        #Now we will iterate through our string 
        for c in s:

            if c in matching:

                if not stack:
                    return False 
            
                if stack[-1] != matching[c]:
                    return False 

                stack.pop()
            else:
                stack.append(c) 
    
        return len(stack) == 0 
        


