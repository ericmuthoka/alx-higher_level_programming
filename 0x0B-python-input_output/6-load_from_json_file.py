#!/usr/bin/python3
"""Defines a function for loading a Python object from a JSON file."""


import json


def load_from_json_file(filename):
    """Load a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename) as f:
        return json.load(f)
