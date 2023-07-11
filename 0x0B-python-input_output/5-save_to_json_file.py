#!/usr/bin/python3
"""Defines a function for saving an object to a JSON file."""


import json


def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file.

    Args:
        my_obj (object): The object to save.
        filename (str): The name of the file to save the object to.

    Returns:
        None
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
