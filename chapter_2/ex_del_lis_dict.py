# import timeit

# for i in [1000, 10000, 100000]:
    
#     code_l = f"del x[{0}]"
#     code_d = f"del y[{0}]"

#     x = list(range(i))
#     timer_l = timeit.Timer(stmt=code_l, setup="from __main__ import x")
    
#     y = {j: None for j in range(i)}
#     timer_d = timeit.Timer(stmt=code_d, setup="from __main__ import y")
    
#     # Result
#     time_l = timer_l.timeit(number=1000)
#     time_d = timer_d.timeit(number=1000)
    
#     print(f"Time for deleting in list : ", time_l)
#     print(f"Time for deleting in dictionary : ", time_d)



import timeit

for i in [1000, 10000, 100000]:
    # Create the data structures.
    x = list(range(i))
    y = {j: None for j in range(i)}
    
    
    # For list deletion, always delete the element at index 0.
    code_l = "del x[0]"
    # For dictionary deletion, delete an arbitrary key (the first one found).
    code_d = "del y[next(iter(y))]"
    
    
    # Create Timer objects with proper setup.
    timer_l = timeit.Timer(stmt=code_l, setup="from __main__ import x")
    timer_d = timeit.Timer(stmt=code_d, setup="from __main__ import y")
    
    # Run deletion 1000 times.
    time_l = timer_l.timeit(number=1000)
    time_d = timer_d.timeit(number=1000)
    
    print(f"Size: {i}")
    print("Time for deleting in list:", time_l)
    print("Time for deleting in dictionary:", time_d)
    print("-" * 50)