#!/usr/bin/python3
"""Defines the MyList class, a subclass of the list class."""


class MyList(list):
    """A subclass of the list class representing a custom list."""

    def print_sorted(self):
        """Prints the list in sorted order (ascending)."""
        print(sorted(self))
