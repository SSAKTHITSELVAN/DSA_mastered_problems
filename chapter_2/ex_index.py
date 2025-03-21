import timeit

x = list(range(100000000))
code_1 = """
x[0]
"""
code_2 = """
x[999]
"""
# setup the Timer
indexing_f = timeit.Timer(code_1, "from __main__ import x")
indexing_l = timeit.Timer(code_2, "from __main__ import x")

# Timer on
time_f = indexing_f.timeit(number=1000)
time_l = indexing_l.timeit(number=1000)

# Result
print(f"Time for indexing at 0 is : {time_f}")
print(f"Time for indexing at last is : {time_l}")