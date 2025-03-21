# from pythonds3 import Queue


# def radix_sort(number_list):
#     """Implementation of the radix sorting"""
    
#     max_num = max(number_list)  # Find the maximum number to determine the number of digits
#     exp = 1  # Start from the least significant digit

#     while max_num // exp > 0:
#         bucket = [Queue() for _ in range(10)]  # Create empty buckets for each digit (0-9)
        
#         for val in number_list:
#             radix_ind = (val // exp) % 10
#             bucket[radix_ind].enqueue(val)
        
#         number_list.clear()  # Clear the original list
        
#         for ele in bucket:
#             while ele.size() > 0:
#                 number_list.append(ele.dequeue())  # Append sorted numbers back
        
#         exp *= 10  # Move to the next digit

#     return number_list


# # Test
# li = [170, 45, 75, 90, 802, 24, 2, 66]
# sorted_list = radix_sort(li[:])  # Pass a copy to avoid modifying the original list
# print(sorted_list)


from collections import deque

def radix_sort(number_list):
    """Implementation of Radix Sort using Queues"""
    
    max_num = max(number_list)  # Find the max number to determine number of passes
    exp = 1  # Start at the least significant digit

    while max_num // exp > 0:
        # Create a list of 10 queues (one for each digit 0-9)
        buckets = [deque() for _ in range(10)]
        
        # Distribute numbers into the respective queues
        for val in number_list:
            radix_ind = (val // exp) % 10
            buckets[radix_ind].append(val)  # Using queue for FIFO behavior
        
        # Collect numbers back into the list
        number_list.clear()
        for queue in buckets:
            while queue:  # Extract elements from queue
                number_list.append(queue.popleft())  # popleft() is O(1)
        
        exp *= 10  # Move to the next digit

    return number_list


# Test
li = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_list = radix_sort(li[:])  # Passing a copy to avoid modifying the original list
print(sorted_list)