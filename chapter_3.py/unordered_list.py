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
    
    def __str__(self):
        list_str = "["
        temp = self.head
        while temp:
            list_str += str(temp.data)
            temp = temp.next
            if temp is not None:
                list_str += ", "
        return list_str + "]"
    
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
    
    def remove_assistant(self, temp, previous):
        if temp is None:
            raise ValueError(f"Element not found...")

        if previous is None:
            self.head = temp.next
        else:
            previous.next = temp.next
        
        self.size -= 1

    def remove(self, item):
        """Remove all occurrences of item"""
        previous = None
        temp = self.head
        flag = -1

        while temp:
            if temp.data == item:
                self.remove_assistant(temp, previous)
                temp = temp.next  # Move to the next node after deletion (important)
                flag = 0
            else:
                previous = temp  # Only update previous if no deletion occurred
                temp = temp.next
        if flag == -1:
            raise Exception("Element not found...")
    
    def append(self, item):
        temp = self.head
        new_node = Node(item)
        if temp is None:
            self.head = new_node
        else:
            while temp.next is not None:
                temp = temp.next
            
            temp.next = new_node
        self.size += 1
        
        
    def index(self, target):
        """Returns the index of the first occurrence of target. Raises ValueError if not found."""
        temp = self.head
        ind = 0  # Start index at 0
        
        while temp:
            if temp.data == target:
                return ind
            temp = temp.next
            ind += 1
            
        raise ValueError(f"Element {target} not found in the list.")
    
    def pop(self):
        """Removes and returns the last element of the list."""
        if self.head is None:
            raise IndexError("Cannot pop from an empty list")
        
        temp = self.head
        previous = None
        
        while temp.next:  # Traverse to the last node
            previous = temp
            temp = temp.next
            
        data = temp.data  # Store the last node's data
        
        if previous is None:  # If there was only one element in the list
            self.head = None
        else:
            previous.next = None  # Correctly remove the last node
        
        self.size += 1
        return data  # Return the popped value
    
    def insert(self, ind, item):
        """Inserts an item at the given index in the linked list."""
        if ind < 0:
            raise IndexError("Negative index is not supported")
        
        new_node = Node(item)
        
        if ind >= self.length():  # Insert at the end
            self.append(item)
            return  # ✅ Prevents extra execution
        
        if ind == 0:  # Insert at the beginning
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for i in range(ind - 1):  # ✅ Correct range
                temp = temp.next
                
            new_node.next = temp.next
            temp.next = new_node
            
        self.size += 1  # ✅ Update the size
    
    def slice(self, start=0, stop=-1):
        if stop == -1 or stop > self.length():
            stop = self.length()
        if start < 0:
            start = 0
            
        # ✅ Return an empty list for invalid ranges
        if start >= self.length() or stop <= start:
            return Unordered_List()
        
        result_list = Unordered_List()
        temp = self.head
        
        # ✅ Move temp to `start` position
        for _ in range(start):
            if temp is None:  # Prevent None access
                return Unordered_List()
            temp = temp.next
            
        # ✅ Append elements in correct order
        for _ in range(stop - start):
            if temp is None:  # Prevent None access
                break
            result_list.append(temp.data)  # ✅ Use append to maintain order
            temp = temp.next
            
        return result_list


# Testing the corrected code
a = Unordered_List()
a.add(5)
a.add(2)
a.add(3)
a.append(77)
a.add(5)
a.append(88)
a.insert(3, 99)

print(a)

b = a.slice(6)
print(b)