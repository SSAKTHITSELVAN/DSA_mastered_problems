from pythonds3 import Stack

def to_str(n, base):
    """convert the number to string"""
    possible_string = '0123456789'
    r_stack = Stack()
    while n > 0:
        if n < base:
            r_stack.push(possible_string[n])
            break
        else:
            r_stack.push(possible_string[n%base])
            n = n//base
    
    res = ""
    while not r_stack.is_empty():
        res += str(r_stack.pop())
    
    return res

print("str")
a = to_str(769, 2)
print(a)
print("end")
#1100000001