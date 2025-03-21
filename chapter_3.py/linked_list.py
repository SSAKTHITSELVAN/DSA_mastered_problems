class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def set_data(self, node_data):
        self.data = node_data
    
    data = property(get_data, set_data)

class Linked_list:
    def __init__(self):
        self.head = Node()
        self.length = 0
    
    def add(self, item):
        self.length += 1
        new_node = Node(data=item)
        if not self.head.data:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp =temp.next
        temp.next = new_node
    
    def remove(self, item_r):
        temp = self.head
        if temp.data == item_r:
            self.head = temp.next
            self.length -= 1
            return
        while temp:
            if temp.data == item_r:
                pre_addr.next = temp.next
                self.length -= 1
                return
            pre_addr = temp
            temp = temp.next
        raise Exception("unable to find")
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    
    def search(self, item_s):
        temp = self.head
        while temp:
            if temp.data == item_s:
                return True
            temp = temp.next
        return False
    
    def is_empty(self):
        return not bool(self.length)
    
    def size(self):
        return self.length
    
    def append(self, item_a):
        self.length += 1
        new_node = Node(item_a)
        
        if not self.head.data:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def index(self, item_i):
        index = -1
        temp = self.head
        while temp:
            index += 1
            if temp.data == item_i:
                return index
            
            temp = temp.next
    
    def insert(self, pos, item_in):
        
        new_node = Node(item_in)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        
        new_node.next = temp.next.next
        temp.next = new_node
    def pop(self, pos=None):
        if not pos and pos != 0:
            print("in")
            pos = self.size()
        
        if pos < 0:
            pos = self.length + pos
        
        temp = self.head
        pre = None
        
        if pos < 1:
            dubli = temp
            self.head = temp.next
            return temp.data
        c = 0
        
        while temp.next and c < pos:
            c += 1
            pre = temp
            temp = temp.next
        if temp.next:
            dubli = temp
            pre.next = temp.next
            return temp.data
        else:
            dubli  = temp
            pre.next = None
            return dubli.data


l = Linked_list()
l.add(5)
l.add(6)
l.add(7)
l.add(8)
l.add(9)
l.add(10)
# l.remove(5)
# l.remove(10)
# l.remove(6)
# print(l.size())
# print(l.is_empty())
# l.print()

# print(l.is_empty())
# print("----------------------------------------")
# l.append(1)
# l.append(2)
# l.append(3)
# print(l.is_empty())/
# print('-'*20)
print("removed - ",l.pop(-2))
l.print()