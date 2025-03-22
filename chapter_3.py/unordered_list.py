class Node:
    """Represents the node"""
    
    def __init__(self, node_data):
        """Initialization of nodes"""
        self._data = node_data
        self._next = None
    
    @property
    def data(self):
        """Data getter"""
        return self._data
    
    @data.setter
    def data(self, node_data):
        """Data setter"""
        self._data = node_data
    
    @property
    def next(self):
        """Next reference getter"""
        return self._next
    
    @next.setter
    def next(self, next_node):
        """Next reference setter"""
        self._next = next_node

class Unordered_List:
    """Represents the unordered list"""
    def __init__(self):
        self.head = None
        self.size = 0
    
    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        self.size += 1
    
    def is_empty(self):
        return not bool(self.head)
    
    def length(self):
        return self.size
    
    def search(self, target):
        "simple linear search"
        temp = self.head
        while temp:
            if temp.data == target:
                return True
            temp = temp.next
        return False
    
    def show_list_items(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    def remove(self, item):
        """remove the item"""
        previous = None
        temp = self.head
        
        while temp:
            if temp.data == item:
                break
            previous = temp
            temp = temp.next
        
        if temp is None:
            raise ValueError(f"Element -- {item} -- not found...")

        if previous is None:
            self.head = temp.next
        else:
            previous.next = temp.next
        
        self.size -= 1

# Testing the corrected code
a = Unordered_List()
a.add(5)
a.add(2)
a.add(3)
a.show_list_items()
print("size  ",a.length())
a.remove(2)
print("size  ",a.length())
a.show_list_items()
print(a.search(5))