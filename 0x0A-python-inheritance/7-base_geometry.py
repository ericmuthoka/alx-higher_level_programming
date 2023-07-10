#!/usr/bin/python3
"""Defines the BaseGeometry class for representing basic geometry."""


class BaseGeometry:
    """Represents the base geometry class."""

    def area(self):
        """Raises an exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
