#!/usr/bin/python3
"""
Unit tests for base.py file.
"""
import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    Class to evaluate different test cases for base.py file.
    """

    def test_instance_type_id_class(self):
        """
        Checks for an instance of the class.
        """
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertFalse(type(b1) == type(Base))
        self.assertFalse(id(b1) == id(Base))
        b2 = Base()
        self.assertTrue(type(b1) == type(b2))
        self.assertFalse(id(b1) == id(b2))

    def test_none_id(self):
        """
        Checks when id is None.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b1 = Base()
        self.assertEqual(b1.id, 3)
        b2 = Base()
        self.assertEqual(b2.id, 4)

    # Rest of the test methods...

    def tearDown(self):
        """
        Tear down test method to reset class attribute.
        """
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass
        try:
            os.remove("Rectangle.csv")
        except Exception:
            pass
        try:
            os.remove("Square.csv")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
