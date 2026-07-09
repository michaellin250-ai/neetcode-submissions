class MinStack:

    def __init__(self):
        #Self.stack allows us to do the other stuff 
        #Self.minStack keeps track of our smallest
        self.stack = []
        self.minStack = [] 

    def push(self, val: int) -> None:
        #For our self.stack pretty easy 
        self.stack.append(val)

        #Since in our min stack we want to gurantee we always get the smallest value we can just set this code up like this 
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] 
        

    def getMin(self) -> int:
        return self.minStack[-1]
