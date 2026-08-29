class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.cap = capacity
        self.q = collections.deque()
        

    def get(self, key: int) -> int:
        print(self.d)
        if key in self.d:
            #need to del from q and readd to maintain use order
            self.q.remove(key)
            self.q.append(key)
            return self.d[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        if key not in self.q:
            self.q.append(key)
        else:
            self.q.remove(key)
            self.q.append(key)
            
        if len(self.q) > self.cap:
            k = self.q.popleft()
            del self.d[k]

        
