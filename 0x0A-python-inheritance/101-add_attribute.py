#!/usr/bin/python3
"""Defines a function to add a new attribute to an object."""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attr: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
