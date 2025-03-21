"""Framework that distributes computational tasks across worker nodes, handles failures, and aggregates results"""

import random

class Task:
    """Represents the task"""
    
    def __init__(self):
        self.task_id = 0
        self.toughness = random.randint(1, 10)
        self.time_needed = random.randint(5, 50)
    
    def processing(self):
        if self.time_needed <= 0:
            print(f"task of id {self.task_id} is completed")
        else:
            self.time_needed -= 1
    