class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = capacity

    def get(self, key: int) -> int:
        print(self.cache)
        if key not in self.cache:
            return -1
        else:
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val

            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache.keys()) == self.size:
                self.cache.pop(next(iter(self.cache)))
        
        self.cache[key] = value
