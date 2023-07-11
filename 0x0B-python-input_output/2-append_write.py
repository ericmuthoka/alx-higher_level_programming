#!/usr/bin/python3
"""Defines a function for appending a string to a UTF8 text file."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
