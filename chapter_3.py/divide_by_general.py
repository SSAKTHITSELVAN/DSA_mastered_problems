from pythonds3 import Stack

def divide_by_2(num: int, base: int):
    """Converts the decimal ti binary"""
    digits = "0123456789ABCDEF"
    stack = Stack()
    bina = -1
    while num > 0:
        bina = num % base
        num //= base
        stack.push(bina)
    
    while not stack.is_empty():
        print(digits[stack.pop()])


divide_by_2(233, 16)
