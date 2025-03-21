class Bank:
    """Banks financial system"""

    def __init__(self):
        self.Bank_bal = 10  # Initial bank balance
        self.mybalance = 0  # Customer balance, initialized to 0

    @property
    def bank_a(self):
        """Allows employees to access the bank balance"""
        if isinstance(self, Employee):
            return self.Bank_bal
        return "error: Access denied"

    @bank_a.setter
    def bank_a(self, increase):
        """Allows employees to update the bank balance"""
        if isinstance(self, Employee):
            self.Bank_bal += increase

    @property
    def cus(self):
        """Allows customers to access their balance"""
        return self.mybalance

    @cus.setter
    def cus(self, increase):
        """Allows customers to deposit money"""
        self.mybalance += increase
        self.Bank_bal += increase


class Employee(Bank):
    """Replicates the bank employee"""

    def __init__(self):
        super().__init__()

    def bank_bal(self):
        """Returns the bank balance"""
        return self.bank_a


class Customer(Bank):
    """Replicates the bank customer"""

    def __init__(self):
        super().__init__()

    def my_bal(self):
        """Returns the customer's balance"""
        return self.cus

    def add_funds(self, money):
        """Allows the customer to deposit money"""
        self.cus = money


# Testing the classes
e = Customer()
print("Employee accessing bank balance:", e.bank_a)  # Expected: "error: Access denied"
e.add_funds(100)  # Customer adds 100 to their balance
print("Customer balance:", e.my_bal())  # Expected: 100
print("Bank balance after customer deposit:", e.Bank_bal)  # Expected: 110

emp = Employee()
print("Employee accessing bank balance:", emp.bank_bal())  # Expected: 10
emp.bank_a = 50  # Employee increases the bank balance
print("Updated Bank balance by Employee:", emp.bank_bal())  # Expected: 60