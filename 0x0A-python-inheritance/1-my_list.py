#!/usr/bin/python3
"""Defines MyList class that inherits from list."""


class MyList(list):
    """Custom list class with additional functionality."""

    def print_sorted(self):
        """Print the list in sorted order (ascending sort)."""
        sorted_list = sorted(self)
        print(sorted_list)
