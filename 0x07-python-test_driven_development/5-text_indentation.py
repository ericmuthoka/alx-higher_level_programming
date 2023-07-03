#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()  # Remove leading and trailing whitespace

    # Iterate through each character in the text
    for char in text:
        print(char, end="")
        if char in [".", "?", ":"]:
            print("\n\n", end="")
    print()
