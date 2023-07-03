#!/usr/bin/python3


import unittest

from max_integer import max_integer


class MaxIntegerTest(unittest.TestCase):
    def test_max_integer(self):
        # Test with an empty list
        self.assertIsNone(max_integer([]))

        # Test with a list containing one element
        self.assertEqual(max_integer([5]), 5)

        # Test with a list containing multiple elements
        self.assertEqual(max_integer([1, 3, 7, 2, 5]), 7)
        self.assertEqual(max_integer([-1, -3, -7, -2, -5]), -1)
        self.assertEqual(max_integer([10, 20, 30, 40, 50]), 50)
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)

        # Test with a list containing negative numbers
        self.assertEqual(max_integer([-5, -2, -10, -1]), -1)

        # Test with a list containing decimal numbers
        self.assertEqual(max_integer([3.14, 2.718, 1.618]), 3.14)
        self.assertEqual(max_integer([10.5, 20.7, 15.3]), 20.7)


if __name__ == '__main__':
    unittest.main()
