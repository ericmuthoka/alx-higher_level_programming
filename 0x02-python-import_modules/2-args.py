#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name itself from the arguments
    num_args = len(args)

    print("Number of argument(s): {}".format(num_args), end="")
    if num_args == 1:
        print(" argument:", end="")
    elif num_args > 1:
        print(" arguments:", end="")
    else:
        print(".", end="")
    print()

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
