# from pythonds3 import Stack

# st = Stack()
# st.push(1)
# st.push(2)
# st.push("q")
# st.push("r3")
# # st.peek()
# print(st.peek(),st.is_empty())
# print(st.pop())
# print(st.peek())

class Stack:
    """stating of the list act as top and end of list act as bottom(base)"""
    def __init__(self):
        self._items: list = []
    
    def push(self, data_item):
        self._items.insert(0, data_item)
    
    def pop(self):
        return self._items.pop(0)
    
    def peek(self):
        return self._items[0]
    
    def is_empty(self):
        return len(self._items) <= 0
    
    def size(self):
        return len(self._items)