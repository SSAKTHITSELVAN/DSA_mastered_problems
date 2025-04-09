
def insertion_sort(arr):
    """sort the array using insertion sort"""
    
    for i in range(1, len(arr)):
        current_index = i
        current_element = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > current_element:
                arr[j+1] = arr[j]
                current_index = j
        arr[current_index] = current_element
    return arr

a = [1,54,87,3,7,2,-56,0,-4]
print(insertion_sort(a))