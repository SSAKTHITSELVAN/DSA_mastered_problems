
def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less_than_pivot = [x for x in arr if x < pivot]
    greater_than_pivot = [y for y in arr if y > pivot]
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

a = [1,32,45,-45,0,67,3,7,8]
print(quick_sort(a))