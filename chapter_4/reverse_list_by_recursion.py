
def reverse_list(arr):
    """Reverse the list by recursion"""
    
    if len(arr) == 1:
        return arr
    return [arr.pop()] + reverse_list(arr)

a = [0, 9, 8, 7, 6, 5, 4, 3]
print(reverse_list(a))