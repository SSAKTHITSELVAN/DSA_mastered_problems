from pythonds3 import Stack, Queue


"""Complete implementation of Calculator"""

class Calculator:
    """represents the calculator"""
    def __init__(self, user_input):
        self.expression = user_input
        self.stack_o = Stack()
        self.queue_r = Queue()
        self.stack_n = Stack()
        self.postfix_con()
    
    def get_output(self):
        return self.postfix_evaluation()
    
    def postfix_con(self):
        precedence = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
        if not bool(self.expression):
            raise ValueError("Enter something to process... Don't leave it empty")
        exp = self.expression.split(" ")
        print("exp -- list  -- ", exp)                           # for debugging purpose
        for i in exp:
            if i.isdigit():
                self.queue_r.enqueue(int(i))
            elif i == '(':
                self.stack_o.push(i)
            elif i in precedence.keys():
                while not self.stack_o.is_empty() and precedence[self.stack_o.peek()] > precedence[i]:
                    self.queue_r.enqueue(self.stack_o.pop())
                self.stack_o.push(i)
            elif i == ")":
                while not self.stack_o.is_empty() and self.stack_o.peek() != '(':
                    self.queue_r.enqueue(self.stack_o.pop())
                self.stack_o.pop()
            else:
                raise ValueError("Invalid operator!")
            
        while not self.stack_o.is_empty():
            self.queue_r.enqueue(self.stack_o.pop())
    
    
    def postfix_evaluation(self):
        if self.queue_r.size() < 2:
            raise ValueError("Additional operators found...")
        while not self.queue_r.is_empty():
            num = self.queue_r.dequeue()
            if isinstance(num, int):
                self.stack_n.push(num)
            else:
                a = self.stack_n.pop()
                b = self.stack_n.pop()
                match num:
                    case '+':
                        self.stack_n.push(a+b)
                    case '-':
                        self.stack_n.push(b-a)
                    case '*':
                        self.stack_n.push(a*b)
                    case '/':
                        if a == 0:
                            raise ZeroDivisionError("Number cannot be divided by zero..")
                        self.stack_n.push(b//a)
        if self.stack_n.size() != 1:
            raise ValueError("Additional operators found...")
        return self.stack_n.pop()


if __name__ == '__main__':
    expression = input()
    c = Calculator(expression)
    ans = c.get_output()
    print(ans)