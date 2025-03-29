import random
from pythonds3 import Queue

class Printer:
    """represents the printer"""
    
    def __init__(self, pps):
        self.pps = pps
        self.current_task = None
        self.remaining_time = 0
    
    def tick(self):
        if self.current_task is not None:
            self.remaining_time -= 1
            if self.remaining_time <= 0:
                self.current_task = None
    
    def is_busy(self):
        return self.current_task is not None
    
    def start_new_task(self, new_task):
        self.current_task = new_task
        self.remaining_time = (self.current_task.no_pages * 60) / self.pps


class Task:
    """Represents the printing task"""
    def __init__(self, current_time):
        self.arrival_time = current_time
        self.no_pages = random.randrange(1,21)
    
    def waiting_time(self, current_time):
        return current_time - self.arrival_time


def simulation(num_seconds, pps):
    """The whole simulation"""
    lab_printer = Printer(pps)
    print_queue = Queue()
    waiting_time = []
    
    for current_second in range(1, num_seconds+1):
        
        if is_any_task():
            new_task = Task(current_second)
            print_queue.enqueue(new_task)
            
            if (not lab_printer.is_busy()) and (not print_queue.is_empty()):
                current_task = print_queue.dequeue()
                lab_printer.start_new_task(current_task)
                waiting_time.append(current_task.waiting_time(current_second))
        lab_printer.tick()
    average_wait = sum(waiting_time) / len(waiting_time) if waiting_time else 0
    print(f"Average Wait {average_wait:.2f} secs | {print_queue.size()} tasks remaining.")



def is_any_task():
    num = random.randrange(1, 181)
    return 180 == num



if __name__ == "__main__":
    
    for i in range(10):
        simulation(3600, 5)