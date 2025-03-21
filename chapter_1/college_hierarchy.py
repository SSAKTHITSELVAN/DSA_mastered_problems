class Human:
    """Represents a human"""
    
    def __init__(self,name, role):
        self._name = name
        self._role = role

class money(Human):
    """gets the salary"""
    
    def __init__(self, name, role, amount):
        super().__init__(name, role)
        self.fee = self.salary = amount


class Principal(money):
    """represent the principal"""
    def __init__(self, name, role, salary):
        super().__init__(name, role, salary)
    
    def details(self):
        print(f"I'm the {self._role} {self._name}, my salary is around {self.salary}")



class Staff(money):
    """represent the staff"""
    def __init__(self, name, role, salary):
        super().__init__(name, role, salary)
    
    def details(self):
        print(f"I'm the {self._role} {self._name}, my salary is around {self.salary}")


class Student(money):
    """represent the Student"""
    def __init__(self, name, role, fee):
        super().__init__(name, role, fee)
    
    def details(self):
        print(f"I'm the {self._role} {self._name}, my fee is around {self.fee}")


s = Student("s1", "stu", "1.5 lk")
s.details()