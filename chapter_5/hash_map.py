class HashTable:
    """ABT of dictionary"""
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def put(self, key, value):
        """computes the hash value and then adds"""
        
        hash_code = self.hashing(key, len(self.slots))
        
        if self.slots[hash_code] is None:
            self.slots[hash_code] = key
            self.data[hash_code] = value
        
        else:
            if self.slots[hash_code] == key:
                self.data[hash_code] = value
            else:
                rehash_code = self.linear_probing(key, len(self.slots))
                
                while(self.slots[rehash_code] is not None and self.slots[rehash_code] != key):
                    rehash_code = self.linear_probing(rehash_code, len(self.slots))
                
                if self.slots[rehash_code] is None:
                    self.slots[rehash_code] = key
                    self.data[rehash_code] = value
                else:
                    self.data[rehash_code] = value
    
    
    def delete(self, key):
        hash_code = self.hashing(key, len(self.slots))
        
        position = hash_code
        while self.slots[position] is not None:
            if self.slots[position] == key:
                print(f"{self.slots[position]} -- {self.data[position]}  is deleted successfully")
                self.slots[position] = None
                self.data[position] = None
                return
            else:
                position = self.linear_probing(position, len(self.slots))
            
            if position == hash_code:
                break
        raise ValueError("Element not found...")
    
    
    def get(self, key):
        """Return the value associated"""
        hash_code = self.hashing(key, len(self.slots))
        
        if self.slots[hash_code] == key:
            return self.data[hash_code], None
        else:
            rehash_code = self.linear_probing(key, len(self.slots))
            
            limit = 0
            while self.slots[rehash_code] != key:
                limit += 1
                if self.slots[rehash_code] is None:
                    return (None, f"you not added it -- {rehash_code}")
                rehash_code = self.linear_probing(rehash_code, len(self.slots))
                if limit == len(self.slots):
                    return (None, "we checked every keys, but not found")
            
            return (self.data[rehash_code], None)
    
    
    def hashing(self, key, size):
        """simple remainder hashing"""
        return (key % size)
    
    def linear_probing(self, key, size):
        """key + 1 remainder for probing"""
        return ((key + 1 ) % size)
    
    def show(self):
        """displaying the key value pairs"""
        res = "{ "
        for i in range(self.size):
            res += f"({self.slots[i]} : {self.data[i]}), "
        res += "}"
        return res

a = HashTable()
a.put(61, 11)
a.put(62, 22)
a.put(60, 100)
a.put(63, 33)
a.put(64, 44)
a.delete(64)
print(a.show())
