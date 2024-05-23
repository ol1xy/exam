import unittest
from project.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_and_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_empty_stack(self):
        with self.assertRaises(ValueError):
            self.stack.pop()

if __name__ == '__main__':
    unittest.main()
