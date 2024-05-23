from project.singleton import SingletonMeta
from project.stack import Stack
from project.operations import Operations

class RPNCalculator(metaclass=SingletonMeta):
    def __init__(self):
        self.stack = Stack()
        self.operations = Operations(self.stack)

    def calculate(self, expression):
        for token in expression.split():
            if token in "+-*/":
                self.operate(token)
            else:
                self.stack.push(float(token))
        return self.stack.pop()

    def operate(self, operator):
        if operator == '+':
            self.operations.add()
        elif operator == '-':
            self.operations.subtract()
        elif operator == '*':
            self.operations.multiply()
        elif operator == '/':
            self.operations.divide()
        else:
            raise ValueError(f"Unknown operator: {operator}")
