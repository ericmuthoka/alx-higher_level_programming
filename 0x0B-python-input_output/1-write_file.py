#!/usr/bin/env python3

def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return the characters written."""
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
