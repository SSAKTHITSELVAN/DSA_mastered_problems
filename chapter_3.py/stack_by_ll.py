class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    """Replication of stack using the linked list"""
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def pop(self):
        poped_data = None
        if self.head is None:
            return -1
        else:
            poped_data = self.head.data
            self.head = self.head.next
        self.length -= 1
        return poped_data
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        return self.length
    
    def peek(self):
        if self.head is None:
            return -1
        return self.head.data


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # Output: 30
print(stack.pop())  # Output: 20
print(stack.peek()) # Output: 10
print(stack.size()) # Output: 1
print(stack.is_empty()) # Output: False
print(stack.pop())  # Output: 10
print(stack.is_empty()) # Output: True
print(stack.pop())  # Output: -1 (Underflow case)