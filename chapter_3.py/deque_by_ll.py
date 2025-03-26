class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Deque:
    """Replication of Deque using the linked list"""
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def add_front(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def add_rear(self, item):
        new_node = Node(item)
        current = self.head
        
        self.length += 1
        
        if current is None:
            self.head = new_node
            return
        
        while current.next is not None:
            current = current.next
        
        current.next = new_node
    
    def remove_front(self):
        if self.head is None:
            raise ValueError("Deque is empty...")
        head_data = self.head.data
        self.head  = self.head.next
        self.length -= 1
        return head_data
    
    def remove_rear(self):
        current = self.head
        previous = None
        
        if current is None:
            raise ValueError("Deque is empty...")
        
        while current.next is not None:
            previous = current
            current = current.next
        top_data = current.data
        
        if previous is None:
            self.head = None
        else:
            previous.next = None
        
        self.length -= 1
        return top_data


# Create a Deque
dq = Deque()

# Add elements at the front
dq.add_front(10)
dq.add_front(20)
dq.add_front(30)

# Add elements at the rear
dq.add_rear(40)
dq.add_rear(50)

# Remove elements from front
print("Removed from front:", dq.remove_front())  # Expected: 30
print("Removed from front:", dq.remove_front())  # Expected: 20

# Remove elements from rear
print("Removed from rear:", dq.remove_rear())  # Expected: 50
print("Removed from rear:", dq.remove_rear())  # Expected: 40

# Check if deque is empty
print("Is deque empty?", dq.head is None)  # Expected: False

# Remove last element
print("Removed from front:", dq.remove_front())  # Expected: 10

# Check if deque is empty now
print("Is deque empty?", dq.head is None)  # Expected: True

# Try removing from an empty deque (should raise an error)
try:
    dq.remove_front()
except ValueError as e:
    print("Error:", e)  # Expected: "Deque is empty..."
