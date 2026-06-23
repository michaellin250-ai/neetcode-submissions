class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict() 
        
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        
        #Key was just used so mark it as most recently 
        self.cache.move_to_end(key)

        #Return that value
        return self.cache[key]
        
        
        
       
        

    def put(self, key: int, value: int) -> None:
        #If our key already exists, its being updated so mark it as most recently
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value 
        
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
