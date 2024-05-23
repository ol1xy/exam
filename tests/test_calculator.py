import unittest
from project.calculator import RPNCalculator

class TestRPNCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = RPNCalculator()

    def test_calculate_addition(self):
        result = self.calculator.calculate("3 4 +")
        self.assertEqual(result, 7.0)

    def test_calculate_subtraction(self):
        result = self.calculator.calculate("10 3 -")
        self.assertEqual(result, 7.0)

    def test_calculate_multiplication(self):
        result = self.calculator.calculate("2 3 *")
        self.assertEqual(result, 6.0)

    def test_calculate_division(self):
        result = self.calculator.calculate("8 4 /")
        self.assertEqual(result, 2.0)

    def test_calculate_complex_expression(self):
        result = self.calculator.calculate("3 4 + 2 * 7 /")
        self.assertEqual(result, 2.0)

    def test_unknown_operator(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate("3 4 ^")

if __name__ == '__main__':
    unittest.main()
