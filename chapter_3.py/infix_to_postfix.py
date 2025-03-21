from pythonds3 import Stack

def infix_postfix(expr):
    op_stack = Stack()
    output_list = []
    prec = {'*': 3, '/': 3, '+': 2, '-': 2}  # No '(' in precedence
    expression = list(expr)

    for tok in expression:
        if tok.isalnum():  # If it's an operand (A, B, C, etc.), add it to output
            output_list.append(tok)
        elif tok == "(":
            op_stack.push(tok)  # Push '(' onto the stack
        elif tok == ")":
            while not op_stack.is_empty() and op_stack.peek() != "(":
                output_list.append(op_stack.pop())
            op_stack.pop()  # Remove '(' but don't add it to output
        elif tok in prec:  # If token is an operator
            while not op_stack.is_empty() and op_stack.peek() != "(" and prec[op_stack.peek()] >= prec[tok]:
                output_list.append(op_stack.pop())
            op_stack.push(tok)

    while not op_stack.is_empty():
        output_list.append(op_stack.pop())

    return " ".join(output_list)

st = "A  +  B * C"
st = st[::-1]
a = infix_postfix(st)  # Expected Output: A B C + *
b = a[::-1]
print(b)
# print(infix_postfix("(A+B)*C-(D-E)*(F+G)"))  # Expected Output: A B + C * D E - F G + * -