#!/usr/bin/python3
"""Retrieve object's attributes and methods."""


def lookup(obj):
    """Return list of attributes and methods.

    Args:
        obj: Object to inspect.

    Returns:
        List of names.

    """
    return dir(obj)
