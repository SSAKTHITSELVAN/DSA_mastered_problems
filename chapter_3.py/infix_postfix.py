from pythonds3 import Stack

def expression_converter(exp_str):
    """Converts infix to postfix notation."""
    
    precedence = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    
    exp = exp_str.split()
    if not exp:
        raise ValueError("Input expression is empty")

    output = ''
    stack = Stack()
    
    for i in exp:
        if i.isalnum():
            output += i + " "
        elif i == "(":
            stack.push(i)
        elif i == ")":
            while not stack.is_empty() and stack.peek() != "(":
                output += stack.pop() + " "
            if stack.is_empty():
                raise ValueError("Mismatched parentheses: Extra closing parenthesis ')'")
            stack.pop()
        elif i in precedence:
            while not stack.is_empty() and precedence.get(stack.peek(), -1) >= precedence[i]:
                output += stack.pop() + " "
            stack.push(i)
        else:
            raise ValueError(f"Unexpected operator: {i}")

    while not stack.is_empty():
        top = stack.pop()
        if top == "(":
            raise ValueError("Mismatched parentheses: Extra opening parenthesis '('")
        output += top + " "

    return output.strip()

# Testing
expressions = [
    "( A + B ) * ( C + D ) * ( E + F )",
    "A * ( ( B + C ) * ( D + E ) )",
    "A * B * C * D + E + F",
    "( A + B ) )",  # Error case
    "( A + ( B - C )"  # Error case
]

for expr in expressions:
    try:
        print(f"Infix: {expr}")
        print(f"Postfix: {expression_converter(expr)}\n")
    except ValueError as e:
        print(f"Error: {e}\n")