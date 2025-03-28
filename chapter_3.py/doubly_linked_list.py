class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None


class Doubly_Linked_List:
    """Implementation of Doubly linked list"""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def size(self):
        return self.length
    
    def is_empty(self):
        return self.head is None
    
    def add(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.back = new_node
            new_node.next = self.head
            new_node.back = self.tail
            self.head = new_node
        
        self.length += 1
    
    def remove(self, target):
        if self.is_empty():
            print("List is empty. Nothing to remove.")
            return
        
        current = self.head
        
        # If head node is the target
        if current.data == target:
            self.head = current.next
            if self.head:
                self.head.back = None
            else:
                self.tail = None  # If list becomes empty
            self.length -= 1
            return
        
        # Traverse to find the target node
        while current and current.data != target:
            current = current.next
        
        if not current:  # If item not found
            print(f"Item {target} not found in the list.")
            return

        if current == self.tail:  # If removing the tail
            self.tail = current.back
            self.tail.next = None
        else:
            current.back.next = current.next
            current.next.back = current.back
        
        self.length -= 1
    
    def show_list_items(self):
        current = self.head
        while current is not None:
            print(f"         {current.data}    ----   back data   --   {current.back.data}   ------ next  -- {current.next}")
            current = current.next

d = Doubly_Linked_List()
d.add(5)
d.add(99)
d.add(100)
d.add(200)
d.add(300)
d.remove(5)
d.show_list_items()