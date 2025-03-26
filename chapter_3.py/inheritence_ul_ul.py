class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    @property
    def _data(self):
        return self.data
    
    @_data.setter
    def _data(self, data):
        self.data = data
    
    @property
    def _next(self):
        return self.next
    
    @_next.setter
    def _next(self, next):
        self.next = next
        

class List:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return bool(self.head)
    
    def length(self):
        return self.size
    
    def remove(self, target):
        current = self.head
        previous = None
        
        while current is not None:
            if current.data == target:
                break
            
            previous = current
            current = current.next
        
        if previous is None:
            self.head = current.next
        elif current is None:
            raise ValueError("element not found...")
        else:
            previous.next = current.next
        
        self.size -= 1
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next
        print("\n")


class Unordered_list(List):
    def __init__(self):
        super().__init__()
    
    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1


class Ordered_list(List):
    def __init__(self):
        super().__init__()
    
    def add(self, item):
        new_node = Node(item)
        current = self.head
        previous = None
        
        while current is not None and current.data < item:
            previous = current
            current = current.next
        
        
        if previous is None:
            new_node.next = self.head
            self.head = new_node
        else:
            previous.next = new_node
            new_node.next = current
        
        self.size += 1
        
        
# ---- Testing the Implementation ----
print("Unordered List Operations:")
ul = Unordered_list()
ul.add(10)
ul.add(20)
ul.add(30)
ul.display()  # Expected: 30 -> 20 -> 10 -> None

ul.remove(20)
ul.display()  # Expected: 30 -> 10 -> None

print("\nOrdered List Operations:")
ol = Ordered_list()
ol.add(15)
ol.add(10)
ol.add(20)
ol.add(5)
ol.add(7)
ol.add(8)
ol.add(50)
ol.display()  # Expected: 5 -> 10 -> 15 -> 20 -> None