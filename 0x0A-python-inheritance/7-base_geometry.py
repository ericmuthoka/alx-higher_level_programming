#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """A class representing the base geometry."""

    def area(self):
        """Raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value to ensure it is an integer greater than 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
