"""Represents the Ordered list"""

class Node:
    """Represents the node"""
    
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


class Ordered_List:
    """Represents the ordered list"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    
    def length(self):
        return self.size
    
    def add(self, item):
        
        new_node = Node(item)
        temp = self.head
        previous = None
        while temp is not None and temp.data < item:
            previous = temp
            temp = temp.next
        
        if previous is None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = temp
            previous.next = new_node
        
        self.size += 1
    
    def show_list(self):
        temp = self.head
        list_str = []
        while temp is not None:
            list_str.append(temp.data)
            temp = temp.next
        return "[" + ", ".join(map(str, list_str)) + "]"
    
    
    def index(self, target):
        ind = 0
        current = self.head
        
        while current is not None:
            if current.data == target:
                return ind
            current = current.next
            ind += 1
        return -1
    
    def remove(self, target):
        current = self.head
        previous = None
        flag = -1
        
        while current is not None:
            if current.data == target:
                if previous is None:
                    self.head = current.next
                elif current is not None:
                    previous.next = current.next
                current = current.next
                flag = 0
            else:
                previous = current
                current = current.next
        self.size -= 1
            
        if flag == -1:
            raise ValueError("The list has no such element...", flag)
    
    
    def pop(self, ind = -1):
        if ind == -1:
            ind = self.length()-1
        current = self.head
        previous = None
        
        if current is None:
            raise IndexError("Unable to pop in empty list...")
        
        
        if ind < 0 or ind >= self.size:
            raise IndexError("Index out of range...")
        
        while current.next is not None:
            if self.index(current.data) == ind:
                break
            previous = current
            current = current.next
        
        data = current.data
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        
        self.size -= 1
        return data







a = Ordered_List()
a.add(1)
a.add(-1)
a.add(5)
a.add(2)
a.add(100)
a.add(2)
print(a.show_list())
print("len -- ",a.length())
print(a.pop(0))
print(a.pop(4))
print(a.pop(3))
print("len -- ",a.length())
print(a.show_list())