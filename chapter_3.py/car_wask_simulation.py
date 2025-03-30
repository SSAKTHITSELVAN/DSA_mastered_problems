import random
from pythonds3 import Queue

class Car_Washing_Machine:
    """Represents the car washing machine"""
    
    def __init__(self, cwm):
        self.current_car = None
        self.remaining_time = 0
        self.cwm = cwm
    
    def tick(self):
        if self.current_car is not None:
            self.remaining_time -= 1
            if self.remaining_time <= 0:
                self.current_car = None
    
    def is_busy(self):
        return self.current_car is not None
    
    def start_wash(self, new_car):
        self.current_car = new_car
        self.remaining_time = self.current_car.tfw * 60 / self.cwm

class Task:
    """Represents the car washing event"""
    def __init__(self, ct):
        self.arrival_time = ct
        self.tfw = random.randrange(1, 30)
    
    def wait_time(self, ct):
        return ct - self.arrival_time


def cars_status():
    num = random.randrange(1, 200)
    return 150 == num

def Simulation(time_period, cwm):
    washer = Car_Washing_Machine(cwm)
    car_queue = Queue()
    waiting_time = []
    
    for time in range(time_period):
        if cars_status():
            new_car = Task(time)
            car_queue.enqueue(new_car)
            
            if(not washer.is_busy()) and (not car_queue.is_empty()):
                current_car = car_queue.dequeue()
                washer.start_wash(current_car)
                waiting_time.append(current_car.wait_time(time))
        washer.tick()
    
    # Compute the average wait time
    average_wait = sum(waiting_time) / len(waiting_time) if waiting_time else 0
    print(f"Average Wait {average_wait:.2f} secs | {car_queue.size()} tasks remaining.")


if __name__ == "__main__":
    for i in range(10):
        Simulation(3600, 2)