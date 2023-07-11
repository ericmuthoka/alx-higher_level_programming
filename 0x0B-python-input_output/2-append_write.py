#!/usr/bin/python3

def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file and return the character count."""
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
