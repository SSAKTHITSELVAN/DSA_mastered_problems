def shell_sort(arr):
    """perform the shell sort for the given array"""
    
    gab = len(arr) // 2
    
    while gab > 0:
        gab_insertion_sort(arr, gab)
        gab //= 2

def gab_insertion_sort(arr, gab):
    """performs the insertion based on gab"""
    for i in range(gab, len(arr)):
        current_ele = arr[i]
        current_index = i
        for j in range(i-gab, -1, -gab):
            if arr[j] > current_ele:
                arr[j+gab] = arr[j]
                current_index = j
        arr[current_index] = current_ele

a = [2,54,67,-1,-34, 0,45,3,6]
shell_sort(a)
print(a)