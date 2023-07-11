#!/usr/bin/python3


def read_file(filename=""):
    """
  Reads a text file (UTF8) and prints it to stdout.

  Args:
    filename (str): The filename of the text file to read.

  Returns:
    None.
  """

    with open(filename, "r", encoding="utf-8") as f:
      data = f.read()
    print(data)
