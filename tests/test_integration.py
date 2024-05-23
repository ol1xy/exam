import unittest
from unittest.mock import patch
from project.calculator import RPNCalculator
from project.main import main

class TestIntegration(unittest.TestCase):
    @patch('builtins.input', side_effect=["3 4 +", "10 2 /", "exit"])
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Result: 7.0")
        mock_print.assert_any_call("Result: 5.0")

if __name__ == '__main__':
    unittest.main()
