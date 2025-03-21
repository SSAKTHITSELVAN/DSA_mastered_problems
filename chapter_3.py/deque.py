class Deque:
    """Deque implementation as a list"""
    
    def __init__(self):
        self.items = []
    
    def add_front(self, item):
        self.items.append(item)
    
    def add_rear(self, item):
        self.items.insert(0, item)
    
    def remove_front(self):
        return self.items.pop()
    
    def remove_rear(self):
        return self.items.pop(0)
    
    def is_empty(self):
        return not bool(self.items)
    
    def size(self):
        return len(self.items)


d = Deque()
print(d.is_empty())
print(d.add_rear(4))
print(d.add_rear("dog"))
print(d.add_front("cat"))
print(d.add_front(True))
print(d.size())
print(d.is_empty())
print(d.add_rear(8.4))
print(d.remove_rear())
print(d.remove_front())