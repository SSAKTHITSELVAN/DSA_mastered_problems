
def fibonacci(a, b, n):
    """Fibonacci calculation using recursion"""
    r = a+b
    if n <= 0:
        return []
    return [r] + fibonacci(b, r, n-1)

# print(fibonacci(-1, 1, 10))

def fibonacci(n):
    """Fibonacci calculation using recursion for specific number"""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative integers.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(2))