#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a function for converting a JSON string to a Python object."""


import json


def from_json_string(my_str):
    """Convert a JSON string to its Python object representation.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python object representation of the JSON string.
    """
    return json.loads(my_str)
