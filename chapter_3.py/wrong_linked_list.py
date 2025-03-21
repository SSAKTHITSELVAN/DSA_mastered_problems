class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        """Incorrect implementation: Updating head first before linking"""
        self.head = Node(data)  # Step 1 (Wrong): Create new node & assign it to head
        self.head.next = self.tail  # Step 2 (Wrong): Try to link old list (but tail is not updated correctly!)
        self.tail = self.head  # Step 3: Update tail reference (but it's wrong)

    def print_nodes(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

# Testing the incorrect implementation
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.print_nodes()