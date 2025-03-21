from pythonds3 import Stack

def binary_converter(num):
    """converts_the number into binary"""
    stack = Stack()
    while num > 0:
        stack.push(num%2)
        num //= 2
    return stack

a = binary_converter(45)
while not a.is_empty():
    print(a.pop(), end=" ")