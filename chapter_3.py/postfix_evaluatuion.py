from pythonds3 import Stack

def perform_arithmetic_oper(stack: Stack) -> tuple:
    """Pop two operands in correct order (left operand first)."""
    if stack.size() < 2:
        raise ValueError("Invalid postfix expression: Not enough operands")
    b = int(stack.pop())  # Right operand
    a = int(stack.pop())  # Left operand
    return a, b

def postfix_evaluator(expr: str) -> int:
    """Evaluates a postfix (Reverse Polish Notation) expression."""
    if not expr.strip():
        raise ValueError("Expression is empty")

    stack = Stack()
    expression = expr.split()

    for digit in expression:
        if digit.isdigit():
            stack.push(digit)
        else:
            if stack.size() < 2:
                raise ValueError("Invalid postfix expression: Not enough operands")

            match digit:
                case '+':
                    b, a = perform_arithmetic_oper(stack)
                    stack.push(a + b)
                case '-':
                    b, a = perform_arithmetic_oper(stack)
                    stack.push(a - b)
                case '*':  # Fixed multiplication operator
                    b, a = perform_arithmetic_oper(stack)
                    stack.push(a * b)
                case '/':
                    b, a = perform_arithmetic_oper(stack)
                    if b == 0:
                        raise ZeroDivisionError("Division by zero error")
                    stack.push(a // b)
                case _:
                    raise ValueError(f"Unexpected character in expression: {digit}")

    if stack.size() != 1:
        raise ValueError("Invalid postfix expression: Too many operands")

    return stack.pop()

# Testing
try:
    print(postfix_evaluator("7 8 + 6 2 / *"))  # Expected: (7+8) * (6/2) = 15 * 3 = 45
    print(postfix_evaluator("3 4 +"))  # Expected: 7
    print(postfix_evaluator("10 2 8 * + 3 -"))  # Expected: 23
    print(postfix_evaluator("5"))  # Expected: 5
    print(postfix_evaluator(""))  # Should raise ValueError
except Exception as e:
    print(f"Error: {e}")