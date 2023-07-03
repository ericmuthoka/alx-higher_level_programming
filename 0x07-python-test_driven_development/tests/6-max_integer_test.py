#!/usr/bin/python3
"""Unittests for max_integer([..]) function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test a sorted list of integers."""
        ordered = [1, 3, 5, 7, 9]
        self.assertEqual(max_integer(ordered), 9)

    def test_unordered_list(self):
        """Test an unsorted list of integers."""
        unordered = [9, 3, 7, 5, 1]
        self.assertEqual(max_integer(unordered), 9)

    def test_max_at_beginning(self):
        """Test a list with the maximum value at the beginning."""
        max_at_beginning = [9, 7, 5, 3, 1]
        self.assertEqual(max_integer(max_at_beginning), 9)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floating-point numbers."""
        floats = [1.5, 3.2, -2.7, 5.8, 4.1]
        self.assertEqual(max_integer(floats), 5.8)

    def test_ints_and_floats(self):
        """Test a list of integers and floating-point numbers."""
        ints_and_floats = [1.5, 5, -2, 4, 3.2]
        self.assertEqual(max_integer(ints_and_floats), 5)

    def test_string(self):
        """Test a string."""
        string = "Hello, World!"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Hello", "World", "Python", "OpenAI"]
        self.assertEqual(max_integer(strings), "World")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
