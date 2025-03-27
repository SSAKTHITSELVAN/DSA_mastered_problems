from unordered_list import Unordered_List
import timeit

def add_100_elements_P(size):
    python_list = []  # Reinitialize for every test run
    for i in range(size):
        python_list.insert(0, 1)

def add_100_elements_l(size):
    linked_list = Unordered_List()  # Reinitialize for every test run
    for i in range(size):
        linked_list.add(i)

for i in [1000, 10000, 50000]:
    pl = timeit.Timer(lambda: add_100_elements_l(i))
    pp = timeit.Timer(lambda: add_100_elements_P(i))
    
    print(f"time required to insert --{i}-- in linked list is - {pl.timeit(number=100)}")
    print(f"time required to insert --{i}-- in python list is - {pp.timeit(number=100)}")
    print("\n")
