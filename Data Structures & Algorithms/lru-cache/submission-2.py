class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity 

    def get(self, key: int) -> int:
        #If our key doesn't exist, return -1 
        if key not in self.cache:
            return -1 
        
        #Key was just used so mark it as most recently used 
        self.cache.move_to_end(key)

        #Return that valuer
        return self.cache[key] 
        

    def put(self, key: int, value: int) -> None:
        #If key already exists, it is being updated, so mark it as most recently used 
        if key in self.cache:
            self.cache.move_to_end(key)

        #Insert or update the key-value pair 
        self.cache[key] = value 

        #If our capacity, remove least recently used item 
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

        
        
