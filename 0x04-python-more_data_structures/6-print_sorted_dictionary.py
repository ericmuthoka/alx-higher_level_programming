#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    # Get the keys of the dictionary.
    keys = list(a_dictionary.keys())

    # Sort the keys.
    keys.sort()

    # Print the keys and values of the dictionary.
    for key in keys:
        print(f"{key}: {a_dictionary[key]}")
