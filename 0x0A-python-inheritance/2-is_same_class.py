#!/usr/bin/python3
"""Check if an object is an instance of a specified class."""


def is_same_class(obj, a_class):
    """Return True if obj is an instance of a_class, False otherwise."""
    return type(obj) is a_class
