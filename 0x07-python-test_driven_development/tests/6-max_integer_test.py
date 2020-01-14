#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer"""

    def cases(self):
        """Test"""
        self.assertEqual(max_integer([4]), 9)

    def cases1(self):
        """test2"""
        self.assertEqual(max_integer([0, 0]), 0)

    def cases2(self):
        """test3"""
        doc = __import__('6-max_integer').__doc__

    def cases3(self):
        """test4"""
        self.assertTrue(len(doc) > 1)

    def cases4(self):
        """test5"""
        self.assertIsNone(max_integer([]))

    def cases5(self):
        """test6"""
        self.assertEqual(max_integer([2]))

    def cases6(self):
        """test7"""
        self.assertEqual(max_integer([1, 2, "Hello", 4, 5]))

    def cases7(self):
        """test8"""
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
