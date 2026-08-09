# test.py

import unittest
from source.main import check_odd_even

class TestOddNumberChecker(unittest.TestCase):

    def test_odd_numbers(self):
        # Asserting that odd numbers correctly return "ODD"
        self.assertEqual(check_odd_even(7), "ODD")
        self.assertEqual(check_odd_even(13), "ODD")
        self.assertEqual(check_odd_even(-5), "ODD")

    def test_even_numbers(self):
        # Asserting that even numbers correctly return "EVEN"
        self.assertEqual(check_odd_even(4), "EVEN")
        self.assertEqual(check_odd_even(0), "EVEN")
        self.assertEqual(check_odd_even(-10), "EVEN")

if __name__ == "__main__":
    unittest.main()