#!/usr/bin/python3
"""Check if object inherits (directly or indirectly) from specified class."""


def inherits_from(obj, a_class):
    """Check if obj inherits (directly or indirectly) from a_class."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
