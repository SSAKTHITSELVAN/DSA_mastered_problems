
def factorial(n):
    """calculates the factorial for 'n' """
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(-5))