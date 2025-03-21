import random
import timeit

for i in [1000, 10000, 100000]:
    dic = {j: None for j in range(i)}  # Ensure dictionary size matches 'i'
    ind = random.randint(0, i - 1)  # Generate a valid index within 'i'
    
    # Measure dictionary get() operation
    t1 = timeit.Timer(lambda: dic.get(ind))  

    # Measure dictionary set operation using a lambda
    t2 = timeit.Timer(lambda: dic.__setitem__(ind, i))  

    print(f"Time for --get-- from {i} elements is --> {t1.timeit(number=100)} seconds")
    print(f"Time for --set-- from {i} elements is --> {t2.timeit(number=100)} seconds\n")