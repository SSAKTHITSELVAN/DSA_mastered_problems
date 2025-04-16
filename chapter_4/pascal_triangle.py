from math import factorial

def pascal_triangle(row):
    for n in range(row):
        print(f"{' ' * (row - n)}", end="")
        for r in range(n + 1):
            a = factorial(n) // (factorial(r) * factorial(n - r))
            print(f"{a} ", end="")
        print()

pascal_triangle(5)