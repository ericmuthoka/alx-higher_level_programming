#!/usr/bin/python3
"""Defines a function for converting a string object to JSON."""


import json


def to_json_string(my_obj):
    """Convert a string object to its JSON representation.

    Args:
        my_obj (str): The string object to convert.

    Returns:
        str: The JSON representation of the string object.
    """
    return json.dumps(my_obj)
