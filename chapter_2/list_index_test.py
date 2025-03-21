import random
import timeit


for i in [1000, 10000, 100000, 10000000]:
    li = list(range(i))
    ind = random.randint(0, i-1)
    t1 = timeit.Timer(f"li[{ind}]", "from __main__ import li, ind")
    print(f" time for {i} is --> {t1.timeit(number=100)}")
