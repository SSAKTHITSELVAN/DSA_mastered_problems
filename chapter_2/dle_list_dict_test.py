import random
import timeit

for i in [1000, 10000, 100000]:
    # Generate random index
    ind = random.randint(0, i - 1)

    # Function to reset dictionary before each run
    def del_from_dict():
        dic = {j: None for j in range(i)}  # Fresh dictionary each time
        del dic[ind]

    # Function to reset list before each run
    def del_from_list():
        li = [k for k in range(i)]  # Fresh list each time
        del li[ind]

    # Timing deletion in dictionary
    t2 = timeit.Timer(del_from_dict)

    # Timing deletion in list
    t1 = timeit.Timer(del_from_list)

    print(f"Time for 'del' in dictionary of {i} elements --> {t2.timeit(number=100)} seconds")
    print(f"Time for 'del' in list of {i} elements --> {t1.timeit(number=100)} seconds\n")
