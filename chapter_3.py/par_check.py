from pythonds3 import Stack

def parenthesis_match(par_str):
    """Check whether the parenthesis is balanced or not"""
    
    stack = Stack()
    for par in par_str:
        if par == '(':
            stack.push(par)
        else:
            if stack.is_empty():
                return False
            else:
                stack.pop()
    
    return stack.is_empty()