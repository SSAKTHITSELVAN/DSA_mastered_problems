class Queue:
    """Two stack queue implementation"""
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, item):
        self.stack1.append(item)  # O(1)
    
    def dequeue(self):
        if not self.stack2:  # Transfer only if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())  # No need to reverse
        
        if not self.stack2:
            raise ValueError("Queue is empty")  # Correct message
        
        return self.stack2.pop()  # O(1) (not pop(0))

    def show_all(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())  # No need to pop(0)

        for i in reversed(self.stack2):  # Print in correct order
            print(i, end=" ")

# Example usage:
a = Queue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)
# a.dequeue()
a.show_all()