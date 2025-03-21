import timeit

"""Queue where the rear is at end of the list"""

class NQueue:
    """Abstract data structure of the queue"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, ele):
        self.items.insert(0, ele)
    
    def dequeue(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)


class RQueue:
    """Queue implementation"""
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return not bool(self.queue)
    
    def size(self):
        return len(self.queue)


import timeit

# ... (Queue implementations as before) ...

if __name__ == "__main__":
    for i in [100, 1000, 10000]:
        q1_enqueue = RQueue()
        q2_enqueue = NQueue()
        q1_dequeue = RQueue()
        q2_dequeue = NQueue()

        def enqueue_q1():
            for j in range(i):
                q1_enqueue.enqueue(j)

        def enqueue_q2():
            for j in range(i):
                q2_enqueue.enqueue(j)

        def dequeue_q1():
            for j in range(i):
                q1_dequeue.enqueue(j)
            for j in range(i):
                q1_dequeue.dequeue()

        def dequeue_q2():
            for j in range(i):
                q2_dequeue.enqueue(j)
            for j in range(i):
                q2_dequeue.dequeue()

        t1_enqueue = timeit.Timer(enqueue_q1)
        t2_enqueue = timeit.Timer(enqueue_q2)
        t1_dequeue = timeit.Timer(dequeue_q1)
        t2_dequeue = timeit.Timer(dequeue_q2)

        print(f"Enqueue {i} elements:")
        print(f"  RQueue: {t1_enqueue.timeit(number=100)}")
        print(f"  NQueue: {t2_enqueue.timeit(number=100)}")
        print(f"Dequeue {i} elements after enqueuing {i} elements:")
        print(f"  RQueue: {t1_dequeue.timeit(number=100)}")
        print(f"  NQueue: {t2_dequeue.timeit(number=100)}")
        print("-" * 20)

    print("Explanation:")
    print("RQueue enqueue is faster because append is O(1). NQueue enqueue is O(n) because insert(0, ele) shifts elements.")
    print("RQueue dequeue is O(n) because pop(0) shifts elements. NQueue dequeue is O(1) because pop() from the end is O(1).")