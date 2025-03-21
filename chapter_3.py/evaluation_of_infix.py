from pythonds3 import Stack

def arithmetic_operation(stack):
    return (int(stack.pop()), int(stack.pop()))

def evaluate_postfix(exp_str):
    """Evaluates the postfix expression"""
    exp = exp_str.split(" ")
    stack = Stack()
    for i in exp:
        if i.isdigit():
            stack.push(i)
        else:
            match(i):
                case '+':
                    b, a = arithmetic_operation(stack)
                    stack.push(a+b)
                case '-':
                    b, a = arithmetic_operation(stack)
                    stack.push(a-b)
                case '.':
                    b, a = arithmetic_operation(stack)
                    stack.push(a*b)
                case '/':
                    b, a = arithmetic_operation(stack)
                    stack.push(a//b)
    return stack.pop()


exp_str = '1 2 3 4 5 . + . +'
print(evaluate_postfix(exp_str))