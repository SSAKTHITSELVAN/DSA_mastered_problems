class Logic_gate:
    """Representation of logic gate"""
    def __init__(self, label):
        self.label = label
        self.output = None
    
    def get_output(self):
        self.output = self.perform_logic_operation()
        return self.output
    
    def get_label(self):
        return self.label


class Binary_Gate(Logic_gate):
    """this is 2 pin gates"""
    
    def __init__(self, label):
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None
    
    def set_pin_a(self):
        if self.pin_a == None:
            self.pin_a = int(input(f"pin_a of {self.label} : "))
    
    def set_pin_b(self):
        if self.pin_b == None:
            self.pin_b = int(input(f"pin_b of {self.label}: "))
    
    # Dedicated for connector
    def set__next_free_pin(self, value):
        """choose the next free pin"""
        if self.pin_a == None:
            self.pin_a = value
        else:
            self.pin_b = value


class Unary_Gate(Logic_gate):
    """this is 1 pin gates"""
    
    def __init__(self, label):
        super().__init__(label)
        self.pin_o = None
    
    def set_pin_o(self):
        if self.pin_o == None:
            self.pin_o = int(input(f"pin_o of {self.label} :"))
    
    # Dedicated for connector
    def set__next_free_pin(self, value):
        """choose the next free pin"""
        if self.pin_o == None:
            self.pin_o = value


class And(Binary_Gate):
    """and gate"""
    
    def __init__(self, label):
        super().__init__(label)
    
    def perform_logic_operation(self):
        """defines the logic operation"""
        
        self.set_pin_a()
        self.set_pin_b()
        
        if self.pin_a and self.pin_b:
            return 1
        return 0


class Or(Binary_Gate):
    """Or gate"""
    
    def __init__(self, label):
        super().__init__(label)
    
    def perform_logic_operation(self):
        """defines the logic operation"""
        
        self.set_pin_a()
        self.set_pin_b()
        
        if self.pin_a or self.pin_b:
            return 1
        return 0


class Not(Unary_Gate):
    """not gate"""
    def __init__(self, label):
        super().__init__(label)
    
    
    def perform_logic_operation(self):
        """defines the logic operation"""
        
        self.set_pin_o()
        
        if self.pin_o:
            return 0
        return 1


class Xor(Binary_Gate):
    """xor gate"""
    def __init__(self, label):
        super().__init__(label)
    
    def perform_logic_operation(self):
        self.set_pin_a()
        self.set_pin_b()
        
        if self.pin_a == self.pin_b:
            return 0
        return 1


class Nand(And):
    """NAND gate (NOT AND)"""
    def perform_logic_operation(self):
        return 1 - super().perform_logic_operation()  # Negate the AND result


class Nor(Or):  # Nor should inherit from Or, not And
    """NOR gate (NOT OR)"""
    def perform_logic_operation(self):
        return 1 - super().perform_logic_operation()  # Negate the OR result

class Connector:
    """connects the logic gates"""
    def __init__(self, t_gate, f_gate):
        self.t_gate = t_gate
        self.f_gate = f_gate
        self.connect_it()
    
    def connect_it(self):
        self.t_gate.set__next_free_pin(self.f_gate.get_output())


class Half_adder:
    """half adder"""
    def __init__(self):
        self.a = int(input())
        self.b = int(input())
        self._xor = Xor("-xor-")
        self._and = And("-and-")
        self.merge_it()
    
    def merge_it(self):
        self._xor.set__next_free_pin(self.a)
        self._xor.set__next_free_pin(self.b)
        self._and.set__next_free_pin(self.a)
        self._and.set__next_free_pin(self.b)
    
    def get_output(self):
        return (self._xor.get_output(), self._and.get_output())

class Full_adder:
    """full adder"""
    def __init__(self):
        self.a = int(input())
        self.b = int(input())
        self.c = int(input())
        self._xor_1 = Xor("-xor_1-")
        self._xor_2 = Xor("-xor_2-")
        self._and_1 = And("-and_1-")
        self._and_2 = And("-and_2-")
        self._or = Or("-or-")
        self.merge_it()
    
    def merge_it(self):
        self._xor_1.set__next_free_pin(self.a)
        self._xor_1.set__next_free_pin(self.b)
        self._and_1.set__next_free_pin(self.a)
        self._and_1.set__next_free_pin(self.b)
        c1 = Connector(self._xor_2, self._xor_1)
        self._xor_2.set__next_free_pin(self.c)
        c2 = Connector(self._and_2, self._xor_1)
        self._and_2.set__next_free_pin(self.c)
        c3 = Connector(self._or, self._and_1)
        c4 = Connector(self._or, self._and_2)
    
    def get_output(self):
        return (self._xor_2.get_output(), self._or.get_output())

h = Full_adder()
s, c = h.get_output()
print("sum  ",s, " -- carry   ", c)