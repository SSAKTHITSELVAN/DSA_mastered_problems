from stack import Stack
from queue_with_performance_of_1_ import Queue
import timeit

stack_p = Stack()
queue_ll = Queue()

def add_elements_p(length):
    for i in range(length):
        stack_p.push(i)

def add_elements_ll(length):
    for i in range(length):
        queue_ll.enqueue(i)

def remove_elements_p():
    stack_p.pop()

def remove_elements_ll():
    queue_ll.dequeue()

for i in [100, 1000, 5000]:
    tas = timeit.Timer(lambda: add_elements_p(i))
    taq = timeit.Timer(lambda: add_elements_ll(i))
    
    tps = timeit.Timer(lambda: remove_elements_p())
    tdq = timeit.Timer(lambda: remove_elements_ll())
    
    
    print(f"Time to push - {i} - elements in Stack is -- {tas.timeit(number=100)}")
    print(f"Time to enqueue - {i} - elements in Queue is -- {taq.timeit(number=100)}")
    print("\n")
    print(f"Time to pop elements in Stack is -- {tps.timeit(number=100)}")
    print(f"Time to dequeue elements in Queue is -- {tdq.timeit(number=100)}")
    print("\n")