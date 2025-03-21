from pythonds3 import Stack

def general_match(par_str):
    """Check whether the parenthesis is balanced or not"""
    stack = Stack()
    for par in par_str:
        if par in '([{':
            stack.push(par)
        else:
            if stack.is_empty():
                return False
            else:
                if not match_po_cl(stack.pop(), par):
                    return False
    
    return stack.is_empty()

def match_po_cl(left, right):
    possible_lefts = '([{'
    possible_rights = ')]}'
    
    return possible_lefts.index(left) == possible_rights.index(right)

ex = "({}{}[])[]"
print(general_match(ex))