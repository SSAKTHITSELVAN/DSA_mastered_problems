import random

def print_queue(queue, num):
    a = queue[:]  # Create a copy to avoid modifying the original
    print("random number is ", num,end=" --- ")
    while a:
        print(a.pop(0), end=" - ")

def hot_potato(name_list):
    queue = name_list[:]  # Create a copy to avoid modifying the original
    
    while len(queue) > 1:
        num = random.randint(1, len(queue))
        print_queue(queue, num)
        for j in range(num):
            queue.append(queue.pop(0))  # Enqueue and dequeue using list methods
        queue.pop(0)
        print()
    return queue[0]

n_l = ['1', '2', '3', '4']
winner = hot_potato(n_l)
print("winner is ---", winner)