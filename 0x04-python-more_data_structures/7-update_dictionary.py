#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # Replace the value
        a_dictionary[key] = value
    else:
        # Add the key and value
        a_dictionary[key] = value
    return a_dictionary
