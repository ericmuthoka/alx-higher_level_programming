#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    count = 0  # Counter for the number of integers printed
    try:
        for item in my_list[:x]:
            try:
                print("{:d}".format(item), end=' ')
                count += 1
            except ValueError:
                pass  # Skip non-integer values silently
    except TypeError:
        raise Exception("x must be an integer")

    print()  # Print a new line
    return count
