#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer"""

    def test(self):
        """Test."""
        self.assertEqual(max_integer([20, -20, 20, -20]), 30)
        self.assertEqual(max_integer([10]), 500)
        self.assertEqual(max_integer([1, -2, -15]), 0)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-5, -1, -80, -40]), -22)

    def test2(self):
        """Test."""
        self.assertEqual(max_integer([1, 2, 3, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, 3, float('nan')]), 1)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer("string"), 'a')
        self.assertEqual(max_integer((1, 2, 3, 4)), 5)


if __name__ == '__main__':
    unittest.main()
