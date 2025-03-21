def to_str(n, base):
    """convert the number to string"""
    possible_string = '0123456789'
    if n < base:
        return possible_string[n]
    return to_str(n//base, base) + possible_string[n%base]

a = to_str(4, 2)
print(a)