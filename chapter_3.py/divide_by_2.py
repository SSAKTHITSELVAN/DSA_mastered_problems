from pythonds3 import Stack

def divide_by_2(num: int):
    """Converts the decimal ti binary"""
    stack = Stack()
    bina = -1
    while num > 0:
        bina = num % 2
        num //= 2
        stack.push(bina)
    
    while not stack.is_empty():
        print(stack.pop())


divide_by_2(233)
