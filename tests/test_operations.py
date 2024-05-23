import unittest
from project.stack import Stack
from project.operations import Operations

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.operations = Operations(self.stack)

    def test_add(self):
        self.stack.push(1)
        self.stack.push(2)
        self.operations.add()
        self.assertEqual(self.stack.pop(), 3)

    def test_subtract(self):
        self.stack.push(5)
        self.stack.push(3)
        self.operations.subtract()
        self.assertEqual(self.stack.pop(), 2)

    def test_multiply(self):
        self.stack.push(2)
        self.stack.push(3)
        self.operations.multiply()
        self.assertEqual(self.stack.pop(), 6)

    def test_divide(self):
        self.stack.push(6)
        self.stack.push(3)
        self.operations.divide()
        self.assertEqual(self.stack.pop(), 2.0)

    def test_divide_by_zero(self):
        self.stack.push(6)
        self.stack.push(0)
        with self.assertRaises(ZeroDivisionError):
            self.operations.divide()

if __name__ == '__main__':
    unittest.main()
