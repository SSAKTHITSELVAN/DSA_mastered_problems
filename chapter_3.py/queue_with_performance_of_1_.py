"""Implementing the queue in way to reduce the time complexity"""

class Node:
    """node class"""
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Queue:
    """Representation of the queue"""
    
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            self.tail = self.head
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    def dequeue(self):
        if self.head == None:
            print("queue is out of order")
        else:
            self.head = self.head.next
            self.size -= 1
            if self.head is None:
                self.tail = None
    def is_empty(self):
        
        return not bool(self.head)
    
    def length(self):
        return self.size
    
    def print_q(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next


q = Queue()
print(" is empty -- ", q.is_empty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print("size -",q.size)
q.dequeue()
q.dequeue()
print("size -",q.size)
q.dequeue()
print(" is empty -- ", q.is_empty())
q.print_q()