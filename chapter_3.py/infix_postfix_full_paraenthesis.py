from pythonds3 import Stack

def in_postfix(exp_str):
    """convert the fully parenthesised expression(infix) to postfix"""
    
    exp = exp_str.split(" ")
    stack = Stack()
    output = ''
    for i in exp:
        if i.isalnum():
            output += i
        elif i in {'+', '-', '/', '.'}:
            stack.push(i)
        elif i == ")":
            output += stack.pop()
    return output

expressions = [
    "( ( ( A + B ) . ( C + D ) ) . ( E + F ) )",
    "( A . ( ( B + C ) . ( D + E ) ) )",
    "( ( ( ( ( A . B ) . C ) . D ) + E ) + F )"
]

for expr in expressions:
    print(f"Infix: {expr}")
    print(f"Postfix: {in_postfix(expr)}\n")