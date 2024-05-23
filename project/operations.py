class Operations:
    def __init__(self, stack):
        self.stack = stack

    def add(self):
        self.stack.push(self.stack.pop() + self.stack.pop())

    def subtract(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.push(b - a)

    def multiply(self):
        self.stack.push(self.stack.pop() * self.stack.pop())

    def divide(self):
        a = self.stack.pop()
        b = self.stack.pop()
        if a == 0:
            raise ZeroDivisionError("Division by zero")
        self.stack.push(b / a)
