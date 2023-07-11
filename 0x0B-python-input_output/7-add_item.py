#!/usr/bin/python3

from sys import argv
from os.path import exists
from json import load, dump


def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file."""
    with open(filename, "w") as f:
        dump(my_obj, f)


def load_from_json_file(filename):
    """Load an object from a JSON file."""
    with open(filename) as f:
        return load(f)


filename = "add_item.json"

if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(argv[1:])

save_to_json_file(items, filename)
