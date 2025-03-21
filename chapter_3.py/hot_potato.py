from pythonds3 import Queue

def hot_potato_game(name_list, num):
    """Simulate the hot potato game"""
    queue = Queue()
    for name in name_list:
        queue.enqueue(name)
    
    
    while queue.size() > 1:
        for i in range(num-1):
            queue.enqueue(queue.dequeue())
        print(f"Your out {queue.dequeue()}")
    
    return queue.dequeue()

print("winner", hot_potato_game(["n1", "n2", "n3", "n4", "n5"], 7))