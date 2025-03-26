class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """Replication of Queue using the linked list"""
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def enqueue(self, item):
        new_node = Node(item)
        
        current = self.head
        self.length += 1
        if current is None:
            self.head = new_node
            return
        
        while current.next is not None:
            current = current.next
        
        current.next = new_node
    
    def dequeue(self):
        if self.head is None:
            raise IndexError("Index out of bound...")
        
        dequeued_data = self.head.data
        self.head = self.head.next
        
        self.length -= 1
        return dequeued_data
    
    def size(self):
        return self.length
    
    def peek(self):
        if self.head is not None:
            return self.head.data
        return -1
    
    def is_empty(self):
        return self.head is None

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  # Output: 10
print(q.peek())     # Output: 20
print(q.size()) # Output: 2
print(q.is_empty()) # Output: False
