class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            
            temp.next = new_node
    
    def print_linked_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
    
    def remove(self, item):
        temp = self.head
        previous = None
        while temp is not None:
            if temp.data == item:
                break
            previous = temp
            temp = temp.next
        
        if temp == None:
            print("no matched value found !")
        if previous == None:
            print("itemen removed is", self.head.data)
            self.head = self.head.next
        else:
            previous.next = temp.next
    
    
    
    
l = LinkedList()
l.add(6)
l.print_linked_list()
l.remove(6)
l.print_linked_list()