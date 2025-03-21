# import timeit
# import random

# for i in [1000, 10000, 100000]:
#     a = random.randrange(0,i)
#     code_s =  f"""x[{a}]={None}"""
#     code_g = f"""
#     x.get({a})
#     """
#     timer_s = timeit.Timer(code_s, "from __main__ import x")
#     timer_g = timeit.Timer(code_g, "from __main__ import x")
    
#     x = { j : None for j in range(i)}
    
#     time_s = timer_s.timeit(number=100)
#     time_g = timer_g.timeit(number=100)
#     # Result
#     print(f"Time taken to set :", timer_s)
#     print(f"Time taken to get :", timer_g)










import timeit
import random

for i in [1000, 10000, 100000]:
    a = random.randrange(0, i)
    
    # Create dictionary x first
    x = {j: None for j in range(i)}
    
    # Use single-line strings for the code to be timed
    code_s = f"x[{a}] = None"
    code_g = f"x.get({a})"
    
    # Now create the timers
    timer_s = timeit.Timer(stmt=code_s, setup="from __main__ import x")
    timer_g = timeit.Timer(stmt=code_g, setup="from __main__ import x")
    
    # Time the execution 100 times each
    time_s = timer_s.timeit(number=100)
    time_g = timer_g.timeit(number=100)
    
    # Print the measured times
    print(f"Time taken to set for dictionary of size {i}: {time_s}")
    print(f"Time taken to get for dictionary of size {i}: {time_g}")
