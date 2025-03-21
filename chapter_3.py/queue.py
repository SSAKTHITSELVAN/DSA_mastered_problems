class Queue:
    """Abstract data structure of the queue"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, ele):
        self.items.insert(0, ele)
    
    def dequeue(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

queue = Queue()
print(queue.is_empty())
print(queue.enqueue(4))
print(queue.enqueue("dog"))
print(queue.enqueue(True))
print(queue.size())
print(queue.is_empty())
print(queue.enqueue(8.4))
print(queue.dequeue())
print(queue.dequeue())
print(queue.size())