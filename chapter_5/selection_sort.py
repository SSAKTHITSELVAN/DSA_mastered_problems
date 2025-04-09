
def selection_sort(arr):
    """Sort the given array"""
    
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


a = [23,5,76,34, -2, -1,14,67, 0]
print(selection_sort(a))
