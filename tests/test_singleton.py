import unittest
from project.singleton import SingletonMeta
from project.calculator import RPNCalculator

class TestSingletonMeta(unittest.TestCase):
    def test_singleton_instance(self):
        instance1 = RPNCalculator()
        instance2 = RPNCalculator()
        self.assertIs(instance1, instance2)

if __name__ == '__main__':
    unittest.main()
